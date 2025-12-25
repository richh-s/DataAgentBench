code = """import json, re
from collections import defaultdict

# Load full results from file
path = var_call_WYJvapnDy1h4BDpskB1clg70
with open(path, 'r') as f:
    data = json.load(f)

max_copies = -1
best_record = None

pattern = re.compile(r"(copied|duplicated|appearing|seen|repeated) (\d+) times")

for row in data:
    desc = row.get('repo_data_description') or ''
    m = pattern.search(desc)
    if not m:
        continue
    count = int(m.group(2))
    if count > max_copies:
        max_copies = count
        best_record = row

result = {
    'max_copies': max_copies,
    'id': best_record.get('id') if best_record else None,
    'sample_repo_name': best_record.get('sample_repo_name') if best_record else None,
    'repo_data_description': best_record.get('repo_data_description') if best_record else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WYJvapnDy1h4BDpskB1clg70': 'file_storage/call_WYJvapnDy1h4BDpskB1clg70.json'}

exec(code, env_args)
