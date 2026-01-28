code = """import json, re
# load large results from previous tool calls (file paths are provided in variables)
with open(var_call_UMpMrz4lCiA9igDmtZ2PavIv, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_ZrFlxzUHvMfCckRIwz8q3PLt, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# build citation map
cit_map = {}
for rec in citations:
    t = rec.get('title')
    if t is None:
        continue
    # normalize whitespace
    key = t.strip()
    # total_citations might be string
    tot = rec.get('total_citations', 0)
    try:
        tot = int(tot)
    except:
        try:
            tot = int(str(tot).strip())
        except:
            tot = 0
    cit_map[key] = tot

results = []

for d in docs:
    filename = d.get('filename','')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = d.get('text','') or ''
    low = text.lower()
    # find a publication year >=2017
    year = None
    # first look for common conference lines like CHI 2018
    m = re.search(r'\b(20(?:1[7-9]|2[0-9]))\b', text)
    if m:
        year = int(m.group(0))
    else:
        # fallback: find any 4-digit year and pick first >2016
        all_yrs = re.findall(r'\b(20[0-9]{2})\b', text)
        for yy in all_yrs:
            y = int(yy)
            if y > 2016 and y <= 2026:
                year = y
                break
    if not year:
        continue
    if year <= 2016:
        continue
    # check contribution contains 'empirical' via substring
    if 'empirical' in low:
        # find matching citation total
        total = None
        # exact match
        if title in cit_map:
            total = cit_map[title]
        else:
            # try various normalizations
            tnorm = title.strip().lower()
            for k,v in cit_map.items():
                if k.strip().lower() == tnorm:
                    total = v
                    break
            if total is None:
                for k,v in cit_map.items():
                    kl = k.strip().lower()
                    if kl in tnorm or tnorm in kl:
                        total = v
                        break
        if total is None:
            total = 0
        results.append({'title': title, 'total_citations': total})

# sort results by title for consistency
results = sorted(results, key=lambda x: x['title'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_oZwUttyf1z8kVala5AUJPXmA': ['paper_docs'], 'var_call_grasnMaKKZOf38O99JQmcWKN': ['Citations', 'sqlite_sequence'], 'var_call_UMpMrz4lCiA9igDmtZ2PavIv': 'file_storage/call_UMpMrz4lCiA9igDmtZ2PavIv.json', 'var_call_ZrFlxzUHvMfCckRIwz8q3PLt': 'file_storage/call_ZrFlxzUHvMfCckRIwz8q3PLt.json'}

exec(code, env_args)
