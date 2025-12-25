code = """import json
import pandas as pd

# Load tracks and sales (re-loading to be safe)
with open(locals()['var_function-call-9894359997541209422'], 'r') as f:
    tracks = json.load(f)
with open(locals()['var_function-call-9894359997541209045'], 'r') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower().strip()
    # Don't squash title "unknown" to empty string yet, let's keep it to see.
    # But usually "unknown" title is bad.
    return s

merged['norm_title'] = merged['title'].apply(normalize)
merged['norm_artist'] = merged['artist'].apply(normalize)

# Filter out rows where title looks clearly invalid if necessary, but first let's see the top groups.
# Group by title and artist
grouped = merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(20)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-9894359997541209422': 'file_storage/function-call-9894359997541209422.json', 'var_function-call-9894359997541209045': 'file_storage/function-call-9894359997541209045.json', 'var_function-call-9024924983516554567': {'title': 'unknown', 'artist': 'None', 'revenue': 17865.87, 'norm_title': '', 'norm_artist': ''}}

exec(code, env_args)
