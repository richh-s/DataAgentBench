code = """import json, pandas as pd

# load sales aggregate
path_sales = var_call_26EOaWd1TYiV3tL5fnePAZbI
with open(path_sales, 'r') as f:
    sales_agg = json.load(f)

# load tracks
path_tracks = var_call_ppWvtCsz5sXolYvVpDXvrzv2
with open(path_tracks, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# ensure numeric
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
sales_df['track_id'] = sales_df['track_id'].astype(int)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# join to get metadata
merged = sales_df.merge(tracks_df, on='track_id', how='left')

# perform simple entity resolution: group by title & artist (casefolded, stripped), and maybe album & year as secondary
for col in ['title','artist','album','year']:
    merged[col] = merged[col].astype(str).str.strip().str.casefold()

# group at real-track level
group_cols = ['title','artist']
real_track = merged.groupby(group_cols, dropna=False)['total_revenue'].sum().reset_index()

# find max revenue
idx = real_track['total_revenue'].idxmax()
best = real_track.loc[idx]

result = {
    'title': best['title'],
    'artist': best['artist'],
    'total_revenue_usd': float(best['total_revenue'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_26EOaWd1TYiV3tL5fnePAZbI': 'file_storage/call_26EOaWd1TYiV3tL5fnePAZbI.json', 'var_call_ppWvtCsz5sXolYvVpDXvrzv2': 'file_storage/call_ppWvtCsz5sXolYvVpDXvrzv2.json', 'var_call_FTMXmIBj9Wlwxm0FwYwxeVGH': ['tracks'], 'var_call_fPErwOWLYOFkaCPGgANmZEtX': ['sales']}

exec(code, env_args)
