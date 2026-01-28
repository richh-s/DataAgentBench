code = """import json
import re
from collections import defaultdict

# Load all patents data to extract UNIV CALIFORNIA publication numbers
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Step 1: Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        # Extract publication number - try multiple patterns
        patterns = [
            r'(?:pub\. number|publication number|pub\. no\.|with pub\. number|has pub\. number)\s+([A-Z]{2}-[A-Z0-9-]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, patents_info, re.IGNORECASE)
            if match:
                uc_pub_numbers.add(match.group(1))
                break

print('UNIV CALIFORNIA patents found:', len(uc_patents))
print('UNIV CALIFORNIA publication numbers:', len(uc_pub_numbers))
print('Sample UC pub numbers:', list(uc_pub_numbers)[:10])

# Store UC pub numbers for next step
with open('uc_pub_numbers.json', 'w') as f:
    json.dump(list(uc_pub_numbers), f)

result = {'uc_patent_count': len(uc_patents), 'uc_pub_numbers': len(uc_pub_numbers)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
