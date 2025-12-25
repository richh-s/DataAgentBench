code = """import re, json, pandas as pd, os
path = var_call_eW2bj5YnxS7biJO5L699EW4v
with open(path) as f:
    data = json.load(f)
pat = re.compile(r'(?:appearing|repeated|duplicated|seen|copied) (\d+) times')
rows = []
for row in data:
    m = pat.search(row.get('repo_data_description',''))
    if not m:
        continue
    count = int(m.group(1))
    rows.append({'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': count})
df = pd.DataFrame(rows)
# ensure each id is unique (contents grouped)
idx = df['copies'].idxmax()
result = df.loc[idx].to_dict()
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SRIJh6NUX8IxJjNHPJIsHoS8': [], 'var_call_eW2bj5YnxS7biJO5L699EW4v': 'file_storage/call_eW2bj5YnxS7biJO5L699EW4v.json'}

exec(code, env_args)
