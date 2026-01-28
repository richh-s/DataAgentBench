code = """import json
from collections import defaultdict

# File paths provided by previous query_db calls
pubs_path = var_call_JuYIc5TDnDtRd8TtislB5SI8
cpc_path = var_call_iWKlRsPXFz8VehE93rIAy156

# Load files
with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level-4 map
level4 = {}
for r in cpc_defs:
    sym = r.get('symbol')
    lvl = r.get('level')
    try:
        if int(float(lvl)) == 4 and sym:
            level4[sym] = r.get('titleFull')
    except Exception:
        pass

# Helpers without regex
months_h2 = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

def contains_h2_2019(s):
    if not s:
        return False
    low = s.lower()
    if '2019' not in low:
        return False
    for m in months_h2:
        if m in low:
            return True
    return False


def find_year(s):
    if not s:
        return None
    s2 = s
    L = len(s2)
    for i in range(L-3):
        t = s2[i:i+4]
        if t.isdigit() and (t.startswith('20') or t.startswith('19')):
            return int(t)
    return None

# Filter publications: Germany detection simplified
filtered = []
for p in pubs:
    pi = p.get('Patents_info','')
    if not pi:
        continue
    if ('DE-' not in pi) and ('from DE' not in pi) and (' DE' not in pi):
        continue
    if not contains_h2_2019(p.get('grant_date','')):
        continue
    filtered.append(p)

# Aggregate counts per level-4 per filing year
counts = defaultdict(lambda: defaultdict(int))
for p in filtered:
    cpc_field = p.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    fy = find_year(p.get('filing_date') or p.get('publication_date') or '')
    if not fy:
        continue
    for e in cpcs:
        if isinstance(e, dict):
            code = e.get('code')
        else:
            code = None
        if not code or len(code) < 3:
            continue
        lvl4 = code[:3]
        if lvl4 in level4:
            counts[lvl4][fy] += 1

# Compute EMA alpha=0.1
alpha = 0.1
results = []
for sym, yc in counts.items():
    years = sorted(yc.keys())
    ema = None
    emaval = {}
    for y in years:
        v = yc[y]
        if ema is None:
            ema = v
        else:
            ema = alpha * v + (1-alpha) * ema
        emaval[y] = ema
    best = max(emaval.keys(), key=lambda yy: emaval[yy])
    results.append({
        'symbol': sym,
        'titleFull': level4.get(sym),
        'best_year': int(best),
        'peak_ema': round(float(emaval[best]), 4),
        'year_counts': {str(y): int(yc[y]) for y in years}
    })

results_sorted = sorted(results, key=lambda r: r['peak_ema'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted, ensure_ascii=False))"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json', 'var_call_HJBw0WnBcgg79MIUSqCfldCG': {'var1': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var2': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}}

exec(code, env_args)
