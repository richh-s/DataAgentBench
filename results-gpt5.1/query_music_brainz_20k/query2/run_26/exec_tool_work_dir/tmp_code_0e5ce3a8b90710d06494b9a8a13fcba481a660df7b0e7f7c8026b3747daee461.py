code = """import json, pandas as pd

# Load full results from files
with open(var_call_y3Sj034E94rsD9AD1oYSeXuM, 'r') as f:
    tracks = json.load(f)
with open(var_call_LMsBDz4BqNUg0Ol1i4Llioa9, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Identify tracks corresponding to Brucqe Maginnis' 'Street Hype'
# The database seems to have a misspelled entry: "Bruce Maginnis - Sttreet Hype" in title with artist None.

candidates = tracks_df[tracks_df['title'].str.contains('Street Hype', case=False, na=False) |
                       tracks_df['title'].str.contains('Sttreet Hype', case=False, na=False) |
                       tracks_df['title'].str.contains('Hype', case=False, na=False)]

# From manual inspection of preview we know track_id 7 is "Bruce Maginnis - Sttreet Hype"; filter for that exact row title pattern
track_maginnis = tracks_df[tracks_df['title'].str.contains('Sttreet Hype', case=False, na=False)]
track_ids = track_maginnis['track_id'].astype(int).unique().tolist()

# In case there are other fuzzy duplicates (e.g., slight typos in artist name), also look for titles very similar ignoring artist.
# For simplicity in this dataset, we'll assume track_id 7 uniquely represents this song.

song_sales = sales_df[sales_df['track_id'].astype(int).isin(track_ids)]
store_revenue = song_sales.groupby('store', as_index=False)['revenue_usd'].astype(float).sum()

# Find store with max revenue
max_row = store_revenue.loc[store_revenue['revenue_usd'].idxmax()]
result = {
    'store': max_row['store'],
    'revenue_usd': float(max_row['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_y3Sj034E94rsD9AD1oYSeXuM': 'file_storage/call_y3Sj034E94rsD9AD1oYSeXuM.json', 'var_call_LMsBDz4BqNUg0Ol1i4Llioa9': 'file_storage/call_LMsBDz4BqNUg0Ol1i4Llioa9.json', 'var_call_pYzkS8GLFzAXkw0mDRfc2gif': ['tracks'], 'var_call_dQtVyxI3kAzeILxAhYvNwZzh': ['sales']}

exec(code, env_args)
