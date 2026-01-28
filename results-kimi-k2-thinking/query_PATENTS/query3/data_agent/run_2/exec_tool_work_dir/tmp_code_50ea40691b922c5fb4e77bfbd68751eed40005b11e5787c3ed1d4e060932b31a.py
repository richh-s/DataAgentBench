code = """import json
import re

# Load UNIV CALIFORNIA patents
uc_file = locals()['var_functions.query_db:40']
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for record in uc_data:
    patents_info = record.get('Patents_info', '')
    pub_match = re.search(r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
    if pub_match:
        uc_pub_numbers.add(pub_match.group(1))

print('UC patents found:', len(uc_pub_numbers))
print('UC pub numbers sample:', list(uc_pub_numbers)[:5])

result = {'uc_pub_numbers': list(uc_pub_numbers), 'count': len(uc_pub_numbers)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
