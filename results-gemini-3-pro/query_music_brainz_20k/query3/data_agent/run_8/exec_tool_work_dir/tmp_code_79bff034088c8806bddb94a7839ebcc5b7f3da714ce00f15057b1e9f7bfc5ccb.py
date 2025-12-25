code = """import json
import pandas as pd

# Load tracks
with open(locals()['var_function-call-9894359997541209422'], 'r') as f:
    tracks = json.load(f)

# Load sales
with open(locals()['var_function-call-9894359997541209045'], 'r') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure track_id matches
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution
# Normalize title and artist
def normalize(s):
    if s is None:
        return ""
    s = str(s).lower().strip()
    if s in ["none", "[unknown]", "unknown"]:
        return ""
    return s

merged['norm_title'] = merged['title'].apply(normalize)
merged['norm_artist'] = merged['artist'].apply(normalize)

# Handle cases where artist is inside title (simple heuristic or just rely on what we have)
# Looking at the data "Daniel Balavoine - L'enfant aux yeux d'Italie" with artist "None"
# It might be safer to group by 'norm_title' if 'norm_artist' is empty? 
# But if I have "Song A" by "Artist X" and "Song A" by "Artist Y", they are different.
# If I have "Song B" by "None", and "Song B" by "Artist Z", maybe they are the same?
# For now, let's group by (norm_title, norm_artist).
# If norm_artist is empty, it effectively groups by title.

# Aggregation
grouped = merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Find highest revenue
top_song = grouped.sort_values(by='total_revenue', ascending=False).iloc[0]

# Retrieve original title/artist for display (just take the first one from the group)
# We can merge back or just find a representative
best_title_norm = top_song['norm_title']
best_artist_norm = top_song['norm_artist']

# Filter merged to get original names
mask = (merged['norm_title'] == best_title_norm) & (merged['norm_artist'] == best_artist_norm)
representatives = merged[mask].head(1)

result_title = representatives['title'].iloc[0]
result_artist = representatives['artist'].iloc[0]
result_revenue = top_song['total_revenue']

print("__RESULT__:")
print(json.dumps({
    "title": result_title,
    "artist": result_artist,
    "revenue": result_revenue,
    "norm_title": best_title_norm,
    "norm_artist": best_artist_norm
}))"""

env_args = {'var_function-call-9894359997541209422': 'file_storage/function-call-9894359997541209422.json', 'var_function-call-9894359997541209045': 'file_storage/function-call-9894359997541209045.json'}

exec(code, env_args)
