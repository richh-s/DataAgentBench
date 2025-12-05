code = """import json, re, pandas as pd
from pathlib import Path

path = var_call_QVpJIeWcfz3r0qUqxsRsMwrC
with open(path) as f:
    data = json.load(f)

df = pd.DataFrame(data)

mask = df['repo_data_description'].str.contains('non-binary', case=False, na=False)
sub = df[mask].copy()

pattern = re.compile(r'(?:appearing|duplicated|repeated|seen|copied) (\d+) times')
sub['copies'] = sub['repo_data_description'].str.extract(pattern)[0].astype(float)

max_row = sub.loc[sub['copies'].idxmax()]
result = {
  'id': max_row['id'],
  'sample_repo_name': max_row['sample_repo_name'],
  'copies': int(max_row['copies'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QVpJIeWcfz3r0qUqxsRsMwrC': 'file_storage/call_QVpJIeWcfz3r0qUqxsRsMwrC.json'}

exec(code, env_args)
