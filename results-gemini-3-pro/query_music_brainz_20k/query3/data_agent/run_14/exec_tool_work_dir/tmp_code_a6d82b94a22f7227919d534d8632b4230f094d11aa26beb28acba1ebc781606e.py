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

# Better Normalization function
def normalize(text):
    if not isinstance(text, str):
        return str(text).lower()
    # Lowercase
    text = text.lower()
    # Remove text in parentheses/brackets (often contains versions like live, remix, etc.)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    # Remove punctuation but keep alphanumeric (including unicode)
    # \w matches [a-zA-Z0-9_] and unicode characters in Python 3 by default if not ASCII flag used.
    # But let's be explicit: remove chars that are NOT words or whitespace
    text = re.sub(r'[^\w\s]', '', text)
    # Remove underscores
    text = text.replace('_', ' ')
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Filter out rows where title became empty (if any, though unlikely to be the top one unless data is bad)
df_valid = df_merged[df_merged['norm_title'] != '']

# Aggregation
grouped = df_valid.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

# Get top 5 to check
top_5 = grouped.head(5).to_dict(orient='records')

# Get sample info for the top 1
top_group = grouped.iloc[0]
original_info = df_merged[
    (df_merged['norm_title'] == top_group['norm_title']) & 
    (df_merged['norm_artist'] == top_group['norm_artist'])
].iloc[0]

result = {
    "top_5": top_5,
    "top_song_sample_title": original_info['title'],
    "top_song_sample_artist": original_info['artist'],
    "top_song_sample_album": original_info['album']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3742390528333561331': 'file_storage/function-call-3742390528333561331.json', 'var_function-call-494577590784018287': 'file_storage/function-call-494577590784018287.json', 'var_function-call-15915298125837850317': {'top_song_norm_title': '', 'top_song_norm_artist': '', 'total_revenue': 177420.82, 'sample_title': 'Приходи - Зн@менатель', 'sample_artist': 'Сплин'}}

exec(code, env_args)
