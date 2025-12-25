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

# Normalization
def normalize(text):
    if not isinstance(text, str):
        return ""
    if text.lower() == "none" or text.lower() == "[unknown]":
        return ""
    
    text = text.lower()
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace('_', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Filter out empty titles
df_clean = df_merged[df_merged['norm_title'] != '']

# Aggregation
grouped = df_clean.groupby(['norm_title', 'norm_artist']).agg(
    revenue_usd=('revenue_usd', 'sum'),
    track_count=('track_id', 'nunique'),
    sample_title=('title', 'first'),
    sample_artist=('artist', 'first')
).reset_index()

grouped = grouped.sort_values('revenue_usd', ascending=False)

# Get top 20
top_20 = grouped.head(20).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_20))"""

env_args = {'var_function-call-3742390528333561331': 'file_storage/function-call-3742390528333561331.json', 'var_function-call-494577590784018287': 'file_storage/function-call-494577590784018287.json', 'var_function-call-15915298125837850317': {'top_song_norm_title': '', 'top_song_norm_artist': '', 'total_revenue': 177420.82, 'sample_title': 'Приходи - Зн@менатель', 'sample_artist': 'Сплин'}, 'var_function-call-1869179159605482992': {'top_5': [{'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': '001', 'norm_artist': 'none', 'revenue_usd': 5866.48}, {'norm_title': '003', 'norm_artist': 'none', 'revenue_usd': 5022.32}, {'norm_title': '005', 'norm_artist': 'none', 'revenue_usd': 4281.18}, {'norm_title': '002', 'norm_artist': 'none', 'revenue_usd': 4237.16}], 'top_song_sample_title': 'None', 'top_song_sample_artist': 'None', 'top_song_sample_album': 'Mijn Restaurant!'}}

exec(code, env_args)
