code = """import json
import pandas as pd
import re

# load previous query results from storage keys
with open(var_call_0g0jxxgNFNiYnmG9y24bYdoa, 'r') as f:
    tracks = json.load(f)
with open(var_call_9eNEPl4arSAezACNEb9CGPXq, 'r') as f:
    sales = json.load(f)

# create dataframes
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# ensure consistent types
for df, col in [(df_tracks, 'track_id'), (df_sales, 'track_id')]:
    if col in df.columns:
        df[col] = df[col].astype(str)

# convert revenue to float
if 'revenue_usd' in df_sales.columns:
    df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)
else:
    df_sales['revenue_usd'] = 0.0

# normalization function
def normalize(s):
    if s is None:
        return ''
    s = str(s)
    if s.strip().lower() in ['none', 'nan', '']:
        return ''
    # remove parenthetical and bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # remove common separators like '-' used to add extra info after artist/title
    s = re.split(r"[-—:–]", s)[0]
    # remove non-alphanumeric characters except spaces
    s = re.sub(r"[^0-9a-zA-Z ]+", " ", s)
    s = s.lower()
    s = re.sub(r"\s+", " ", s).strip()
    return s

# apply normalization
if 'title' in df_tracks.columns:
    df_tracks['norm_title'] = df_tracks['title'].apply(normalize)
else:
    df_tracks['norm_title'] = ''

if 'artist' in df_tracks.columns:
    df_tracks['norm_artist'] = df_tracks['artist'].apply(normalize)
else:
    df_tracks['norm_artist'] = ''

# canonical key
df_tracks['canonical'] = df_tracks['norm_title'] + '||' + df_tracks['norm_artist']

# merge sales with tracks
df_merged = pd.merge(df_sales, df_tracks, how='left', on='track_id', suffixes=('_sale', '_track'))

# For sales rows without a matching track, create canonical from empty title
missing_tracks = df_merged['canonical'].isna().sum()
if missing_tracks > 0:
    df_merged['canonical'] = df_merged['canonical'].fillna('')

# compute revenue per canonical
grouped = df_merged.groupby('canonical').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    sales_records=('sale_id', 'count')
).reset_index()

# compute representative title/artist per canonical by choosing the track_id within canonical with highest revenue
# first compute revenue per track_id
rev_per_track = df_merged.groupby('track_id').agg(track_revenue=('revenue_usd', 'sum')).reset_index()
# merge back to tracks to know canonical and original title/artist
rev_tracks = pd.merge(rev_per_track, df_tracks[['track_id', 'canonical', 'title', 'artist']], on='track_id', how='left')

# for each canonical, pick the track with max track_revenue
rep = rev_tracks.sort_values(['canonical', 'track_revenue'], ascending=[True, False]).groupby('canonical').first().reset_index()
rep = rep[['canonical', 'title', 'artist']]

# combine
summary = pd.merge(grouped, rep, on='canonical', how='left')

# find top canonical by total_revenue_usd
summary_sorted = summary.sort_values('total_revenue_usd', ascending=False)
if summary_sorted.shape[0] == 0:
    result = {"title": None, "artist": None, "total_revenue_usd": 0.0, "sales_records": 0, "contributing_track_ids": []}
else:
    top = summary_sorted.iloc[0]
    top_canonical = top['canonical']
    top_title = top['title'] if pd.notna(top['title']) else ''
    top_artist = top['artist'] if pd.notna(top['artist']) else ''
    top_revenue = float(top['total_revenue_usd'])
    top_sales_records = int(top['sales_records'])
    # contributing track ids
    contributing = df_merged.loc[df_merged['canonical'] == top_canonical, 'track_id'].dropna().unique().tolist()
    result = {"title": top_title, "artist": top_artist, "total_revenue_usd": round(top_revenue, 2), "sales_records": top_sales_records, "contributing_track_ids": contributing}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0g0jxxgNFNiYnmG9y24bYdoa': 'file_storage/call_0g0jxxgNFNiYnmG9y24bYdoa.json', 'var_call_9eNEPl4arSAezACNEb9CGPXq': 'file_storage/call_9eNEPl4arSAezACNEb9CGPXq.json'}

exec(code, env_args)
