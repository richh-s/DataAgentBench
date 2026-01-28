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

    # Ground truth is a list of records with title and total_citations
    if not isinstance(ground_truth, list):
        return False, f"Ground truth should be a list, got {type(ground_truth)}"

    expected_count = len(ground_truth)
    expected_titles = {record.get('title', '') for record in ground_truth}
    expected_total = sum(record.get('total_citations', 0) for record in ground_truth)

    # Try to parse LLM output as JSON first
    try:
        parsed_output = json.loads(llm_output)
        if isinstance(parsed_output, list):
            # Check if lengths match
            if len(parsed_output) != expected_count:
                return False, f"Expected {expected_count} records, got {len(parsed_output)}"

            # Sort both lists for comparison
            def sort_key(record):
                return (record.get('title', ''), tuple(sorted(record.items())))

            predicted_sorted = sorted(parsed_output, key=sort_key)
            ground_truth_sorted = sorted(ground_truth, key=sort_key)

            # Compare each record
            for i, (pred, gt) in enumerate(zip(predicted_sorted, ground_truth_sorted)):
                if pred != gt:
                    return False, f"Record {i+1} mismatch: predicted {pred}, expected {gt}"

            return True, f"All {expected_count} records match exactly"
    except (json.JSONDecodeError, TypeError):
        pass

    # Fallback: Check if output contains all expected titles and reasonable citation counts
    found_titles = 0
    for title in expected_titles:
        if title.lower() in llm_output.lower():
            found_titles += 1

    if found_titles == expected_count:
        # Check if total citations sum is mentioned
        numbers = re.findall(r'\b(\d{1,3}(?:,\d{3})*|\d+)\b', llm_output)
        found_nums = [int(n.replace(',', '')) for n in numbers]

        if expected_total in found_nums:
            return True, f"Found all {expected_count} titles and total citations {expected_total} in output"
        else:
            # Check if we found all individual citation counts
            expected_citations = {record.get('total_citations', 0) for record in ground_truth}
            if expected_citations.issubset(set(found_nums)):
                return True, f"Found all {expected_count} titles and all individual citation counts in output"

    if found_titles > 0:
        return False, f"Found {found_titles}/{expected_count} titles. Expected all titles to be present."

    return False, f"Expected {expected_count} paper records with titles and citations. Could not parse output."


if __name__ == "__main__":
    # Test examples
    test_cases = [
        '[{"title": "Paper A", "total_citations": 100}, {"title": "Paper B", "total_citations": 200}]',
        "Paper A has 100 citations, Paper B has 200 citations.",
        "I found 2 papers in the physical activity domain from 2016.",
    ]
    for test in test_cases:
        result, reason = validate(test)
        print(f"Input: {test[:60]}...")
        print(f"Result: {result}, Reason: {reason}\n")
