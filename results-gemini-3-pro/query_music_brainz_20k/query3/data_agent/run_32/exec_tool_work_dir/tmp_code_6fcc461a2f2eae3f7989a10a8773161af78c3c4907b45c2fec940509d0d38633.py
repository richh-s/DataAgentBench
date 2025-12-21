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
    # Lowercase, remove accents could be good but let's stick to standard chars
    text = text.lower()
    # Remove things in brackets e.g. (live), (remix) might differentiate versions?
    # The prompt asks for "Which song". Usually remix is a different track, but "live" might be same song?
    # However, duplicates are mentioned. "Duplicates generated from different sources".
    # Let's strip special chars and extra spaces.
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def clean_artist_title(artist, title):
    # Check for invalid artist
    invalid_artists = ['none', '[unknown]', 'unknown', 'various artists', '']
    
    artist_norm = normalize(artist)
    title_norm = normalize(title)
    
    if artist_norm in invalid_artists or not artist_norm:
        # Try to extract from title if " - " exists in original string
        # But we only have normalized strings here? No, let's use original for splitting
        if title and " - " in title:
            parts = title.split(" - ", 1)
            possible_artist = normalize(parts[0])
            possible_title = normalize(parts[1])
            if possible_artist:
                return possible_artist, possible_title
    
    return artist_norm, title_norm

for track in tracks_data:
    track_id = str(track['track_id'])
    title = track.get('title', '')
    artist = track.get('artist', '')
    
    # Clean/Resolve
    final_artist, final_title = clean_artist_title(artist, title)
    
    # Key for aggregation
    # If we still don't have an artist, we might just use title, but risk collision.
    # We'll use a tuple.
    key = (final_artist, final_title)
    
    # Get revenue
    rev = revenue_map.get(track_id, 0.0)
    
    if key in song_revenue:
        song_revenue[key] += rev
    else:
        song_revenue[key] = rev
        # Keep a nice formatted name for display
        display_artist = artist if artist and str(artist).lower() not in ['none', '[unknown]'] else final_artist
        display_title = title
        song_names[key] = f"{display_title} by {display_artist}"

# Find max
best_song = None
max_rev = -1.0

for key, rev in song_revenue.items():
    if rev > max_rev:
        max_rev = rev
        best_song = key

print("__RESULT__:")
print(json.dumps({
    "best_song_key": best_song,
    "revenue": max_rev,
    "display_name": song_names.get(best_song, "Unknown")
}))"""

env_args = {'var_function-call-11257887081723726084': ['sales'], 'var_function-call-11257887081723725315': ['tracks'], 'var_function-call-1799123912854599991': 'file_storage/function-call-1799123912854599991.json', 'var_function-call-1799123912854599852': 'file_storage/function-call-1799123912854599852.json'}

exec(code, env_args)
