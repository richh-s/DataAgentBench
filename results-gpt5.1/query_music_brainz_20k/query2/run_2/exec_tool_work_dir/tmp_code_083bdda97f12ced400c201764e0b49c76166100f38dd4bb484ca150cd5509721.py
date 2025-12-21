code = """import json, pandas as pd

# Load full tracks data
with open(var_call_TIRlkB33DS7YH7NLNy59DNGJ, 'r') as f:
    tracks = json.load(f)

# Find track_ids corresponding to Brucqe/Brucqe-like Maginnis 'Street Hype'
tracks_df = pd.DataFrame(tracks)

# Normalize strings for fuzzy matching simple typos
def norm(s):
    return ''.join(c.lower() for c in (s or '') if c.isalnum())

target_title = norm("Street Hype")
possible_titles = tracks_df['title'].fillna('').apply(norm)
possible_artists = tracks_df['title'].fillna('')  # artist missing; name embedded in title

# We look for records where normalized title contains something like streethype and maginnis present
mask = possible_titles.str.contains('streethype') & tracks_df['title'].str.contains('Maginnis', case=False, na=False)
bruce_tracks = tracks_df[mask]

# Get their track_ids
track_ids = bruce_tracks['track_id'].astype(int).tolist()

# Now load sales data
with open(var_call_uy6lO5uMG2mcBNQ2QSZAltLI, 'r') as f:
    sales = json.load(f)

sales_df = pd.DataFrame(sales)

# Filter sales for these track_ids
sales_df['track_id'] = sales_df['track_id'].astype(int)
bruce_sales = sales_df[sales_df['track_id'].isin(track_ids)]

# Aggregate revenue by store
agg = bruce_sales.groupby('store', as_index=False)['revenue_usd'].sum()
# revenue_usd currently strings; convert
agg['revenue_usd'] = agg['revenue_usd'].astype(float)
agg = agg.sort_values('revenue_usd', ascending=False)

result = {}
if not agg.empty:
    top = agg.iloc[0]
    result = {"store": top['store'], "revenue_usd": float(top['revenue_usd'])}

out = json.dumps(result)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_TIRlkB33DS7YH7NLNy59DNGJ': 'file_storage/call_TIRlkB33DS7YH7NLNy59DNGJ.json', 'var_call_uy6lO5uMG2mcBNQ2QSZAltLI': 'file_storage/call_uy6lO5uMG2mcBNQ2QSZAltLI.json'}

exec(code, env_args)
