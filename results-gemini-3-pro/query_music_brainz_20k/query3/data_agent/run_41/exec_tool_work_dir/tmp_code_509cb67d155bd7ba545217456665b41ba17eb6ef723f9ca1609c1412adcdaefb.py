code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-8306236312507333947'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8306236312507331086'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue'] = pd.to_numeric(df_sales['revenue'])
# track_id in sales might be int or string, ensure consistency
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Function to normalize and extract artist/title
def normalize_row(row):
    title = row['title']
    artist = row['artist']
    
    if title is None: title = ""
    if artist is None: artist = ""
    
    title = str(title).strip()
    artist = str(artist).strip()
    
    # Handle "None" string or empty artist
    if artist.lower() in ['none', ''] and ' - ' in title:
        parts = title.split(' - ', 1)
        artist = parts[0].strip()
        title = parts[1].strip()
        
    return pd.Series([artist.lower(), title.lower()])

merged[['norm_artist', 'norm_title']] = merged.apply(normalize_row, axis=1)

# Group by normalized artist and title
grouped = merged.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()

# Sort
top_song = grouped.sort_values(by='revenue', ascending=False).iloc[0]

# Retrieve original casing for display? 
# We can find one of the original rows matching the norm_artist and norm_title to get a nice display string.
# But for the answer, usually "Title by Artist" is enough.

# Let's find the original title/artist for the top entry
best_match = merged[(merged['norm_artist'] == top_song['norm_artist']) & (merged['norm_title'] == top_song['norm_title'])].iloc[0]

result = {
    "title": best_match['title'],
    "artist": best_match['artist'],
    "norm_title": top_song['norm_title'],
    "norm_artist": top_song['norm_artist'],
    "total_revenue": top_song['revenue']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7702967746608488128': ['tracks'], 'var_function-call-7702967746608485357': ['sales'], 'var_function-call-8306236312507333947': 'file_storage/function-call-8306236312507333947.json', 'var_function-call-8306236312507331086': 'file_storage/function-call-8306236312507331086.json'}

exec(code, env_args)
