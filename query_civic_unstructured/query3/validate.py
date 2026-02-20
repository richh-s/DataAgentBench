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
    expected_results = []
    for k, v in ground_truth.items():
        expected_results.extend(v)  # assuming ground_truth is a dict of lists
    if not expected_results:
        # If no results expected, check for "no results", "none", "0 projects"
        if any(phrase in llm_output.lower() for phrase in ['no project', 'no result', 'none found', '0 project', 'zero project']):
            return True, "Correctly identified no matching projects"
        return False, "Expected no results, but output doesn't indicate empty result"

    # Check if output contains the actual project names
    output_lower = llm_output.lower().replace("warningn", "warning")

    for result in expected_results:
        project_name = result["Project_Name"].lower().replace("warningn", "warning")
        funding_source = result["Funding_Source"].lower().replace("warningn", "warning")
        amount = result["Amount"]
        status = result["Status"]

        if project_name not in output_lower:
            return False, f"Expected project '{project_name}' not found in output"
        
        if funding_source.lower() not in output_lower:
            return False, f"Expected funding source '{funding_source}' for project '{project_name}' not found in output"
        
        if str(amount) not in output_lower.replace(",", "") or (f"{str(int(amount/1000))}k" not in output_lower) or (f"${str(int(amount/1000))} k" not in output_lower):
            return False, f"Expected amount '{amount}' for project '{project_name}' not found in output"
        
        if status.lower() not in output_lower:
            return False, f"Expected status '{status}' for project '{project_name}' not found in output"
    
    return True, f"Found all {len(expected_results)} expected projects in output"


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
