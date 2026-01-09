code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
docs_src = var_call_urqQvPDDNTuisiC9AaBv7TRX
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Load citations totals
tot_src = var_call_lRDmaLR0wnwMoQWFAwDd3Sla
if isinstance(tot_src, str):
    with open(tot_src, 'r', encoding='utf-8') as f:
        totals = json.load(f)
else:
    totals = tot_src

tot_map = {}
for r in totals:
    title = r.get('title')
    tc = r.get('total_citations')
    try:
        tc_i = int(tc)
    except Exception:
        try:
            tc_i = int(float(tc))
        except Exception:
            tc_i = None
    tot_map[title] = tc_i

# helper extract year near header (first 2000 chars)
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def infer_year(text):
    head = text[:2500]
    years = [int(m.group(1)) for m in year_pat.finditer(head)]
    # choose most common year in head
    if not years:
        return None
    # prefer 2016 if present
    if 2016 in years:
        return 2016
    # otherwise take max <= current maybe
    return max(years)

results = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # domain filter: contains physical activity
    if 'physical activity' not in text.lower() and 'physical activity' not in title.lower():
        continue
    yr = infer_year(text)
    if yr != 2016:
        continue
    tc = tot_map.get(title)
    results.append({'title': title, 'total_citations': tc})

# de-dup by title
seen=set(); dedup=[]
for r in results:
    if r['title'] in seen:
        continue
    seen.add(r['title'])
    dedup.append(r)

dedup_sorted = sorted(dedup, key=lambda x: (-(x['total_citations'] or -1), x['title']))

print('__RESULT__:')
print(json.dumps(dedup_sorted))"""

env_args = {'var_call_urqQvPDDNTuisiC9AaBv7TRX': 'file_storage/call_urqQvPDDNTuisiC9AaBv7TRX.json', 'var_call_lRDmaLR0wnwMoQWFAwDd3Sla': 'file_storage/call_lRDmaLR0wnwMoQWFAwDd3Sla.json'}

exec(code, env_args)
