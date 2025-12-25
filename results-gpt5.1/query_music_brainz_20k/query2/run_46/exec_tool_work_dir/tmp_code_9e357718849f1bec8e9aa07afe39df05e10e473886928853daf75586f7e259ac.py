code = """import json, pandas as pd

# Load full tracks data
with open(var_call_Rhyllvn6s9wGUwkdtUD3hy9p, 'r') as f:
    tracks = json.load(f)

# Identify track_ids for Brucqe/Brucqe-like Street Hype by fuzzy reasoning on strings
tracks_df = pd.DataFrame(tracks)

# Normalize text
for col in ['title', 'artist']:
    tracks_df[col] = tracks_df[col].astype(str).str.lower()

# Look for rows that clearly correspond to Bruce/Brucqe Maginnis - Street Hype despite typos
candidates = tracks_df[tracks_df['title'].str.contains('street hype', na=False) | tracks_df['title'].str.contains('sttreet hype', na=False)]

# Prepare result with candidate track_ids
candidate_ids = candidates['track_id'].astype(int).tolist()

# Load full sales data
with open(var_call_nQ0pyBdHW5EVWn6gqYsI5zNg, 'r') as f:
    sales = json.load(f)

sales_df = pd.DataFrame(sales)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Filter sales for candidate track_ids
rel_sales = sales_df[sales_df['track_id'].isin(candidate_ids)]

# Aggregate revenue by store across all countries
agg = rel_sales.groupby('store', as_index=False)['revenue_usd'].sum()

# Find store with max revenue
if len(agg) == 0:
    result = {'store': None, 'revenue_usd': 0}
else:
    top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {'store': top['store'], 'revenue_usd': round(float(top['revenue_usd']), 2)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Rhyllvn6s9wGUwkdtUD3hy9p': 'file_storage/call_Rhyllvn6s9wGUwkdtUD3hy9p.json', 'var_call_nQ0pyBdHW5EVWn6gqYsI5zNg': 'file_storage/call_nQ0pyBdHW5EVWn6gqYsI5zNg.json', 'var_call_DszZhN29Pg0vPu97dkJ9UYdG': ['tracks'], 'var_call_VTvqsUUwqMY19eEevM8r7JoP': ['sales']}

exec(code, env_args)
