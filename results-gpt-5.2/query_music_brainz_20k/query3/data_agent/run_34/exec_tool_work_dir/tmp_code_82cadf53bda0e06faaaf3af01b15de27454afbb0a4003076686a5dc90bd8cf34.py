code = """import json, pandas as pd

with open(var_call_K6pNnJA0y6eEPho7e0x3iJZ4, 'r', encoding='utf-8') as f:
    sales_by_track = json.load(f)
with open(var_call_03vrOZFdUe9s1kZ69WwVJPHI, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

df_sales['track_id'] = df_sales['track_id'].astype(int)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# Since sales track_id count equals tracks count and duplicates are only potential,
# pick highest revenue track_id and map to its title/artist.
idx = df_sales['total_revenue_usd'].idxmax()
top_track_id = int(df_sales.loc[idx, 'track_id'])
max_rev = float(df_sales.loc[idx, 'total_revenue_usd'])
row = df_tracks[df_tracks['track_id'] == top_track_id].iloc[0]

answer = {
    'track_id': top_track_id,
    'title': row['title'],
    'artist': row['artist'],
    'album': row['album'],
    'total_revenue_usd': round(max_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_K6pNnJA0y6eEPho7e0x3iJZ4': 'file_storage/call_K6pNnJA0y6eEPho7e0x3iJZ4.json', 'var_call_03vrOZFdUe9s1kZ69WwVJPHI': 'file_storage/call_03vrOZFdUe9s1kZ69WwVJPHI.json', 'var_call_wpzP1hV7WKhfYIvv2QnuSgoX': [{'n_sales': '58049', 'n_track_ids': '19375'}], 'var_call_iiOtFqlN29Z6OtnFYQImaI5f': [{'n_tracks': '19375', 'n_titles': '18967', 'n_artists': '8994'}]}

exec(code, env_args)
