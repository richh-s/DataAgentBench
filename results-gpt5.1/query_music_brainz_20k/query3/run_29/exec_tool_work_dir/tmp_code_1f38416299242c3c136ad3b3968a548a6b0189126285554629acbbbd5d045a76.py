code = """import json, pandas as pd

# Load full results from files
with open(var_call_feHAsr3GexqSb5BqTMwuxrDP, 'r') as f:
    tracks = json.load(f)
with open(var_call_pyeB3Aq3hslkq5r9pcjDCpQk, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric columns
for col in ['track_id', 'source_id']:
    tracks_df[col] = pd.to_numeric(tracks_df[col], errors='coerce')
for col in ['sale_id', 'track_id', 'units_sold', 'revenue_usd']:
    sales_df[col] = pd.to_numeric(sales_df[col], errors='coerce')

# Basic normalization for entity resolution: lowercase and strip for title+artist+album
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].astype(str).str.lower().str.strip()

# Build a simple canonical key: title + '|' + artist + '|' + album
tracks_df['canon_key'] = tracks_df['title'].fillna('') + '|' + tracks_df['artist'].fillna('') + '|' + tracks_df['album'].fillna('')

# Some records may have extremely poor metadata; still they will share canon_key if duplicates

# Map each track_id to its canon_key
track_key_map = tracks_df[['track_id', 'canon_key']]

# Join sales with track keys
sales_enriched = sales_df.merge(track_key_map, on='track_id', how='left')

# Aggregate revenue by canon_key
rev_by_canon = sales_enriched.groupby('canon_key', as_index=False)['revenue_usd'].sum()

# Find max revenue canon_key
top_row = rev_by_canon.sort_values('revenue_usd', ascending=False).iloc[0]

# Get representative track metadata for this canon_key
rep_track = tracks_df[tracks_df['canon_key'] == top_row['canon_key']].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': float(top_row['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_feHAsr3GexqSb5BqTMwuxrDP': 'file_storage/call_feHAsr3GexqSb5BqTMwuxrDP.json', 'var_call_pyeB3Aq3hslkq5r9pcjDCpQk': 'file_storage/call_pyeB3Aq3hslkq5r9pcjDCpQk.json', 'var_call_uJ6kU03IRnwHSuXVCWveRaMw': ['tracks'], 'var_call_nrkzFVkqE6qJ3R9VZqlKbk92': ['sales']}

exec(code, env_args)
