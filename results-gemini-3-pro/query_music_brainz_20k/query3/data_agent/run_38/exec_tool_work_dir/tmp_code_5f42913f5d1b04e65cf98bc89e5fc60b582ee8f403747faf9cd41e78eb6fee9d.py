code = """import json
import re

# Load data
with open(locals()['var_function-call-3828468449816819381'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-8657562732755232343'], 'r') as f:
    tracks_data = json.load(f)

# Helper for normalization
def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    # Replace common separators
    s = s.replace('&', 'and').replace('+', 'and')
    # Keep only alphanumeric
    return re.sub(r'[^a-z0-9]', '', s)

# Process tracks to build map: track_id -> entity_key
track_map = {}
entity_display = {} # key -> {title, artist, max_len}

for t in tracks_data:
    tid = t['track_id']
    title = t['title'] if t['title'] != 'None' else ''
    artist = t['artist'] if t['artist'] != 'None' else ''
    
    # Heuristic: Fix missing artist if title has ' - '
    # Also clean up "unknown" artists
    if artist.lower() in ['[unknown]', 'unknown', '', 'none']:
        artist = ''
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # Assign first part to artist, second to title
            # This handles "Artist - Title" format often found in messy data
            artist_candidate = parts[0].strip()
            title_candidate = parts[1].strip()
            if artist_candidate and title_candidate:
                artist = artist_candidate
                title = title_candidate

    # Normalize
    n_artist = normalize(artist)
    n_title = normalize(title)
    
    # Composite key
    # If artist is still empty, the key is just the title. 
    # This might merge different songs with same title but unknown artist. 
    # Given the prompt, usually we have title and artist.
    key = f"{n_artist}|{n_title}"
    
    track_map[tid] = key
    
    # Save display info (keep the one with longest original strings as it's likely more complete)
    current_len = len(title) + len(artist)
    if key not in entity_display or current_len > entity_display[key]['len']:
        entity_display[key] = {
            'title': title,
            'artist': artist,
            'len': current_len
        }

# Aggregate revenue
entity_revenue = {}

for s in sales_data:
    tid = s['track_id']
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    
    if tid in track_map:
        key = track_map[tid]
        if key in entity_revenue:
            entity_revenue[key] += rev
        else:
            entity_revenue[key] = rev

# Find max
if not entity_revenue:
    print("__RESULT__:")
    print(json.dumps("No revenue data found."))
else:
    best_key = max(entity_revenue, key=entity_revenue.get)
    max_rev = entity_revenue[best_key]
    best_info = entity_display[best_key]
    
    result = {
        'title': best_info['title'],
        'artist': best_info['artist'],
        'total_revenue_usd': max_rev,
        'key': best_key
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json'}

exec(code, env_args)
