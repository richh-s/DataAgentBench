code = """import json
import re

# Read the file path from the storage variable
file_path = locals()['var_functions.query_db:14']

# Read the entire file
with open(file_path, 'r') as f:
    uc_data = json.load(f)

# Extract publication numbers from the Patents_info field
uc_pub_numbers = []
pub_num_pattern = r'pub\. number\s*([A-Z]{2}-[A-Z0-9-]+\s*-\s*[A-Z0-9]+|US-[A-Z0-9]+\s*-\s*[A-Z0-9]+|WO-[A-Z0-9]+\s*-\s*[A-Z0-9]+|[^\s]+-[A-Z0-9-]+-[^\s]+)' 

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    # Remove any extra spaces in hyphenated parts
    patents_info_clean = re.sub(r'\s*-\s*', '-', patents_info)
    # Find publication number
    match = re.search(r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)', patents_info_clean)
    if match:
        pub_num_raw = match.group(1).strip()
        uc_pub_numbers.append(pub_num_raw)

print('__RESULT__:')
print(json.dumps({
    'count': len(uc_pub_numbers),
    'sample': uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents'}

exec(code, env_args)
