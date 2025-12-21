code = """import json
import re

with open(locals()['var_function-call-15720467439112676785'], 'r') as f:
    revenue_data = json.load(f)
with open(locals()['var_function-call-13827168507574417079'], 'r') as f:
    tracks_data = json.load(f)

track_revenue = {str(e['track_id']): float(e['total_revenue'] or 0) for e in revenue_data if e['total_revenue']}

def normalize(s):
    if not s: return ""
    s = re.sub(r'\([^)]*\)', '', s) # Remove (...)
    s = re.sub(r'\[[^]]*\]', '', s) # Remove [...]
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def get_identity(track):
    title = track.get('title', '') or ''
    artist = track.get('artist', '') or ''
    
    artist_lower = artist.lower()
    invalid_artists = ['none', 'unknown', '[unknown]', '', 'null', 'various artists']
    is_artist_valid = artist_lower not in invalid_artists
    
    if not is_artist_valid and ' - ' in title:
        parts = title.split(' - ', 1)
        return normalize(parts[1]), normalize(parts[0])
    
    return normalize(title), normalize(artist) if is_artist_valid else ""

identity_groups = {}

for track in tracks_data:
    tid = str(track['track_id'])
    if tid not in track_revenue: continue
    
    norm_title, norm_artist = get_identity(track)
    
    # Filter out empty/bad titles
    if not norm_title or norm_title == 'none': continue
    if re.match(r'^\d+$', norm_title): continue # Purely numeric title like "003"
    
    # Filter out empty artists
    if not norm_artist: continue
    
    key = (norm_title, norm_artist)
    if key not in identity_groups:
        identity_groups[key] = {'revenue': 0.0, 'tracks': []}
    
    identity_groups[key]['revenue'] += track_revenue[tid]
    identity_groups[key]['tracks'].append(track)

# Sort
sorted_identities = sorted(identity_groups.items(), key=lambda x: x[1]['revenue'], reverse=True)

# Print top 5
results = []
for i in range(min(5, len(sorted_identities))):
    key, data = sorted_identities[i]
    rep_track = data['tracks'][0]
    # Find best display name
    for t in data['tracks']:
        if t.get('title') and len(t['title']) > len(rep_track['title']):
             rep_track = t

    results.append({
        "rank": i+1,
        "key": key,
        "revenue": data['revenue'],
        "title": rep_track.get('title'),
        "artist": rep_track.get('artist')
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15720467439112676785': 'file_storage/function-call-15720467439112676785.json', 'var_function-call-13827168507574417079': 'file_storage/function-call-13827168507574417079.json', 'var_function-call-4873491316950649724': [{'rank': 1, 'key': ['none', ''], 'display': 'None by 幡谷尚史', 'revenue': 17150.55}, {'rank': 2, 'key': ['003', ''], 'display': '003-', 'revenue': 8582.15}, {'rank': 3, 'key': ['001', ''], 'display': '00-1', 'revenue': 7467.97}, {'rank': 4, 'key': ['004', ''], 'display': '004-/', 'revenue': 7271.32}, {'rank': 5, 'key': ['005', ''], 'display': '005', 'revenue': 6155.29}], 'var_function-call-391238844812898672': [{'rank': 1, 'key': ['003', ''], 'revenue': 8582.15, 'sample_title': '003-', 'sample_artist': ' ', 'num_tracks': 9}, {'rank': 2, 'key': ['001', ''], 'revenue': 7467.97, 'sample_title': '00-1', 'sample_artist': '[unknown]', 'num_tracks': 7}, {'rank': 3, 'key': ['004', ''], 'revenue': 7271.32, 'sample_title': '004-"" (, , , )', 'sample_artist': ' ', 'num_tracks': 8}, {'rank': 4, 'key': ['005', ''], 'revenue': 6155.29, 'sample_title': '005- ', 'sample_artist': ' ', 'num_tracks': 8}, {'rank': 5, 'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_title': 'Groovey', 'sample_artist': 'Rich Matteson', 'num_tracks': 4}, {'rank': 6, 'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'sample_artist': 'Syb van der Ploeg', 'num_tracks': 3}, {'rank': 7, 'key': ['009', ''], 'revenue': 5045.7, 'sample_title': '009-  ', 'sample_artist': ' ', 'num_tracks': 4}, {'rank': 8, 'key': ['002', ''], 'revenue': 5013.4400000000005, 'sample_title': '002-', 'sample_artist': ' ', 'num_tracks': 4}, {'rank': 9, 'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_title': 'Vagga', 'sample_artist': 'Ske', 'num_tracks': 3}, {'rank': 10, 'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'sample_artist': '[tiidmäldä]', 'num_tracks': 3}]}

exec(code, env_args)
