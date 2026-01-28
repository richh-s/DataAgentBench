code = """import json
import re
from collections import defaultdict

# helper to load stored variables
def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pubs = load_var(var_call_nG4KOJF59HBROpIB7PwbHqX5)
cpc_defs = load_var(var_call_hnFavxwW0sybhS8wFekNe8f8)

# Build level-4 CPC mapping
level4_symbols = set()
symbol_title = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    title = rec.get('titleFull')
    if sym:
        level4_symbols.add(sym)
        symbol_title[sym] = title

counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    filing = rec.get('filing_date','') or ''
    years = re.findall('[0-9]{4}', filing)
    if not years:
        for field in ('publication_date','grant_date'):
            years = re.findall('[0-9]{4}', rec.get(field,'') or '')
            if years:
                break
    if not years:
        continue
    year = int(years[0])
    cpc_field = rec.get('cpc') or ''
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # fallback: extract codes with simple regex
        codes = re.findall('"code"\s*:\s*"([^"]+)"', cpc_field)
        cpcs = [{'code': c} for c in codes]
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else ''
        if not code:
            continue
        top = code.split('/')[0][:3]
        if top in level4_symbols:
            counts[top][year] += 1

alpha = 0.1
results = []
for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], -kv[0]))[0]
    best_ema = ema_by_year[best_year]
    results.append({'symbol': sym, 'titleFull': symbol_title.get(sym,''), 'best_year': int(best_year), 'best_ema': float(best_ema)})

results_sorted = sorted(results, key=lambda r: r['best_ema'], reverse=True)
output = json.dumps(results_sorted)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_Ze1b7rTSuWSboYm69ypbIYtw': 'file_storage/call_Ze1b7rTSuWSboYm69ypbIYtw.json', 'var_call_hnFavxwW0sybhS8wFekNe8f8': 'file_storage/call_hnFavxwW0sybhS8wFekNe8f8.json', 'var_call_nG4KOJF59HBROpIB7PwbHqX5': 'file_storage/call_nG4KOJF59HBROpIB7PwbHqX5.json'}

exec(code, env_args)
