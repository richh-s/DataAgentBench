code = """import json, re
from statistics import mean

# Load full citations result
with open(var_call_WN3oMTLFS9V3V4iXVIYyV8s5, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_3RkYaGWs5KK6mtZ8iy1Jx7im, 'r') as f:
    papers = json.load(f)

# Index papers by title (filename without .txt)
index = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # Heuristic: source is ACM if 'ACM' appears near copyright/permission lines
    is_acm = False
    header = text[:4000]
    if re.search(r'\bACM\b', header):
        is_acm = True
    index[title] = {'is_acm': is_acm}

# Collect citation counts for ACM papers cited in 2018
counts = []
for row in citations:
    title = row['title']
    info = index.get(title)
    if not info:
        continue
    if info['is_acm']:
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        counts.append(c)

avg = mean(counts) if counts else None

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WN3oMTLFS9V3V4iXVIYyV8s5': 'file_storage/call_WN3oMTLFS9V3V4iXVIYyV8s5.json', 'var_call_3RkYaGWs5KK6mtZ8iy1Jx7im': 'file_storage/call_3RkYaGWs5KK6mtZ8iy1Jx7im.json'}

exec(code, env_args)
