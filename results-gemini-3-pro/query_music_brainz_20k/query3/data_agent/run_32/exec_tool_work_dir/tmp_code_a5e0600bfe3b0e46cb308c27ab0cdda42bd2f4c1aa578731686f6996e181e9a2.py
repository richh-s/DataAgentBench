code = """import json
import re

# Load data
with open(locals()['var_function-call-1799123912854599991'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-1799123912854599852'], 'r') as f:
    tracks_data = json.load(f)

# Map track_id to revenue
revenue_map = {}
for entry in sales_data:
    track_id = str(entry['track_id'])
    try:
        rev = float(entry['total_revenue'])
    except:
        rev = 0.0
    revenue_map[track_id] = rev

# Entity resolution and aggregation
song_revenue = {}
song_names = {}

def normalize(text):
    if not text:
        return ""
    text = str(text).lower()
    # Remove things in brackets for better matching? e.g. "Song (Live)" vs "Song"
    # But wait, different versions might be different products. 
    # However, "duplicates generated from different sources" suggests we should match them.
    # Let's try removing text inside parenthesis
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def clean_artist_title(artist, title):
    # Check for invalid artist
    invalid_artists = ['none', '[unknown]', 'unknown', 'various artists', '', 'null']
    
    # We work with original strings first for splitting
    if not artist or str(artist).lower() in invalid_artists:
        if title and " - " in title:
            parts = title.split(" - ", 1)
            artist = parts[0]
            title = parts[1]
    
    artist_norm = normalize(artist)
    title_norm = normalize(title)
    
    return artist_norm, title_norm

for track in tracks_data:
    track_id = str(track['track_id'])
    title = track.get('title', '')
    artist = track.get('artist', '')
    
    # Clean/Resolve
    final_artist, final_title = clean_artist_title(artist, title)
    
    if not final_title or final_title == 'none':
        continue

    # Key for aggregation
    key = (final_artist, final_title)
    
    # Get revenue
    rev = revenue_map.get(track_id, 0.0)
    
    if key in song_revenue:
        song_revenue[key] += rev
    else:
        song_revenue[key] = rev
        # Construct display name
        d_artist = artist if artist and str(artist).lower() not in ['none', '[unknown]'] else final_artist
        d_title = title
        song_names[key] = f"{d_title} by {d_artist}"

# Sort and get top 10
sorted_songs = sorted(song_revenue.items(), key=lambda x: x[1], reverse=True)

top_songs = []
for key, rev in sorted_songs[:10]:
    top_songs.append({
        "key": key,
        "revenue": rev,
        "display_name": song_names.get(key, "Unknown")
    })

print("__RESULT__:")
print(json.dumps(top_songs))"""

env_args = {'var_function-call-11257887081723726084': ['sales'], 'var_function-call-11257887081723725315': ['tracks'], 'var_function-call-1799123912854599991': 'file_storage/function-call-1799123912854599991.json', 'var_function-call-1799123912854599852': 'file_storage/function-call-1799123912854599852.json', 'var_function-call-4323077467602865475': {'best_song_key': ['none', 'none'], 'revenue': 14647.52, 'display_name': 'None by none'}}

exec(code, env_args)
