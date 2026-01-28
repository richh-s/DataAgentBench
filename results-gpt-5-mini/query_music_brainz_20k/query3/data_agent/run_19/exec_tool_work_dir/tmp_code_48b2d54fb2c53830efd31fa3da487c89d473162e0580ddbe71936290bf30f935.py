code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_AVLqUJcWn6h0bAHGBtnFobhc, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_iL10fxtaLS3sBa5sVknhu6pf, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure numeric types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Normalize function
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ('none', 'nan', ''):
        return ''
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    # replace common qualifiers
    s = re.sub(r"\b(live|remix|acoustic|version|edit|original|feat\.?|ft\.?|remastered)\b", "", s, flags=re.I)
    # remove non-alphanumeric
    s = re.sub(r"[^0-9a-zA-Z]+", " ", s)
    s = s.lower().strip()
    # collapse spaces
    s = re.sub(r"\s+", " ", s)
    return s

# Apply normalization
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)

# Create grouping key using title + artist (fallback to album if artist missing)
tracks_df['entity_key'] = tracks_df.apply(lambda r: (r['norm_title'] + ' || ' + (r['norm_artist'] if r['norm_artist'] else r['norm_album'])).strip(), axis=1)

# Sum revenue per track_id from sales
sales_by_track = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Merge with tracks to map track_id to entity_key
merged = pd.merge(sales_by_track, tracks_df[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# For track_ids without a matching track record, keep track_id as its own key
merged['entity_key'] = merged['entity_key'].fillna(merged['track_id'].astype(str))

# Aggregate revenue by entity_key
agg = merged.groupby('entity_key').agg(
    total_revenue_usd = ('revenue_usd','sum'),
    contributing_track_ids = ('track_id', lambda x: list(x.astype(str))),
    num_track_records = ('track_id', 'nunique')
).reset_index()

# Attach a representative title/artist/album/year by picking the most frequent among group
rep = merged.groupby('entity_key').agg(
    rep_title = ('title', lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else ''),
    rep_artist = ('artist', lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else ''),
    rep_album = ('album', lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else ''),
    rep_year = ('year', lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else '')
).reset_index()

agg = agg.merge(rep, on='entity_key', how='left')

# Find max revenue
agg['total_revenue_usd'] = agg['total_revenue_usd'].astype(float)
max_row = agg.loc[agg['total_revenue_usd'].idxmax()]

result = {
    'title': max_row['rep_title'] if pd.notna(max_row['rep_title']) else None,
    'artist': max_row['rep_artist'] if pd.notna(max_row['rep_artist']) else None,
    'album': max_row['rep_album'] if pd.notna(max_row['rep_album']) else None,
    'year': max_row['rep_year'] if pd.notna(max_row['rep_year']) else None,
    'total_revenue_usd': round(float(max_row['total_revenue_usd']),2),
    'contributing_track_ids': max_row['contributing_track_ids'],
    'num_track_records': int(max_row['num_track_records'])
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AVLqUJcWn6h0bAHGBtnFobhc': 'file_storage/call_AVLqUJcWn6h0bAHGBtnFobhc.json', 'var_call_iL10fxtaLS3sBa5sVknhu6pf': 'file_storage/call_iL10fxtaLS3sBa5sVknhu6pf.json'}

exec(code, env_args)
