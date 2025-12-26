import json
import re
from pathlib import Path

def load_sql_query():
    """Load SQL query from sql.json in the same folder."""
    sql_file = Path(__file__).parent / "sql.json"
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_query = json.load(f)
    return sql_query

def parse_sql_select_key(sql_query):
    """Parse SELECT clause to determine the key name in ground_truth.json."""
    select_match = re.search(r'SELECT\s+(.+?)\s+FROM', sql_query, re.IGNORECASE | re.DOTALL)
    if not select_match:
        return None
    
    select_str = select_match.group(1).strip()
    
    # Check for AS alias (e.g., SUM(...) AS total_citations)
    alias_match = re.search(r'AS\s+(\w+)', select_str, re.IGNORECASE)
    if alias_match:
        return alias_match.group(1)
    
    # Check for aggregate functions without alias
    if re.search(r'SUM\s*\(', select_str, re.IGNORECASE):
        return 'total_citations'  # default for SUM
    elif re.search(r'AVG\s*\(', select_str, re.IGNORECASE):
        return 'avg_citations'  # default for AVG
    elif re.search(r'COUNT\s*\(', select_str, re.IGNORECASE):
        return 'count'  # default for COUNT
    elif re.search(r'MAX\s*\(', select_str, re.IGNORECASE):
        return 'max_value'  # default for MAX
    elif re.search(r'MIN\s*\(', select_str, re.IGNORECASE):
        return 'min_value'  # default for MIN
    
    # If no aggregate, try to extract column name
    # Remove table prefixes and parentheses
    col_match = re.search(r'[cp]\.(\w+)', select_str, re.IGNORECASE)
    if col_match:
        return col_match.group(1)
    
    return None

def validate(predicted_result) -> bool:
    """
    Validate predicted answer against ground truth.
    
    Args:
        predicted_result: A number (int or float) representing the predicted result
    
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
    
    # Parse SQL to determine the key
    sql_query = load_sql_query()
    key = parse_sql_select_key(sql_query)
    
    # Get ground truth answer
    if key and key in ground_truth:
        ground_truth_answer = ground_truth[key]
    elif len(ground_truth) == 1:
        # If only one key, use that
        ground_truth_answer = list(ground_truth.values())[0]
    else:
        print(f"❌ Error: Could not determine ground truth key from SQL or ground_truth.json")
        return False
    
    # Validate predicted_result is a number
    if not isinstance(predicted_result, (int, float)):
        print(f"❌ Error: predicted_result must be a number, got {type(predicted_result)}")
        return False
    
    # Convert to appropriate type: int if it's a whole number, float otherwise
    if isinstance(predicted_result, float) and predicted_result.is_integer():
        predicted_answer = int(predicted_result)
    else:
        predicted_answer = predicted_result
    
    # Compare predicted answer with ground truth
    # Handle both int and float comparisons
    if isinstance(ground_truth_answer, float) or isinstance(predicted_answer, float):
        # Use approximate comparison for floats
        if abs(predicted_answer - ground_truth_answer) < 0.01:
            print(f"✅ Validation passed")
            print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
            return True
    else:
        # Integer comparison
        if predicted_answer == ground_truth_answer:
            print(f"✅ Validation passed")
            print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
            return True
    
    print(f"❌ Validation failed")
    print(f"   Predicted: {predicted_answer}, Ground truth: {ground_truth_answer}")
    return False

if __name__ == "__main__":
    # Example usage
    test_case = 11203
    result = validate(test_case)
    print(f"\nValidation result: {result}")

