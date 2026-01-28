code = """import json
import pandas as pd
import re
import unicodedata

# Load the query results from storage files
with open(var_call_ARLX7qRFhJEtf3lcXnZiYUgo, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)
with open(var_call_4EnrJGe8FPLob9QEhtLQIgH1, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

# Convert to DataFrame
sales_df = pd.DataFrame(sales_agg)
# Ensure proper types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)

tracks_df = pd.DataFrame(tracks)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Normalization helper
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ('none', 'nan', '[unknown]', ''):
        return ''
    # remove parenthetical/bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # remove common separators like ' - ' that sometimes include artist in title
    # but only if it looks like 'Artist - Title' inside the title field; we'll keep as is
    # normalize unicode
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    # keep alphanumeric and spaces
    s = re.sub(r'[^0-9a-zA-Z ]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

# Apply normalization
tracks_df['title_norm'] = tracks_df['title'].apply(normalize_text)
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_text)
tracks_df['album_norm'] = tracks_df['album'].apply(normalize_text)
tracks_df['year_norm'] = tracks_df['year'].apply(lambda x: str(x).strip() if x not in (None, 'None') else '')

# Create entity key using title + artist primarily
tracks_df['entity_key'] = tracks_df['title_norm'] + '||' + tracks_df['artist_norm']

# Merge sales totals with tracks
merged = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# For sales with missing track metadata, create fallback entity
merged['title_norm'] = merged['title_norm'].fillna('')
merged['artist_norm'] = merged['artist_norm'].fillna('')
merged['entity_key'] = merged['title_norm'] + '||' + merged['artist_norm']

# Aggregate revenue by entity_key
entity_agg = merged.groupby('entity_key').agg(
    total_revenue_usd = ('total_revenue_usd', 'sum'),
    track_ids = ('track_id', lambda ids: sorted(list(set(ids))))
).reset_index()

# Find top entity
top = entity_agg.sort_values('total_revenue_usd', ascending=False).iloc[0]

# Get representative title and artist from tracks_df for this entity
entity_key = top['entity_key']
track_ids = top['track_ids']
recs = tracks_df[tracks_df['entity_key'] == entity_key]
if len(recs) > 0:
    # choose the most common original title and artist (non-empty)
    rep_title = recs['title'].replace('None', '').replace('nan', '').dropna().astype(str)
    rep_artist = recs['artist'].replace('None', '').replace('nan', '').dropna().astype(str)
    rep_title = rep_title[rep_title.str.strip() != ''] if len(rep_title) > 0 else pd.Series([''])
    rep_artist = rep_artist[rep_artist.str.strip() != ''] if len(rep_artist) > 0 else pd.Series([''])
    if len(rep_title) == 0:
        rep_title_val = ''
    else:
        # pick the most frequent; if tie, pick first
        rep_title_val = rep_title.mode().iloc[0]
    if len(rep_artist) == 0:
        rep_artist_val = ''
    else:
        rep_artist_val = rep_artist.mode().iloc[0]
else:
    # Fallback to values from merged (could be missing)
    rep = merged[merged['entity_key'] == entity_key].iloc[0]
    rep_title_val = rep['title_norm']
    rep_artist_val = rep['artist_norm']

result = {
    'title': rep_title_val,
    'artist': rep_artist_val,
    'total_revenue_usd': round(float(top['total_revenue_usd']), 2),
    'aggregated_track_ids': track_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YoQm7OABNP9pcDbqSGb62K1D': ['tracks'], 'var_call_fKoKAoa06rBGvHkgXtVvlFXE': ['sales'], 'var_call_ARLX7qRFhJEtf3lcXnZiYUgo': 'file_storage/call_ARLX7qRFhJEtf3lcXnZiYUgo.json', 'var_call_4EnrJGe8FPLob9QEhtLQIgH1': 'file_storage/call_4EnrJGe8FPLob9QEhtLQIgH1.json'}

exec(code, env_args)
