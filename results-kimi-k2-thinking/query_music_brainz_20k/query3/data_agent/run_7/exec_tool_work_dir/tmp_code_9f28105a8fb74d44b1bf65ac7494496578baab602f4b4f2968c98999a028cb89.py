code = """import pandas as pd, json, os, numpy as np

# Read tracks file
with open('/var/folders/4p/cm35df9n20b6d8j2y4q7j6c80000gn/T/tmp9q7k7n3d.json','r') as f:
    tracks = pd.DataFrame(json.load(f))

# Read sales file
with open('/var/folders/4p/cm35df9n20b6d8j2y4q7j6c80000gn/T/tmp4z1g9l8a.json','r') as f:
    sales = pd.DataFrame(json.load(f))

# Ensure revenue numeric and track_id int
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce')
sales['track_id'] = pd.to_numeric(sales['track_id'], errors='coerce')
sales = sales.dropna(subset=['track_id'])

# Compute total revenue per track_id
revenue_by_track = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Clean tracks DataFrame
# Replace string 'None' with np.nan for relevant columns
cols = ['title','artist','album','year','language','length','source_track_id','source_id']
for col in cols:
    tracks[col] = tracks[col].replace('None', np.nan)
    # also strip whitespace
    if tracks[col].dtype == object:
        tracks[col] = tracks[col].astype(str).str.strip()
    # treat empty strings as nan
    tracks[col] = tracks[col].replace('', np.nan)

# Convert track_id to int
tracks['track_id'] = pd.to_numeric(tracks['track_id'], errors='coerce')

# Merge revenue onto tracks
tracks_rev = tracks.merge(revenue_by_track, on='track_id', how='left')

# Fill missing revenue with 0
tracks_rev['revenue_usd'] = tracks_rev['revenue_usd'].fillna(0)

# Create a grouping key: use title + artist + album + year (as string) after normalizing
# Convert missing to empty string
for col in ['title','artist','album','year']:
    tracks_rev[col] = tracks_rev[col].fillna('')
    # Lowercase and remove extra whitespace
    tracks_rev[col] = tracks_rev[col].astype(str).str.lower().str.replace(r'\s+', ' ', regex=True).str.strip()

# Build key (maybe include album and year to differentiate versions)
tracks_rev['key'] = tracks_rev['title'] + '::' + tracks_rev['artist'] + '::' + tracks_rev['album'] + '::' + tracks_rev['year']

# Now group by key and sum revenue
grouped = tracks_rev.groupby('key', as_index=False).agg({'revenue_usd':'sum','track_id':'count'})
# Rename track_id count as occurrence count for info
grouped = grouped.rename(columns={'track_id':'track_count'})

# Sort descending by revenue
top = grouped.sort_values('revenue_usd', ascending=False).head(10)
print('__RESULT__:')
print(top.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
