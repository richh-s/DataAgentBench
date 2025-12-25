code = """import json, re
import pandas as pd

path = var_call_r5FH4VT4GmIChWPyWd9guDvN
with open(path, 'r') as f:
    data = json.load(f)

# extract copy count from description
pattern = re.compile(r"(copied|duplicated|appearing|seen|repeated) (\d+) times")
rows = []
for row in data:
    desc = row.get('repo_data_description','')
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    rows.append({'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies})

if not rows:
    result = None
else:
    df = pd.DataFrame(rows)
    # each file uniquely by id already; find max copies
    max_copies = df['copies'].max()
    top = df[df['copies'] == max_copies].iloc[0]
    result = {'repo_name': top['sample_repo_name'], 'file_id': top['id'], 'copies': int(top['copies'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_r5FH4VT4GmIChWPyWd9guDvN': 'file_storage/call_r5FH4VT4GmIChWPyWd9guDvN.json'}

exec(code, env_args)
