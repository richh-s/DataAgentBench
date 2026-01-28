code = """import json
import re
from collections import defaultdict

# Load data from storage variables (file paths)
path_pubs = var_call_eHhzzvffZKuv18Bck4To6rw3
path_cpc = var_call_OO9OQSilSfjKNR4LlPA9iiC0

with open(path_pubs, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping of level-4 symbols to titleFull
cpc_map = {rec['symbol']: rec.get('titleFull') for rec in cpc_defs}
# Sort symbols by length descending for longest-prefix match
symbols_sorted = sorted(cpc_map.keys(), key=lambda x: -len(x))

# Helper to extract filing year
year_re = re.compile(r'(19|20)\d{2}')

# Filter pubs to Germany: look for 'Germany' or word-boundary 'DE'
filtered = []
for p in pubs:
    info = p.get('Patents_info','')
    if not isinstance(info, str):
        continue
    if re.search(r'\bDE\b', info, re.IGNORECASE) or 'germany' in info.lower():
        filtered.append(p)

# Aggregate counts per group per filing year
counts = defaultdict(lambda: defaultdict(int))
for p in filtered:
    filing = p.get('filing_date','') or ''
    m = year_re.search(filing)
    if not m:
        # try grant_date if filing_date missing
        f2 = p.get('grant_date','') or ''
        m = year_re.search(f2)
    if not m:
        continue
    year = int(m.group(0))
    # parse cpc JSON-like string
    cpc_field = p.get('cpc','') or ''
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpc_list = json.loads(cpc_field.replace("\n", "").replace("\t", ""))
        except Exception:
            continue
    codes = []
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        code = code.replace(' ', '')
        codes.append(code)
    # for each code, map to level-4 symbol
    matched_symbols = set()
    for code in codes:
        for sym in symbols_sorted:
            if code.upper().startswith(sym.upper()):
                matched_symbols.add(sym)
                break
    for sym in matched_symbols:
        counts[sym][year] += 1

# For each symbol, compute EMA across years (include zeros for gaps)
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    if sym not in cpc_map:
        continue
    years = sorted(year_counts.keys())
    if not years:
        continue
    min_y = min(years)
    max_y = max(years)
    # build full series
    series = [year_counts.get(y, 0) for y in range(min_y, max_y+1)]
    # compute EMA
    ema_vals = []
    ema = None
    for v in series:
        if ema is None:
            ema = v
        else:
            ema = alpha * v + (1 - alpha) * ema
        ema_vals.append(ema)
    # find year with max EMA
    max_idx = max(range(len(ema_vals)), key=lambda i: ema_vals[i])
    best_year = min_y + max_idx
    best_year_ema = ema_vals[max_idx]
    results.append({
        'symbol': sym,
        'titleFull': cpc_map.get(sym),
        'best_year': best_year,
        'best_year_ema': round(best_year_ema, 6)
    })

# Sort results by best_year_ema descending
results_sorted = sorted(results, key=lambda x: -x['best_year_ema'])

import json as _json
print("__RESULT__:")
print(_json.dumps(results_sorted))"""

env_args = {'var_call_eHhzzvffZKuv18Bck4To6rw3': 'file_storage/call_eHhzzvffZKuv18Bck4To6rw3.json', 'var_call_OO9OQSilSfjKNR4LlPA9iiC0': 'file_storage/call_OO9OQSilSfjKNR4LlPA9iiC0.json'}

exec(code, env_args)
