import json
import re
from pathlib import Path


def validate(llm_output: str):
    """
    Validate LLM output against ground truth.

    Args:
        llm_output: String output from the LLM containing the answer

    Returns:
        Tuple of (is_valid: bool, reason: str)
    """
    # Load ground truth
    ground_truth_file = Path(__file__).parent / "ground_truth.json"

    try:
        with open(ground_truth_file, 'r', encoding='utf-8') as f:
            ground_truth = json.load(f)
    except FileNotFoundError:
        return False, f"Ground truth file not found at {ground_truth_file}"
    except json.JSONDecodeError as e:
        return False, f"Failed to parse ground truth JSON: {e}"

    # Expected answer is a list of results with Project_Name, Funding_Source, Amount, Status
    expected_results = ground_truth.get("results", [])

    if not expected_results:
        # If no results expected, check for "no results", "none", "0 projects"
        if any(phrase in llm_output.lower() for phrase in ['no project', 'no result', 'none found', '0 project', 'zero project']):
            return True, "Correctly identified no matching projects"
        return False, "Expected no results, but output doesn't indicate empty result"

    # Check if output contains the actual project names
    output_lower = llm_output.lower()
    matched_projects = []

    for result in expected_results:
        project_name = result.get("Project_Name", "")
        # Normalize: lowercase and fix the typo
        normalized_name = project_name.lower().replace("warningn", "warning")
        normalized_output = output_lower.replace("warningn", "warning")

        if normalized_name in normalized_output:
            matched_projects.append(project_name)

    # Require ALL expected projects to be mentioned
    if len(matched_projects) == len(expected_results):
        return True, f"Found all {len(expected_results)} expected projects in output"

    return False, f"Expected {len(expected_results)} projects, found {len(matched_projects)}. Missing: {[r['Project_Name'] for r in expected_results if r['Project_Name'] not in matched_projects]}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        'The projects are: 1) Outdoor Warning Sirens - Design (FEMA Project) with $43,000 from Local Business Support, status: design',
        'Found 2 projects matching criteria',
        '[]',  # empty result
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:60]}...")
        print(f"Result: {result}, Reason: {reason}\n")
