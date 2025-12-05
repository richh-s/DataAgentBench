code = """import json, re, pandas as pd
path = var_call_OYxAE8vfOM9R7if1yC8HSJIp
with open(path, 'r') as f:
    data = json.load(f)
pat = re.compile(r'(?:duplicated|appearing|copied|seen|repeated) (\d+) times', re.IGNORECASE)
rows = []
for row in data:
    m = pat.search(row.get('repo_data_description') or '')
    if not m:
        continue
    count = int(m.group(1))
    rows.append({'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': count})

df = pd.DataFrame(rows)
idx = df['copies'].idxmax()
result = df.loc[idx].to_dict()
out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_EcPcfVqtxxMHEwLNDl68ykI8': [], 'var_call_oFcDskj8PkKSuc4jITEb3xLv': [], 'var_call_OYxAE8vfOM9R7if1yC8HSJIp': 'file_storage/call_OYxAE8vfOM9R7if1yC8HSJIp.json'}

exec(code, env_args)
