code = """import json, pandas as pd

# Load full aggregated sales
with open(var_call_oY643Ib4GOZptKpXdUenNiKT, 'r') as f:
    sales_agg = json.load(f)

# Load full tracks
with open(var_call_4t2b0jjyua9xt7UpHpqYqxo3, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# Convert numeric columns
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Merge
df = sales_df.merge(tracks_df, on='track_id', how='left')

# Basic normalization for entity resolution: normalize title and artist
for col in ['title', 'artist', 'album']:
    df[col] = df[col].fillna('')

# Create a canonical key using lowercased stripped title + artist + album
df['canon'] = (df['title'].str.lower().str.strip() + '|' +
               df['artist'].str.lower().str.strip() + '|' +
               df['album'].str.lower().str.strip())

# Group by this canonical representation to approximate real-world tracks
grouped = df.groupby('canon', dropna=False)['total_revenue'].sum().reset_index()

# Find max revenue canonical track
max_row = grouped.sort_values('total_revenue', ascending=False).iloc[0]
canon_key = max_row['canon']
max_revenue = float(max_row['total_revenue'])

# Get one representative row for details
rep = df[df['canon'] == canon_key].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep.get('year', None),
    'estimated_total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oY643Ib4GOZptKpXdUenNiKT': 'file_storage/call_oY643Ib4GOZptKpXdUenNiKT.json', 'var_call_4t2b0jjyua9xt7UpHpqYqxo3': 'file_storage/call_4t2b0jjyua9xt7UpHpqYqxo3.json'}

exec(code, env_args)
