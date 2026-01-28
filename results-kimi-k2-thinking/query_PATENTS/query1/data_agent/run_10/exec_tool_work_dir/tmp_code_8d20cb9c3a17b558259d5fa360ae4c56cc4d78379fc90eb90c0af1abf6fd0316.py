code = """import json
import re
import os
from collections import defaultdict

# Retrieve file paths from storage
level5_file = locals()['var_functions.query_db:5']
pub_file = locals()['var_functions.query_db:6']

# Load level 5 CPC symbols (list of dicts with 'symbol')
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

level5_symbols = [row['symbol'] for row in level5_data]

# For faster matching, group symbols by length descending (to prioritize longer matches)
# But all level5 symbols appear to be length 4 (like A01H). We'll still sort descending.
level5_symbols_sorted = sorted(level5_symbols, key=lambda x: -len(x))

# Precompute a set for quick membership? Not directly; we'll match by prefix.
# We'll create a dictionary keyed by first two chars for quick filtering.
from collections import defaultdict
prefix_map = defaultdict(list)
for sym in level5_symbols_sorted:
    if len(sym) >= 2:
        prefix_map[sym[:2]].append(sym)
    else:
        prefix_map[sym[:1]].append(sym)

# Load publication data; it's a list of records (could be large)
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

# Regex to extract year from publication_date
year_regex = re.compile(r'(\d{4})$')

# Count patents per (group, year)
counts = defaultdict(int)

for row in pub_data:
    date_str = row.get('publication_date', '')
    m = year_regex.search(date_str)
    if not m:
        continue
    year = int(m.group(1))
    # Parse CPC codes
    cpc_str = row.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        continue
    # For each CPC code, find level5 group
    for item in cpc_list:
        code = item.get('code')
        if not code:
            continue
        # Use prefix map to limit candidate groups
        prefix_key = code[:2] if len(code) >= 2 else code[:1]
        candidates = prefix_map.get(prefix_key, [])
        matched = None
        for sym in candidates:
            if code.startswith(sym):
                matched = sym
                break
        if matched:
            counts[(matched, year)] += 1

# Determine years present
years = sorted(set(year for _, year in counts.keys()))

# For each group, compute EMA across years
alpha = 0.2

groups = set(g for g, _ in counts.keys())
# Prepare result: group -> best year and best EMA value
best_year_per_group = {}
for g in groups:
    # Build series of counts per year (0 if missing)
    series = [counts.get((g, y), 0) for y in years]
    # compute EMA
    ema = None
    best_ema = None
    best_y = None
    for idx, val in enumerate(series):
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        # track best
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_y = years[idx]
    best_year_per_group[g] = (best_y, best_ema)

# Filter groups whose best year is 2022
selected_groups = [g for g, (y, _) in best_year_per_group.items() if y == 2022]

# Output selected groups as a JSON list
print('__RESULT__:')
print(json.dumps(selected_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
