code = """import json
import pandas as pd
import re

# Load data from storage variables (file paths)
tracks_path = var_call_UsgRyyU5oGCdccLQcpJh2pEq
sales_path = var_call_ft9F3k93luiBxl2t6hJKu1AG

def load_json(path_or_obj):
    if isinstance(path_or_obj, str):
        # it's a filepath
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return path_or_obj

tracks = load_json(tracks_path)
sales = load_json(sales_path)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize and clean columns
for df, col_types in [(tracks_df, {'track_id': int}), (sales_df, {'sale_id': int, 'track_id': int, 'units_sold': int})]:
    # attempt conversions if columns exist
    for col, typ in col_types.items():
        if col in df.columns:
            try:
                df[col] = df[col].astype(typ)
            except Exception:
                # coerce
                df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')

# revenue_usd to float
if 'revenue_usd' in sales_df.columns:
    sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0).astype(float)

# Normalization helper
_non_alnum_re = re.compile(r'[^0-9a-z ]')
_multispace_re = re.compile(r'\s+')

def norm_text(x):
    if x is None:
        return ''
    s = str(x)
    if s.lower() in ['none', 'nan', 'nan.0', "nan"]:
        return ''
    s = s.lower()
    # remove parenthetical content which often contains live/acoustic notes
    s = re.sub(r"\([^)]*\)", " ", s)
    s = _non_alnum_re.sub(' ', s)
    s = _multispace_re.sub(' ', s).strip()
    return s

# Create normalized keys using title + artist + album
for col in ['title', 'artist', 'album']:
    if col not in tracks_df.columns:
        tracks_df[col] = ''

tracks_df['title_norm'] = tracks_df['title'].apply(norm_text)
tracks_df['artist_norm'] = tracks_df['artist'].apply(norm_text)
tracks_df['album_norm'] = tracks_df['album'].apply(norm_text)

# Entity key
tracks_df['entity_key'] = (tracks_df['title_norm'] + '|' + tracks_df['artist_norm']).replace('nan|nan', '')

# Aggregate sales by track_id
sales_agg = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()
# track_id in sales may be int or str; ensure types match
# Convert tracks_df.track_id to int where possible
try:
    tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'], errors='coerce').astype('Int64')
except Exception:
    pass

# Merge sales with tracks
merged = pd.merge(sales_agg, tracks_df, on='track_id', how='left')

# For any sales with missing track metadata, fill entity_key with track_id
merged['entity_key'] = merged['entity_key'].fillna('')
missing_mask = merged['entity_key'] == ''
merged.loc[missing_mask, 'entity_key'] = merged.loc[missing_mask, 'track_id'].astype(str)

# Aggregate revenue by entity_key (entity resolution)
entity_agg = merged.groupby('entity_key', as_index=False).agg({'revenue_usd': 'sum'})
# find max
max_row = entity_agg.loc[entity_agg['revenue_usd'].idxmax()]
max_key = max_row['entity_key']
max_revenue = float(max_row['revenue_usd'])

# Get representative metadata for this entity: choose the most common (non-empty) title/artist/album among tracks mapping to this key
tracks_for_entity = tracks_df[tracks_df['entity_key'] == max_key]
if tracks_for_entity.empty:
    # maybe the key is just track_id string
    tid = int(max_key)
    # find track row
    tr = tracks_df[tracks_df['track_id'] == tid]
    if not tr.empty:
        rep = tr.iloc[0]
        rep_title = rep['title']
        rep_artist = rep['artist']
        rep_album = rep['album']
        track_ids = [int(tid)]
    else:
        rep_title = ''
        rep_artist = ''
        rep_album = ''
        track_ids = []
else:
    # pick most frequent non-empty title
    def pick_most_common(col):
        vals = tracks_for_entity[col].dropna().astype(str)
        vals = vals[~vals.str.lower().isin(['none', 'nan', 'nan.0', ""])]
        if vals.empty:
            return ''
        return vals.value_counts().idxmax()

    rep_title = pick_most_common('title')
    rep_artist = pick_most_common('artist')
    rep_album = pick_most_common('album')
    track_ids = tracks_for_entity['track_id'].dropna().astype(int).unique().tolist()

result = {
    'title': rep_title,
    'artist': rep_artist,
    'album': rep_album,
    'total_revenue_usd': round(max_revenue, 2),
    'matched_track_ids': track_ids,
    'entity_key': max_key
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UsgRyyU5oGCdccLQcpJh2pEq': 'file_storage/call_UsgRyyU5oGCdccLQcpJh2pEq.json', 'var_call_ft9F3k93luiBxl2t6hJKu1AG': 'file_storage/call_ft9F3k93luiBxl2t6hJKu1AG.json'}

exec(code, env_args)
