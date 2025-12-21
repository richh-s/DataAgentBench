code = """import json, pandas as pd

with open(var_call_lsX5TY4OjsqobXJ89jdySv25, 'r') as f:
    tracks = json.load(f)
with open(var_call_VJ6uJYzPDrSElqNvCHRKpZyo, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

tracks_df['canon_key'] = tracks_df['title'] + '||' + tracks_df['artist']

track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()

sales_df['track_id'] = sales_df['track_id'].astype(str)

sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

revenue_by_track = sales_df.groupby('canon_key', as_index=False)['revenue_usd'].sum()

rep_tracks = tracks_df.drop_duplicates('canon_key').set_index('canon_key')[['title','artist']]

result_df = revenue_by_track.join(rep_tracks, on='canon_key')

max_row = result_df.loc[result_df['revenue_usd'].idxmax()]

answer = {
    'title': max_row['title'],
    'artist': max_row['artist'],
    'total_revenue_usd': float(max_row['revenue_usd'])
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lsX5TY4OjsqobXJ89jdySv25': 'file_storage/call_lsX5TY4OjsqobXJ89jdySv25.json', 'var_call_VJ6uJYzPDrSElqNvCHRKpZyo': 'file_storage/call_VJ6uJYzPDrSElqNvCHRKpZyo.json', 'var_call_rnAoApFMn5Xshcwr5tgJqByB': ['tracks'], 'var_call_LvQkDxIdoaEnlurZTJoCoI7p': ['sales']}

exec(code, env_args)
