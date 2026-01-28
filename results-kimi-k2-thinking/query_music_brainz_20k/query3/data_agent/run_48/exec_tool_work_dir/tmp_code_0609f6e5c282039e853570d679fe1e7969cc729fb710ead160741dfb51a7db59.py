code = """import json
import re
from collections import defaultdict

# Load full datasets
tracks_file = locals()['var_functions.query_db:5']
sales_file = locals()['var_functions.query_db:8']

with open(tracks_file, 'r') as f:
    tracks = json.load(f)

with open(sales_file, 'r') as f:
    sales = json.load(f)

# Step 1: Clean and normalize track data
def clean_text(text):
    if text is None or text == 'None':
        return ''
    return str(text).strip().lower()

def extract_artist_from_title(title):
    if '-' in title:
        return title.split('-')[0].strip()
    return ''

def normalize_year(year):
    if year is None or year == 'None' or year == '':
        return None
    year_str = str(year).strip()
    # Extract digits
    digits = re.findall(r'\d+', year_str)
    if not digits:
        return None
    year_num = int(digits[0])
    # Convert 2-digit years to 4-digit
    if year_num < 100:
        if year_num > 50:
            year_num += 1900
        else:
            year_num += 2000
    return year_num

# Clean tracks data
cleaned_tracks = []
for track in tracks:
    title = clean_text(track['title'])
    artist = clean_text(track['artist'])
    
    # If artist is empty or unknown, try to extract from title
    if artist in ['', '[unknown]', 'unknown', 'none']:
        if '-' in track.get('title', ''):
            artist = clean_text(extract_artist_from_title(track['title']))
    
    cleaned_track = {
        'track_id': track['track_id'],
        'title': title,
        'artist': artist,
        'album': clean_text(track['album']),
        'year': normalize_year(track['year']),
        'original_title': track['title'],
        'original_artist': track['artist']
    }
    cleaned_tracks.append(cleaned_track)

# Step 2: Create a key for entity resolution
def get_entity_key(track):
    # Use title and artist as primary key
    # Remove common words and punctuation for better matching
    def simplify(text):
        if not text:
            return ''
        # Remove punctuation and common words
        text = re.sub(r'[^\w\s]', ' ', text)
        words = text.split()
        # Remove common words
        common = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'between', 'among', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
        words = [w for w in words if w not in common]
        return ' '.join(words)
    
    title_simp = simplify(track['title'])
    artist_simp = simplify(track['artist'])
    
    # Use a combination of simplified title and artist
    return f"{title_simp}|{artist_simp}"

# Group tracks by entity
entity_groups = defaultdict(list)
for track in cleaned_tracks:
    key = get_entity_key(track)
    entity_groups[key].append(track)

# Step 3: Aggregate sales by track_id and then by entity
sales_by_track_id = defaultdict(float)
for sale in sales:
    track_id = sale['track_id']
    revenue = float(sale['revenue_usd'])
    sales_by_track_id[track_id] += revenue

# Sum up revenue for each entity
entity_revenues = defaultdict(float)
entity_track_counts = defaultdict(int)
entity_track_ids = defaultdict(list)

for key, tracks_in_group in entity_groups.items():
    for track in tracks_in_group:
        track_id = track['track_id']
        revenue = sales_by_track_id.get(track_id, 0)
        entity_revenues[key] += revenue
        entity_track_ids[key].append(track_id)
    entity_track_counts[key] = len(tracks_in_group)

# Step 4: Find the entity with highest revenue
sorted_entities = sorted(entity_revenues.items(), key=lambda x: x[1], reverse=True)

# Get top 10 for analysis
top_10 = []
for key, revenue in sorted_entities[:10]:
    track_ids = entity_track_ids[key]
    sample_tracks = [t for t in cleaned_tracks if t['track_id'] in track_ids][:3]
    top_10.append({
        'key': key,
        'revenue': revenue,
        'track_count': entity_track_counts[key],
        'sample_tracks': sample_tracks
    })

print('__RESULT__:')
print(json.dumps(top_10))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'tracks_count': 19375, 'sales_count': 58049, 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.execute_python:18': {'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}], 'tracks_count': 19375, 'sales_count': 58049}}

exec(code, env_args)
