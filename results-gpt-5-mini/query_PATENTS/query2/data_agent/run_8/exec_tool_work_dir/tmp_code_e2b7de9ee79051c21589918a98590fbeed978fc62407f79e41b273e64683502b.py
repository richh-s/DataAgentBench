code = """import json
import re
from collections import defaultdict

# Load data from storage files
with open(var_call_W2pspK7nUP7yhZZAW1nXuO95, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_aQmPonclfy6L3wi98CbYh7bV, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build lookup for level-4 CPC titles
cpc_title = {d.get('symbol'): d.get('titleFull') for d in cpc_defs}

# Regex helpers
year_re = re.compile(r'(19|20)\d{2}')
symbol_re = re.compile(r'^([A-Z]\d{2})')

# Aggregate counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()
for rec in pubs:
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    year = None
    if m:
        year = int(m.group(0))
    else:
        pi = rec.get('Patents_info','')
        m2 = year_re.search(pi)
        if m2:
            year = int(m2.group(0))
    if year is None:
        continue
    all_years.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code:
            continue
        m3 = symbol_re.match(code.strip())
        if m3:
            sym = m3.group(1)
        else:
            sym = code.strip()[:3]
        counts[sym][year] += 1

# Compute EMA per symbol and find best year
alpha = 0.1
results = []
for sym, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    ema_prev = None
    ema_by_year = {}
    for y in years:
        val = yc.get(y, 0)
        if ema_prev is None:
            ema = float(val)
        else:
            ema = alpha * float(val) + (1 - alpha) * ema_prev
        ema_by_year[y] = ema
        ema_prev = ema
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    max_ema = max(ema_by_year.values())
    results.append({"symbol": sym, "titleFull": cpc_title.get(sym), "best_year": int(best_year), "max_ema": round(float(max_ema), 6)})

# Sort and prepare final output
results_sorted = sorted(results, key=lambda d: d['max_ema'], reverse=True)
final = [{"cpc_group_code": r['symbol'], "titleFull": r['titleFull'], "best_year": r['best_year']} for r in results_sorted]

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_W2pspK7nUP7yhZZAW1nXuO95': 'file_storage/call_W2pspK7nUP7yhZZAW1nXuO95.json', 'var_call_aQmPonclfy6L3wi98CbYh7bV': 'file_storage/call_aQmPonclfy6L3wi98CbYh7bV.json'}

exec(code, env_args)
