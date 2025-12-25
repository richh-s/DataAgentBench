code = """import json, re
import pandas as pd

path = var_call_EpbXI9X6Nj3sFOZ6xeUX9Rro
with open(path, 'r') as f:
    data = json.load(f)

# extract copy count from description like 'copied 35 times' or 'appearing 21 times' or 'seen 1 times'
pattern = re.compile(r'(?:copied|appearing|repeated|seen) (\d+) times')

rows = []
for row in data:
    desc = row['repo_data_description'] or ''
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(1))
    rows.append({"id": row['id'], "sample_repo_name": row['sample_repo_name'], "copies": copies})

df = pd.DataFrame(rows)
# ensure unique by id, keep max copies per id just in case
idx = df.groupby('id')['copies'].idxmax()
df_unique = df.loc[idx]

max_copies = df_unique['copies'].max()
most_copied = df_unique[df_unique['copies'] == max_copies]

# pick the first row (any, since id unique) and get repo
result_repo = most_copied.iloc[0]['sample_repo_name']
result = json.dumps({"repo_name": result_repo, "copies": int(max_copies)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_EpbXI9X6Nj3sFOZ6xeUX9Rro': 'file_storage/call_EpbXI9X6Nj3sFOZ6xeUX9Rro.json'}

exec(code, env_args)
