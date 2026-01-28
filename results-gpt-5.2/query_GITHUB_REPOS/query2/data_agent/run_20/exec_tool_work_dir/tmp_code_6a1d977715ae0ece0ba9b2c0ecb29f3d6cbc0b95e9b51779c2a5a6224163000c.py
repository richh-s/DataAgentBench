code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_RQQapJ50qiUOPBMzdnTIcNrd
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Parse copy count from repo_data_description
pat = re.compile(r'(?:duplicated|appearing|appears|seen|repeated|copied)\s+(\d+)\s+times', re.IGNORECASE)

best = None  # (copies, id, repo)
for r in records:
    desc = r.get('repo_data_description') or ''
    m = pat.search(desc)
    if not m:
        continue
    copies = int(m.group(1))
    fid = r.get('id')
    repo = r.get('sample_repo_name')
    cand = (copies, fid, repo)
    if best is None or cand[0] > best[0] or (cand[0]==best[0] and cand[1] < best[1]):
        best = cand

out = {
    'most_frequently_copied_file_id': best[1] if best else None,
    'copy_count': best[0] if best else None,
    'repository': best[2] if best else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RQQapJ50qiUOPBMzdnTIcNrd': 'file_storage/call_RQQapJ50qiUOPBMzdnTIcNrd.json'}

exec(code, env_args)
