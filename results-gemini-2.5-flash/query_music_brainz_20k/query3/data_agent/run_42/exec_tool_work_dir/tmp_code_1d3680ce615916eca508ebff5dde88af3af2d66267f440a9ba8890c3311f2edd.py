code = """import pandas as pd
import json

# Load tracks data
with open(locals()['var_function-call-10295572818500520287'], 'r') as f:
    tracks_data = json.load(f)
tracks_df = pd.DataFrame(tracks_data)

# Load sales data
with open(locals()['var_function-call-17026769556184926932'], 'r') as f:
    sales_data = json.load(f)
sales_df = pd.DataFrame(sales_data)

# Convert track_id to numeric for merging
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Merge dataframes
merged_df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# Preprocessing for entity resolution: fill NaNs, strip whitespace, lowercase
for col in ['title', 'artist', 'album', 'year']:
    merged_df[col] = merged_df[col].fillna('').astype(str).str.strip().str.lower()

# Group by identifying song attributes and sum revenue
# This approach to entity resolution is simplified and assumes that combining these fields
# will create a sufficiently unique identifier for each song.
# More robust entity resolution would involve fuzzy matching or a dedicated identifier.
song_revenue = merged_df.groupby(['title', 'artist', 'album', 'year'])['revenue_usd'].sum().reset_index()

# Find the song with the highest total revenue
highest_revenue_song = song_revenue.loc[song_revenue['revenue_usd'].idxmax()]

# Format the output
result = {
    "title": highest_revenue_song['title'],
    "artist": highest_revenue_song['artist'],
    "album": highest_revenue_song['album'],
    "year": highest_revenue_song['year'],
    "total_revenue_usd": highest_revenue_song['revenue_usd']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-17380640938118454955': ['tracks'], 'var_function-call-10295572818500520287': 'file_storage/function-call-10295572818500520287.json', 'var_function-call-6868761160078250927': ['sales'], 'var_function-call-17026769556184926932': 'file_storage/function-call-17026769556184926932.json'}

exec(code, env_args)
