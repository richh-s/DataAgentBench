code = """import json
import re

with open(locals()['var_function-call-3828468449816819381'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-8657562732755232343'], 'r') as f:
    tracks_data = json.load(f)

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = s.replace('&', 'and').replace('+', 'and')
    s = "".join(c for c in s if c.isalnum())
    return s

track_map = {}
entity_display = {} 
tracks_info = {t['track_id']: t for t in tracks_data}

# Check specific IDs
check_ids = ["2029", "1216", "260", "2780"]
debug_info = {}

for t in tracks_data:
    tid = t['track_id']
    title = t['title'] if t['title'] != 'None' else ''
    artist = t['artist'] if t['artist'] != 'None' else ''
    
    if artist.lower() in ['[unknown]', 'unknown', '', 'none']:
        artist = ''
        if ' - ' in title:
            parts = title.split(' - ', 1)
            if parts[0].strip() and parts[1].strip():
                artist = parts[0].strip()
                title = parts[1].strip()

    n_artist = normalize(artist)
    n_title = normalize(title)
    key = f"{n_artist}|{n_title}"
    track_map[tid] = key
    
    current_len = len(title) + len(artist)
    if key not in entity_display or current_len > entity_display[key]['len']:
        entity_display[key] = {'title': title, 'artist': artist, 'len': current_len}

    if tid in check_ids:
        debug_info[tid] = {'original': t, 'mapped_key': key, 'display': entity_display[key]}

entity_revenue = {}
for s in sales_data:
    tid = s['track_id']
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    if tid in track_map:
        key = track_map[tid]
        entity_revenue[key] = entity_revenue.get(key, 0) + rev

sorted_entities = sorted(entity_revenue.items(), key=lambda x: x[1], reverse=True)

top_results = []
for k, rev in sorted_entities[:20]:
    info = entity_display[k]
    top_results.append({
        'title': info['title'],
        'artist': info['artist'],
        'revenue': rev,
        'key': k
    })

print("__RESULT__:")
print(json.dumps({'top_20': top_results, 'debug_info': debug_info}))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json', 'var_function-call-11634248558502887746': {'title': '"Аркан" (цимбали, скрипка, дводенцівка, бубен) (Космацькі музики - Етнічна музика України)', 'artist': 'Космацькі музики', 'total_revenue_usd': 219645.05000000005, 'key': '|'}, 'var_function-call-13096650854876462206': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}]}

exec(code, env_args)
