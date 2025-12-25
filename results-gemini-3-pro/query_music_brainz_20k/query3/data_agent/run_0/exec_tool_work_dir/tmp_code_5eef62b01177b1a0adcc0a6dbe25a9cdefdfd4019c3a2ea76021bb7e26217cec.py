code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8682200878932963124'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8682200878932962997'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Pre-process sales: convert track_id to string (if not already) and total_revenue to float
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Pre-process tracks: convert track_id to string
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join sales to tracks to get revenue per track_id
df_merged = pd.merge(df_tracks, df_sales, on='track_id', how='left')
df_merged['total_revenue'] = df_merged['total_revenue'].fillna(0)

# Entity Resolution
# Function to normalize strings
def normalize(s):
    if not isinstance(s, str) or s is None or s == 'None':
        return ''
    s = s.lower()
    # Remove text in parentheses/brackets which might be extra info like (live), (remix), etc.
    # But be careful, sometimes it's part of the title.
    # Given the hint "duplicates may not match exactly", we'll try a basic normalization first.
    # Let's strip punctuation and extra spaces.
    s = re.sub(r'[^\w\s]', '', s)
    return s.strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Group by normalized title and artist
# We include original title/artist for display purposes (taking the first one)
grouped = df_merged.groupby(['norm_title', 'norm_artist']).agg({
    'total_revenue': 'sum',
    'title': 'first',
    'artist': 'first'
}).reset_index()

# Sort by revenue
grouped = grouped.sort_values('total_revenue', ascending=False)

top_song = grouped.iloc[0]

result = {
    "title": top_song['title'],
    "artist": top_song['artist'],
    "revenue": top_song['total_revenue'],
    "norm_title": top_song['norm_title'],
    "norm_artist": top_song['norm_artist']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8682200878932963124': 'file_storage/function-call-8682200878932963124.json', 'var_function-call-8682200878932962997': 'file_storage/function-call-8682200878932962997.json'}

exec(code, env_args)
