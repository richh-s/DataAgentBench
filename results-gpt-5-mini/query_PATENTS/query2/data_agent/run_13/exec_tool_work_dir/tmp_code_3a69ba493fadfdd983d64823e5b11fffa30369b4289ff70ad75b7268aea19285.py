code = """import json, re

# load query results from storage variables
with open(var_call_OmRNX83dyGJw6pDYgfkBbK3G, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_pbbgtafowuKchytUxWpyKUzq, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# build cpc symbol -> titleFull mapping
cpc_map = {rec.get('symbol'): rec.get('titleFull') for rec in cpc_defs}

# helper to extract year
year_re = re.compile(r'(19|20)\d{2}')
month_re = re.compile(r'Jul|July|Aug|August|Sep|Sept|September|Oct|October|Nov|November|Dec|December', re.I)

def looks_like_germany(info):
    if not info:
        return False
    if ' from DE' in info or ' from DE,' in info:
        return True
    if re.search(r'\bDE\b', info):
        return True
    if 'DE-' in info:
        return True
    return False

counts = {}  # group -> year -> count

for rec in pubs:
    grant = rec.get('grant_date') or ''
    if not grant or not re.search(r'2019', grant):
        continue
    if not month_re.search(grant):
        continue
    info = rec.get('Patents_info') or ''
    if not looks_like_germany(info):
        continue
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        # try looking in grant as fallback
        m2 = year_re.search(grant)
        if m2:
            filing_year = int(m2.group(0))
        else:
            continue
    else:
        filing_year = int(m.group(0))

    # parse cpc json-like field
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # attempt to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\n", "").replace("\t", ""))
        except Exception:
            cpcs = []

    groups = set()
    for ce in cpcs:
        code = (ce.get('code') if isinstance(ce, dict) else None) or ''
        code = code.upper()
        m2 = re.match(r'^([A-Z]\d{2})', code)
        if m2:
            groups.add(m2.group(1))
        elif len(code) >= 3:
            groups.add(code[:3])

    for g in groups:
        counts.setdefault(g, {})
        counts[g][filing_year] = counts[g].get(filing_year, 0) + 1

# compute EMA per group (alpha 0.1)
alpha = 0.1
results = []
for g, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    emas = {}
    ema = None
    for y in years:
        x = year_counts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * ema
        emas[y] = ema
    # find best year where EMA is maximal
    best_year = max(emas.items(), key=lambda kv: kv[1])[0]
    max_ema = emas[best_year]
    results.append({'cpc_group': g, 'titleFull': cpc_map.get(g, ''), 'best_year': best_year, 'max_ema': round(float(max_ema), 4)})

# sort by max_ema desc and take top 10
results_sorted = sorted(results, key=lambda r: r['max_ema'], reverse=True)
output = results_sorted[:10]

print("__RESULT__:")
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_pbbgtafowuKchytUxWpyKUzq': 'file_storage/call_pbbgtafowuKchytUxWpyKUzq.json', 'var_call_OmRNX83dyGJw6pDYgfkBbK3G': 'file_storage/call_OmRNX83dyGJw6pDYgfkBbK3G.json'}

exec(code, env_args)
