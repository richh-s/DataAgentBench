code = """import json, re
import pandas as pd

def load_mongo(path_or_list):
    if isinstance(path_or_list, str):
        with open(path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_list

docs = load_mongo(var_call_eVrI8OuXTgjZjZ2CbaODIcSm)

# identify 2016 + physical activity papers via heuristic parsing
res_titles = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','') or ''
    if not re.search(r'(?i)physical activity', text):
        continue
    # year detection: look for copyright year or venue year patterns
    m = re.search(r'Copyright\s+(\d{4})', text)
    year = int(m.group(1)) if m else None
    if year != 2016:
        continue
    res_titles.append(title)

# citations totals
cits = var_call_yX1sMCVBVrV9q7SybGHWoVIA
if isinstance(cits, str):
    with open(cits, 'r', encoding='utf-8') as f:
        cits = json.load(f)

cit_map = {r['title']: int(r['total_citations']) for r in cits}

out = []
for t in sorted(set(res_titles)):
    out.append({'title': t, 'total_citations': cit_map.get(t)})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eVrI8OuXTgjZjZ2CbaODIcSm': 'file_storage/call_eVrI8OuXTgjZjZ2CbaODIcSm.json', 'var_call_yX1sMCVBVrV9q7SybGHWoVIA': 'file_storage/call_yX1sMCVBVrV9q7SybGHWoVIA.json'}

exec(code, env_args)
