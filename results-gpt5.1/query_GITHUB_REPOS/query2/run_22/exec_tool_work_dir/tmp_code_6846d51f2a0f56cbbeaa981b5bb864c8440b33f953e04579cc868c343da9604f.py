code = """import json, re, pandas as pd
from pathlib import Path

path = var_call_9Cg0vEo2YQ2JwnUMNtamEc2z
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

df = pd.DataFrame(rows)
# ensure unique by id (take max copies per id just in case)
df = df.sort_values(['id','copies'], ascending=[True,False]).drop_duplicates('id')
# find file with maximum copies
max_copies = df['copies'].max()
max_files = df[df['copies'] == max_copies]
result = {
  'max_copies': int(max_copies),
  'files': max_files.to_dict(orient='records')
}
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9Cg0vEo2YQ2JwnUMNtamEc2z': 'file_storage/call_9Cg0vEo2YQ2JwnUMNtamEc2z.json'}

exec(code, env_args)
