code = """import json
import re

# Load data
with open(locals()['var_function-call-15720467439112676785'], 'r') as f:
    revenue_data = json.load(f)

with open(locals()['var_function-call-13827168507574417079'], 'r') as f:
    tracks_data = json.load(f)

# Convert revenue to dict: track_id -> revenue
track_revenue = {}
for entry in revenue_data:
    try:
        tid = str(entry['track_id'])
        rev = float(entry['total_revenue']) if entry['total_revenue'] else 0.0
        track_revenue[tid] = rev
    except:
        continue

# Helper to normalize strings
def normalize(s):
    if not s:
        return ""
    # Remove things in brackets/parentheses like (acoustic), [live], etc? 
    # Maybe risky if the song title is "Song (Remix)" and "Song" are different.
    # But usually for "highest revenue song", we want to aggregate all versions.
    # Let's remove content in parens/brackets for better matching.
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    
    # Lowercase, remove non-alphanumeric chars except spaces
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def get_identity(track):
    title = track.get('title', '') or ''
    artist = track.get('artist', '') or ''
    
    # Check if artist is missing or placeholder
    artist_lower = artist.lower()
    invalid_artists = ['none', 'unknown', '[unknown]', '']
    is_artist_valid = artist_lower not in invalid_artists
    
    # Heuristic for "Artist - Title" in title field if artist is missing
    if not is_artist_valid and ' - ' in title:
        parts = title.split(' - ', 1)
        pot_artist = parts[0]
        pot_title = parts[1]
        return normalize(pot_title), normalize(pot_artist)
    
    # If artist is valid, or title doesn't have hyphen
    return normalize(title), normalize(artist) if is_artist_valid else ""

# Aggregate revenue by identity
identity_revenue = {}
identity_display = {} # Keep one display version

for track in tracks_data:
    tid = str(track['track_id'])
    if tid not in track_revenue:
        continue
        
    rev = track_revenue[tid]
    norm_title, norm_artist = get_identity(track)
    
    if not norm_title: # Skip empty titles
        continue
        
    key = (norm_title, norm_artist)
    
    if key not in identity_revenue:
        identity_revenue[key] = 0.0
        # Store a display version (Title by Artist)
        display_title = track.get('title', '')
        display_artist = track.get('artist', '')
        if not display_artist or display_artist.lower() == 'none':
             identity_display[key] = display_title
        else:
             identity_display[key] = f"{display_title} by {display_artist}"
             
    identity_revenue[key] += rev

# Find top revenue
sorted_identities = sorted(identity_revenue.items(), key=lambda x: x[1], reverse=True)

# Output top 5 for debugging/verification
top_5 = []
for i in range(min(5, len(sorted_identities))):
    key, rev = sorted_identities[i]
    display = identity_display.get(key, str(key))
    top_5.append({"rank": i+1, "key": key, "display": display, "revenue": rev})

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-15720467439112676785': 'file_storage/function-call-15720467439112676785.json', 'var_function-call-13827168507574417079': 'file_storage/function-call-13827168507574417079.json'}

exec(code, env_args)
