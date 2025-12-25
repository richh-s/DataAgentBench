code = """import json
import pandas as pd
import numpy as np

sales_file_path = locals()['var_function-call-3874821068292434244']
tracks_file_path = locals()['var_function-call-13479378208221018498']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(text):
    if pd.isna(text) or text is None:
        return ""
    s = str(text).strip().lower()
    if s == "none" or s == "nan":
        return ""
    return s

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Filter out empty titles
valid_songs = df_merged[df_merged['norm_title'] != ""]

grouped = valid_songs.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped_sorted = grouped.sort_values(by='total_revenue', ascending=False)

top_5 = grouped_sorted.head(5).to_dict(orient='records')

# Get original names for these
results = []
for item in top_5:
    mask = (df_merged['norm_title'] == item['norm_title']) & (df_merged['norm_artist'] == item['norm_artist'])
    rep = df_merged.loc[mask].iloc[0]
    results.append({
        "original_title": rep['title'],
        "original_artist": rep['artist'],
        "revenue": item['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3874821068292434244': 'file_storage/function-call-3874821068292434244.json', 'var_function-call-13479378208221018498': 'file_storage/function-call-13479378208221018498.json', 'var_function-call-13071031815735748921': {'song': 'None', 'artist': 'None', 'revenue': 14647.52}}

exec(code, env_args)
