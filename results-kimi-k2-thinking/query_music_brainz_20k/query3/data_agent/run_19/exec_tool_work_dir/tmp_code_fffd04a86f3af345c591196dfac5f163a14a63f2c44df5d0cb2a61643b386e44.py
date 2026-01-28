code = """import json
import pandas as pd

# Load data again for verification
tracks_file_path = locals()['var_functions.query_db:14']
sales_file_path = locals()['var_functions.query_db:20']

import os
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Calculate revenue per track_id first
revenue_per_track_id = sales_df.groupby('track_id')['revenue_usd'].sum().sort_values(ascending=False)

# Show top 5 tracks by revenue
top_5_tracks = revenue_per_track_id.head(5)

result = {
    'top_5_tracks_by_track_id': {
        track_id: {
            'revenue': round(revenue, 2),
            'info': tracks_df[tracks_df['track_id'] == track_id][['title', 'artist', 'album', 'year']].to_dict('records')[0] 
                   if not tracks_df[tracks_df['track_id'] == track_id].empty 
                   else 'Track info not found'
        }
        for track_id, revenue in top_5_tracks.items()
    }
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'tracks_loaded': 19375, 'sales_loaded': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'title_clean': "daniel balavoine - l'enfant aux yeux d'italie", 'artist_clean': 'daniel balavoine'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'title_clean': '007', 'artist_clean': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'title_clean': 'action painting! - mustard gas', 'artist_clean': 'action painting!'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': 349, 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': 122, 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': 373, 'revenue_usd': 371.57}]}, 'var_functions.execute_python:30': {'top_track_title': 'chi to rome (broke one edit)', 'top_track_artist': 'lazy ants & rob threezy', 'top_track_album': 'chi to rome', 'top_track_year': 2011.0, 'total_revenue_usd': 3091.77, 'num_track_ids': 2}}

exec(code, env_args)
