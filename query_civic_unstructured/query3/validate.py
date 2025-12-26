import json
from pathlib import Path

def validate(predicted_result: dict) -> bool:
    """
    Validate predicted answer against ground truth.
    
    Args:
        predicted_result: A dictionary with one key-value pair where:
            - key: doc_file name (e.g., "malibucity_agenda__01262022-1835.txt")
            - value: predicted answer (list of records, where each record is a dict with columns)
    
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
    
    # Check if predicted_result has exactly one key-value pair
    if len(predicted_result) != 1:
        print(f"❌ Error: Expected exactly one key-value pair, got {len(predicted_result)}")
        return False
    
    # Get the doc_file name and predicted answer
    doc_file = list(predicted_result.keys())[0]
    predicted_answer = predicted_result[doc_file]
    
    # Check if doc_file exists in ground truth
    if doc_file not in ground_truth:
        print(f"❌ Error: Document '{doc_file}' not found in ground truth")
        return False
    
    # Get ground truth answer
    ground_truth_answer = ground_truth[doc_file]
    
    # Both should be lists
    if not isinstance(predicted_answer, list):
        print(f"❌ Error: Predicted answer should be a list, got {type(predicted_answer)}")
        return False
    
    if not isinstance(ground_truth_answer, list):
        print(f"❌ Error: Ground truth answer should be a list, got {type(ground_truth_answer)}")
        return False
    
    # Compare lists - they should have the same length and same records
    if len(predicted_answer) != len(ground_truth_answer):
        print(f"❌ Validation failed: {doc_file}")
        print(f"   Predicted: {len(predicted_answer)} records, Ground truth: {len(ground_truth_answer)} records")
        return False
    
    # Sort both lists for comparison (by Project_Name and then by other fields)
    def sort_key(record):
        return tuple(sorted(record.items()))
    
    predicted_sorted = sorted(predicted_answer, key=sort_key)
    ground_truth_sorted = sorted(ground_truth_answer, key=sort_key)
    
    # Compare each record
    for i, (pred_record, gt_record) in enumerate(zip(predicted_sorted, ground_truth_sorted)):
        if pred_record != gt_record:
            print(f"❌ Validation failed: {doc_file}")
            print(f"   Record {i+1} mismatch:")
            print(f"   Predicted: {pred_record}")
            print(f"   Ground truth: {gt_record}")
            return False
    
    print(f"✅ Validation passed: {doc_file}")
    print(f"   Predicted: {len(predicted_answer)} records, Ground truth: {len(ground_truth_answer)} records")
    return True

if __name__ == "__main__":
    # Example usage
    test_case = {
        "malibucity_agenda__01262022-1835.txt": [
            {
                "Project_Name": "Test Project",
                "Funding_Source": "Test Source",
                "Amount": 10000,
                "Status": "design"
            }
        ]
    }
    result = validate(test_case)
    print(f"\nValidation result: {result}")

