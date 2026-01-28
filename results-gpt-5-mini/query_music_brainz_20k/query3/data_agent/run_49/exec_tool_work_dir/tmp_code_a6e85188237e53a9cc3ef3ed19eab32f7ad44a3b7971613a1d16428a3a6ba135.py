code = """import json
import pandas as pd
import unicodedata
import re

# Load previous tool results from files
with open(var_call_HLDgQC4bNxK0XECLUUmEqCwz, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_VFAOGtOHKbslz2q2XOg2UI2Y, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure track_id columns are strings
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Convert revenue to numeric
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Aggregate revenue by track_id
revenue_by_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Merge aggregated revenue with track metadata
merged = revenue_by_track.merge(df_tracks, on='track_id', how='left')

# Normalization utilities
remove_words = ['live', 'remix', 'acoustic', 'version', 'feat', 'featuring', 'remastered', 'edit', 'intro', 'outro', 'radio', 'single']

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', '[unknown]', ''):
        return ''
    # remove content in parentheses/brackets
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # unicode normalize
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = s.lower()
    # remove punctuation
    s = re.sub(r"[^0-9a-z\s]", " ", s)
    # remove remove_words
    for w in remove_words:
        s = re.sub(r"\b" + re.escape(w) + r"\b", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Apply normalization
merged['title_norm'] = merged['title'].apply(normalize_text)
merged['artist_norm'] = merged['artist'].apply(normalize_text)
merged['album_norm'] = merged['album'].apply(normalize_text)
merged['year_norm'] = merged['year'].fillna('').astype(str).apply(lambda y: (re.search(r"(\d{4})", y) or re.search(r"(\d{2})", y) or re.search(r"(\d+)", y)).group(0) if y and re.search(r"(\d{4})|\d{2}|\d+", y) else '')

# Build grouping key: prefer title+artist, if artist missing use title+album
def make_key(row):
    if row['title_norm'] == '':
        return ''
    if row['artist_norm'] != '':
        return row['title_norm'] + '|' + row['artist_norm']
    if row['album_norm'] != '':
        return row['title_norm'] + '|' + row['album_norm']
    # fallback to title only
    return row['title_norm']

merged['entity_key'] = merged.apply(make_key, axis=1)

# Group by entity_key and aggregate revenue and track_ids
grouped = merged.groupby('entity_key').agg({
    'revenue_usd': 'sum',
    'track_id': lambda ids: list(ids.dropna().unique()),
    'title': lambda vals: [v for v in vals.dropna().unique()],
    'artist': lambda vals: [v for v in vals.dropna().unique()]
}).reset_index()

# Remove empty keys
grouped = grouped[grouped['entity_key'].str.strip() != '']

# Find top group by revenue
if len(grouped) == 0:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'track_ids': []
    }
else:
    top = grouped.sort_values('revenue_usd', ascending=False).iloc[0]
    # pick representative title and artist: choose first non-null non-empty
    rep_title = None
    rep_artist = None
    if isinstance(top['title'], list) and len(top['title'])>0:
        for t in top['title']:
            if t and str(t).strip().lower() not in ('none', ''):
                rep_title = t
                break
    if isinstance(top['artist'], list) and len(top['artist'])>0:
        for a in top['artist']:
            if a and str(a).strip().lower() not in ('none', '[unknown]', ''):
                rep_artist = a
                break
    # fallback values
    if not rep_title:
        rep_title = top['entity_key'].split('|')[0]
    if not rep_artist:
        parts = top['entity_key'].split('|')
        rep_artist = parts[1] if len(parts)>1 else ''

    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(float(top['revenue_usd']), 2),
        'track_ids': top['track_id'],
        'group_count': len(top['track_id'])
    }

# Also create a plain text answer
title_disp = result['title'] if result['title'] is not None else ''
artist_disp = result['artist'] if result['artist'] is not None else ''
answer_text = f"{title_disp} by {artist_disp} generated the highest total revenue: ${result['total_revenue_usd']:.2f} across all stores and countries."

output = {
    'result': result,
    'answer_text': answer_text
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HLDgQC4bNxK0XECLUUmEqCwz': 'file_storage/call_HLDgQC4bNxK0XECLUUmEqCwz.json', 'var_call_VFAOGtOHKbslz2q2XOg2UI2Y': 'file_storage/call_VFAOGtOHKbslz2q2XOg2UI2Y.json'}

exec(code, env_args)
