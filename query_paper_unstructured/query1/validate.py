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

    # Expected answer is total_citations
    expected_value = ground_truth.get("total_citations", 0)

    # Try to extract a number from the LLM output
    # Look for patterns like "12345", "12,345", "total: 12345", "answer is 12345"
    numbers = re.findall(r'\b(\d{1,3}(?:,\d{3})*|\d+)\b', llm_output)

    if not numbers:
        return False, f"No numbers found in LLM output. Expected total_citations: {expected_value}"

    # Clean numbers (remove commas) and check if any matches
    for num_str in numbers:
        num = int(num_str.replace(',', ''))
        if num == expected_value:
            return True, f"Found correct total_citations {expected_value} in output"

    # List found numbers for debugging
    found_nums = [int(n.replace(',', '')) for n in numbers]
    return False, f"Expected total_citations {expected_value}, but found numbers: {found_nums}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        "The total citation count is 11203.",
        "There are 11,203 citations for papers in the food domain.",
        "11203",
        "I found 5000 citations",  # wrong answer
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:50]}...")
        print(f"Result: {result}, Reason: {reason}\n")
