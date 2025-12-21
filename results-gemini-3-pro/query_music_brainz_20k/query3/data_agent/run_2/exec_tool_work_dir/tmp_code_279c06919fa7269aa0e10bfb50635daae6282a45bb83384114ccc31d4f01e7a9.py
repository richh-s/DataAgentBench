code = """import json
import re

# Load data
with open(locals()['var_function-call-10663605738424963180'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-10663605738424965213'], 'r') as f:
    tracks_data = json.load(f)

# Create sales lookup
sales_map = {}
for s in sales_data:
    tid = str(s['track_id'])
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    sales_map[tid] = rev

def normalize_text(text):
    if not text or text.lower() in ['none', 'unknown', '[unknown]']:
        return ""
    # Lowercase
    text = text.lower()
    # Remove things in parens/brackets
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    # Remove special chars (keep only alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Collapse spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

aggregated_revenue = {}
track_info_map = {}

for t in tracks_data:
    tid = str(t['track_id'])
    rev = sales_map.get(tid, 0.0)
    
    raw_title = t['title']
    raw_artist = t['artist']
    
    # Handle "Artist - Title" in title field if artist is missing
    if (not raw_artist or str(raw_artist).lower() in ['none', 'unknown', '[unknown]']) and raw_title and ' - ' in raw_title:
        parts = raw_title.split(' - ', 1)
        raw_artist = parts[0]
        raw_title = parts[1]
        
    n_title = normalize_text(raw_title)
    n_artist = normalize_text(raw_artist)
    
    # Skip if title is empty
    if not n_title:
        continue
        
    key = (n_title, n_artist)
    
    if key not in aggregated_revenue:
        aggregated_revenue[key] = 0.0
        track_info_map[key] = {'titles': [], 'artists': []}
        
    aggregated_revenue[key] += rev
    track_info_map[key]['titles'].append(raw_title)
    track_info_map[key]['artists'].append(raw_artist)

# Find max
best_key = None
max_rev = -1.0

for key, rev in aggregated_revenue.items():
    if rev > max_rev:
        max_rev = rev
        best_key = key

result = {}
if best_key:
    info = track_info_map[best_key]
    # Pick the most common title/artist representation or just the first one
    from collections import Counter
    def most_common(lst):
        return Counter(lst).most_common(1)[0][0]
    
    final_title = most_common(info['titles'])
    final_artist = most_common(info['artists'])
    
    result = {
        "title": final_title,
        "artist": final_artist,
        "revenue_usd": max_rev,
        "normalized_key": best_key
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10663605738424963180': 'file_storage/function-call-10663605738424963180.json', 'var_function-call-10663605738424965213': 'file_storage/function-call-10663605738424965213.json'}

exec(code, env_args)
