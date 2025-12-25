code = """import json, re
from pathlib import Path

path = Path(var_call_wDIt7Jj3DpajTlGGKn68FC7l)
with path.open() as f:
    data = json.load(f)

max_copies = -1
max_record = None
pattern = re.compile(r"(copied|appearing|repeated|duplicated) (\d+) times")
for row in data:
    desc = row.get('repo_data_description','')
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        max_record = {'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies}

result = max_record

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wDIt7Jj3DpajTlGGKn68FC7l': 'file_storage/call_wDIt7Jj3DpajTlGGKn68FC7l.json'}

exec(code, env_args)
