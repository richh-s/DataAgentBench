code = """import pandas as pd
import json
import re

# Load data
sales_file_path = locals()['var_function-call-18273672994042049859']
tracks_file_path = locals()['var_function-call-5279454901003549866']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\s*\(.*?\)\s*', ' ', text)
    text = re.sub(r'\s*\[.*?\]\s*', ' ', text)
    text = re.sub(r'^\d+[\-\.]\s*', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track(row):
    title = str(row['title'])
    artist = str(row['artist'])
    missing_artist = artist.lower() in ['none', 'null', '[unknown]', 'unknown', '']
    if missing_artist:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            return parts[0], parts[1]
        else:
            return "unknown", title
    else:
        return artist, title

cleaned = df.apply(clean_track, axis=1)
df['clean_artist'] = cleaned.apply(lambda x: x[0])
df['clean_title'] = cleaned.apply(lambda x: x[1])
df['norm_artist'] = df['clean_artist'].apply(normalize_text)
df['norm_title'] = df['clean_title'].apply(normalize_text)

# Inspect the top groups
grouped = df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_3_indices = grouped.head(3).index

# Let's get the original data for these top groups
top_groups = grouped.head(3)
print("Top Groups:")
print(top_groups.to_json(orient='records'))

print("\nDetails for Rank 1 (unknown, empty):")
rank1_df = df[(df['norm_artist'] == 'unknown') & (df['norm_title'] == '')]
print(rank1_df[['track_id', 'title', 'artist', 'revenue_usd', 'clean_title', 'clean_artist']].head(10).to_json(orient='records'))

print("\nDetails for Rank 2 (empty, empty):")
rank2_df = df[(df['norm_artist'] == '') & (df['norm_title'] == '')]
print(rank2_df[['track_id', 'title', 'artist', 'revenue_usd', 'clean_title', 'clean_artist']].head(10).to_json(orient='records'))"""

env_args = {'var_function-call-18273672994042049859': 'file_storage/function-call-18273672994042049859.json', 'var_function-call-5279454901003549866': 'file_storage/function-call-5279454901003549866.json', 'var_function-call-15598782705051859165': [{'norm_artist': 'unknown', 'norm_title': '', 'total_revenue': 45147.94}, {'norm_artist': '', 'norm_title': '', 'total_revenue': 25679.65}, {'norm_artist': 'unknown', 'norm_title': 'none', 'total_revenue': 14647.52}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'total_revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'total_revenue': 6611.56}, {'norm_artist': 'echolyn', 'norm_title': 'letters a short essay', 'total_revenue': 6280.0}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'total_revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'total_revenue': 6125.34}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'total_revenue': 6008.71}]}

exec(code, env_args)
