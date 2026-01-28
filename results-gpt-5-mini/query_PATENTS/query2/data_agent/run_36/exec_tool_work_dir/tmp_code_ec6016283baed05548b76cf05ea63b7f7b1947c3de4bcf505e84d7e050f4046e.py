code = """import json
import ast
from collections import defaultdict

# Load file paths from storage
path_pubs = var_call_eHhzzvffZKuv18Bck4To6rw3
path_cpc = var_call_OO9OQSilSfjKNR4LlPA9iiC0

with open(path_pubs, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Map level-4 symbols to titleFull
cpc_map = {rec['symbol']: rec.get('titleFull') for rec in cpc_defs}
symbols_sorted = sorted(cpc_map.keys(), key=lambda x: -len(x))

# helper to extract year (4-digit starting with 19 or 20)
def extract_year(text):
    if not text:
        return None
    s = str(text)
    for i in range(len(s)-3):
        sub = s[i:i+4]
        if sub.isdigit() and (sub.startswith('19') or sub.startswith('20')):
            return int(sub)
    return None

# Filter pubs to Germany
filtered = []
for p in pubs:
    info = p.get('Patents_info','')
    if not isinstance(info, str):
        continue
    if 'germany' in info.lower() or (' DE ' in (' '+info+' ')) or info.strip().endswith('DE'):
        filtered.append(p)

# Aggregate counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
for p in filtered:
    year = extract_year(p.get('filing_date') or '')
    if year is None:
        year = extract_year(p.get('grant_date') or '')
    if year is None:
        continue
    cpc_field = p.get('cpc','') or ''
    cpc_list = None
    if isinstance(cpc_field, list):
        cpc_list = cpc_field
    else:
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            try:
                cpc_list = ast.literal_eval(cpc_field)
            except Exception:
                cpc_list = None
    if not cpc_list:
        continue
    codes = []
    for entry in cpc_list:
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, (list,tuple)) and len(entry)>0:
            code = entry[0]
        else:
            code = None
        if not code:
            continue
        code = str(code).replace(' ','')
        codes.append(code)
    matched = set()
    for code in codes:
        for sym in symbols_sorted:
            if code.upper().startswith(sym.upper()):
                matched.add(sym)
                break
    for sym in matched:
        counts[sym][year] += 1

# Compute EMA per symbol
alpha = 0.1
results = []
for sym, yc in counts.items():
    if sym not in cpc_map:
        continue
    years = sorted(yc.keys())
    if not years:
        continue
    min_y, max_y = years[0], years[-1]
    series = [yc.get(y,0) for y in range(min_y, max_y+1)]
    ema = None
    ema_vals = []
    for v in series:
        if ema is None:
            ema = v
        else:
            ema = alpha * v + (1 - alpha) * ema
        ema_vals.append(ema)
    # find max EMA and corresponding year
    max_idx = max(range(len(ema_vals)), key=lambda i: ema_vals[i])
    best_year = min_y + max_idx
    best_year_ema = ema_vals[max_idx]
    results.append({
        'symbol': sym,
        'titleFull': cpc_map.get(sym),
        'best_year': best_year,
        'best_year_ema': round(best_year_ema,6)
    })

results_sorted = sorted(results, key=lambda x: -x['best_year_ema'])

import json as _json
print("__RESULT__:")
print(_json.dumps(results_sorted))"""

env_args = {'var_call_eHhzzvffZKuv18Bck4To6rw3': 'file_storage/call_eHhzzvffZKuv18Bck4To6rw3.json', 'var_call_OO9OQSilSfjKNR4LlPA9iiC0': 'file_storage/call_OO9OQSilSfjKNR4LlPA9iiC0.json'}

exec(code, env_args)
