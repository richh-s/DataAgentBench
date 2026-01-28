code = """import json
import pandas as pd

# Load data
tracks_file_path = locals()['var_functions.query_db:0']
sales_file_path = locals()['var_functions.query_db:5']

with open(tracks_file_path, 'r') as file:
    tracks_data = json.load(file)
    
with open(sales_file_path, 'r') as file:
    sales_data = json.load(file)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert data types
for df in [sales_df, tracks_df]:
    df['track_id'] = pd.to_numeric(df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])

# Normalize text for comparison
def normalize_text(text):
    if pd.isna(text) or text is None or text in ['None', 'Unknown', 'unknown', '[unknown]', '   ', '']:
        return None
    return str(text).strip().lower()

tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)

# Filter out invalid tracks
valid_tracks = tracks_df[
    tracks_df['norm_title'].notna() & 
    tracks_df['norm_artist'].notna() &
    (tracks_df['norm_title'] != 'none') &
    (tracks_df['norm_artist'] != 'none') &
    (tracks_df['norm_title'] != '') &
    (tracks_df['norm_artist'] != '')
].copy()

print('Total tracks: ' + str(len(tracks_df)))
print('Valid tracks: ' + str(len(valid_tracks)))

# Merge with sales
valid_tracks_with_sales = valid_tracks.merge(sales_df, on='track_id', how='inner')

# Group by normalized title and artist
entity_revenue = valid_tracks_with_sales.groupby(['norm_title', 'norm_artist']).agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'track_id': 'nunique',
    'country': lambda x: len(set(x)),
    'store': lambda x: len(set(x))
}).reset_index()

entity_revenue = entity_revenue.sort_values('revenue_usd', ascending=False)

# Get top 5
top_5 = entity_revenue.head(5)
print('\nTop 5 songs by revenue:')

result_list = []
for idx, row in top_5.iterrows():
    # Get original track info
    orig_tracks = valid_tracks[
        (valid_tracks['norm_title'] == row['norm_title']) & 
        (valid_tracks['norm_artist'] == row['norm_artist'])
    ]
    
    original_title = orig_tracks.iloc[0]['title']
    original_artist = orig_tracks.iloc[0]['artist']
    
    info = {
        'title': str(original_title),
        'artist': str(original_artist),
        'revenue': float(row['revenue_usd']),
        'duplicate_entries': int(row['track_id'])
    }
    result_list.append(info)

# Return top song
result = result_list[0]
result['top_5'] = result_list

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'track_id': 14719, 'revenue_usd': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, 'var_functions.execute_python:12': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'track_id': 14719, 'total_revenue': 2522.82, 'found_duplicates': 0, 'sales_countries': 3, 'sales_stores': 3, 'total_units_sold': 361428441458421}, 'var_functions.execute_python:14': {'title': 'unknown', 'artist': 'None', 'total_revenue_usd': 17865.87, 'track_ids': [1032, 2126, 2153, 3422, 4421, 5048, 7036, 7146, 7185, 7481, 9011, 9478, 9612, 9788, 10617, 12019, 12196, 14462, 15386, 15469, 16886, 18790], 'is_entity_with_duplicates': True, 'num_duplicates': 21, 'total_units_sold': 15540, 'countries': 5, 'stores': 5}}

exec(code, env_args)
