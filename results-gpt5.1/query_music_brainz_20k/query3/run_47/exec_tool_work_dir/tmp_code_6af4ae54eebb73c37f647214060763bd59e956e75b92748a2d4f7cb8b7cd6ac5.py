code = """import json, pandas as pd

# Load full results from files
with open(var_call_mIdL87NZ9ZOyn9aFUs6ass2M, 'r') as f:
    tracks = json.load(f)
with open(var_call_k3bmwsoS9lO2TNodQPBOuuwc, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure numeric types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])

# Basic entity resolution: group by normalized title+artist+album+year
for col in ['title','artist','album','year']:
    tracks_df[col] = tracks_df[col].fillna('')

tracks_df['title_norm'] = tracks_df['title'].str.strip().str.lower()
tracks_df['artist_norm'] = tracks_df['artist'].str.strip().str.lower()
tracks_df['album_norm'] = tracks_df['album'].str.strip().str.lower()
tracks_df['year_norm'] = tracks_df['year'].str.strip()

tracks_df['entity_key'] = tracks_df['title_norm'] + '|' + tracks_df['artist_norm'] + '|' + tracks_df['album_norm'] + '|' + tracks_df['year_norm']

# Map each track_id to entity_key
id_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df = sales_df.merge(id_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity_key
entity_revenue = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Get track metadata for each entity (take first occurrence)
entity_meta = tracks_df.groupby('entity_key').agg({'title':'first','artist':'first','album':'first','year':'first'}).reset_index()

result_df = entity_revenue.merge(entity_meta, on='entity_key', how='left')

# Find the entity with max revenue
max_row = result_df.loc[result_df['revenue_usd'].idxmax()]

result = {
    'title': max_row['title'],
    'artist': max_row['artist'],
    'album': max_row['album'],
    'year': max_row['year'],
    'total_revenue_usd': float(max_row['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mIdL87NZ9ZOyn9aFUs6ass2M': 'file_storage/call_mIdL87NZ9ZOyn9aFUs6ass2M.json', 'var_call_k3bmwsoS9lO2TNodQPBOuuwc': 'file_storage/call_k3bmwsoS9lO2TNodQPBOuuwc.json'}

exec(code, env_args)
