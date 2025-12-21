code = """import json, pandas as pd

# Load full data from files
with open(var_call_hGUIbrfde6qHo777r1pyqEsA, 'r') as f:
    tracks = json.load(f)
with open(var_call_dTrg2azifwLMAnvCKEactETe, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric fields
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Simple entity resolution heuristic: group by (normalized title, normalized artist, normalized album, normalized year)
# Normalize strings: lowercase, strip, collapse spaces
for col in ['title', 'artist', 'album', 'year']:
    def norm(x):
        if x is None:
            return ''
        x = str(x).strip().lower()
        x = ' '.join(x.split())
        return x
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm)

# Create an entity key
tracks_df['entity_key'] = (tracks_df['title_norm'] + '|' +
                           tracks_df['artist_norm'] + '|' +
                           tracks_df['album_norm'] + '|' +
                           tracks_df['year_norm'])

# Map each track_id to an entity_key
track_entity = tracks_df[['track_id', 'entity_key']]

# Join sales with entity info
sales_merged = sales_df.merge(track_entity, on='track_id', how='left')

# Aggregate revenue by entity_key
entity_revenue = sales_merged.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Find the entity with max revenue
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# Get a representative track (first one) for that entity to retrieve human-readable info
rep_track = tracks_df[tracks_df['entity_key'] == top_entity['entity_key']].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(float(top_entity['revenue_usd']), 2)
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_hGUIbrfde6qHo777r1pyqEsA': 'file_storage/call_hGUIbrfde6qHo777r1pyqEsA.json', 'var_call_dTrg2azifwLMAnvCKEactETe': 'file_storage/call_dTrg2azifwLMAnvCKEactETe.json'}

exec(code, env_args)
