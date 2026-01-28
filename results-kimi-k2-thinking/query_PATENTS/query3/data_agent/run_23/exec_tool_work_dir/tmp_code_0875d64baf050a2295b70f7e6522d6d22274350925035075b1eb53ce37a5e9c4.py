code = """import json
import re

# Read the full result from the previous query
result_file = var_functions.query_db:12
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = var_functions.query_db:12

# Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for patterns like "pub. number XXXXX" or "publication number XXXXX"
    match = re.search(r'pub\. number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers': uc_pub_numbers[:10],  # Show first 10
    'total_uc_pub_numbers': len(uc_pub_numbers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
