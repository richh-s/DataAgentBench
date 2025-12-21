code = """import json
import re
import pandas as pd

# Load data (using previous variable names)
with open(locals()['var_function-call-2634326689479579170'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-2634326689479580217'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    text = re.sub(r'^\s*\d+[\.\-\s]+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_artist(text):
    if not isinstance(text, str):
        return "unknown"
    norm = normalize_text(text)
    if norm in ["none", "unknown", "", "null"]:
        return "unknown"
    return norm

df_merged['norm_title'] = df_merged['title'].apply(normalize_text)
df_merged['norm_artist'] = df_merged['artist'].apply(clean_artist)

# Filter out invalid titles
invalid_titles = ["none", "null", "", "unknown", "track", "audio"]
df_filtered = df_merged[~df_merged['norm_title'].isin(invalid_titles)]

grouped = df_filtered.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

# Get top 5 results
top_songs = grouped.head(5).to_dict(orient='records')

# Add example original titles
results = []
for song in top_songs:
    mask = (df_merged['norm_title'] == song['norm_title']) & (df_merged['norm_artist'] == song['norm_artist'])
    example = df_merged[mask].iloc[0]
    song['example_title'] = example['title']
    song['example_artist'] = example['artist']
    results.append(song)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2634326689479579170': 'file_storage/function-call-2634326689479579170.json', 'var_function-call-2634326689479580217': 'file_storage/function-call-2634326689479580217.json', 'var_function-call-8303588462130579925': {'norm_title': 'none', 'norm_artist': 'unknown', 'revenue': 14647.52, 'example_title': 'None', 'example_artist': 'None'}}

exec(code, env_args)
