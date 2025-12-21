code = """import json, pandas as pd

# Load full data from JSON files
with open(var_call_EBe54M4e39OdMrlvALYxXtlV, 'r') as f:
    tracks = json.load(f)
with open(var_call_QQiRgv5Um9SKlGrTq7j4nJBc, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize title/artist/album strings for fuzzy matching
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Heuristic entity key: title + artist (when artist is available), otherwise title+album
# Also remove some obviously non-title prefixes like track numbers of form '001-' etc.
tracks_df['norm_title'] = tracks_df['title'].str.replace(r'^\d+[-:. ]*', '', regex=True).str.replace(r'[^a-z0-9]+', ' ', regex=True).str.strip()
tracks_df['norm_artist'] = tracks_df['artist'].str.replace(r'[^a-z0-9]+', ' ', regex=True).str.strip()
tracks_df['norm_album'] = tracks_df['album'].str.replace(r'[^a-z0-9]+', ' ', regex=True).str.strip()

# Build an entity key; prefer title+artist if artist present, else title+album, else title only
cond_artist = tracks_df['norm_artist'] != ''
cond_album = ~cond_artist & (tracks_df['norm_album'] != '')
tracks_df['entity_key'] = tracks_df['norm_title']
tracks_df.loc[cond_artist, 'entity_key'] = tracks_df.loc[cond_artist, 'norm_title'] + ' || ' + tracks_df.loc[cond_artist, 'norm_artist']
tracks_df.loc[cond_album, 'entity_key'] = tracks_df.loc[cond_album, 'norm_title'] + ' || ' + tracks_df.loc[cond_album, 'norm_album']

# Map track_id -> entity_key
id_to_entity = tracks_df.set_index('track_id')['entity_key']

# Attach entity_key to sales
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df = sales_df.merge(id_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Sum revenue per entity (real-world track)
# Convert revenue to float
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
entity_revenue = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Identify top-earning entity
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]
top_key = top_entity['entity_key']

# Within that entity, pick a representative track (first one) to get a nice title/artist/album
rep = tracks_df[tracks_df['entity_key'] == top_key].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': float(top_entity['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EBe54M4e39OdMrlvALYxXtlV': 'file_storage/call_EBe54M4e39OdMrlvALYxXtlV.json', 'var_call_QQiRgv5Um9SKlGrTq7j4nJBc': 'file_storage/call_QQiRgv5Um9SKlGrTq7j4nJBc.json', 'var_call_BuPa88ghypVGi3u7htneyQmk': ['tracks'], 'var_call_Iwvv1EXEtcdKsmXHhsiK5DUL': ['sales']}

exec(code, env_args)
