code = """import pandas as pd
import re
import json

# Load data from storage file paths
tracks = pd.read_json(var_call_W2YcNklkq0YoBazzqyHV7R9n)
sales = pd.read_json(var_call_mqUlTU9mv8gGYR2YiRDWEXxr)

# Ensure correct dtypes
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)

# Normalization function
def norm_text(s):
    if pd.isna(s):
        return ''
    s = str(s).strip()
    if s.lower() in ['none','[unknown]','', '   ']:
        return ''
    # remove content in parentheses/brackets
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    s = s.lower()
    # replace non-alphanumeric with space
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    # remove common descriptors
    s = re.sub(r'\b(live|remix|acoustic|version|feat|featuring|ft|remastered|edit)\b', '', s)
    # remove standalone years/numbers
    s = re.sub(r'\b\d{2,4}\b', '', s)
    # collapse spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Build entity key for each track
def make_key(row):
    title = norm_text(row.get('title',''))
    artist = norm_text(row.get('artist',''))
    album = norm_text(row.get('album',''))
    year = norm_text(row.get('year',''))
    if artist:
        return title + ' || ' + artist
    else:
        return title + ' || ' + album + ' || ' + year

tracks['entity_key'] = tracks.apply(make_key, axis=1)

# Map track_id to entity_key
track_to_entity = tracks.set_index('track_id')['entity_key'].to_dict()

# Map sales to entity
sales['entity_key'] = sales['track_id'].map(track_to_entity)

# Convert revenue to float
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)

# Aggregate revenue by entity_key
revenue_by_entity = sales.groupby('entity_key', dropna=True)['revenue_usd'].sum().reset_index()

# Find max revenue
if revenue_by_entity.empty:
    result = {"error": "No sales data available"}
else:
    top = revenue_by_entity.sort_values('revenue_usd', ascending=False).iloc[0]
    top_key = top['entity_key']
    total_revenue = float(top['revenue_usd'])
    # collect all track_ids belonging to this entity
    track_ids = tracks[tracks['entity_key'] == top_key]['track_id'].tolist()
    # choose representative title and artist: most common non-empty
    def most_common_nonempty(series):
        vals = series.dropna().astype(str).str.strip()
        vals = vals[~vals.isin(['','None','[unknown]'])]
        if vals.empty:
            return ''
        return vals.value_counts().idxmax()
    rep_title = most_common_nonempty(tracks[tracks['entity_key']==top_key]['title'])
    rep_artist = most_common_nonempty(tracks[tracks['entity_key']==top_key]['artist'])
    result = {
        "representative_title": rep_title,
        "representative_artist": rep_artist,
        "track_ids": track_ids,
        "total_revenue_usd": round(total_revenue, 2)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W2YcNklkq0YoBazzqyHV7R9n': 'file_storage/call_W2YcNklkq0YoBazzqyHV7R9n.json', 'var_call_mqUlTU9mv8gGYR2YiRDWEXxr': 'file_storage/call_mqUlTU9mv8gGYR2YiRDWEXxr.json'}

exec(code, env_args)
