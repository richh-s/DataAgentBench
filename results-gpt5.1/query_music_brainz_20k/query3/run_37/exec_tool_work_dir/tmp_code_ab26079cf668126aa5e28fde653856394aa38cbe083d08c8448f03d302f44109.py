code = """import json, pandas as pd

with open(var_call_uTg9OKu7POLs2292UrlvPpR7, 'r') as f:
    tracks = json.load(f)
with open(var_call_t20wMIjWb9RmFUrnefNxd9Ft, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# ensure revenue_usd is float
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

import numpy as np

def norm(x):
    if pd.isna(x) or str(x).strip().lower() in ['none', 'unknown', '[unknown]']:
        return ''
    return ' '.join(str(x).strip().lower().split())

for col in ['title','artist','album','year']:
    tracks_df[col + '_n'] = tracks_df[col].apply(norm)

keys = []
for _, r in tracks_df.iterrows():
    t, a, al = r['title_n'], r['artist_n'], r['album_n']
    if t and a and al:
        key = f"{t}|||{a}|||{al}"
    elif t and a:
        key = f"{t}|||{a}"
    elif t and al:
        key = f"{t}|||{al}"
    else:
        key = t
    keys.append(key)
tracks_df['canon_key'] = keys

track_to_key = tracks_df.set_index('track_id')['canon_key']

sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

rev_by_song = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()

rev_by_song = rev_by_song[rev_by_song['canon_key'].notna() & (rev_by_song['canon_key'] != '')]

idx = rev_by_song['revenue_usd'].idxmax()
best_key = rev_by_song.loc[idx, 'canon_key']
max_rev = float(rev_by_song.loc[idx, 'revenue_usd'])

rep = tracks_df[tracks_df['canon_key'] == best_key].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': round(max_rev, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uTg9OKu7POLs2292UrlvPpR7': 'file_storage/call_uTg9OKu7POLs2292UrlvPpR7.json', 'var_call_t20wMIjWb9RmFUrnefNxd9Ft': 'file_storage/call_t20wMIjWb9RmFUrnefNxd9Ft.json', 'var_call_wUZNWBoQxRccJ0luB0allZni': ['tracks'], 'var_call_RajDMdM5l75ohO7AWGo09dU6': ['sales']}

exec(code, env_args)
