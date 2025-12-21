code = """import json
import pandas as pd
import re

# Load data (using cached files)
sales_path = locals()['var_function-call-571140759892803866']
tracks_path = locals()['var_function-call-7555422285547670374']

with open(sales_path, 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)
df_sales['track_id'] = df_sales['track_id'].astype(str)

with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Simple search for verification
candidates = ['fischerspooner', 'syb van der ploeg', 'ske', 'fausto papetti', 'vrisak generacije']

def check_candidate(row):
    s = str(row['artist']).lower() + " " + str(row['title']).lower()
    for c in candidates:
        if c in s:
            return c
    return None

df['candidate'] = df.apply(check_candidate, axis=1)
subset = df[df['candidate'].notnull()][['track_id', 'title', 'artist', 'total_revenue', 'candidate']]

print("__RESULT__:")
print(subset.to_json(orient='records'))"""

env_args = {'var_function-call-571140759892803866': 'file_storage/function-call-571140759892803866.json', 'var_function-call-7555422285547670374': 'file_storage/function-call-7555422285547670374.json', 'var_function-call-7889678482353499176': 'file_storage/function-call-7889678482353499176.json', 'var_function-call-18009921770386681425': [{'artist_clean': 'none', 'title_clean_core': '', 'total_revenue': 41667.5}, {'artist_clean': '', 'title_clean_core': '', 'total_revenue': 19264.52}, {'artist_clean': 'none', 'title_clean_core': 'none', 'total_revenue': 14647.52}, {'artist_clean': 'fischerspooner', 'title_clean_core': 'emerge', 'total_revenue': 6665.27}, {'artist_clean': 'syb van der ploeg', 'title_clean_core': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'artist_clean': 'ske', 'title_clean_core': 'vagga', 'total_revenue': 6611.56}, {'artist_clean': 'fausto papetti', 'title_clean_core': 'lovers', 'total_revenue': 6259.3}, {'artist_clean': 'vrisak generacije', 'title_clean_core': 'ne veruj', 'total_revenue': 6125.34}, {'artist_clean': 'neil biggin', 'title_clean_core': 'chile', 'total_revenue': 6008.71}, {'artist_clean': 'guts pie earshot', 'title_clean_core': 'travel', 'total_revenue': 5825.26}], 'var_function-call-15580389738942202909': [{'artist_clean': '', 'title_clean_core': '003-', 'total_revenue': 6841.18}, {'artist_clean': 'fischerspooner', 'title_clean_core': 'emerge', 'total_revenue': 6665.27}, {'artist_clean': 'syb van der ploeg', 'title_clean_core': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'artist_clean': 'ske', 'title_clean_core': 'vagga', 'total_revenue': 6611.56}, {'artist_clean': 'fausto papetti', 'title_clean_core': 'lovers', 'total_revenue': 6259.3}, {'artist_clean': 'vrisak generacije', 'title_clean_core': 'ne veruj', 'total_revenue': 6125.34}, {'artist_clean': 'neil biggin', 'title_clean_core': 'chile', 'total_revenue': 6008.71}, {'artist_clean': 'guts pie earshot', 'title_clean_core': 'travel', 'total_revenue': 5825.26}, {'artist_clean': 'hotstylz', 'title_clean_core': 'lookin boy', 'total_revenue': 5712.89}, {'artist_clean': 'rich matteson', 'title_clean_core': 'groovey', 'total_revenue': 5668.5}, {'artist_clean': 'pras', 'title_clean_core': 'ghetto supastar', 'total_revenue': 5514.57}, {'artist_clean': 'mike oldfield', 'title_clean_core': 'to be free', 'total_revenue': 5432.46}, {'artist_clean': 'berlin', 'title_clean_core': 'sex', 'total_revenue': 5420.8}, {'artist_clean': 'love amongst ruin', 'title_clean_core': 'truth', 'total_revenue': 5379.11}, {'artist_clean': 'wotan', 'title_clean_core': 'mother forest', 'total_revenue': 5277.67}, {'artist_clean': 'suzanne de bussac', 'title_clean_core': 'faded', 'total_revenue': 5251.56}, {'artist_clean': 'atb', 'title_clean_core': 'let u go', 'total_revenue': 5227.45}, {'artist_clean': '', 'title_clean_core': '005-', 'total_revenue': 5222.0}, {'artist_clean': 'luke bryan', 'title_clean_core': 'all my friends say', 'total_revenue': 5180.93}, {'artist_clean': 'lemon d', 'title_clean_core': 'jah love', 'total_revenue': 5168.45}]}

exec(code, env_args)
