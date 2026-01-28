code = """import json
import pandas as pd
import re

# Load data from storage paths
with open(var_call_dEMYOPD4LBJ7h42alJqtJU2H, 'r') as f:
    tracks = json.load(f)
with open(var_call_KcfUv7xeBl4n1OctCF3GGCJH, 'r') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure proper types
if 'track_id' in df_tracks.columns:
    df_tracks['track_id'] = df_tracks['track_id'].astype(int)
if 'track_id' in df_sales.columns:
    df_sales['track_id'] = df_sales['track_id'].astype(int)

# Convert revenue to float
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)

# Normalization function
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', '', 'nan', 'na', "[unknown]", '   '):
        return ''
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # lowercase
    s = s.lower()
    # remove punctuation except spaces and alphanumerics
    s = re.sub(r"[^0-9a-z ]+", "", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Apply normalization to title and artist (and album/year)
for col in ['title', 'artist', 'album', 'year']:
    if col in df_tracks.columns:
        df_tracks[f'norm_{col}'] = df_tracks[col].apply(normalize_text)
    else:
        df_tracks[f'norm_{col}'] = ''

# Build a dedup key prioritizing title+artist, fallback to title+album+year
def dedup_key(row):
    if row['norm_artist']:
        return row['norm_title'] + '|' + row['norm_artist']
    # if artist missing, use album and year to help
    return row['norm_title'] + '|' + row['norm_album'] + '|' + row['norm_year']

df_tracks['dedup_key'] = df_tracks.apply(dedup_key, axis=1)

# Group tracks by dedup_key and collect track_ids
groups = df_tracks.groupby('dedup_key').agg({
    'track_id': lambda ids: list(ids),
    'title': lambda vals: vals.dropna().astype(str).loc[vals.astype(str).str.lower()!='none'].iloc[0] if any(vals.astype(str).str.lower()!='none') else vals.iloc[0],
    'artist': lambda vals: vals.dropna().astype(str).loc[vals.astype(str).str.lower()!='none'].iloc[0] if any(vals.astype(str).str.lower()!='none') else vals.iloc[0]
}).rename(columns={'title':'rep_title','artist':'rep_artist'}).reset_index()

# Sum revenue per track_id
revenue_per_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Map revenue to groups by summing revenues of member track_ids
def sum_group_revenue(track_id_list):
    s = 0.0
    details = []
    for tid in track_id_list:
        row = revenue_per_track[revenue_per_track['track_id']==tid]
        if not row.empty:
            val = float(row['revenue_usd'].iloc[0])
        else:
            val = 0.0
        s += val
        details.append({'track_id': int(tid), 'revenue_usd': round(val, 2)})
    return pd.Series([round(s,2), details])

groups[['total_revenue_usd','revenue_by_track']] = groups['track_id'].apply(sum_group_revenue)

# Find max revenue group
max_idx = groups['total_revenue_usd'].idxmax()
max_group = groups.loc[max_idx]

result = {
    'title': str(max_group['rep_title']),
    'artist': str(max_group['rep_artist']),
    'total_revenue_usd': float(max_group['total_revenue_usd']),
    'contributing_track_ids': [int(t) for t in max_group['track_id']],
    'revenue_by_track': max_group['revenue_by_track']
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dEMYOPD4LBJ7h42alJqtJU2H': 'file_storage/call_dEMYOPD4LBJ7h42alJqtJU2H.json', 'var_call_KcfUv7xeBl4n1OctCF3GGCJH': 'file_storage/call_KcfUv7xeBl4n1OctCF3GGCJH.json'}

exec(code, env_args)
