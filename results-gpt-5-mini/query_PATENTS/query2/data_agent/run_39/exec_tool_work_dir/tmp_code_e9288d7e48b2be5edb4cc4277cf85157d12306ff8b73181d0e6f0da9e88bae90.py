code = """import json, re

# Load data from storage files
with open(var_call_DMAEOo5DrMotGIVPrTjyP2li, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_UmrUJeFBC7EB7BaY8VzqWJio, 'r', encoding='utf-8') as f:
    defs = json.load(f)

# Build mapping for level-4 CPC titles
title_map = {d.get('symbol'): d.get('titleFull') for d in defs if d.get('symbol')}

# Helper: check if grant_date is in second half of 2019
h2_tokens = ['july','jul','august','aug','september','sept','sep','october','oct','november','nov','december','dec']

alpha = 0.1

counts = {}  # counts[group][year] = count

for p in pubs:
    grant = (p.get('grant_date') or '').lower()
    if '2019' not in grant:
        continue
    # check month in H2
    if not any(tok in grant for tok in h2_tokens):
        continue
    # check Germany in Patents_info
    pinfo = (p.get('Patents_info') or '').lower()
    is_germany = False
    if re.search(r'\bde\b', pinfo):
        is_germany = True
    if 'de-' in pinfo or 'from de' in pinfo or ' in de' in pinfo or '(de' in pinfo:
        is_germany = True
    if not is_germany:
        continue
    # extract filing year
    filing = p.get('filing_date') or ''
    m = re.search(r'(\d{4})', filing)
    if not m:
        # try priority_date or Patents_info
        m = re.search(r'(\d{4})', p.get('priority_date') or '')
    if not m:
        m = re.search(r'(\d{4})', pinfo)
    if not m:
        continue
    year = int(m.group(1))
    # parse CPC field
    cpc_field = p.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code')
        if not code or len(code) < 3:
            continue
        group = code[:3]
        counts.setdefault(group, {})
        counts[group][year] = counts[group].get(year, 0) + 1

# For each group compute EMA across years sorted
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    # compute EMA
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], -x[0]))[0]
    best_ema = ema_by_year[best_year]
    title = title_map.get(group) or ''
    results.append({'cpc_group': group, 'titleFull': title, 'best_year': int(best_year), 'best_ema': round(float(best_ema), 4)})

# Sort results by best_ema desc
results.sort(key=lambda x: x['best_ema'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_DMAEOo5DrMotGIVPrTjyP2li': 'file_storage/call_DMAEOo5DrMotGIVPrTjyP2li.json', 'var_call_UmrUJeFBC7EB7BaY8VzqWJio': 'file_storage/call_UmrUJeFBC7EB7BaY8VzqWJio.json'}

exec(code, env_args)
