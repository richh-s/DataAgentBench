code = """import json
import pandas as pd

# Load sales data
with open('var_function-call-3874821068292434244.json', 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open('var_function-call-13479378208221018498.json', 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize(text):
    if text is None:
        return ""
    return str(text).strip().lower()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Group by normalized title and artist
grouped = df_merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Find max revenue
top_song = grouped.loc[grouped['total_revenue'].idxmax()]

# Get original title/artist (just pick one from the group to be nice, or use the normalized keys)
# To get a "nice" title, I can fetch the first title from the original dataframe that matches the norm keys.
# But simply returning the normalized one might be enough, or I can try to find the original.

print("__RESULT__:")
print(json.dumps({
    "top_song_title": top_song['norm_title'],
    "top_song_artist": top_song['norm_artist'],
    "total_revenue": top_song['total_revenue']
}))"""

env_args = {'var_function-call-3874821068292434244': 'file_storage/function-call-3874821068292434244.json', 'var_function-call-13479378208221018498': 'file_storage/function-call-13479378208221018498.json'}

exec(code, env_args)
