import json
from pathlib import Path

def validate(predicted_result: dict) -> bool:
    """
    Validate predicted answer against ground truth.
    
    Args:
        predicted_result: A dictionary with one key-value pair where:
            - key: doc_file name (e.g., "malibucity_agenda__01262022-1835.txt")
            - value: predicted answer (integer count)
    
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
    
    # Compare predicted answer with ground truth
    if predicted_answer == ground_truth_answer:
        print(f"✅ Validation passed: {doc_file}")
        print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
        return True
    else:
        print(f"❌ Validation failed: {doc_file}")
        print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
        return False

if __name__ == "__main__":
    # Example usage
    test_case = {
        "malibucity_agenda__01262022-1835.txt": 5
    }
    result = validate(test_case)
    print(f"\nValidation result: {result}")

