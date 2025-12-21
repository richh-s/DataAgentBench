code = """import json, pandas as pd
from pathlib import Path

tracks_path = Path(var_call_gvB3KbJ4PVewzrTvomh8dCSD)
sales_path = Path(var_call_dO7v4HiW28YyUyjfetggOvw3)
tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

tracks['norm_title'] = tracks['title'].str.strip().str.lower()
tracks['norm_artist'] = tracks['artist'].fillna('').str.strip().str.lower()
tracks['norm_album'] = tracks['album'].fillna('').str.strip().str.lower()

agg_tracks = tracks.groupby(['norm_title','norm_artist','norm_album'], dropna=False).agg({
    'track_id': list,
    'title': 'first',
    'artist': 'first',
    'album': 'first'
}).reset_index()

sales['track_id'] = sales['track_id'].astype(int)

records = []
for _, row in agg_tracks.iterrows():
    ids = row['track_id']
    grp_sales = sales[sales['track_id'].isin(ids)]
    if grp_sales.empty:
        continue
    total_rev = grp_sales['revenue_usd'].astype(float).sum()
    records.append({
        'title': row['title'],
        'artist': row['artist'],
        'album': row['album'],
        'track_ids': ids,
        'total_revenue_usd': float(total_rev)
    })

df_res = pd.DataFrame(records)
row_max = df_res.loc[df_res['total_revenue_usd'].idxmax()]

answer = {
    'title': row_max['title'],
    'artist': row_max['artist'],
    'album': row_max['album'],
    'track_ids': row_max['track_ids'],
    'total_revenue_usd': row_max['total_revenue_usd']
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_gvB3KbJ4PVewzrTvomh8dCSD': 'file_storage/call_gvB3KbJ4PVewzrTvomh8dCSD.json', 'var_call_dO7v4HiW28YyUyjfetggOvw3': 'file_storage/call_dO7v4HiW28YyUyjfetggOvw3.json'}

exec(code, env_args)
