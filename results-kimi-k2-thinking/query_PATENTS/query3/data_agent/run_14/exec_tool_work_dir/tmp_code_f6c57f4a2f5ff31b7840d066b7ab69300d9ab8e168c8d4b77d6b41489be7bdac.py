code = """import json
import re

# Load data from storage
file_path = locals()['var_functions.query_db:30']
with open(file_path, 'r') as f:
    univ_california_records = json.load(f)

print('Total UNIV CALIFORNIA patents found:', len(univ_california_records))

# Extract publication numbers from Patents_info
pub_pattern = re.compile(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)')
univ_calif_pub_numbers = []

for record in univ_california_records:
    patents_info = record.get('Patents_info', '')
    if patents_info:
        matches = pub_pattern.findall(patents_info)
        univ_calif_pub_numbers.extend(matches)

print('Extracted publication numbers:', len(univ_calif_pub_numbers))
print('Sample:', univ_calif_pub_numbers[:10])

# Store for later use
result = {
    'count': len(univ_calif_pub_numbers),
    'publication_numbers': univ_calif_pub_numbers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:22': [{'total_rows': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
