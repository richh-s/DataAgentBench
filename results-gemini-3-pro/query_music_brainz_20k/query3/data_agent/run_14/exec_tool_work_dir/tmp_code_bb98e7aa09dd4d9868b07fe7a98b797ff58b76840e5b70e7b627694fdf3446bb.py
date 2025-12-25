code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3742390528333561331'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-494577590784018287'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove text in parentheses/brackets (e.g. remix, live, date)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    # Remove special chars
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Handle cases where artist is None or 'none' or 'unknown'
# If artist is missing, we might rely on title. 
# But let's check the top songs.

# Aggregation
grouped = df_merged.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

# Get original title/artist for the top result (just picking one from the group)
top_group = grouped.iloc[0]
original_info = df_merged[
    (df_merged['norm_title'] == top_group['norm_title']) & 
    (df_merged['norm_artist'] == top_group['norm_artist'])
].iloc[0]

result = {
    "top_song_norm_title": top_group['norm_title'],
    "top_song_norm_artist": top_group['norm_artist'],
    "total_revenue": top_group['revenue_usd'],
    "sample_title": original_info['title'],
    "sample_artist": original_info['artist']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3742390528333561331': 'file_storage/function-call-3742390528333561331.json', 'var_function-call-494577590784018287': 'file_storage/function-call-494577590784018287.json'}

exec(code, env_args)
