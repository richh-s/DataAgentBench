code = """import json
import pandas as pd

# Load the full tracks data from the file
with open('var_functions.query_db:12.json', 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrame
tracks_df = pd.DataFrame(tracks_data)
print(f"Tracks dataset: {len(tracks_df)} records")
print("\nFirst few records:")
print(tracks_df.head(3))

# Check for duplicates by comparing key attributes
print("\nBasic info:")
print(f"Unique track_ids: {tracks_df['track_id'].nunique()}")
print(f"Unique titles: {tracks_df['title'].nunique()}")
print(f"Unique artists: {tracks_df['artist'].nunique()}")

# Check for nulls in key fields
print("\nNull values in key fields:")
print(f"title: {tracks_df['title'].isnull().sum()}")
print(f"artist: {tracks_df['artist'].isnull().sum()}")
print(f"album: {tracks_df['album'].isnull().sum()}")

# Sample some tracks to see potential duplicates similar to the example shown
sample_tracks = tracks_df.head(20)
print("\nSample tracks:")
for i, row in sample_tracks.iterrows():
    print(f"ID {row['track_id']}: {row['artist']} - {row['title']}")

# Also get sales data
print("\n" + "="*50 + " SALES DATA " + "="*50)

# Get full sales data
with open('var_functions.query_db:5.json', 'r') as f:
    sales_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
print(f"Sales dataset: {len(sales_df)} records")
print("\nFirst few records:")
print(sales_df.head(3))

# Aggregate sales by track_id
sales_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
print(f"\nTotal revenue by track_id (top 10):")
print(sales_by_track.sort_values('revenue_usd', ascending=False).head(10))

# Now let's look at some potential duplicates
# I'll look for tracks with similar names but different track_ids
print("\n" + "="*50 + " CHECKING FOR DUPLICATES " + "="*50)

# Find tracks that appear to be the same song
# Group by normalized title and artist to find duplicates
tracks_df['title_clean'] = tracks_df['title'].str.strip().str.lower()
tracks_df['artist_clean'] = tracks_df['artist'].str.strip().str.lower()

# Look for duplicates
potential_duplicates = tracks_df.groupby(['title_clean', 'artist_clean']).agg({
    'track_id': list,
    'year': list,
    'source_id': list
}).reset_index()

# Filter for groups with multiple track_ids
duplicates = potential_duplicates[potential_duplicates['track_id'].apply(len) > 1]
print(f"Found {len(duplicates)} potential duplicate groups")
print("\nSample duplicate groups:")
for i, row in duplicates.head(5).iterrows():
    print(f"\n{row['title_clean']} - {row['artist_clean']}")
    track_ids = row['track_id']
    years = row['year']
    sources = row['source_id']
    for j in range(len(track_ids)):
        track_info = tracks_df[tracks_df['track_id'] == track_ids[j]].iloc[0]
        print(f"  Track {track_ids[j]}: year='{years[j]}', source='{sources[j]}', actual artist='{track_info['artist']}'")

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({"message": "Data loaded successfully", "track_count": len(tracks_df), "sales_count": len(sales_df)}))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': [{'total_tracks': '19375'}], 'var_functions.query_db:10': [{'total_sales': '58049'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
