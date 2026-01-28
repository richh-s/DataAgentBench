code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

papers = load_records(var_call_vCUdTQg2FKmMxdoVX0kKfXyL)
cites = load_records(var_call_oisrREIfYp0vJbMavVKozCIA)

cite_map = {}
for r in cites:
    title = r.get('title')
    tc = r.get('total_citations')
    try:
        tc_int = int(tc)
    except Exception:
        try:
            tc_int = int(float(tc))
        except Exception:
            tc_int = 0
    cite_map[title] = tc_int

year_pat = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
    if not text:
        return None
    head = text[:2500]
    m = re.search(r"Copyright\s+(?:\d{4}\s*)?\u00a9\s*(19\d{2}|20\d{2})", head)
    if m:
        return int(m.group(1))
    m = year_pat.search(head)
    if m:
        return int(m.group(1))
    return None

results = []
for doc in papers:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = doc.get('text','')
    if not re.search(r"physical\s+activity", text, flags=re.I):
        continue
    year = extract_year(text)
    if year != 2016:
        continue
    results.append({'title': title, 'total_citations': int(cite_map.get(title, 0))})

results = sorted(results, key=lambda x: (-x['total_citations'], x['title']))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_oisrREIfYp0vJbMavVKozCIA': 'file_storage/call_oisrREIfYp0vJbMavVKozCIA.json', 'var_call_vCUdTQg2FKmMxdoVX0kKfXyL': 'file_storage/call_vCUdTQg2FKmMxdoVX0kKfXyL.json'}

exec(code, env_args)
