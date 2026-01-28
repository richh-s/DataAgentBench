code = """import json
import re
from collections import defaultdict

# Access the result from storage using locals()
result_var = locals()['var_functions.query_db:12']

# Read the full result from the previous query
if isinstance(result_var, str) and result_var.endswith('.json'):
    with open(result_var, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_var

# Extract all UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for patterns like "pub. number XXXXX" or "publication number XXXXX"
    match = re.search(r'pub\. number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)

# Now we have all UNIV CALIFORNIA publication numbers
print('__RESULT__:')
print(json.dumps({
    'message': f'Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers',
    'count': len(uc_pub_numbers),
    'sample_pub_numbers': list(uc_pub_numbers)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patents_count': 169, 'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'total_uc_pub_numbers': 114}, 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
