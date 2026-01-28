code = """import json
import re

# Load the data from storage
storage_key = 'var_functions.query_db:6'
results = []

# Check if it's a file path or direct data
storage_value = locals()[storage_key]
if isinstance(storage_value, str) and storage_value.endswith('.json'):
    with open(storage_value, 'r') as f:
        results = json.load(f)
else:
    results = storage_value

print(f"Total UNIV CALIFORNIA patents: {len(results)}")

# Extract assignee from Patents_info text
if results:
    print("Sample Patents_info structures:")
    for i in range(min(5, len(results))):
        info_str = results[i].get('Patents_info', '')
        print(f"  {i}: {info_str}")
        
        # Look for assignee patterns
        patterns = [
            r'(?:owned by|assigned to|holds|is owned by|is assigned to)\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)(?:\.|,|\s(?:and|or|with|which|has)\s)',
            r'by\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)\s+(?:holds|owns|is assigned|has)'
        ]
        
        assignee = None
        for pattern in patterns:
            matches = re.findall(pattern, info_str, re.IGNORECASE)
            if matches:
                assignee = matches[0].strip()
                print(f"    Extracted assignee: {assignee}")
                break"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition']}

exec(code, env_args)
