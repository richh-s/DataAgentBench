code = """import json
from collections import defaultdict

# Load files
with open('file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json','r',encoding='utf-8') as f:
    pubs = json.load(f)
with open('file_storage/call_iWKlRsPXFz8VehE93rIAy156.json','r',encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Level-4 map
level4 = {}
for r in cpc_defs:
    sym = r.get('symbol')
    lvl = r.get('level')
    try:
        if int(float(lvl))==4 and sym:
            level4[sym]=r.get('titleFull')
    except Exception:
        pass

# Helper: is Germany
def is_germany(s):
    if not s:
        return False
    s2 = s
    if 'DE-' in s2 or 'from DE' in s2 or '\bDE\b' in s2:
        return True
    # simple token check
    toks = s2.replace(',',' ').replace('.',' ').split()
    if 'DE' in toks:
        return True
    return False

# months in H2
months_h2 = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

# find year in string by searching range
def find_year(s):
    if not s:
        return None
    for y in range(1970, 2030):
        if str(y) in s:
            return y
    return None

# filter publications
filtered = []
for p in pubs:
    pi = p.get('Patents_info','')
    if not is_germany(pi):
        continue
    gd = (p.get('grant_date') or '').lower()
    if '2019' not in gd:
        continue
    if not any(m in gd for m in months_h2):
        continue
    filtered.append(p)

# aggregate counts per level4 symbol per filing year
counts = defaultdict(lambda: defaultdict(int))
for p in filtered:
    cpc_field = p.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'","\""))
        except Exception:
            continue
    filing = p.get('filing_date') or p.get('publication_date') or ''
    fy = find_year(filing)
    if not fy:
        continue
    for e in cpcs:
        code = e.get('code') if isinstance(e, dict) else None
        if not code or len(code)<3:
            continue
        lvl4 = code[:3]
        if lvl4 in level4:
            counts[lvl4][fy] += 1

# compute EMA alpha=0.1
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
            ema = alpha*v + (1-alpha)*ema
        emaval[y]=ema
    best = max(emaval.keys(), key=lambda yy: emaval[yy])
    results.append({'symbol':sym,'titleFull':level4.get(sym),'best_year':int(best),'peak_ema':round(float(emaval[best]),4),'year_counts':{str(y):int(yc[y]) for y in years}})

results_sorted = sorted(results, key=lambda r: r['peak_ema'], reverse=True)
print('__RESULT__:')
print(json.dumps(results_sorted, ensure_ascii=False))"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json', 'var_call_HJBw0WnBcgg79MIUSqCfldCG': {'var1': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var2': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}}

exec(code, env_args)
