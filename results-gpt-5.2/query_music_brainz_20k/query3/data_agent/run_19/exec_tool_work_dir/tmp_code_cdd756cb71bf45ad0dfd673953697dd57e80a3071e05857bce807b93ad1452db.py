code = """import json, pandas as pd

# Load sales revenue by track_id
sales_src = var_call_9GCgFNunDVdjCloCYOhNxHs9
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_W4nEbbIGcmIX7aABTrerFN7U
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Entity resolution: canonical key based on normalized title+artist+album
import re

def norm_str(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none' or x.strip() == '':
        return ''
    x = x.lower()
    x = re.sub(r"\s+", " ", x)
    x = x.strip()
    return x

def clean_title(t):
    t = norm_str(t)
    # if title includes leading "artist - title" pattern and artist missing, split
    # but we handle separately
    t = re.sub(r"\(live\)", "", t)
    t = re.sub(r"\s*\-\s*\d{4}-\d{2}-\d{2}:.*$", "", t)  # remove date/venue suffixes
    t = re.sub(r"\s*\(.*?\)", lambda m: m.group(0) if len(m.group(0))<5 else "", t)  # drop long parentheses
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def clean_album(a):
    a = norm_str(a)
    a = re.sub(r"\([^)]*\)", "", a)
    a = re.sub(r"[^a-z0-9 ]+", " ", a)
    a = re.sub(r"\s+", " ", a).strip()
    return a

def clean_artist(a):
    a = norm_str(a)
    a = re.sub(r"[^a-z0-9 ]+", " ", a)
    a = re.sub(r"\s+", " ", a).strip()
    return a

tracks_df['artist_clean'] = tracks_df['artist'].apply(clean_artist)
tracks_df['album_clean'] = tracks_df['album'].apply(clean_album)
tracks_df['title_clean'] = tracks_df['title'].apply(clean_title)

# attempt to recover missing artist when embedded in title like "X - Y"
mask_missing_artist = tracks_df['artist_clean'].eq('')
# raw title string
raw_title = tracks_df['title'].apply(lambda x: '' if x is None or str(x).lower()=='none' else str(x))
# split on ' - '
split = raw_title.str.split(' - ', n=1, expand=True)
if split.shape[1] == 2:
    embedded_artist = split[0].apply(clean_artist)
    embedded_title = split[1].apply(clean_title)
    # use embedded if it looks like a name and title not empty
    use = mask_missing_artist & embedded_artist.ne('') & embedded_title.ne('')
    tracks_df.loc[use, 'artist_clean'] = embedded_artist[use]
    # keep original title_clean already derived from full; replace with embedded_title for better matching
    tracks_df.loc[use, 'title_clean'] = embedded_title[use]

tracks_df['entity_key'] = tracks_df['title_clean'] + '|' + tracks_df['artist_clean'] + '|' + tracks_df['album_clean']
# fallback when title_clean empty
tracks_df.loc[tracks_df['title_clean'].eq(''), 'entity_key'] = 'trackid|' + tracks_df['track_id'].astype(str)

# merge sales with entity keys
m = sales_df.merge(tracks_df[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')

# aggregate by entity_key
agg = (m.groupby('entity_key', as_index=False)
         .agg(total_revenue_usd=('total_revenue_usd','sum'),
              track_ids=('track_id', lambda s: sorted(set(map(int,s)))),
              titles=('title', lambda s: [x for x in s if x is not None and str(x).lower()!='none'][:3],),
              artists=('artist', lambda s: [x for x in s if x is not None and str(x).lower()!='none'][:3],)))

agg = agg.sort_values('total_revenue_usd', ascending=False)

top = agg.iloc[0].to_dict()
# pick representative title/artist (most common non-null)
rep = m[m['entity_key']==top['entity_key']].copy()
rep['title_s'] = rep['title'].astype(str)
rep['artist_s'] = rep['artist'].astype(str)
rep_title = rep.loc[~rep['title_s'].str.lower().eq('none'), 'title_s'].mode()
rep_artist = rep.loc[~rep['artist_s'].str.lower().eq('none'), 'artist_s'].mode()
ans = {
    'entity_key': top['entity_key'],
    'total_revenue_usd': float(top['total_revenue_usd']),
    'representative_title': (rep_title.iloc[0] if len(rep_title)>0 else None),
    'representative_artist': (rep_artist.iloc[0] if len(rep_artist)>0 else None),
    'track_ids': top['track_ids']
}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_9GCgFNunDVdjCloCYOhNxHs9': 'file_storage/call_9GCgFNunDVdjCloCYOhNxHs9.json', 'var_call_W4nEbbIGcmIX7aABTrerFN7U': 'file_storage/call_W4nEbbIGcmIX7aABTrerFN7U.json'}

exec(code, env_args)
