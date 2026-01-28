code = """import json
import re
from collections import defaultdict

# Load query results from storage variables provided by previous tool calls
# var_call_K2cwh4mwDPx9oRXyXMpa5PFL and var_call_qhP6ZF1fuxXclDI4I2MzdJam are file paths
with open(var_call_K2cwh4mwDPx9oRXyXMpa5PFL, 'r') as f:
    pub_records = json.load(f)
with open(var_call_qhP6ZF1fuxXclDI4I2MzdJam, 'r') as f:
    cpc_def_records = json.load(f)

# Build set of valid level-5 symbols from cpc_definition query
valid_level5 = set()
for r in cpc_def_records:
    sym = r.get('symbol')
    if sym:
        valid_level5.add(sym)

# Count unique (per publication) occurrences of level-5 groups per year
counts = defaultdict(int)  # key (group, year) -> count
all_years = set()
for rec in pub_records:
    filing = rec.get('filing_date') or ''
    m = re.search(r'(19|20)\d{2}', filing)
    if not m:
        # try in publication_date or other fields? skip if no year
        continue
    year = int(m.group(0))
    all_years.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field is a JSON-like string; parse
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    groups = set()
    for item in cpcs:
        code = item.get('code','')
        # extract level-5 group as first 4-char pattern like A01B, H01M, etc.
        m2 = re.match(r'^([A-Z]\d{2}[A-Z])', code)
        if m2:
            groups.add(m2.group(1))
    for g in groups:
        counts[(g, year)] += 1

# For each group, compute EMA across the years (sorted ascending for that group)
alpha = 0.2
best_year_by_group = {}
ema_by_group_year = {}

for g in list({k[0] for k in counts.keys()}):
    # skip groups not in valid level-5 definitions
    if g not in valid_level5:
        continue
    # get years where this group could have data: use sorted list of all_years to ensure continuity
    years = sorted(all_years)
    ema = None
    best_year = None
    best_ema = None
    for y in years:
        val = counts.get((g, y), 0)
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        ema_by_group_year[(g, y)] = ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = y
    if best_year is not None:
        best_year_by_group[g] = best_year

# Select groups whose best year is 2022
result = sorted([g for g, y in best_year_by_group.items() if y == 2022])

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_K2cwh4mwDPx9oRXyXMpa5PFL': 'file_storage/call_K2cwh4mwDPx9oRXyXMpa5PFL.json', 'var_call_qhP6ZF1fuxXclDI4I2MzdJam': 'file_storage/call_qhP6ZF1fuxXclDI4I2MzdJam.json'}

exec(code, env_args)
