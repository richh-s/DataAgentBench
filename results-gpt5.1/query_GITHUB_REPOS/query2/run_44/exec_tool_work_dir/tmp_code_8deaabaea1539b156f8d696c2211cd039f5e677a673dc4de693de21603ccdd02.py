code = """import json, re
from pathlib import Path

path = var_call_eJ8Nss1uzPUBNdG6bgY47CSZ
with open(path) as f:
    data = json.load(f)

max_copies = -1
best = None
pat = re.compile(r"(copied|duplicated|appearing|seen|repeated) (\d+) times")

for row in data:
    desc = row.get('repo_data_description','').lower()
    if 'non-binary' not in desc:
        continue
    m = pat.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = row

result = {'max_copies': max_copies, 'file_id': best.get('id') if best else None, 'repo_name': best.get('sample_repo_name') if best else None, 'sample_path': best.get('sample_path') if best else None}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9clNU4gRO2og2IUATkP80xDM': [], 'var_call_FD1G8tjoCWnOvHPeichgaJin': [], 'var_call_eJ8Nss1uzPUBNdG6bgY47CSZ': 'file_storage/call_eJ8Nss1uzPUBNdG6bgY47CSZ.json'}

exec(code, env_args)
