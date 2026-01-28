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

    # Expected answer is avg_citations (float)
    expected_value = ground_truth.get("avg_citations", 0)

    # Try to extract numbers (including decimals) from the LLM output
    # Look for patterns like "45.67", "45,123.67", "average: 45.67"
    numbers = re.findall(r'\b(\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)\b', llm_output)

    if not numbers:
        return False, f"No numbers found in LLM output. Expected avg_citations: {expected_value}"

    # Clean numbers (remove commas) and check if any matches (with tolerance for floats)
    for num_str in numbers:
        try:
            num = float(num_str.replace(',', ''))
            # Use approximate comparison for floats (within 0.01)
            if abs(num - expected_value) < 0.01:
                return True, f"Found correct avg_citations {expected_value} in output"
        except ValueError:
            continue

    # List found numbers for debugging
    found_nums = []
    for n in numbers:
        try:
            found_nums.append(float(n.replace(',', '')))
        except ValueError:
            pass
    return False, f"Expected avg_citations {expected_value}, but found numbers: {found_nums}"


if __name__ == "__main__":
    # Test examples
    test_cases = [
        "The average citation count is 45.67.",
        "Average: 45.67 citations per paper.",
        "45.67",
        "I found 50.00 average citations",  # wrong answer
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:50]}...")
        print(f"Result: {result}, Reason: {reason}\n")
