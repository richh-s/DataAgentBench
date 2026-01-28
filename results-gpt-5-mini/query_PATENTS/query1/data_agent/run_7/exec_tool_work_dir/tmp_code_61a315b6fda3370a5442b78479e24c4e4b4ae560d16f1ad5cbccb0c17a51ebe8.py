code = """import json
import re
from collections import defaultdict

# Load data from previous tool results
with open(var_call_55tgGOstL09wi5mWwp3sc5Lr, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_a5WG0LvzGSxch0A3uljqMPK5, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build set of level-5 CPC symbols
level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Regex to extract year and group
year_re = re.compile(r'(19|20)\d{2}')
group_re = re.compile(r'^[A-Z]\d{2}[A-Z]')

counts = defaultdict(int)
all_years_set = set()

for pub in pubs:
    cpc_text = pub.get('cpc')
    filing = pub.get('filing_date')
    if not cpc_text or not filing:
        continue
    # extract year
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    all_years_set.add(year)
    # parse cpc JSON
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        # try to sanitize common issues
        try:
            # replace single quotes with double
            cpc_list = json.loads(cpc_text.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        code = code.strip()
        gm = group_re.match(code)
        if not gm:
            continue
        group = gm.group(0)
        if group in level5_symbols:
            counts[(group, year)] += 1

# Compute EMA per group per year
alpha = 0.2
# Determine global year range
if not all_years_set:
    result = []
else:
    years = sorted(all_years_set)
    ema_by_group_year = {}
    groups = sorted({g for (g,y) in counts.keys()})
    # include groups even if some years missing
    for g in groups:
        ema = None
        for y in years:
            cnt = counts.get((g,y), 0)
            if ema is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1-alpha) * ema
            ema_by_group_year[(g,y)] = ema
    # For each group, find best year (max EMA). Tie-breaker: latest year
    best_year_by_group = {}
    for g in groups:
        best_y = None
        best_ema = None
        for y in years:
            val = ema_by_group_year.get((g,y), 0)
            if best_ema is None or val > best_ema or (val == best_ema and y > best_y):
                best_ema = val
                best_y = y
        best_year_by_group[g] = (best_y, best_ema)
    # Select groups whose best year is 2022
    result = sorted([g for g,(y,e) in best_year_by_group.items() if y == 2022])

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_55tgGOstL09wi5mWwp3sc5Lr': 'file_storage/call_55tgGOstL09wi5mWwp3sc5Lr.json', 'var_call_a5WG0LvzGSxch0A3uljqMPK5': 'file_storage/call_a5WG0LvzGSxch0A3uljqMPK5.json'}

exec(code, env_args)
