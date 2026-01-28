code = """import json, pandas as pd

# Load Mongo filenames
with open(var_call_fs7xxjX7GVKUtRnsF4gnwGrD, 'r') as f:
    mongo_records = json.load(f)
chi_titles = {r['filename'].rsplit('.txt', 1)[0] for r in mongo_records}

# Load citation records for 2020
with open(var_call_pbb3kZJLyT9ChSgqmjo9LECt, 'r') as f:
    cit_records = json.load(f)

# Filter to CHI papers by title match
cit_df = pd.DataFrame(cit_records)
# ensure citation_count numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'])

chi_mask = cit_df['title'].isin(chi_titles)
chi_total = int(cit_df.loc[chi_mask, 'citation_count'].sum())

result = chi_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fs7xxjX7GVKUtRnsF4gnwGrD': 'file_storage/call_fs7xxjX7GVKUtRnsF4gnwGrD.json', 'var_call_pbb3kZJLyT9ChSgqmjo9LECt': 'file_storage/call_pbb3kZJLyT9ChSgqmjo9LECt.json'}

exec(code, env_args)
