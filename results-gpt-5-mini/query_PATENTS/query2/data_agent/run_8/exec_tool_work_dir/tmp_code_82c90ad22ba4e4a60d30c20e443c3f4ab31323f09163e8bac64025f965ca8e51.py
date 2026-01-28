code = """import json
import re
from collections import defaultdict

# Load data from storage files (paths provided in variables)
with open(var_call_W2pspK7nUP7yhZZAW1nXuO95, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_aQmPonclfy6L3wi98CbYh7bV, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build lookup for level-4 CPC titles
cpc_title = {d.get('symbol'): d.get('titleFull') for d in cpc_defs}

# Helper to extract year from filing_date
year_re = re.compile(r'(19|20)\d{2}')
# Helper to extract level-4 symbol from CPC code (letter + two digits)
symbol_re = re.compile(r'^([A-Z]\d{2})')

# Aggregate counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year]=count
all_years = set()
for rec in pubs:
    filing = rec.get('filing_date') or ''
    # find year
    ym = year_re.findall(filing)
    year = None
    if ym:
        # findall returns list of matches of group(1) so better use search
        m = year_re.search(filing)
        if m:
            year = int(m.group(0))
    # fallback: try to find a 4-digit anywhere in Patents_info
    if year is None:
        pi = rec.get('Patents_info','')
        m = year_re.search(pi)
        if m:
            year = int(m.group(0))
    if year is None:
        continue
    all_years.add(year)

    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field may already be a JSON string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean and eval-like
        try:
            cpcs = json.loads(cpc_field.replace("\'","\""))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        m = symbol_re.match(code.strip())
        if not m:
            # try alternative: first 3 chars
            sym = code.strip()[:3]
        else:
            sym = m.group(1)
        counts[sym][year] += 1

# For each symbol compute EMA across its sorted years
alpha = 0.1
results = []
for sym, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    # compute EMA sequentially in chronological order
    ema_prev = None
    ema_by_year = {}
    for y in years:
        val = yc.get(y, 0)
        if ema_prev is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema_prev
        ema_by_year[y] = ema
        ema_prev = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    results.append({"symbol": sym, "titleFull": cpc_title.get(sym), "best_year": best_year, "max_ema": round(max(ema_by_year.values()), 6)})

# Sort results by max_ema descending
results_sorted = sorted(results, key=lambda d: d['max_ema'], reverse=True)
# Prepare final output with only requested fields (title, code, best year)
final = [{"cpc_group_code": r['symbol'], "titleFull": r['titleFull'], "best_year": r['best_year']} for r in results_sorted]

import json as _json
print("__RESULT__:")
print(_json.dumps(final))"""

env_args = {'var_call_W2pspK7nUP7yhZZAW1nXuO95': 'file_storage/call_W2pspK7nUP7yhZZAW1nXuO95.json', 'var_call_aQmPonclfy6L3wi98CbYh7bV': 'file_storage/call_aQmPonclfy6L3wi98CbYh7bV.json'}

exec(code, env_args)
