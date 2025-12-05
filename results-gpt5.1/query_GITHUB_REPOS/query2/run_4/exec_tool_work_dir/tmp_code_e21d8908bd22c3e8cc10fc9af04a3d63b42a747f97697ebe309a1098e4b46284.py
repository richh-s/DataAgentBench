code = """import json, re
import pandas as pd

path = var_call_WRsDLuZf6DqzWOEQd1PfzXIN
with open(path, 'r') as f:
    data = json.load(f)

# Extract copy counts from repo_data_description (e.g., 'copied 35 times', 'appearing 8 times', 'seen 1 times')
pattern = re.compile(r"(copied|appearing|appears|duplicated|repeated|seen) (\d+) times")

records = []
for row in data:
    desc = row.get('repo_data_description', '') or ''
    m = pattern.search(desc)
    if not m:
        continue
    copies = int(m.group(2))
    records.append({'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies})

if not records:
    result = json.dumps(None)
else:
    df = pd.DataFrame(records)
    # Group by id to ensure uniqueness and take max copies per id (should be same if consistent)
    agg = df.groupby('id', as_index=False)['copies'].max()
    # Find max copy count
    max_copies = agg['copies'].max()
    top_ids = agg[agg['copies'] == max_copies]['id'].tolist()
    # For these ids, collect associated repos (should be unique but we'll take set)
    top_df = df[df['id'].isin(top_ids)]
    # Choose first repo arbitrarily if multiple; question asks for repository containing that file
    # If multiple repos have same file id, we'll list unique repos
    result_obj = {
        'max_copies': int(max_copies),
        'file_ids': top_ids,
        'repos': sorted(top_df['sample_repo_name'].unique().tolist())
    }
    result = json.dumps(result_obj)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_WRsDLuZf6DqzWOEQd1PfzXIN': 'file_storage/call_WRsDLuZf6DqzWOEQd1PfzXIN.json'}

exec(code, env_args)
