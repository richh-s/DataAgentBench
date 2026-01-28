code = """import json
import pandas as pd

# Read previous python result
res = json.loads(var_call_23Dox7p3A9RmLJJnMVuDZUmk)

# For transparency, let's compute top 3 groups to ensure correctness
tracks_path = var_call_9ksKfgeBSeGqi6ZS3zfuGO9x
sales_path = var_call_N2XtFAzb2T8Xv7zyNtytDrnl
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# reuse normalization from earlier: simple exact mapping
# build mapping track_id -> title/artist
track_meta = tracks_df.set_index('track_id')[['title','artist']].to_dict(orient='index')

# sum revenue per track_id
rev_per_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
# attach title/artist where available
rev_per_track['title'] = rev_per_track['track_id'].map(lambda tid: track_meta.get(tid, {}).get('title',''))
rev_per_track['artist'] = rev_per_track['track_id'].map(lambda tid: track_meta.get(tid, {}).get('artist',''))

top3 = rev_per_track.sort_values('revenue_usd', ascending=False).head(3)

# prepare json-friendly output
out = top3.to_dict(orient='records')
for r in out:
    r['revenue_usd'] = round(float(r['revenue_usd']),2)

print("__RESULT__:")
print(json.dumps({'top3_tracks_by_track_id': out}))"""

env_args = {'var_call_9ksKfgeBSeGqi6ZS3zfuGO9x': 'file_storage/call_9ksKfgeBSeGqi6ZS3zfuGO9x.json', 'var_call_N2XtFAzb2T8Xv7zyNtytDrnl': 'file_storage/call_N2XtFAzb2T8Xv7zyNtytDrnl.json', 'var_call_23Dox7p3A9RmLJJnMVuDZUmk': {'title': '... - ...', 'artist': 'None', 'total_revenue_usd': 120656.95}}

exec(code, env_args)
