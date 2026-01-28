code = """import json
# Load the tracks query result stored in var_call_JeNOHXWVJNWbh4shv0ffr1hv
data_var = var_call_JeNOHXWVJNWbh4shv0ffr1hv

# If the storage entry is a file path (string), open it; otherwise assume it's already a list
if isinstance(data_var, str):
    with open(data_var, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = data_var

matches = []
for r in tracks:
    title = (r.get('title') or '').lower()
    artist = (r.get('artist') or '').lower()
    # Heuristics: match if title contains both street and hype, or artist contains maginnis/brucqe, or title contains maginnis/brucqe
    if (('street' in title and 'hype' in title) 
        or 'maginnis' in artist 
        or 'brucqe' in artist 
        or 'maginnis' in title 
        or 'brucqe' in title):
        matches.append(r)

# Collect unique track_ids
track_ids = sorted(list({int(m['track_id']) for m in matches if str(m.get('track_id')).isdigit()}))

output = {'track_ids': track_ids, 'matches_count': len(matches), 'matches_sample': matches[:20]}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_JeNOHXWVJNWbh4shv0ffr1hv': 'file_storage/call_JeNOHXWVJNWbh4shv0ffr1hv.json'}

exec(code, env_args)
