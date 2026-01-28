code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_IIBHYuV7HCtnURZhqtCOiazr, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_c8a3oiESd5JMwtN1BsajLyTu, 'r', encoding='utf-8') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure correct dtypes
for col in ['track_id']:
    if col in df_tracks.columns:
        df_tracks[col] = df_tracks[col].astype(str)
for col in ['track_id','revenue_usd']:
    if col in df_sales.columns:
        df_sales[col] = df_sales[col].astype(str)

df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization helpers
STOPWORDS = set(['live','remix','acoustic','version','edit','feat','featuring','ft','remastered','single','radio'])

def remove_parentheticals(s):
    return re.sub(r"\(.*?\)", "", s)

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ['none','[unknown]','nan','']:
        return ''
    s = remove_parentheticals(s)
    s = s.lower()
    # replace common separators
    s = s.replace(' - ', ' - ')
    # remove punctuation
    s = re.sub(r"[^a-z0-9\s-]", " ", s)
    # split on hyphen if it's surrounding artist-title patterns later
    # remove stopwords
    tokens = s.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    s = ' '.join(tokens)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Preprocess tracks: try to extract artist from title if artist empty
records = []
for _, row in df_tracks.iterrows():
    t = dict(row)
    title = t.get('title', '')
    artist = t.get('artist', '')
    # treat placeholders as empty
    if isinstance(artist, str) and artist.strip().lower() in ['none','[unknown]','']:
        artist = ''
    # if artist missing but title looks like 'Artist - Title', split
    if (not artist) and isinstance(title, str) and ' - ' in title:
        parts = title.split(' - ', 1)
        # Heuristic: if left part contains letters and not too long, assume it's artist
        left = parts[0].strip()
        right = parts[1].strip()
        if len(left) > 0 and len(left) < 60:
            artist = left
            title = right
    # Clean up
    norm_title = normalize_text(title)
    norm_artist = normalize_text(artist)
    norm_album = normalize_text(t.get('album', ''))
    norm_year = normalize_text(t.get('year', ''))
    # Form a key: prefer title+artist, fallback include album/year
    if norm_title and norm_artist:
        key = norm_title + '|' + norm_artist
    elif norm_title:
        key = norm_title
        if norm_album:
            key = key + '|' + norm_album
        elif norm_year:
            key = key + '|' + norm_year
    else:
        key = norm_album or norm_year or ''
    t['_norm_title'] = norm_title
    t['_norm_artist'] = norm_artist
    t['_key'] = key
    records.append(t)

df_tracks_norm = pd.DataFrame(records)

# Map track_id to key
trackid_to_key = df_tracks_norm.set_index('track_id')['_key'].to_dict()

# Merge sales with track keys
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['key'] = df_sales['track_id'].map(trackid_to_key)

# For any sales with missing key (no track record), use raw track_id as key
missing_keys = df_sales['key'].isna()
if missing_keys.any():
    df_sales.loc[missing_keys, 'key'] = 'missing_track_' + df_sales.loc[missing_keys, 'track_id']

# Aggregate revenue per key
agg = df_sales.groupby('key', as_index=False)['revenue_usd'].sum()
agg = agg.sort_values('revenue_usd', ascending=False)

# Get top key
if agg.shape[0] == 0:
    result = {
        'track_ids': [],
        'total_revenue_usd': 0.0,
        'representative_title': None,
        'representative_artist': None,
        'key': None
    }
else:
    top = agg.iloc[0]
    top_key = top['key']
    top_revenue = float(top['revenue_usd'])
    # find all track_ids in this cluster
    track_ids = df_tracks_norm[df_tracks_norm['_key'] == top_key]['track_id'].tolist()
    # choose representative title and artist: most common non-empty
    subset = df_tracks_norm[df_tracks_norm['_key'] == top_key]
    rep_title = None
    rep_artist = None
    if not subset.empty:
        # pick title with max length (likely full) or first non-empty
        titles = subset['title'].fillna('')
        titles = [t for t in titles if str(t).strip().lower() not in ['none','']]
        if titles:
            # choose the most frequent normalized title
            rep_title = titles[0]
            # try to choose the title whose normalized form equals the norm_title
            rep_title = subset.loc[subset['_norm_title'] != '', 'title'].iloc[0]
        artists = subset['artist'].fillna('')
        artists = [a for a in artists if str(a).strip().lower() not in ['none','[unknown]','']]
        if artists:
            rep_artist = artists[0]
    result = {
        'track_ids': track_ids,
        'total_revenue_usd': round(top_revenue, 2),
        'representative_title': rep_title,
        'representative_artist': rep_artist,
        'key': top_key
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IIBHYuV7HCtnURZhqtCOiazr': 'file_storage/call_IIBHYuV7HCtnURZhqtCOiazr.json', 'var_call_c8a3oiESd5JMwtN1BsajLyTu': 'file_storage/call_c8a3oiESd5JMwtN1BsajLyTu.json'}

exec(code, env_args)
