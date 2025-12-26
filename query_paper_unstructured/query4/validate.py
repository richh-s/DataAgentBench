import json
from pathlib import Path

def validate(predicted_result) -> bool:
    """
    Validate predicted answer against ground truth.
    
    Args:
        predicted_result: A list of records, where each record is a dict with columns
        (e.g., [{"title": "Paper 1", "total_citations": 100}, ...])
    
    Returns:
        True if predicted answer matches ground truth, False otherwise
    """
    # Load ground truth from local JSON file
    ground_truth_file = Path(__file__).parent / "ground_truth.json"
    
    try:
        with open(ground_truth_file, 'r', encoding='utf-8') as f:
            ground_truth = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Ground truth file not found at {ground_truth_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error: Failed to parse ground truth JSON: {e}")
        return False
    
    # Validate predicted_result is a list
    if not isinstance(predicted_result, list):
        print(f"❌ Error: predicted_result must be a list, got {type(predicted_result)}")
        return False
    
    # Ground truth should also be a list
    if not isinstance(ground_truth, list):
        print(f"❌ Error: Ground truth should be a list, got {type(ground_truth)}")
        return False
    
    # Compare lists - they should have the same length and same records
    if len(predicted_result) != len(ground_truth):
        print(f"❌ Validation failed")
        print(f"   Predicted: {len(predicted_result)} records, Ground truth: {len(ground_truth)} records")
        return False
    
    # Sort both lists for comparison
    def sort_key(record):
        # Sort by title first, then by other fields
        return (record.get('title', ''), tuple(sorted(record.items())))
    
    predicted_sorted = sorted(predicted_result, key=sort_key)
    ground_truth_sorted = sorted(ground_truth, key=sort_key)
    
    # Compare each record
    for i, (pred_record, gt_record) in enumerate(zip(predicted_sorted, ground_truth_sorted)):
        if pred_record != gt_record:
            print(f"❌ Validation failed")
            print(f"   Record {i+1} mismatch:")
            print(f"   Predicted: {pred_record}")
            print(f"   Ground truth: {gt_record}")
            return False
    
    print(f"✅ Validation passed")
    print(f"   Predicted: {len(predicted_result)} records, Ground truth: {len(ground_truth)} records")
    return True

if __name__ == "__main__":
    # Example usage
    test_case = [
        {
            "title": "Test Paper",
            "total_citations": 100
        }
    ]
    result = validate(test_case)
    print(f"\nValidation result: {result}")

