code = """import json
import re
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Loaded ' + str(len(all_patents)) + ' patents')

# Step 1: Extract UNIV CALIFORNIA publication numbers and application numbers
uc_pub_numbers = set()
uc_app_numbers = set()
uc_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-[^\s,\)]+)', patents_info, re.IGNORECASE)
        if pub_match:
            uc_pub_numbers.add(pub_match.group(1))
        
        # Extract application number
        app_match = re.search(r'(?:application|app\. number|patent application)[\s(]+([A-Z]{2}-[0-9]+-[A-Z])', patents_info, re.IGNORECASE)
        if app_match:
            uc_app_numbers.add(app_match.group(1))

print('UNIV CALIFORNIA patents: ' + str(len(uc_patents)))
print('UNIV CALIFORNIA pub numbers: ' + str(len(uc_pub_numbers)))
print('UNIV CALIFORNIA app numbers: ' + str(len(uc_app_numbers)))

# Save identifiers
with open('uc_identifiers.json', 'w') as f:
    json.dump({'publication': list(uc_pub_numbers), 'application': list(uc_app_numbers)}, f)

result = {'uc_patents': len(uc_patents), 'uc_pub_numbers': len(uc_pub_numbers)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
