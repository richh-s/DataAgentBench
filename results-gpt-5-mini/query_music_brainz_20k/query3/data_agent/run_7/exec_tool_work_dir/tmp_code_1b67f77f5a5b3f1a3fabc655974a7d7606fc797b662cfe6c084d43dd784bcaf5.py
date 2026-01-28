code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage file paths
tracks_path = var_call_Prsov1T2ibSdMPH83TN1R9za
sales_path = var_call_tzT3J9ypH2x99ByQ6mBybvfK

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Normalize types
# Some values may be strings; convert track_id columns to int
for df in (df_tracks, df_sales):
    if 'track_id' in df.columns:
        df['track_id'] = pd.to_numeric(df['track_id'], errors='coerce').astype('Int64')

# Convert revenue to numeric
if 'revenue_usd' in df_sales.columns:
    df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Merge sales with track metadata
df = df_sales.merge(df_tracks, on='track_id', how='left', suffixes=('_sale', '_track'))

# Normalization functions
def remove_parenthetical(s):
    return re.sub(r"\([^)]*\)", "", s)

def strip_brackets(s):
    return re.sub(r"\[[^]]*\]", "", s)

def normalize_text(s):
    if s is None:
        return ''
    if isinstance(s, float) and pd.isna(s):
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', "nan", "na", "[unknown]", "unknown", "\\u2013", ""):
        return ''
    # remove parenthetical and bracketed content
    s = remove_parenthetical(s)
    s = strip_brackets(s)
    # remove common live/performance timestamps after colon or dash
    s = re.split(' - |: ', s)[0]
    # unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # lower
    s = s.lower()
    # remove punctuation except alnum and spaces
    s = re.sub(r"[^0-9a-z\\s]", "", s)
    # collapse spaces
    s = re.sub(r"\\s+", " ", s)
    return s.strip()

# Apply normalization to title and artist and album
for col in ['title', 'artist', 'album']:
    if col in df.columns:
        df[col+'_norm'] = df[col].apply(normalize_text)
    else:
        df[col+'_norm'] = ''

# Create a grouping key: prefer title+artist; if artist missing, include album

def make_key(row):
    title = row.get('title_norm', '')
    artist = row.get('artist_norm', '')
    album = row.get('album_norm', '')
    if title == '' and album != '':
        title = album
    key = title
    if artist:
        key = key + '|' + artist
    else:
        key = key + '|' + album
    return key

df['entity_key'] = df.apply(make_key, axis=1)

# Aggregate revenue by entity_key
agg = df.groupby('entity_key').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    count_sales=('sale_id', 'count')
).reset_index()

# Find max
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False)
if agg_sorted.shape[0] == 0:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'track_ids': [],
        'final_answer_text': 'No data available.'
    }
else:
    top = agg_sorted.iloc[0]
    top_key = top['entity_key']
    top_revenue = float(round(top['total_revenue_usd'], 2))
    # gather representative metadata from one of the tracks in this group
    rows = df[df['entity_key'] == top_key]
    # choose most common title and artist among rows
    rep_title = rows['title'].dropna().astype(str).mode().iloc[0] if not rows['title'].dropna().empty else ''
    rep_artist = rows['artist'].dropna().astype(str).mode().iloc[0] if not rows['artist'].dropna().empty else ''
    track_ids = sorted(list(set([int(x) for x in rows['track_id'].dropna().unique()])))
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': top_revenue,
        'track_ids': track_ids,
        'count_sales_records': int(top['count_sales']),
        'final_answer_text': f"The song '{rep_title}' by {rep_artist} generated the highest total revenue: ${top_revenue:.2f}."
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Prsov1T2ibSdMPH83TN1R9za': 'file_storage/call_Prsov1T2ibSdMPH83TN1R9za.json', 'var_call_tzT3J9ypH2x99ByQ6mBybvfK': 'file_storage/call_tzT3J9ypH2x99ByQ6mBybvfK.json'}

exec(code, env_args)
