code = """import json
import re
from collections import Counter

# Load data (re-loading to be safe, though variables persist in session, the files are safer)
with open(locals()['var_function-call-10663605738424963180'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-10663605738424965213'], 'r') as f:
    tracks_data = json.load(f)

sales_map = {}
for s in sales_data:
    tid = str(s['track_id'])
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    sales_map[tid] = rev

def normalize_text(text):
    if not text or text.lower() in ['none', 'unknown', '[unknown]']:
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text) # remove (...)
    text = re.sub(r'\[[^]]*\]', '', text) # remove [...]
    text = re.sub(r'[^a-z0-9\s]', '', text) # remove non-alnum
    text = re.sub(r'\s+', ' ', text).strip()
    return text

aggregated_revenue = {}
track_info_map = {}

for t in tracks_data:
    tid = str(t['track_id'])
    rev = sales_map.get(tid, 0.0)
    
    raw_title = t['title']
    raw_artist = t['artist']
    
    # Split "Artist - Title" if Artist is None
    if (not raw_artist or str(raw_artist).lower() in ['none', 'unknown', '[unknown]']) and raw_title and ' - ' in raw_title:
        parts = raw_title.split(' - ', 1)
        # Heuristic: if the first part is short/looks like track number (e.g. "01"), maybe it's not artist?
        # But for now let's trust the split
        raw_artist = parts[0]
        raw_title = parts[1]
        
    n_title = normalize_text(raw_title)
    n_artist = normalize_text(raw_artist)
    
    if not n_title:
        continue
        
    key = (n_title, n_artist)
    
    if key not in aggregated_revenue:
        aggregated_revenue[key] = 0.0
        track_info_map[key] = {'titles': [], 'artists': [], 'ids': []}
        
    aggregated_revenue[key] += rev
    track_info_map[key]['titles'].append(raw_title)
    track_info_map[key]['artists'].append(raw_artist)
    track_info_map[key]['ids'].append(tid)

# Sort by revenue
sorted_items = sorted(aggregated_revenue.items(), key=lambda x: x[1], reverse=True)

top_results = []
for i in range(10):
    if i >= len(sorted_items): break
    key, rev = sorted_items[i]
    info = track_info_map[key]
    top_results.append({
        "key": key,
        "revenue": rev,
        "sample_titles": info['titles'][:5],
        "sample_artists": info['artists'][:5],
        "count": len(info['ids'])
    })

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-10663605738424963180': 'file_storage/function-call-10663605738424963180.json', 'var_function-call-10663605738424965213': 'file_storage/function-call-10663605738424965213.json', 'var_function-call-10167274036622288126': {'title': '003-', 'artist': 'None', 'revenue_usd': 8582.15, 'normalized_key': ['003', '']}}

exec(code, env_args)
