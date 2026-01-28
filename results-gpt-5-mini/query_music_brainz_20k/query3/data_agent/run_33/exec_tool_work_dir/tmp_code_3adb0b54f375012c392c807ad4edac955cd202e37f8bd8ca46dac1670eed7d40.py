code = """import json
import pandas as pd
import unicodedata, re

# Load data from previous query_db results (file paths or lists)
def load_var(v):
    if isinstance(v, str):
        # likely a filepath
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

tracks_raw = load_var(var_call_ns6Z9gVOU1sAp4K88Tx2WCmE)
sales_raw = load_var(var_call_4Vn4Lwg7kPkm9yEhBdntZB59)

df_tracks = pd.DataFrame(tracks_raw)
df_sales = pd.DataFrame(sales_raw)

# Normalize column types
for c in ['track_id']:
    if c in df_tracks.columns:
        df_tracks[c] = df_tracks[c].astype(str)
if 'track_id' in df_sales.columns:
    df_sales['track_id'] = df_sales['track_id'].astype(str)

# convert revenue to float
if 'revenue_usd' in df_sales.columns:
    df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Helpers
missing_vals = set([None, 'None', 'none', '', ' ', '   ', '[unknown]', 'Unknown', 'unknown'])

def is_missing(x):
    if x is None:
        return True
    s = str(x).strip()
    return s in missing_vals

# Extract artist from title if needed: pattern 'Artist - Title' or 'Artist - Title'
def split_artist_title(title):
    if not isinstance(title, str):
        return title, None
    parts = title.split(' - ', 1)
    if len(parts) == 2:
        left, right = parts[0].strip(), parts[1].strip()
        # Heuristic: if left contains letters and spaces and not too long and right not empty
        if 1 <= len(left) <= 60 and len(right) > 0:
            return right, left
    return title, None

# Normalize strings: remove parenthesis/brackets content, accents, punctuation, stopwords
_remove_re = re.compile(r"\(.*?\)|\[.*?\]")
_punct_re = re.compile(r"[^0-9a-zA-Z\s]")
_multi_space = re.compile(r"\s+")
_stopwords = set(['live','remix','acoustic','version','intro','outro','live)','live(','feat','featuring','ft','edit'])

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = _remove_re.sub(' ', s)
    s = s.replace('/', ' ').replace(':', ' ').replace('-', ' ')
    # remove accents
    s = unicodedata.normalize('NFKD', s)
    s = ''.join([c for c in s if not unicodedata.combining(c)])
    # remove punctuation
    s = _punct_re.sub(' ', s)
    s = s.lower()
    # remove stopwords
    tokens = [t for t in s.split() if t not in _stopwords]
    s = ' '.join(tokens)
    s = _multi_space.sub(' ', s).strip()
    return s

# Prepare tracks: clean title and artist
clean_titles = []
clean_artists = []
orig_title_for_key = []
orig_artist_for_key = []

for idx, row in df_tracks.iterrows():
    title = row.get('title')
    artist = row.get('artist')
    # treat 'None' strings
    artist_missing = is_missing(artist)
    title_missing = is_missing(title)
    # if artist missing, try to split from title
    if artist_missing and not title_missing and isinstance(title, str) and ' - ' in title:
        t, a = split_artist_title(title)
        if a:
            title = t
            artist = a
    # store originals
    orig_title_for_key.append(title if title is not None else '')
    orig_artist_for_key.append(artist if artist is not None else '')
    # normalize
    ntitle = normalize_text(title) if not title_missing else ''
    nartist = normalize_text(artist) if not artist_missing else ''
    clean_titles.append(ntitle)
    clean_artists.append(nartist)

# Add normalized columns
df_tracks['norm_title'] = clean_titles
df_tracks['norm_artist'] = clean_artists

# Create entity key
df_tracks['entity_key'] = df_tracks['norm_title'] + '|' + df_tracks['norm_artist']

# Aggregate revenue per track_id in sales
revenue_by_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum()
revenue_by_track.columns = ['track_id','total_revenue']

# Merge with tracks to get entity keys
merged = revenue_by_track.merge(df_tracks[['track_id','entity_key','title','artist','norm_title','norm_artist']], on='track_id', how='left')

# For any sales with missing track metadata, create keys from track_id
merged['entity_key'] = merged['entity_key'].fillna('missing_'+merged['track_id'])

# Aggregate by entity_key
agg = merged.groupby('entity_key', as_index=False).agg({'total_revenue':'sum'})

# Get representative title/artist for each entity_key: choose the most common original pair among tracks
rep = df_tracks.groupby('entity_key').agg({'title': lambda s: s.dropna().iloc[0] if len(s.dropna())>0 else '', 'artist': lambda s: s.dropna().iloc[0] if len(s.dropna())>0 else ''}).reset_index()

agg = agg.merge(rep, on='entity_key', how='left')

# Find max
agg['total_revenue'] = agg['total_revenue'].astype(float)
max_row = agg.sort_values('total_revenue', ascending=False).iloc[0]

result = {
    'title': max_row['title'] if pd.notna(max_row['title']) else '',
    'artist': max_row['artist'] if pd.notna(max_row['artist']) else '',
    'normalized_title': None if (not max_row.get('entity_key')) else max_row['entity_key'].split('|')[0],
    'normalized_artist': None if (not max_row.get('entity_key')) else max_row['entity_key'].split('|')[1] if '|' in max_row['entity_key'] else '',
    'total_revenue_usd': round(float(max_row['total_revenue']),2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ns6Z9gVOU1sAp4K88Tx2WCmE': 'file_storage/call_ns6Z9gVOU1sAp4K88Tx2WCmE.json', 'var_call_4Vn4Lwg7kPkm9yEhBdntZB59': 'file_storage/call_4Vn4Lwg7kPkm9yEhBdntZB59.json'}

exec(code, env_args)
