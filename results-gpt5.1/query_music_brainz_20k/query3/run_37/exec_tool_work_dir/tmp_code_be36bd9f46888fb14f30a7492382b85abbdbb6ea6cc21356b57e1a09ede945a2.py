code = """import json, pandas as pd

# Load full data from JSON files
with open(var_call_uTg9OKu7POLs2292UrlvPpR7, 'r') as f:
    tracks = json.load(f)
with open(var_call_t20wMIjWb9RmFUrnefNxd9Ft, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning
for col in ['track_id']:
    tracks_df[col] = tracks_df[col].astype(int)
    sales_df[col] = sales_df[col].astype(int)

# Build a canonical key for entity resolution using lowercased stripped title+artist+album
# Handle None and 'None' etc.
def norm(x):
    if pd.isna(x) or str(x).strip().lower() in ['none', 'unknown', '[unknown]']:
        return ''
    return ' '.join(str(x).strip().lower().split())

tracks_df['title_n'] = tracks_df['title'].apply(norm)
tracks_df['artist_n'] = tracks_df['artist'].apply(norm)
tracks_df['album_n'] = tracks_df['album'].apply(norm)
tracks_df['year_n'] = tracks_df['year'].apply(norm)

# Canonical key: title + artist + album; if album missing, fall back to title+artist; if artist missing, use title+album; if both missing, just title.
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

# Map each track_id to its canonical key
track_to_key = tracks_df.set_index('track_id')['canon_key']

sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

# Aggregate revenue by canonical key
rev_by_song = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].astype(float).sum().reset_index()

# Remove empty keys (tracks with no usable identifying info)
rev_by_song = rev_by_song[rev_by_song['canon_key'] != '']

# Find max revenue song
idx = rev_by_song['revenue_usd'].idxmax()
best_key = rev_by_song.loc[idx, 'canon_key']
max_rev = float(rev_by_song.loc[idx, 'revenue_usd'])

# From tracks, pick a representative record for this key (e.g., first occurrence)
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
