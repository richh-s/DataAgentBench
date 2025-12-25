code = """import json
import re

# Load data
with open(locals()['var_function-call-3828468449816819381'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-8657562732755232343'], 'r') as f:
    tracks_data = json.load(f)

# Improved normalization
def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    # Replace common separators with something distinctive or just remove
    # Replacing & with 'and' might be english specific but generally okay
    s = s.replace('&', 'and').replace('+', 'and')
    # Keep all alphanumeric characters (Unicode safe in Python 3)
    s = "".join(c for c in s if c.isalnum())
    return s

# Process tracks
track_map = {}
entity_display = {} 

for t in tracks_data:
    tid = t['track_id']
    title = t['title'] if t['title'] != 'None' else ''
    artist = t['artist'] if t['artist'] != 'None' else ''
    
    # Heuristic for missing artist
    if artist.lower() in ['[unknown]', 'unknown', '', 'none']:
        artist = ''
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # Only apply if it looks like a clean split?
            # e.g. "Artist - Title"
            a = parts[0].strip()
            t_str = parts[1].strip()
            if a and t_str:
                artist = a
                title = t_str

    n_artist = normalize(artist)
    n_title = normalize(title)
    
    key = f"{n_artist}|{n_title}"
    
    track_map[tid] = key
    
    # Save display info
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
# Exclude the empty key "|" if it exists and has high revenue (likely junk)
# But if it's the only one, well...
sorted_entities = sorted(entity_revenue.items(), key=lambda x: x[1], reverse=True)

# Print top 5 for inspection
top_results = []
for k, rev in sorted_entities[:5]:
    info = entity_display[k]
    top_results.append({
        'title': info['title'],
        'artist': info['artist'],
        'revenue': rev,
        'key': k
    })

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json', 'var_function-call-11634248558502887746': {'title': '"Аркан" (цимбали, скрипка, дводенцівка, бубен) (Космацькі музики - Етнічна музика України)', 'artist': 'Космацькі музики', 'total_revenue_usd': 219645.05000000005, 'key': '|'}}

exec(code, env_args)
