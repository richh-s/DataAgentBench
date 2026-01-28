code = """import json
import pandas as pd
import re
import unicodedata

# Load query results from storage variables (file paths)
tracks_path = var_call_A5Y1y31G3ibipHAtuujdK7Mf
sales_path = var_call_iV526ETgONRMqZbLiMscV0Lc

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Clean column types
for c in ['track_id','sale_id']:
    if c in tracks_df.columns:
        tracks_df[c] = pd.to_numeric(tracks_df[c], errors='coerce')
if 'track_id' in sales_df.columns:
    sales_df['track_id'] = pd.to_numeric(sales_df['track_id'], errors='coerce')
if 'revenue_usd' in sales_df.columns:
    sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')

# Normalization helpers

def strip_accents(s):
    if not isinstance(s, str):
        return ''
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return s

paren_re = re.compile(r"\(.*?\)|\[.*?\]|\{.*?\}")
non_alnum_re = re.compile(r'[^0-9a-z ]+')
multisp_re = re.compile(r'\s+')

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ('none','nan','', "[unknown]", 'unknown'):
        return ''
    s = s.strip()
    # remove parenthetical content
    s = paren_re.sub(' ', s)
    s = strip_accents(s)
    s = s.lower()
    # replace punctuation with space
    s = non_alnum_re.sub(' ', s)
    s = multisp_re.sub(' ', s)
    return s.strip()

# Preprocess tracks: fix cases where title contains 'artist - title' and artist missing

def split_title_artist(row):
    title = '' if pd.isna(row.get('title')) else str(row.get('title'))
    artist = '' if pd.isna(row.get('artist')) else str(row.get('artist'))
    if (not artist or artist.strip().lower() in ('none','')) and ' - ' in title:
        parts = title.split(' - ', 1)
        # assume left is artist, right is title
        artist_candidate = parts[0].strip()
        title_candidate = parts[1].strip()
        return title_candidate, artist_candidate
    return title, artist

tracks_df[['clean_title_raw','clean_artist_raw']] = tracks_df.apply(lambda r: pd.Series(split_title_artist(r)), axis=1)

# Normalize fields
for col in ['clean_title_raw','clean_artist_raw','album','year']:
    tracks_df[col] = tracks_df[col].fillna('')

tracks_df['norm_title'] = tracks_df['clean_title_raw'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['clean_artist_raw'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)
# Normalize year to digits only
tracks_df['norm_year'] = tracks_df['year'].astype(str).apply(lambda s: ''.join(re.findall(r'\d{2,4}', s)) if s and s.lower() not in ('none','nan') else '')

# Create entity key using available attributes
tracks_df['entity_key'] = (tracks_df['norm_title'] + '|' + tracks_df['norm_artist'] + '|' + tracks_df['norm_album'] + '|' + tracks_df['norm_year']).apply(lambda s: s.strip('|'))

# Aggregate sales by track_id
sales_agg = sales_df.groupby('track_id', dropna=True).agg({'revenue_usd': 'sum'}).reset_index()

# Merge with tracks
merged = pd.merge(tracks_df, sales_agg, how='left', left_on='track_id', right_on='track_id')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0.0)

# Aggregate by entity_key (entity resolution)
entity_grp = merged.groupby('entity_key').agg({
    'revenue_usd': 'sum',
    'track_id': lambda x: list(x.dropna().astype(int).unique()),
    'title': lambda x: x.dropna().astype(str).mode().iat[0] if not x.dropna().empty else '',
    'artist': lambda x: x.dropna().astype(str).mode().iat[0] if not x.dropna().empty else ''
}).reset_index()

# Find max revenue entity
entity_grp = entity_grp.sort_values('revenue_usd', ascending=False)
if entity_grp.empty:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'track_ids': []}
else:
    top = entity_grp.iloc[0]
    result = {
        'title': top['title'],
        'artist': top['artist'],
        'total_revenue_usd': round(float(top['revenue_usd']), 2),
        'track_ids': top['track_id']
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IPEie9R1lxLsbAgDohNfLkLw': ['tracks'], 'var_call_2mDq8gZtx0E7k3Q5LzFh9mMI': ['sales'], 'var_call_A5Y1y31G3ibipHAtuujdK7Mf': 'file_storage/call_A5Y1y31G3ibipHAtuujdK7Mf.json', 'var_call_iV526ETgONRMqZbLiMscV0Lc': 'file_storage/call_iV526ETgONRMqZbLiMscV0Lc.json'}

exec(code, env_args)
