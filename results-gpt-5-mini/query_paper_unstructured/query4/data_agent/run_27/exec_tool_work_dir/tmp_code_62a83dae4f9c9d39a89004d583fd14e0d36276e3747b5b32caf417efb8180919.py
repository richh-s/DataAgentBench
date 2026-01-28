code = """import json, re
with open(var_call_iCUHDVbiSw0006lfDawFS6sX, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_AweFdR2rSs65N5Jw4r1U7H0h, 'r', encoding='utf-8') as f:
    citations = json.load(f)

cit_map = {rec.get('title','').strip(): int(rec.get('total_citations') or 0) for rec in citations}

results = []
for doc in papers:
    filename = doc.get('filename','')
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = (doc.get('text') or '').lower()
    if 'physical activity' in text and '2016' in text:
        total = cit_map.get(title.strip(), 0)
        results.append({'title': title, 'total_citations': total})

# dedupe
seen=set(); uniq=[]
for r in results:
    if r['title'] not in seen:
        seen.add(r['title']); uniq.append(r)

import json as _json
print("__RESULT__:")
print(_json.dumps(uniq))"""

env_args = {'var_call_iCUHDVbiSw0006lfDawFS6sX': 'file_storage/call_iCUHDVbiSw0006lfDawFS6sX.json', 'var_call_AweFdR2rSs65N5Jw4r1U7H0h': 'file_storage/call_AweFdR2rSs65N5Jw4r1U7H0h.json', 'var_call_eoTtOoTwL4iz64RmupnIoHVA': []}

exec(code, env_args)
