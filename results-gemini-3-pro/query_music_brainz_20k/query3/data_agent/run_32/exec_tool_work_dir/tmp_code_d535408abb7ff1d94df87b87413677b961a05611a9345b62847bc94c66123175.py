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
groups = {}

def normalize(text):
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def clean_artist_title(artist, title):
    invalid_artists = ['none', '[unknown]', 'unknown', 'various artists', '', 'null']
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
    
    key_artist, key_title = clean_artist_title(artist, title)
    
    # Filter out invalid artists for the ranking
    if not key_artist or key_artist == 'none':
        continue
    
    key = (key_artist, key_title)
    
    if key not in groups:
        groups[key] = 0.0
    
    groups[key] += revenue_map.get(track_id, 0.0)

# Sort
sorted_groups = sorted(groups.items(), key=lambda x: x[1], reverse=True)

# Print top 10
result_list = []
for key, rev in sorted_groups[:10]:
    result_list.append({
        "artist": key[0],
        "title": key[1],
        "revenue": rev
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-11257887081723726084': ['sales'], 'var_function-call-11257887081723725315': ['tracks'], 'var_function-call-1799123912854599991': 'file_storage/function-call-1799123912854599991.json', 'var_function-call-1799123912854599852': 'file_storage/function-call-1799123912854599852.json', 'var_function-call-4323077467602865475': {'best_song_key': ['none', 'none'], 'revenue': 14647.52, 'display_name': 'None by none'}, 'var_function-call-15343428881387402340': [{'key': ['none', '001'], 'revenue': 5866.4800000000005, 'display_name': '00-1 by none'}, {'key': ['rich matteson', 'groovey'], 'revenue': 5417.34, 'display_name': 'Rich Matteson - Groovey by rich matteson'}, {'key': ['syb van der ploeg', 'zo gaat het leven aan je voor'], 'revenue': 5256.43, 'display_name': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur) by Syb van der Ploeg'}, {'key': ['none', '003'], 'revenue': 5022.32, 'display_name': '003- by none'}, {'key': ['ske', 'vagga'], 'revenue': 4981.380000000001, 'display_name': 'Ske - Vagga by ske'}, {'key': ['tiidmäldä', 'kiä meil pahanu'], 'revenue': 4916.11, 'display_name': '[tiidmäldä] - Kiä meil pahanu? by tiidmäldä'}, {'key': ['fischerspooner', 'emerge'], 'revenue': 4896.24, 'display_name': 'Fischerspooner - Emerge (Dexter remix) by fischerspooner'}, {'key': ['hans zimmer', 'best friends'], 'revenue': 4806.24, 'display_name': 'Hans Zimmer - Best Friends by hans zimmer'}, {'key': ['echolyn', 'letters a short essay'], 'revenue': 4694.76, 'display_name': 'Letters A Short Essay (As the World) by echolyn'}, {'key': ['vrisak generacije', 'ne veruj'], 'revenue': 4693.259999999999, 'display_name': 'Ne veruj (Beer Drinkers Revenge) by Vrisak generacije'}], 'var_function-call-13851524421035754446': [{'key': ['none', '001'], 'total_revenue': 5866.48, 'tracks': [{'track_id': '18', 'original_title': '00-1', 'original_artist': 'None', 'revenue': 939.3100000000001}, {'track_id': '9044', 'original_title': '001-', 'original_artist': 'None', 'revenue': 1435.13}, {'track_id': '10149', 'original_title': '001-', 'original_artist': 'None', 'revenue': 303.88}, {'track_id': '11049', 'original_title': '001-', 'original_artist': 'None', 'revenue': 866.8199999999999}, {'track_id': '13656', 'original_title': '001- (Main Title Song)', 'original_artist': 'None', 'revenue': 1184.73}, {'track_id': '15937', 'original_title': '001-', 'original_artist': 'None', 'revenue': 1136.61}]}, {'key': ['rich matteson', 'groovey'], 'total_revenue': 5417.34, 'tracks': [{'track_id': '6146', 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None', 'revenue': 1288.75}, {'track_id': '8829', 'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'revenue': 2142.48}, {'track_id': '16496', 'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'revenue': 949.8199999999999}, {'track_id': '17312', 'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'revenue': 1036.29}]}, {'key': ['syb van der ploeg', 'zo gaat het leven aan je voor'], 'total_revenue': 5256.43, 'tracks': [{'track_id': '3024', 'original_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'original_artist': 'Syb van der Ploeg', 'revenue': 1754.6800000000003}, {'track_id': '3435', 'original_title': 'Zo gaat het leven aan je voor', 'original_artist': 'Syb van der Ploeg', 'revenue': 2024.37}, {'track_id': '13225', 'original_title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'original_artist': 'None', 'revenue': 1477.38}]}, {'key': ['none', '003'], 'total_revenue': 5022.320000000001, 'tracks': [{'track_id': '3833', 'original_title': '003-', 'original_artist': 'None', 'revenue': 496.93}, {'track_id': '7540', 'original_title': '003-', 'original_artist': 'None', 'revenue': 949.57}, {'track_id': '9453', 'original_title': '003-,  ', 'original_artist': 'None', 'revenue': 248.95}, {'track_id': '10208', 'original_title': '003-', 'original_artist': 'None', 'revenue': 1045.5900000000001}, {'track_id': '11778', 'original_title': '003- (Instrumenntal)', 'original_artist': 'None', 'revenue': 1326.5900000000001}, {'track_id': '15920', 'original_title': '003-', 'original_artist': 'None', 'revenue': 954.69}]}, {'key': ['ske', 'vagga'], 'total_revenue': 4981.38, 'tracks': [{'track_id': '6188', 'original_title': 'Ske - Vagga', 'original_artist': 'None', 'revenue': 1459.5600000000002}, {'track_id': '12735', 'original_title': 'Vagga', 'original_artist': 'Ske', 'revenue': 1358.13}, {'track_id': '14686', 'original_title': 'Vagga (Feelings Are Great)', 'original_artist': 'Ske', 'revenue': 2163.69}]}]}

exec(code, env_args)
