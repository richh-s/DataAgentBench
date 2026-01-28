code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage-provided file paths
tracks_path = var_call_ayltcv6R6h3XkIP2tsWbzWOV
sales_path = var_call_NidmLYU5jksboUYcD9rBGo3a

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize types and missing values
tracks_df = tracks_df.fillna('')
tracks_df = tracks_df.replace({'None': ''})

sales_df = sales_df.fillna('')
sales_df = sales_df.replace({'None': ''})

# Ensure numeric types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'], errors='coerce').astype('Int64')
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'], errors='coerce').astype('Int64')

# Normalization helpers
def strip_accents(s):
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    return s

paren_re = re.compile(r"\(.*?\)")
non_alnum_re = re.compile(r'[^a-z0-9\s]')
multispace_re = re.compile(r'\s+')

def normalize_title_artist(title, artist):
    title = '' if pd.isna(title) else str(title)
    artist = '' if pd.isna(artist) else str(artist)

    # If artist is empty but title contains ' - ' assume 'Artist - Title' format
    if (artist.strip() == '' or artist.strip().lower() in ['none', '[unknown]']) and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            left, right = parts
            # Heuristic: if left looks like an artist (no parentheses and has letters), use it
            if len(left.strip()) > 0 and len(right.strip()) > 0:
                artist_candidate = left.strip()
                title_candidate = right.strip()
                artist = artist_candidate
                title = title_candidate

    # Remove parenthetical content from title
    title = paren_re.sub('', title)

    # Normalize accents and lowercase
    title = strip_accents(title).lower()
    artist = strip_accents(artist).lower()

    # Remove common extraneous markers like 'feat', 'remix' from title and artist
    # Keep it simple: remove content after ':' in title, which often contains metadata
    if ':' in title:
        title = title.split(':', 1)[0]

    # Remove non-alphanumeric characters
    title = non_alnum_re.sub(' ', title)
    artist = non_alnum_re.sub(' ', artist)

    # Collapse whitespace and strip
    title = multispace_re.sub(' ', title).strip()
    artist = multispace_re.sub(' ', artist).strip()

    return title, artist

# Apply normalization
tracks_df[['title_norm', 'artist_norm']] = tracks_df.apply(lambda row: pd.Series(normalize_title_artist(row.get('title',''), row.get('artist',''))), axis=1)

# Create canonical key using title + artist primarily
tracks_df['canonical_key'] = tracks_df.apply(lambda r: (r['title_norm'] + '||' + r['artist_norm']).strip(' |') , axis=1)

# For empty artist, key is just title
tracks_df.loc[tracks_df['artist_norm']=='', 'canonical_key'] = tracks_df.loc[tracks_df['artist_norm']=='', 'title_norm']

# Group track_ids by canonical_key
grouped = tracks_df.groupby('canonical_key')['track_id'].apply(list).reset_index()

# Map each track_id to a canonical representative (choose smallest track_id)
track_to_entity = {}
entity_representative = {}
for _, row in grouped.iterrows():
    key = row['canonical_key']
    ids = [int(x) for x in row['track_id'] if not pd.isna(x)]
    if not ids:
        continue
    rep = min(ids)
    entity_representative[rep] = key
    for tid in ids:
        track_to_entity[tid] = rep

# Aggregate sales by track_id
sales_agg = sales_df.groupby('track_id', dropna=True)['revenue_usd'].sum().reset_index()

# Map sales track_id to entity representative
sales_agg['track_id_int'] = sales_agg['track_id'].astype('Int64')

# For sales track_ids not in tracks, they won't map; handle gracefully by using their own id
sales_agg['entity'] = sales_agg['track_id_int'].apply(lambda x: int(track_to_entity[x]) if (not pd.isna(x) and int(x) in track_to_entity) else (int(x) if not pd.isna(x) else None))

# Sum revenue by entity
entity_revenue = sales_agg.groupby('entity')['revenue_usd'].sum().reset_index()

# Find top entity
if entity_revenue.empty:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'track_ids': []}
else:
    top = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]
    top_entity = int(top['entity'])
    top_revenue = float(top['revenue_usd'])

    # Determine representative title and artist from tracks_df for the entity
    rep_row = tracks_df[tracks_df['track_id'] == top_entity]
    if not rep_row.empty:
        rep_title = rep_row.iloc[0].get('title','')
        rep_artist = rep_row.iloc[0].get('artist','')
    else:
        # If representative not found, try to pull any track that maps to this entity
        mapped_ids = [tid for tid,v in track_to_entity.items() if v==top_entity]
        rep_title = ''
        rep_artist = ''
        if mapped_ids:
            r = tracks_df[tracks_df['track_id'] == mapped_ids[0]]
            if not r.empty:
                rep_title = r.iloc[0].get('title','')
                rep_artist = r.iloc[0].get('artist','')

    # Also list all track_ids that correspond
    linked_track_ids = [tid for tid,v in track_to_entity.items() if v==top_entity]

    result = {
        'title': rep_title if rep_title is not None else '',
        'artist': rep_artist if rep_artist is not None else '',
        'total_revenue_usd': round(top_revenue, 2),
        'track_ids': linked_track_ids
    }

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_MRQtOKBsQiZyQwSabAJpVV8v': ['tracks'], 'var_call_QU2F8pyOgb511xShGBwxpyDR': ['sales'], 'var_call_ayltcv6R6h3XkIP2tsWbzWOV': 'file_storage/call_ayltcv6R6h3XkIP2tsWbzWOV.json', 'var_call_NidmLYU5jksboUYcD9rBGo3a': 'file_storage/call_NidmLYU5jksboUYcD9rBGo3a.json'}

exec(code, env_args)
