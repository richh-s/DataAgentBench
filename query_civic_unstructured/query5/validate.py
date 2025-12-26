import json
from pathlib import Path

def validate(predicted_result: dict) -> bool:
    """
    Validate predicted answer against ground truth.
    
    Args:
        predicted_result: A dictionary with one key-value pair where:
            - key: doc_file name (e.g., "malibucity_agenda__01262022-1835.txt")
            - value: predicted answer (dict with aggregate values, e.g., {"Total_Funding": 100000})
    
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
    
    # Both should be dictionaries
    if not isinstance(predicted_answer, dict):
        print(f"❌ Error: Predicted answer should be a dictionary, got {type(predicted_answer)}")
        return False
    
    if not isinstance(ground_truth_answer, dict):
        print(f"❌ Error: Ground truth answer should be a dictionary, got {type(ground_truth_answer)}")
        return False
    
    # Compare dictionaries - all keys and values must match
    if set(predicted_answer.keys()) != set(ground_truth_answer.keys()):
        print(f"❌ Validation failed: {doc_file}")
        print(f"   Predicted keys: {set(predicted_answer.keys())}")
        print(f"   Ground truth keys: {set(ground_truth_answer.keys())}")
        return False
    
    # Compare each value
    for key in predicted_answer.keys():
        pred_value = predicted_answer[key]
        gt_value = ground_truth_answer[key]
        
        # Convert to same type for comparison (handle int/float differences)
        if isinstance(pred_value, (int, float)) and isinstance(gt_value, (int, float)):
            # For numeric values, allow small floating point differences
            if abs(pred_value - gt_value) > 0.01:
                print(f"❌ Validation failed: {doc_file}")
                print(f"   Key '{key}': Predicted={pred_value}, Ground truth={gt_value}")
                return False
        elif pred_value != gt_value:
            print(f"❌ Validation failed: {doc_file}")
            print(f"   Key '{key}': Predicted={pred_value}, Ground truth={gt_value}")
            return False
    
    print(f"✅ Validation passed: {doc_file}")
    print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
    return True

if __name__ == "__main__":
    # Example usage
    test_case = {
        "malibucity_agenda__01262022-1835.txt": {
            "Total_Funding": 100000
        }
    }
    result = validate(test_case)
    print(f"\nValidation result: {result}")

