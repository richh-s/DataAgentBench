code = """import json, re
from collections import defaultdict, OrderedDict

# Load data from storage files
pubs_path = var_call_2b7MtYbe89sLgoFYZ9fEa4RH
level5_path = var_call_nsECyHgv5Hw9S2y4pgl3P5Un

with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

with open(level5_path, 'r', encoding='utf-8') as f:
    level5 = json.load(f)

# Build set of level-5 symbols
level5_set = set()
for r in level5:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip())

# Helper to extract year
year_re = re.compile(r"(19|20)\d{2}")
# Helper to extract group code (CPC group symbol like A01B, C01B, H01M)
group_re = re.compile(r'^[A-Z][0-9]{2}[A-Z]')

# counts[group][year] = count
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    fd = rec.get('filing_date')
    if not fd or not isinstance(fd, str):
        continue
    m = year_re.search(fd)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    # cpc_field is a JSON-like string; try to load
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    seen_groups = set()
    for entry in cpcs:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper()
        gm = group_re.match(code)
        if not gm:
            continue
        group = gm.group(0)
        # Only consider level-5 groups present in cpc_definition
        if group not in level5_set:
            continue
        # To avoid counting duplicates within same publication for same group-year,
        # count each group once per publication
        if group in seen_groups:
            continue
        seen_groups.add(group)
        counts[group][year] += 1

# For each group compute EMA over years (sorted ascending). alpha = 0.2
alpha = 0.2
best_years = {}
for group, year_counts in counts.items():
    # sort years
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
    # find year with max ema; if tie pick latest year
    max_ema = None
    max_year = None
    for y, e in ema_by_year.items():
        if (max_ema is None) or (e > max_ema) or (e == max_ema and y > max_year):
            max_ema = e
            max_year = y
    if max_year is not None:
        best_years[group] = max_year

# Select groups whose best year == 2022
result = sorted([g for g, y in best_years.items() if y == 2022])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2b7MtYbe89sLgoFYZ9fEa4RH': 'file_storage/call_2b7MtYbe89sLgoFYZ9fEa4RH.json', 'var_call_nsECyHgv5Hw9S2y4pgl3P5Un': 'file_storage/call_nsECyHgv5Hw9S2y4pgl3P5Un.json'}

exec(code, env_args)
