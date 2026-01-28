code = """import json
path = var_call_VPIjJV0MwaTNmYb1IXbnb3Ip
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
seen = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'fema' in low or 'emergency' in low or 'caloes' in low or 'disaster' in low or 'federal' in low:
            start = max(0, idx-3)
            end = min(len(lines), idx+4)
            for j in range(start, end):
                l = lines[j].strip()
                ll = l.lower()
                if any(k in ll for k in ['project','repairs','repair','improvements','facility','phase','playground','walkway']):
                    if l and l not in seen:
                        seen.add(l)
                        found.append({'Project_Name': l})

print('__RESULT__:')
print(json.dumps(found))"""

env_args = {'var_call_VPIjJV0MwaTNmYb1IXbnb3Ip': 'file_storage/call_VPIjJV0MwaTNmYb1IXbnb3Ip.json'}

exec(code, env_args)
