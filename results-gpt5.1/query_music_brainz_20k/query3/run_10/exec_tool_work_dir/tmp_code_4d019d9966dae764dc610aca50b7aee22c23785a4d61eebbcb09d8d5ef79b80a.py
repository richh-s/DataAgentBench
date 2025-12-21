code = """import json, pandas as pd

# Load full tracks and sales data from the JSON files
with open(var_call_6BTthnbWC5BBqY7a3gAbPItF, 'r') as f:
    tracks = json.load(f)
with open(var_call_Rq73CbXVZieKqIqntuK3owby, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric columns
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Basic normalization for entity resolution: lowercase & strip for title and artist
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Create a simple blocking key combining title and artist; also consider album and year when available
tracks_df['year_norm'] = tracks_df['year'].fillna('').astype(str).str.extract(r'(\d{2,4})', expand=False)

# Group by (title, artist, album, year_norm) as a proxy for a real-world track
group_cols = ['title', 'artist', 'album', 'year_norm']
tracks_df['entity_id'] = tracks_df.groupby(group_cols, dropna=False).ngroup()

# Map track_id -> entity_id
track_to_entity = tracks_df.set_index('track_id')['entity_id']

sales_df['entity_id'] = sales_df['track_id'].map(track_to_entity)

# Some sales may map to missing tracks; drop those
sales_df = sales_df.dropna(subset=['entity_id'])

# Aggregate revenue per entity
entity_revenue = sales_df.groupby('entity_id', as_index=False)['revenue_usd'].sum()

# Find top-1 entity by revenue
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# Get representative track info for that entity (first occurrence)
rep_track = tracks_df[tracks_df['entity_id'] == top_entity['entity_id']].iloc[0]

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

env_args = {'var_call_6BTthnbWC5BBqY7a3gAbPItF': 'file_storage/call_6BTthnbWC5BBqY7a3gAbPItF.json', 'var_call_Rq73CbXVZieKqIqntuK3owby': 'file_storage/call_Rq73CbXVZieKqIqntuK3owby.json', 'var_call_h3GbBJMxXQE1WKAfAzdybQjj': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}, {'track_id': '12984', 'total_revenue': '2401.71'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997'}, {'track_id': '666', 'total_revenue': '2382.74'}, {'track_id': '12620', 'total_revenue': '2377.59'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue': '2365.59'}, {'track_id': '3462', 'total_revenue': '2359.23'}, {'track_id': '9639', 'total_revenue': '2351.68'}, {'track_id': '18760', 'total_revenue': '2349.33'}, {'track_id': '2516', 'total_revenue': '2346.18'}, {'track_id': '6326', 'total_revenue': '2331.91'}, {'track_id': '5836', 'total_revenue': '2321.31'}, {'track_id': '9988', 'total_revenue': '2317.41'}, {'track_id': '18508', 'total_revenue': '2308.44'}, {'track_id': '10760', 'total_revenue': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue': '2288.23'}, {'track_id': '14169', 'total_revenue': '2281.23'}, {'track_id': '9649', 'total_revenue': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue': '2275.85'}, {'track_id': '7422', 'total_revenue': '2275.04'}, {'track_id': '8705', 'total_revenue': '2273.46'}, {'track_id': '5933', 'total_revenue': '2271.62'}, {'track_id': '5809', 'total_revenue': '2269.24'}, {'track_id': '16084', 'total_revenue': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue': '2250.04'}, {'track_id': '15664', 'total_revenue': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue': '2246.94'}, {'track_id': '13102', 'total_revenue': '2244.51'}, {'track_id': '4145', 'total_revenue': '2243.27'}, {'track_id': '13132', 'total_revenue': '2238.21'}, {'track_id': '13211', 'total_revenue': '2233.62'}, {'track_id': '2244', 'total_revenue': '2230.04'}, {'track_id': '18846', 'total_revenue': '2227.95'}, {'track_id': '2029', 'total_revenue': '2226.42'}, {'track_id': '3488', 'total_revenue': '2222.25'}, {'track_id': '17669', 'total_revenue': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue': '2211.97'}, {'track_id': '12551', 'total_revenue': '2210.78'}]}

exec(code, env_args)
