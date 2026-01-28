code = """import json, re
with open(var_call_UMpMrz4lCiA9igDmtZ2PavIv, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_ZrFlxzUHvMfCckRIwz8q3PLt, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# build a map from filename (without .txt) to document text
doc_map = {}
for d in docs:
    fn = d.get('filename','')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    doc_map[title.strip()] = d.get('text','') or ''

# build total citation map from citations list
cit_map = {}
for rec in citations:
    t = rec.get('title')
    if not t:
        continue
    tot = rec.get('total_citations', 0)
    try:
        tot = int(tot)
    except:
        try:
            tot = int(str(tot).strip())
        except:
            tot = 0
    cit_map[t.strip()] = tot

results = []
for title, total in cit_map.items():
    text = doc_map.get(title)
    if text is None:
        # try fuzzy matching: case-insensitive exact
        for k in doc_map.keys():
            if k.lower() == title.lower():
                text = doc_map[k]
                break
    if not text:
        continue
    low = text.lower()
    if 'empirical' not in low:
        continue
    # find years 2017-2026
    years = re.findall(r"\b(20(?:1[7-9]|2[0-6]))\b", text)
    years = [int(y) for y in years]
    if not years:
        continue
    # pick the earliest year mention >=2017
    year = min([y for y in years if y>=2017] or [0])
    if year <= 2016:
        continue
    results.append({'title': title, 'total_citations': total})

# sort
results = sorted(results, key=lambda x: x['title'].lower())

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_oZwUttyf1z8kVala5AUJPXmA': ['paper_docs'], 'var_call_grasnMaKKZOf38O99JQmcWKN': ['Citations', 'sqlite_sequence'], 'var_call_UMpMrz4lCiA9igDmtZ2PavIv': 'file_storage/call_UMpMrz4lCiA9igDmtZ2PavIv.json', 'var_call_ZrFlxzUHvMfCckRIwz8q3PLt': 'file_storage/call_ZrFlxzUHvMfCckRIwz8q3PLt.json', 'var_call_k80NjCbEIROUNEXL9cmvYB37': []}

exec(code, env_args)
