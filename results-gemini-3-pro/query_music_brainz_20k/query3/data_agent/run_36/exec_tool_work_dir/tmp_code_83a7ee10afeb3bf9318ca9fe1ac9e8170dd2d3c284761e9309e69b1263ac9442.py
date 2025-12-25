code = """import json
import re

with open(locals()['var_function-call-15720467439112676785'], 'r') as f:
    revenue_data = json.load(f)
with open(locals()['var_function-call-13827168507574417079'], 'r') as f:
    tracks_data = json.load(f)

track_revenue = {str(e['track_id']): float(e['total_revenue'] or 0) for e in revenue_data if e['total_revenue']}

def normalize(s):
    if not s: return ""
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def get_identity(track):
    title = track.get('title', '') or ''
    artist = track.get('artist', '') or ''
    
    artist_lower = artist.lower()
    invalid_artists = ['none', 'unknown', '[unknown]', '']
    is_artist_valid = artist_lower not in invalid_artists
    
    if not is_artist_valid and ' - ' in title:
        parts = title.split(' - ', 1)
        return normalize(parts[1]), normalize(parts[0])
    
    return normalize(title), normalize(artist) if is_artist_valid else ""

identity_groups = {} # Store list of tracks for each key

for track in tracks_data:
    tid = str(track['track_id'])
    if tid not in track_revenue: continue
    
    norm_title, norm_artist = get_identity(track)
    if not norm_title or norm_title == 'none': continue # Skip obvious bad ones
    
    key = (norm_title, norm_artist)
    if key not in identity_groups:
        identity_groups[key] = {'revenue': 0.0, 'tracks': []}
    
    identity_groups[key]['revenue'] += track_revenue[tid]
    identity_groups[key]['tracks'].append(track)

# Sort
sorted_identities = sorted(identity_groups.items(), key=lambda x: x[1]['revenue'], reverse=True)

# Print top 10 with details
results = []
for i in range(min(10, len(sorted_identities))):
    key, data = sorted_identities[i]
    # Pick a representative title/artist from the tracks
    # Prefer one with a valid artist
    rep_track = data['tracks'][0]
    for t in data['tracks']:
        if t.get('artist') and t.get('artist').lower() != 'none':
            rep_track = t
            break
            
    results.append({
        "rank": i+1,
        "key": key,
        "revenue": data['revenue'],
        "sample_title": rep_track.get('title'),
        "sample_artist": rep_track.get('artist'),
        "num_tracks": len(data['tracks'])
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15720467439112676785': 'file_storage/function-call-15720467439112676785.json', 'var_function-call-13827168507574417079': 'file_storage/function-call-13827168507574417079.json', 'var_function-call-4873491316950649724': [{'rank': 1, 'key': ['none', ''], 'display': 'None by 幡谷尚史', 'revenue': 17150.55}, {'rank': 2, 'key': ['003', ''], 'display': '003-', 'revenue': 8582.15}, {'rank': 3, 'key': ['001', ''], 'display': '00-1', 'revenue': 7467.97}, {'rank': 4, 'key': ['004', ''], 'display': '004-/', 'revenue': 7271.32}, {'rank': 5, 'key': ['005', ''], 'display': '005', 'revenue': 6155.29}]}

exec(code, env_args)
