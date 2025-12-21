code = """import json, pandas as pd
from pathlib import Path

tracks_path = Path(var_call_jCUYhMzaB57aFpdzjn5WIGH4)
sales_path = Path(var_call_5YTozwsD9hytPq5E5z9Ac6d7)

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

tracks['title_clean'] = tracks['title'].str.strip().str.lower()
tracks['artist_clean'] = tracks['artist'].fillna('').str.strip().str.lower()
tracks['album_clean'] = tracks['album'].fillna('').str.strip().str.lower()

track_groups = tracks.groupby(['title_clean','artist_clean','album_clean'], dropna=False)['track_id'].apply(list).reset_index()
track_groups['group_id'] = track_groups.index

track_to_group = tracks.merge(track_groups[['title_clean','artist_clean','album_clean','group_id']], on=['title_clean','artist_clean','album_clean'], how='left')[['track_id','group_id']]

sales['track_id'] = sales['track_id'].astype(int)
track_to_group['track_id'] = track_to_group['track_id'].astype(int)

sales_grouped = sales.merge(track_to_group, on='track_id', how='left')

revenue_by_group = sales_grouped.groupby('group_id', dropna=False)['revenue_usd'].sum().reset_index()
max_group = revenue_by_group.loc[revenue_by_group['revenue_usd'].idxmax()]

best_group_id = max_group['group_id']

rep_track = track_to_group.merge(tracks, on='track_id', how='left')
rep_track = rep_track[rep_track['group_id'] == best_group_id].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': float(max_group['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jCUYhMzaB57aFpdzjn5WIGH4': 'file_storage/call_jCUYhMzaB57aFpdzjn5WIGH4.json', 'var_call_5YTozwsD9hytPq5E5z9Ac6d7': 'file_storage/call_5YTozwsD9hytPq5E5z9Ac6d7.json'}

exec(code, env_args)
