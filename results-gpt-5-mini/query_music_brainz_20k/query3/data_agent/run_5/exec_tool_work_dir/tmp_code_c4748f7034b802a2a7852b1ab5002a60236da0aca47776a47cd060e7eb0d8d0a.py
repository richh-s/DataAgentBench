code = """import json
import pandas as pd
import re
import unicodedata

# Load data from previous query results (file paths stored in variables)
tracks_path = var_call_BhzMJfPgM9BSevCdAbACYAR4
sales_path = var_call_uf1TVDzlYNflgPVtg2zGATDe

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize types
for col in ['track_id', 'source_id']:
    if col in tracks_df.columns:
        tracks_df[col] = pd.to_numeric(tracks_df[col], errors='coerce')

sales_df['track_id'] = pd.to_numeric(sales_df['track_id'], errors='coerce')
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')

# Normalization function for titles and artists

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    # Remove common placeholders
    if s.lower() in ['none', "nan", "n/a", ""]:
        return ''
    # Unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # Remove parenthetical/bracket content
    s = re.sub(r"\(.*?\)|\[.*?\]|\{.*?\}", ' ', s)
    # Lowercase
    s = s.lower()
    # Remove common descriptors
    s = re.sub(r"\b(live|remix|acoustic|radio edit|version|feat\.|feat|ft\.|ft|remastered|live at|instrumental)\b", ' ', s)
    # Remove punctuation
    s = re.sub(r"[^a-z0-9& ]+", ' ', s)
    # Collapse whitespace
    s = re.sub(r"\s+", ' ', s)
    s = s.strip()
    return s

tracks_df['title_norm'] = tracks_df['title'].apply(normalize_text)
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_text)

# Create signature: prefer title + artist; if artist missing, use title only
tracks_df['signature'] = tracks_df.apply(lambda r: (r['title_norm'] + '||' + r['artist_norm']).strip('||') if (r['title_norm'] or r['artist_norm']) else '', axis=1)

# For rows where signature is empty, fallback to title raw
tracks_df.loc[tracks_df['signature']=='', 'signature'] = tracks_df.loc[tracks_df['signature']=='', 'title'].fillna('')

# Map track_id to signature
trackid_to_sig = tracks_df.set_index('track_id')['signature'].to_dict()

# Assign signature to sales
sales_df['signature'] = sales_df['track_id'].map(trackid_to_sig)

# For any sales with missing signature (no matching track_id), set as unknown
sales_df['signature'] = sales_df['signature'].fillna('')

# Aggregate revenue by signature
agg = sales_df.groupby('signature', dropna=False)['revenue_usd'].sum().reset_index()
# Find max
agg_sorted = agg.sort_values('revenue_usd', ascending=False)
if agg_sorted.shape[0]==0:
    result = {"title": None, "artist": None, "total_revenue_usd": 0.0, "track_ids": [], "num_tracks": 0}
else:
    top = agg_sorted.iloc[0]
    top_sig = top['signature']
    top_revenue = float(top['revenue_usd']) if not pd.isna(top['revenue_usd']) else 0.0
    # Find representative title and artist from tracks for this signature
    matches = tracks_df[tracks_df['signature']==top_sig]
    if not matches.empty:
        # Choose the most common (mode) title and artist
        rep_title = matches['title'].mode().iloc[0] if matches['title'].mode().size>0 else matches['title'].iloc[0]
        rep_artist = matches['artist'].mode().iloc[0] if matches['artist'].mode().size>0 else matches['artist'].iloc[0]
        track_ids = matches['track_id'].dropna().astype(int).astype(str).tolist()
        num_tracks = len(track_ids)
    else:
        rep_title = ''
        rep_artist = ''
        track_ids = []
        num_tracks = 0
    result = {
        "title": rep_title,
        "artist": rep_artist,
        "total_revenue_usd": round(top_revenue, 2),
        "track_ids": track_ids,
        "num_tracks": num_tracks,
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0E53r1NVs26S8I5czEcdVNj9': ['tracks'], 'var_call_BbzpGLC6b1WY3zcAeuSqJpaW': ['sales'], 'var_call_BhzMJfPgM9BSevCdAbACYAR4': 'file_storage/call_BhzMJfPgM9BSevCdAbACYAR4.json', 'var_call_uf1TVDzlYNflgPVtg2zGATDe': 'file_storage/call_uf1TVDzlYNflgPVtg2zGATDe.json'}

exec(code, env_args)
