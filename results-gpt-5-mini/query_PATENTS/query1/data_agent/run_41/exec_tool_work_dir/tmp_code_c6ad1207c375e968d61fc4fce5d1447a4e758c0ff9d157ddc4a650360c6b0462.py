code = """import json
import re
from collections import defaultdict

# Load data from previous query results
with open(var_call_1f1Xy2715iU2Zra0nIdBBnFE, 'r') as f:
    pubs = json.load(f)
with open(var_call_PJRsyvTwtZTfhi6rypiMAQC0, 'r') as f:
    level5_rows = json.load(f)

level5_symbols = set(r['symbol'] for r in level5_rows if r.get('symbol'))

# Helper to extract year from filing_date string
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Build counts per group per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing_date = rec.get('filing_date')
    year = extract_year(filing_date)
    if year is None:
        continue
    all_years.add(year)
    # Parse cpc field which is a JSON string
    try:
        parsed = json.loads(cpc_field)
    except Exception:
        # try to fix common issues: replace single quotes with double
        try:
            parsed = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    groups_in_pub = set()
    if isinstance(parsed, list):
        for entry in parsed:
            code = entry.get('code') if isinstance(entry, dict) else None
            if not code or not isinstance(code, str):
                continue
            group = code[:4]
            if group in level5_symbols:
                groups_in_pub.add(group)
    # increment count once per group per publication
    for g in groups_in_pub:
        counts[g][year] += 1

if not counts:
    result = []
else:
    years_sorted = sorted(all_years)
    # For consistent EMA, ensure we consider continuous range of years
    if years_sorted:
        min_y, max_y = years_sorted[0], years_sorted[-1]
        years_range = list(range(min_y, max_y+1))
    else:
        years_range = []

    alpha = 0.2
    ema_by_group = {}
    # compute EMA for each group across years_range
    for g, yc in counts.items():
        ema_map = {}
        prev_ema = None
        for y in years_range:
            x = yc.get(y, 0)
            if prev_ema is None:
                ema = x
            else:
                ema = alpha * x + (1 - alpha) * prev_ema
            ema_map[y] = ema
            prev_ema = ema
        ema_by_group[g] = ema_map

    # Determine best year for each group (year with max EMA)
    best_year_by_group = {}
    max_ema_by_group = {}
    for g, emamap in ema_by_group.items():
        # find year(s) with max ema
        best_year = max(emamap.items(), key=lambda kv: (kv[1], kv[0]))[0]
        best_year_by_group[g] = best_year
        max_ema_by_group[g] = emamap[best_year]

    # Additionally, identify groups that were 'highest EMA each year'
    # For each year, find group(s) with max EMA
    top_by_year = defaultdict(list)
    for y in years_range:
        max_ema = None
        for g, emamap in ema_by_group.items():
            val = emamap.get(y, 0)
            if max_ema is None or val > max_ema:
                max_ema = val
                top_by_year[y] = [g]
            elif val == max_ema:
                top_by_year[y].append(g)

    # Now return only the CPC group codes at level 5 whose best year is 2022
    result = [g for g, byear in best_year_by_group.items() if byear == 2022]
    result.sort()

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1f1Xy2715iU2Zra0nIdBBnFE': 'file_storage/call_1f1Xy2715iU2Zra0nIdBBnFE.json', 'var_call_PJRsyvTwtZTfhi6rypiMAQC0': 'file_storage/call_PJRsyvTwtZTfhi6rypiMAQC0.json'}

exec(code, env_args)
