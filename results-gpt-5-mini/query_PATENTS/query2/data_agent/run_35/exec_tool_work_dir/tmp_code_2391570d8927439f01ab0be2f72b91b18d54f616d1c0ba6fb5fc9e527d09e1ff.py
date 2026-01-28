code = """import json
# Load files
with open(var_call_uX35j8swiDeRTrhkqYrZ3t7S, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_7yMwBGdeJJXK2ZKHMVmTmgWn, 'r', encoding='utf-8') as f:
    defs = json.load(f)

# Map
cpc_map = {d['symbol']: d['titleFull'] for d in defs}

# Helper to find first 4-digit year
def find_year(s):
    if not s: return None
    digits = ''
    for ch in s:
        if ch.isdigit():
            digits += ch
            if len(digits) == 4:
                return int(digits)
        else:
            digits = ''
    return None

months = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']
from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))
for rec in pubs:
    gd = rec.get('grant_date','')
    if '2019' not in gd: continue
    if not any(m in gd for m in months): continue
    year = find_year(rec.get('filing_date',''))
    if not year:
        year = find_year(gd)
    if not year: continue
    # parse cpc
    cpc_field = rec.get('cpc','')
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    for e in cpcs:
        code = e.get('code') if isinstance(e, dict) else None
        if not code: continue
        grp = code[:3]
        if len(grp) < 3 or not grp[0].isalpha() or not grp[1:3].isdigit():
            continue
        if grp in cpc_map:
            counts[grp][year] += 1

# Compute EMA
alpha = 0.1
results = []
for grp, yc in counts.items():
    years = sorted(yc.keys())
    ema = None
    ema_by_year = {}
    for y in years:
        cnt = yc.get(y,0)
        if ema is None:
            ema = float(cnt)
        else:
            ema = alpha * cnt + (1-alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    results.append({'symbol': grp, 'titleFull': cpc_map.get(grp, ''), 'best_year': int(best_year), 'best_ema': round(float(best_ema),3)})

results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)
print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_VrLjYDKCzlPz4wvziBWhrxsY': 'file_storage/call_VrLjYDKCzlPz4wvziBWhrxsY.json', 'var_call_uX35j8swiDeRTrhkqYrZ3t7S': 'file_storage/call_uX35j8swiDeRTrhkqYrZ3t7S.json', 'var_call_H43HOmSBNUjo7iHO18cuHoOk': 'file_storage/call_H43HOmSBNUjo7iHO18cuHoOk.json', 'var_call_7yMwBGdeJJXK2ZKHMVmTmgWn': 'file_storage/call_7yMwBGdeJJXK2ZKHMVmTmgWn.json', 'var_call_ZoxDuyfmA0ExiNj3X6GL6mWl': {'pubs': 72, 'cpcs': 137}}

exec(code, env_args)
