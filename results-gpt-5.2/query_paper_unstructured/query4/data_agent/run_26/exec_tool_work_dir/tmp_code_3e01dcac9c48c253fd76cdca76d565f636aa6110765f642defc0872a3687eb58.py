code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

papers = load_records(var_call_vCUdTQg2FKmMxdoVX0kKfXyL)
cites = load_records(var_call_oisrREIfYp0vJbMavVKozCIA)

# Build citation map
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

# Heuristic extract year from first 2000 chars
year_pat = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
    if not text:
        return None
    head = text[:2500]
    # look for copyright year first
    m = re.search(r"Copyright\s+(?:\d{4}\s*)?\u00a9\s*(19\d{2}|20\d{2})", head)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|PervasiveHealth|OzCHI)[^\n]{0,80}\b(19\d{2}|20\d{2})\b", head)
    if m:
        return int(m.group(1))
    # fallback: first plausible year
    m = year_pat.search(head)
    if m:
        return int(m.group(1))
    return None

results = []
for doc in papers:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = doc.get('text','')
    # domain match: physical activity anywhere in text (case-insensitive)
    if not re.search(r"physical\s+activity", text, flags=re.I):
        continue
    year = extract_year(text)
    if year != 2016:
        continue
    total_citations = cite_map.get(title, 0)
    results.append({'title': title, 'total_citations': total_citations})

# sort desc citations
results = sorted(results, key=lambda x: (-x['total_citations'], x['title']))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_oisrREIfYp0vJbMavVKozCIA': 'file_storage/call_oisrREIfYp0vJbMavVKozCIA.json', 'var_call_vCUdTQg2FKmMxdoVX0kKfXyL': 'file_storage/call_vCUdTQg2FKmMxdoVX0kKfXyL.json'}

exec(code, env_args)
