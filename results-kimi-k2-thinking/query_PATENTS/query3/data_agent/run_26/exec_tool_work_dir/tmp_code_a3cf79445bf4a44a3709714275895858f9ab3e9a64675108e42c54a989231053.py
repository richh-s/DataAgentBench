code = """import json
import re

# Load the UC patents data
result_file = locals()['var_functions.query_db:6']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_file

# Extract publication numbers of all UC patents
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for publication number patterns like US-2022074631-A1
    matches = re.findall(r'pub\.?\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if matches:
        uc_pub_numbers.extend(matches)
    else:
        # Alternative pattern
        matches = re.findall(r' publication\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
        if matches:
            uc_pub_numbers.extend(matches)

# Remove duplicates
uc_pub_numbers = list(set(uc_pub_numbers))

print('__RESULT__:')
print(json.dumps(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA', 'var_functions.execute_python:10': 'Found 1112 unique cited publication numbers', 'var_functions.query_db:12': []}

exec(code, env_args)
