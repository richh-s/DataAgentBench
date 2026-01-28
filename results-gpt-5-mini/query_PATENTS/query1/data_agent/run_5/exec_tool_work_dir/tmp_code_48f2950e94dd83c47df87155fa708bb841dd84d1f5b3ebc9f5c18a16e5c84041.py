code = """import json, re
from collections import defaultdict

pubs_path = var_call_Qy8TLTMJbymlJg5NMi8vsBsp
lvl5_path = var_call_endGIMHBmlkYqjJhD6Jmx1EL

with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(lvl5_path, 'r', encoding='utf-8') as f:
    lvl5 = json.load(f)

level5_set = set()
for r in lvl5:
    s = r.get('symbol')
    if s:
        level5_set.add(s.strip().upper())

pattern = re.compile(r'\d{4}')

def year_of(s):
    if not s or not isinstance(s, str):
        return None
    m = pattern.search(s)
    return int(m.group(0)) if m else None

counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for pub in pubs:
    y = year_of(pub.get('filing_date'))
    if not y:
        continue
    all_years.add(y)
    cf = pub.get('cpc')
    if not cf:
        continue
    try:
        cpcs = json.loads(cf) if isinstance(cf, str) else cf
    except Exception:
        continue
    if not isinstance(cpcs, list):
        continue
    groups = set()
    for e in cpcs:
        code = e.get('code') if isinstance(e, dict) else None
        if not code or not isinstance(code, str):
            continue
        c = code.strip().upper().replace(' ', '')
        if len(c) < 4:
            continue
        g = re.sub('[^A-Z0-9]', '', c[:4])
        if g in level5_set:
            groups.add(g)
    for g in groups:
        counts[g][y] += 1

# compute EMA and pick those whose best year is 2022
res = []
if all_years:
    years = list(range(min(all_years), max(all_years)+1))
    alpha = 0.2
    for g, yc in counts.items():
        series = [yc.get(yr, 0) for yr in years]
        ema = series[0] if series else 0
        emas = [ema]
        for v in series[1:]:
            ema = alpha * v + (1-alpha) * ema
            emas.append(ema)
        idx = max(range(len(emas)), key=lambda i: (emas[i], years[i]))
        if years[idx] == 2022:
            res.append(g)

res.sort()
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Qy8TLTMJbymlJg5NMi8vsBsp': 'file_storage/call_Qy8TLTMJbymlJg5NMi8vsBsp.json', 'var_call_endGIMHBmlkYqjJhD6Jmx1EL': 'file_storage/call_endGIMHBmlkYqjJhD6Jmx1EL.json'}

exec(code, env_args)
