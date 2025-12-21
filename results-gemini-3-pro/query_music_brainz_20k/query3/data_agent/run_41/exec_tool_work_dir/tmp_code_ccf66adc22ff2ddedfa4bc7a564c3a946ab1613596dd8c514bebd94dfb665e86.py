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
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Function to normalize
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

# Filter out invalid titles
merged = merged[~merged['norm_title'].isin(['none', '', 'null'])]

# Group
grouped = merged.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values(by='revenue', ascending=False).head(5)

results = []
for index, row in top_songs.iterrows():
    # Find original representation
    match = merged[(merged['norm_artist'] == row['norm_artist']) & (merged['norm_title'] == row['norm_title'])].iloc[0]
    results.append({
        "title": match['title'],
        "artist": match['artist'], # This might be None in the original record but split in normalization
        "inferred_artist": row['norm_artist'],
        "inferred_title": row['norm_title'],
        "total_revenue": row['revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7702967746608488128': ['tracks'], 'var_function-call-7702967746608485357': ['sales'], 'var_function-call-8306236312507333947': 'file_storage/function-call-8306236312507333947.json', 'var_function-call-8306236312507331086': 'file_storage/function-call-8306236312507331086.json', 'var_function-call-6625596137426329529': {'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}}

exec(code, env_args)
