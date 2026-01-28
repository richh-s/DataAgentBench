code = """import json, re
from collections import defaultdict

# Load data from storage-provided file paths
with open(var_call_WMIQtQebmqIJbCsUsEDASVye, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_oEJNX49OGy0cqALWlqYSt83k, 'r', encoding='utf-8') as f:
    lvl5 = json.load(f)

level5_set = set()
for r in lvl5:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip())

# Aggregate counts per group per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    # extract year
    m = re.search(r"(19|20)\d{2}", filing)
    if not m:
        continue
    year = int(m.group(0))
    all_years.add(year)
    # parse cpc JSON list
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # if already a list or malformed, skip
        continue
    groups = set()
    for obj in cpcs:
        code = obj.get('code') if isinstance(obj, dict) else None
        if not code:
            continue
        code = code.strip()
        # extract level-5 group as first 4 chars like 'A01B' or match pattern
        m2 = re.match(r'^([A-Z]\d{2}[A-Z])', code)
        if m2:
            grp = m2.group(1)
        else:
            grp = code[:4]
        groups.add(grp)
    for g in groups:
        counts[g][year] += 1

if not all_years:
    result = []
else:
    min_year = min(all_years)
    max_year = max(all_years)
    # ensure 2022 is in range
    if 2022 > max_year:
        max_year = 2022
    alpha = 0.2
    selected = []
    for g, yc in counts.items():
        # compute EMA across global year range
        ema_prev = None
        ema_by_year = {}
        for y in range(min_year, max_year+1):
            count = yc.get(y, 0)
            if ema_prev is None:
                ema = count
            else:
                ema = alpha * count + (1 - alpha) * ema_prev
            ema_by_year[y] = ema
            ema_prev = ema
        # find year(s) with max EMA; choose the earliest of ties? choose the year with max, if multiple choose the latest
        max_ema = max(ema_by_year.values())
        best_years = [y for y, v in ema_by_year.items() if v == max_ema]
        best_year = max(best_years)
        if best_year == 2022 and g in level5_set:
            selected.append(g)
    result = sorted(selected)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WMIQtQebmqIJbCsUsEDASVye': 'file_storage/call_WMIQtQebmqIJbCsUsEDASVye.json', 'var_call_oEJNX49OGy0cqALWlqYSt83k': 'file_storage/call_oEJNX49OGy0cqALWlqYSt83k.json'}

exec(code, env_args)
