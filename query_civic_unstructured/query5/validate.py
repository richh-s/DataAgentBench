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

    # Expected answer is total_funding
    expected_total = ground_truth.get("total_funding", 0)

    # Try to extract numbers from the LLM output
    # Handle formats like "$557,000", "557000", "557,000", "$557000"
    cleaned_output = llm_output.replace(',', '').replace('$', '')
    numbers = re.findall(r'\b(\d+)\b', cleaned_output)

    if not numbers:
        # Special case: if expected is 0, check for "0", "zero", "none", "no funding"
        if expected_total == 0:
            if any(word in llm_output.lower() for word in ['0', 'zero', 'none', 'no funding', 'no projects']):
                return True, f"Found indication of zero/no funding in output (expected: {expected_total})"
        return False, f"No numbers found in LLM output. Expected total_funding: {expected_total}"

    # Check if any extracted number matches the expected total
    for num_str in numbers:
        num = int(num_str)
        if num == expected_total:
            return True, f"Found correct total_funding {expected_total} in output"

    return False, f"Expected total_funding {expected_total}, but found numbers: {[int(n) for n in numbers]}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        "The total funding for disaster-related projects that started in 2022 is $557,000.",
        "Total: 557000",
        "$557,000",
        "Found $1,996,000 in funding",  # wrong amount
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:50]}...")
        print(f"Result: {result}, Reason: {reason}\n")
