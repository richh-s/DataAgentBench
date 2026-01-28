code = """import json, re
from collections import defaultdict, Counter

# Load data from storage files
with open(var_call_5bcSGW9ZN5FTHqcNmjF8ZAqO, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_25dn6za87cohOevYDOr9HHhc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

level5_set = set()
for item in cpc_defs:
    sym = item.get('symbol')
    if sym:
        level5_set.add(sym.strip())

# Extract year and cpc codes
year_re = re.compile(r'(19|20)\d{2}')
counts = defaultdict(Counter)  # level5 -> Counter(year->count)
min_year = None
max_year = None

for rec in pubs:
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    if min_year is None or year < min_year:
        min_year = year
    if max_year is None or year > max_year:
        max_year = year
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\'", '"'))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or len(code) < 4:
            continue
        level5 = code[:4]
        if level5 in level5_set:
            counts[level5][year] += 1

if min_year is None:
    # no valid data
    result = []
else:
    # compute EMA per level5 across the global year range
    years = list(range(min_year, max_year+1))
    alpha = 0.2
    ema_by_code = {}
    for code, counter in counts.items():
        ema_values = {}
        prev_ema = None
        for y in years:
            x = counter.get(y, 0)
            if prev_ema is None:
                ema = float(x)
            else:
                ema = alpha * x + (1 - alpha) * prev_ema
            ema_values[y] = ema
            prev_ema = ema
        ema_by_code[code] = ema_values

    # find codes whose best year (year with max EMA) is 2022
    selected = []
    for code, emamap in ema_by_code.items():
        # get year(s) with max EMA
        best_year = max(emamap.items(), key=lambda kv: (kv[1], -kv[0]))[0]
        if best_year == 2022:
            selected.append(code)
    result = sorted(selected)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l5K0VFdbdCmXRO8Pwm4CmNKA': ['publicationinfo'], 'var_call_CMyNyAYKUazmwjhYgfXZAhZs': ['cpc_definition'], 'var_call_5bcSGW9ZN5FTHqcNmjF8ZAqO': 'file_storage/call_5bcSGW9ZN5FTHqcNmjF8ZAqO.json', 'var_call_25dn6za87cohOevYDOr9HHhc': 'file_storage/call_25dn6za87cohOevYDOr9HHhc.json'}

exec(code, env_args)
