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

    # Expected answer is a count
    expected_count = ground_truth.get("count", 0)

    # Try to extract a number from the LLM output
    # Look for patterns like "12", "12 projects", "count: 12", "answer is 12"
    numbers = re.findall(r'\b(\d+)\b', llm_output)

    if not numbers:
        return False, f"No numbers found in LLM output. Expected count: {expected_count}"

    # Check if any extracted number matches the expected count
    for num_str in numbers:
        num = int(num_str)
        if num == expected_count:
            return True, f"Found correct count {expected_count} in output"

    # If we have the expected count as a string match
    if str(expected_count) in llm_output:
        return True, f"Found correct count {expected_count} in output"
    
    return False, f"Expected count {expected_count}, but found numbers: {numbers}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        "The answer is 12 capital projects.",
        "There are 12 projects with design status and funding > $50,000",
        "12",
        "I found 5 projects",  # wrong answer
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:50]}...")
        print(f"Result: {result}, Reason: {reason}\n")
