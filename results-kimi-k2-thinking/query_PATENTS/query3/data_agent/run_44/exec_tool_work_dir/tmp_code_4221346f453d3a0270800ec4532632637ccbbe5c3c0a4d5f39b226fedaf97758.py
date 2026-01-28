code = """import json
import re

# Load both datasets
uc_file = locals().get('var_functions.query_db:5')
nonuc_file = locals().get('var_functions.query_db:18')

with open(uc_file) as f:
    uc_data = json.load(f)

with open(nonuc_file) as f:
    nonuc_data = json.load(f)

# Extract UC publication numbers from Patents_info
uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    # Look for patterns like "US-2022074631-A1" or "pub. number US-2022074631-A1"
    matches = re.findall(r'[A-Z]{2}-\d{6,12}-[A-Z]\d?', info)
    uc_pub_numbers.update(matches)

print('__RESULT__:')
print(json.dumps({
    'uc_patents': len(uc_data),
    'nonuc_patents': len(nonuc_data),
    'uc_pub_numbers_found': len(uc_pub_numbers),
    'sample_uc_numbers': list(uc_pub_numbers)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}}

exec(code, env_args)
