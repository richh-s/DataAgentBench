code = """import re, json
from collections import defaultdict

records_file = var_call_s141RMzqOXVBmSh191vyvWYJ

with open(records_file, 'r') as f:
    data = json.load(f)

max_copies = -1
max_record = None

pattern = re.compile(r'(?:duplicated|appearing|repeated|seen|copied) (\d+) times')

for row in data:
    desc = row.get('repo_data_description') or ''
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(1))
    if copies > max_copies:
        max_copies = copies
        max_record = row

result = {'max_copies': max_copies, 'id': max_record['id'], 'sample_repo_name': max_record['sample_repo_name'], 'repo_data_description': max_record['repo_data_description']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s141RMzqOXVBmSh191vyvWYJ': 'file_storage/call_s141RMzqOXVBmSh191vyvWYJ.json'}

exec(code, env_args)
