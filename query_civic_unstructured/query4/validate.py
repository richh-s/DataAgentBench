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

    # Expected answers: count and total_funding
    expected_count = ground_truth.get("count", 0)
    expected_total = ground_truth.get("total_funding", 0)

    # Try to extract numbers from the LLM output
    cleaned_output = llm_output.replace(',', '').replace('$', '')
    numbers = re.findall(r'\b(\d+)\b', cleaned_output)
    numbers_int = [int(n) for n in numbers]

    if not numbers:
        return False, f"No numbers found in LLM output. Expected count: {expected_count}, total_funding: {expected_total}"

    # Check if both expected values are in the output
    count_found = expected_count in numbers_int
    total_found = expected_total in numbers_int

    if count_found and total_found:
        return True, f"Found both count ({expected_count}) and total_funding ({expected_total}) in output"

    # # Partial credit - if at least one is correct
    # if count_found:
    #     return True, f"Found correct count ({expected_count}) in output. Total funding may not match."

    # if total_found:
    #     return True, f"Found correct total_funding ({expected_total}) in output. Count may not match."

    return False, f"Expected count: {expected_count}, total_funding: {expected_total}, but found: {numbers_int}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        "There are 7 projects that started in Spring 2022, with a total funding of $373,000.",
        "Count: 7, Total: 373000",
        "43 projects, $1,963,000 total",
        "Found 5 projects",  # wrong count
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:50]}...")
        print(f"Result: {result}, Reason: {reason}\n")
