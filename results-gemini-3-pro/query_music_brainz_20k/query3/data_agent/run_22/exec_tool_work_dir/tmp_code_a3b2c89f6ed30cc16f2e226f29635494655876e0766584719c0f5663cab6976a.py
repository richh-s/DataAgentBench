code = """import json
import pandas as pd

# Load tracks
with open(locals()['var_function-call-2457622807540925275'], 'r') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)

# Load sales
with open(locals()['var_function-call-6100282308464487853'], 'r') as f:
    sales = json.load(f)
df_sales = pd.DataFrame(sales)

# Merge
df_sales['revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Simple search
keywords = ['groovey', 'all my friends say', 'rich matteson', 'luke bryan']
matches = []

for idx, row in df.iterrows():
    s = (str(row['title']) + " " + str(row['artist'])).lower()
    if any(k in s for k in keywords):
        matches.append({
            'track_id': row['track_id'],
            'title': row['title'],
            'artist': row['artist'],
            'revenue': row['revenue']
        })

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-2457622807540925275': 'file_storage/function-call-2457622807540925275.json', 'var_function-call-6100282308464487853': 'file_storage/function-call-6100282308464487853.json', 'var_function-call-7903873907971748242': {'artist': '[Unknown]', 'title': 'None', 'revenue': 14647.52}, 'var_function-call-1063100188911444143': [{'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5417.34}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 4110.55}, {'norm_artist': 'kerstin gier', 'norm_title': 'kapitel 01', 'revenue': 4091.12}, {'norm_artist': 'damian marley', 'norm_title': 'beautiful (instrumental)', 'revenue': 4004.42}, {'norm_artist': 'matthew barber', 'norm_title': 'the story of your life', 'revenue': 3962.97}]}

exec(code, env_args)
