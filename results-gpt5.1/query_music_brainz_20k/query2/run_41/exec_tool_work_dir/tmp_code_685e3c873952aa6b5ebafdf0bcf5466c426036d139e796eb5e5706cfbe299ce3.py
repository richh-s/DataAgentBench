code = """import json
import pandas as pd

# Load full tracks data
with open(var_call_6n52Qd6dJtqEwRm6yHLtUTmp, 'r') as f:
    tracks = json.load(f)

# Find track_ids corresponding to Brucqe/Brucq/Bruce Maginnis Street Hype, allowing for typos
tracks_df = pd.DataFrame(tracks)

# Normalize text
for col in ['title', 'artist']:
    tracks_df[col] = tracks_df[col].astype(str).str.lower()

candidates = tracks_df[tracks_df['title'].str.contains('street hype', na=False)]

# Also allow common misspelling 'sttreet hype'
candidates = pd.concat([
    candidates,
    tracks_df[tracks_df['title'].str.contains('sttreet hype', na=False)]
]).drop_duplicates(subset=['track_id'])

# Further filter for artist name variants like brucqe/brucq/bruce maginnis
name_patterns = ['brucqe', 'brucq', 'bruce', 'maginnis']
mask = pd.Series(False, index=candidates.index)
for pat in name_patterns:
    mask = mask | candidates['title'].str.contains(pat, na=False) | candidates['artist'].str.contains(pat, na=False)

candidates = candidates[mask]

track_ids = candidates['track_id'].astype(int).tolist()

# Load full sales data
with open(var_call_8OwB5kHcxOGAohG3fVtT5Wzq, 'r') as f:
    sales = json.load(f)

sales_df = pd.DataFrame(sales)

sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

filtered = sales_df[sales_df['track_id'].isin(track_ids)]

if filtered.empty:
    result = {"store": None, "revenue_usd": 0.0}
else:
    agg = filtered.groupby('store', as_index=False)['revenue_usd'].sum()
    top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {"store": top['store'], "revenue_usd": round(float(top['revenue_usd']), 2)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_6n52Qd6dJtqEwRm6yHLtUTmp': 'file_storage/call_6n52Qd6dJtqEwRm6yHLtUTmp.json', 'var_call_8OwB5kHcxOGAohG3fVtT5Wzq': 'file_storage/call_8OwB5kHcxOGAohG3fVtT5Wzq.json'}

exec(code, env_args)
