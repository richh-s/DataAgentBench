code = """import json, re, os

# load full swift repos
path1 = var_call_PbiKqvzJVr3n1TqdQ4g3Bv0S
with open(path1) as f:
    swift_rows = json.load(f)
swift_repos = {r['repo_name'] for r in swift_rows}

# load full contents subset
path2 = var_call_rhEaKFrG4HFjeutHJOSmXNBF
with open(path2) as f:
    contents_rows = json.load(f)

records = []
for r in contents_rows:
    desc = r['repo_data_description']
    m = re.search(r'(?:duplicated|appearing|seen|repeated|copied) (\d+) times', desc)
    if not m:
        continue
    copies = int(m.group(1))
    if r['sample_repo_name'] in swift_repos:
        records.append((r['id'], r['sample_repo_name'], copies))

if not records:
    result = None
else:
    max_copies = max(c for _,_,c in records)
    cand = [rec for rec in records if rec[2] == max_copies]
    file_id, repo, _ = cand[0]
    result = {'repo_name': repo, 'file_id': file_id, 'copies': max_copies}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_PbiKqvzJVr3n1TqdQ4g3Bv0S': 'file_storage/call_PbiKqvzJVr3n1TqdQ4g3Bv0S.json', 'var_call_rhEaKFrG4HFjeutHJOSmXNBF': 'file_storage/call_rhEaKFrG4HFjeutHJOSmXNBF.json'}

exec(code, env_args)
