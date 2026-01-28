code = """import json, pandas as pd

# load sales totals by track_id
p_sales = var_call_2bBgFFMatQFKm2BjrTwuNE3x
if isinstance(p_sales, str):
    with open(p_sales, 'r', encoding='utf-8') as f:
        sales_totals = json.load(f)
else:
    sales_totals = p_sales

p_tracks = var_call_RYRFhyUVvsdZ2fFHV5CQ0hYe
if isinstance(p_tracks, str):
    with open(p_tracks, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = p_tracks

sales_df = pd.DataFrame(sales_totals)
tracks_df = pd.DataFrame(tracks)

sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# entity resolution key: normalized (title, artist, album). Use title field cleanup.
# Some records embed artist in title like "Artist - Title" when artist is None.

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none' or s.strip() == '':
        return ''
    s = s.strip().lower()
    return ' '.join(s.split())

# derive canonical artist/title when artist missing and title contains " - "

def split_title_artist(row):
    title = row.get('title', None)
    artist = row.get('artist', None)
    title_s = '' if title is None else str(title)
    artist_s = '' if artist is None else str(artist)
    if artist_s.lower() == 'none' or artist_s.strip() == '':
        # try split
        if ' - ' in title_s:
            a, t = title_s.split(' - ', 1)
            # avoid cases like track numbers (e.g., "007-A ...")
            if len(a) > 1 and not a.strip().isdigit() and not a.strip().startswith('00'):
                return t, a
    return title_s, artist_s

tracks_df[['title2','artist2']] = tracks_df.apply(lambda r: pd.Series(split_title_artist(r)), axis=1)
tracks_df['k_title'] = tracks_df['title2'].map(norm)
tracks_df['k_artist'] = tracks_df['artist2'].map(norm)
tracks_df['k_album'] = tracks_df['album'].map(norm)

# merge sales to tracks
m = sales_df.merge(tracks_df[['track_id','k_title','k_artist','k_album','title2','artist2']], on='track_id', how='left')

# group by resolved entity key
m['entity_key'] = m['k_title'] + '||' + m['k_artist'] + '||' + m['k_album']

g = m.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    rep_title=('title2', lambda x: next((v for v in x if v and str(v).lower()!='none'), None)),
    rep_artist=('artist2', lambda x: next((v for v in x if v and str(v).lower()!='none'), None)),
    rep_album=('k_album', 'first'),
    n_track_ids=('track_id','nunique')
).reset_index()

g = g.sort_values('total_revenue_usd', ascending=False)

top = g.iloc[0].to_dict()
# format
answer_obj = {
    'title': None if pd.isna(top.get('rep_title')) else top.get('rep_title'),
    'artist': None if pd.isna(top.get('rep_artist')) else top.get('rep_artist'),
    'total_revenue_usd': float(top['total_revenue_usd']),
    'distinct_track_ids_merged': int(top['n_track_ids'])
}

print('__RESULT__:')
print(json.dumps(answer_obj))"""

env_args = {'var_call_2bBgFFMatQFKm2BjrTwuNE3x': 'file_storage/call_2bBgFFMatQFKm2BjrTwuNE3x.json', 'var_call_RYRFhyUVvsdZ2fFHV5CQ0hYe': 'file_storage/call_RYRFhyUVvsdZ2fFHV5CQ0hYe.json'}

exec(code, env_args)
