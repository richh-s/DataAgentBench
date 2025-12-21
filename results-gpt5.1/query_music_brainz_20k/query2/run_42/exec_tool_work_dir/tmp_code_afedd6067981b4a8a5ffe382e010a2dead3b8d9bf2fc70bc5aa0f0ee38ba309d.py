code = """import json, pandas as pd

# Load full track data
with open(var_call_niWlyDlvzYTppozASWrvi2rI, 'r') as f:
    tracks = json.load(f)
tracks_df = pd.DataFrame(tracks)

# Identify track_ids corresponding to Brucqe/ Bruce Maginnis Street Hype (allowing for typos)
mask = tracks_df['title'].str.contains('Street Hype', case=False, na=False) | tracks_df['title'].str.contains('Sttreet Hype', case=False, na=False)
mask = mask & tracks_df['title'].str.contains('Maginnis', case=False, na=False)
relevant_tracks = tracks_df[mask]

# Load full sales data
with open(var_call_fFGfvO99yttYx5ruXXsdLcDs, 'r') as f:
    sales = json.load(f)
sales_df = pd.DataFrame(sales)

# Filter sales for these track_ids
rel_sales = sales_df[sales_df['track_id'].isin(relevant_tracks['track_id'].astype(str).tolist())]

# Aggregate revenue by store across all countries
agg = rel_sales.groupby('store', as_index=False)['revenue_usd'].sum()

# Convert revenue_usd to float
agg['revenue_usd'] = agg['revenue_usd'].astype(float)

# Find store with max revenue
if not agg.empty:
    top_row = agg.sort_values('revenue_usd', ascending=False).iloc[0]
    result = {
        'store': top_row['store'],
        'total_revenue_usd': float(top_row['revenue_usd'])
    }
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_niWlyDlvzYTppozASWrvi2rI': 'file_storage/call_niWlyDlvzYTppozASWrvi2rI.json', 'var_call_fFGfvO99yttYx5ruXXsdLcDs': 'file_storage/call_fFGfvO99yttYx5ruXXsdLcDs.json', 'var_call_Q42nLY8jjarYeN2KEutQqmHP': ['tracks'], 'var_call_zY6AT8ZuCaisE2D8963J7Muo': ['sales']}

exec(code, env_args)
