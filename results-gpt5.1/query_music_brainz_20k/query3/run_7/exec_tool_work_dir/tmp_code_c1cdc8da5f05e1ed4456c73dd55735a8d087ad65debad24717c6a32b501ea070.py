code = """import json, pandas as pd

# Load full results from files
with open(var_call_rph01zd62uwMAKHNuKgj50Rt, 'r') as f:
    tracks = json.load(f)
with open(var_call_MGifTbMQpT6O72lau5rBrooB, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric columns
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Basic cleaning: normalize title and artist for matching
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Heuristic: define a canonical key per real-world track based on normalized title + artist + album (when available)
# Some fields like year/length are noisy, so use them only when present and short
tracks_df['year_norm'] = tracks_df['year'].fillna('').astype(str).str.strip()
tracks_df['length_norm'] = tracks_df['length'].fillna('').astype(str).str.strip()

# Use title + artist as primary key; fall back to title + album if artist missing/unknown-like
unknown_markers = set(['none', 'unknown', '[unknown]', ''])

def make_key(row):
    title = row['title']
    artist = row['artist']
    album = row['album']
    # strip punctuation & spaces for robustness
    import re
    def norm(s):
        return re.sub(r'[^a-z0-9]+', '', s)
    t = norm(title)
    a = norm(artist)
    al = norm(album)
    if a and artist not in unknown_markers:
        return f"ta::{t}::{a}"
    elif al:
        return f"tal::{t}::{al}"
    else:
        return f"t::{t}"

tracks_df['entity_key'] = tracks_df.apply(make_key, axis=1)

# Map each track_id to an entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']
sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity (real-world track)
entity_rev = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Get top entity
top_entity = entity_rev.sort_values('revenue_usd', ascending=False).iloc[0]

# For that entity, find a representative track row (e.g., the one with most complete info)
entity_tracks = tracks_df[tracks_df['entity_key'] == top_entity['entity_key']].copy()

# Score completeness
def completeness_score(row):
    score = 0
    for col in ['title', 'artist', 'album', 'year', 'language']:
        v = str(row[col]) if pd.notna(row[col]) else ''
        if v and v.lower() not in ['none', 'unknown', '[unknown]']:
            score += 1
    return score

entity_tracks['score'] = entity_tracks.apply(completeness_score, axis=1)
rep = entity_tracks.sort_values('score', ascending=False).iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(float(top_entity['revenue_usd']), 2)
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_rph01zd62uwMAKHNuKgj50Rt': 'file_storage/call_rph01zd62uwMAKHNuKgj50Rt.json', 'var_call_MGifTbMQpT6O72lau5rBrooB': 'file_storage/call_MGifTbMQpT6O72lau5rBrooB.json'}

exec(code, env_args)
