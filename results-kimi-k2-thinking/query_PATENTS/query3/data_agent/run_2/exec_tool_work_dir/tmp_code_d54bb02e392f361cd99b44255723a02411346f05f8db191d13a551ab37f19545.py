code = """import json
import re
import os

# Load all UNIV CALIFORNIA patents data
file_path = locals()['var_functions.query_db:14']

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract UNIV CALIFORNIA patent publication numbers
uc_pub_numbers = set()
uc_patents = []

for record in data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        pub_num_match = re.search(r'(?:pub\. number|publication number|has pub\. number|pub\. number is)\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if pub_num_match:
            pub_num = pub_num_match.group(1)
            uc_pub_numbers.add(pub_num)
            uc_patents.append({
                'publication_number': pub_num,
                'patents_info': patents_info
            })

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")
print(f"UC Publication numbers: {list(uc_pub_numbers)}")

result = {
    'uc_pub_numbers': list(uc_pub_numbers),
    'uc_patents_count': len(uc_patents)
}
__RESULT__:
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
