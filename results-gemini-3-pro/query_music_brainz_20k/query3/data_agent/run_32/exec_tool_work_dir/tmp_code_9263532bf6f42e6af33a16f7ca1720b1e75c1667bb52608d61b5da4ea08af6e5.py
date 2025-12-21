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

# Grouping
groups = {} # key -> list of tracks

def normalize(text):
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r'\(.*?\)', '', text) # Remove content in parenthesis
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    return text.strip()

def clean_artist_title(artist, title):
    invalid_artists = ['none', '[unknown]', 'unknown', 'various artists', '', 'null']
    
    # Try split if artist is missing
    if not artist or str(artist).lower() in invalid_artists:
        if title and " - " in title:
            parts = title.split(" - ", 1)
            artist = parts[0]
            title = parts[1]
    
    return normalize(artist), normalize(title)

for track in tracks_data:
    track_id = str(track['track_id'])
    title = track.get('title', '')
    artist = track.get('artist', '')
    
    # Filter very short titles/artists which might be garbage "001"
    # Although some songs have short names.
    
    key_artist, key_title = clean_artist_title(artist, title)
    
    if not key_title or key_title == 'none':
        continue
        
    key = (key_artist, key_title)
    
    if key not in groups:
        groups[key] = []
    
    groups[key].append({
        "track_id": track_id,
        "original_title": title,
        "original_artist": artist,
        "revenue": revenue_map.get(track_id, 0.0)
    })

# Calculate group revenue
group_stats = []
for key, tracks in groups.items():
    total_rev = sum(t['revenue'] for t in tracks)
    group_stats.append({
        "key": key,
        "total_revenue": total_rev,
        "tracks": tracks
    })

# Sort
group_stats.sort(key=lambda x: x['total_revenue'], reverse=True)

# Print detailed top 5
print("__RESULT__:")
print(json.dumps(group_stats[:5]))"""

env_args = {'var_function-call-11257887081723726084': ['sales'], 'var_function-call-11257887081723725315': ['tracks'], 'var_function-call-1799123912854599991': 'file_storage/function-call-1799123912854599991.json', 'var_function-call-1799123912854599852': 'file_storage/function-call-1799123912854599852.json', 'var_function-call-4323077467602865475': {'best_song_key': ['none', 'none'], 'revenue': 14647.52, 'display_name': 'None by none'}, 'var_function-call-15343428881387402340': [{'key': ['none', '001'], 'revenue': 5866.4800000000005, 'display_name': '00-1 by none'}, {'key': ['rich matteson', 'groovey'], 'revenue': 5417.34, 'display_name': 'Rich Matteson - Groovey by rich matteson'}, {'key': ['syb van der ploeg', 'zo gaat het leven aan je voor'], 'revenue': 5256.43, 'display_name': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur) by Syb van der Ploeg'}, {'key': ['none', '003'], 'revenue': 5022.32, 'display_name': '003- by none'}, {'key': ['ske', 'vagga'], 'revenue': 4981.380000000001, 'display_name': 'Ske - Vagga by ske'}, {'key': ['tiidmäldä', 'kiä meil pahanu'], 'revenue': 4916.11, 'display_name': '[tiidmäldä] - Kiä meil pahanu? by tiidmäldä'}, {'key': ['fischerspooner', 'emerge'], 'revenue': 4896.24, 'display_name': 'Fischerspooner - Emerge (Dexter remix) by fischerspooner'}, {'key': ['hans zimmer', 'best friends'], 'revenue': 4806.24, 'display_name': 'Hans Zimmer - Best Friends by hans zimmer'}, {'key': ['echolyn', 'letters a short essay'], 'revenue': 4694.76, 'display_name': 'Letters A Short Essay (As the World) by echolyn'}, {'key': ['vrisak generacije', 'ne veruj'], 'revenue': 4693.259999999999, 'display_name': 'Ne veruj (Beer Drinkers Revenge) by Vrisak generacije'}]}

exec(code, env_args)
