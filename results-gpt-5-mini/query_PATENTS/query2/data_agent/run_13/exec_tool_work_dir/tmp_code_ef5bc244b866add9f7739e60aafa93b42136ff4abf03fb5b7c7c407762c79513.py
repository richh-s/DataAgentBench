code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_OmRNX83dyGJw6pDYgfkBbK3G, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_pbbgtafowuKchytUxWpyKUzq, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from CPC symbol to titleFull
cpc_map = {rec.get('symbol'): rec.get('titleFull') for rec in cpc_defs if rec.get('symbol')}

# Regexes
year_re = re.compile(r'(19|20)\d{2}')
month_re = re.compile(r'\b(Jul|July|Aug|August|Sep|Sept|September|Oct|October|Nov|November|Dec|December)\b', re.I)

def is_germany(info):
    if not info:
        return False
    info_up = info.upper()
    if ' DE ' in f' {info_up} ':
        return True
    if 'FROM DE' in info_up or 'DE-' in info_up or 'DE,' in info_up:
        return True
    # also check for country code patterns like 'DE,' or '(DE)'
    if re.search(r'\bDE[-,)]', info_up):
        return True
    return False

# Aggregate counts per CPC group (level 4 symbol like 'G06') by filing year
counts = {}

for rec in pubs:
    grant = rec.get('grant_date') or ''
    if not grant or '2019' not in grant:
        continue
    # only second half months
    if not month_re.search(grant):
        continue
    info = rec.get('Patents_info') or ''
    if not is_germany(info):
        continue
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if m:
        filing_year = int(m.group(0))
    else:
        # fallback to grant year
        m2 = year_re.search(grant)
        if not m2:
            continue
        filing_year = int(m2.group(0))

    # parse cpc field which is a JSON-like string
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try cleaning newlines and tabs
        try:
            cleaned = cpc_field.replace('\n', '').replace('\t', '')
            cpcs = json.loads(cleaned)
        except Exception:
            cpcs = []

    groups = set()
    for ce in cpcs:
        if isinstance(ce, dict):
            code = (ce.get('code') or '').upper()
        else:
            code = str(ce).upper()
        # extract level-4 group symbol: letter + two digits
        m3 = re.match(r'^([A-Z]\d{2})', code)
        if m3:
            groups.add(m3.group(1))
        else:
            # fallback: first 3 chars
            if len(code) >= 3:
                groups.add(code[:3])

    for g in groups:
        counts.setdefault(g, {})
        counts[g][filing_year] = counts[g].get(filing_year, 0) + 1

# Compute EMA (alpha=0.1) per group across years and pick best year
alpha = 0.1
results = []
for g, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    ema = None
    emas = {}
    for y in years:
        x = yc[y]
        if ema is None:
            ema = float(x)
        else:
            ema = alpha * float(x) + (1 - alpha) * ema
        emas[y] = ema
    best_year = max(emas.items(), key=lambda kv: kv[1])[0]
    max_ema = emas[best_year]
    results.append({
        'cpc_group': g,
        'titleFull': cpc_map.get(g, ''),
        'best_year': int(best_year),
        'max_ema': round(float(max_ema), 4)
    })

# Sort and take top entries
results_sorted = sorted(results, key=lambda r: r['max_ema'], reverse=True)
output = results_sorted[:10]

print("__RESULT__:")
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_pbbgtafowuKchytUxWpyKUzq': 'file_storage/call_pbbgtafowuKchytUxWpyKUzq.json', 'var_call_OmRNX83dyGJw6pDYgfkBbK3G': 'file_storage/call_OmRNX83dyGJw6pDYgfkBbK3G.json'}

exec(code, env_args)
