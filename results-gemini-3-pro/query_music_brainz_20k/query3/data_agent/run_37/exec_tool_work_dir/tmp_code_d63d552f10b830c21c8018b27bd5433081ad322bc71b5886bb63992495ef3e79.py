code = """import json
import pandas as pd
import re

# Reload data (re-using logic from previous step, abbreviated)
with open(locals()['var_function-call-5828808762132496056'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8680221993785875883'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_string(s):
    if s is None:
        return ""
    return str(s).lower().strip()

def normalize_track(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    if artist in ["none", "[unknown]", ""]:
        artist = ""
        if " - " in title:
            parts = title.split(" - ", 1)
            artist_candidate = parts[0].strip()
            title_candidate = parts[1].strip()
            if not re.match(r'^\d+$', artist_candidate):
                 artist = artist_candidate
                 title = title_candidate
    title = re.sub(r'^\d+[\.\-]\s*', '', title)
    title = re.sub(r'^\d+\s+', '', title)
    title = re.sub(r'\(.*?\)', '', title)
    title = re.sub(r'\[.*?\]', '', title)
    if " - " in title:
        title = title.split(" - ")[0]
    return pd.Series([artist.strip(), title.strip()])

df[['norm_artist', 'norm_title']] = df.apply(normalize_track, axis=1)

# Debug: look at rows where norm_title is empty or "none"
bad_rows = df[(df['norm_title'] == "") | (df['norm_title'] == "none")]

print("__RESULT__:")
print(json.dumps({
    "bad_rows_sample": bad_rows[['track_id', 'title', 'artist', 'norm_artist', 'norm_title']].head(20).to_dict(orient='records')
}))"""

env_args = {'var_function-call-5828808762132496056': 'file_storage/function-call-5828808762132496056.json', 'var_function-call-8680221993785875883': 'file_storage/function-call-8680221993785875883.json', 'var_function-call-1138439901428454656': {'top_song': {'artist': '', 'title': '', 'total_revenue': 63152.73}, 'top_5': [{'norm_artist': '', 'norm_title': '', 'revenue_usd': 63152.73}, {'norm_artist': '', 'norm_title': 'none', 'revenue_usd': 14647.52}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue_usd': 9013.69}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'revenue_usd': 7744.25}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue_usd': 7515.88}]}}

exec(code, env_args)
