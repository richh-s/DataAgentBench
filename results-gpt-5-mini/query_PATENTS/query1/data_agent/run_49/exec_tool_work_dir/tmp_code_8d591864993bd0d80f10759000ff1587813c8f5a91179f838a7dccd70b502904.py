code = """import json
import re
from collections import defaultdict

# Load data from storage-provided file paths
with open(var_call_3RJwBAtp6NVw1Vmx1jikSgmm, 'r') as f:
    level5_records = json.load(f)
with open(var_call_iyOqHsSbUsNSUsJcxleuLzY0, 'r') as f:
    pub_records = json.load(f)

# Extract level-5 symbols
level5_symbols = set()
for r in level5_records:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Helper to extract year from publication_date
year_re = re.compile(r'(\d{4})')

def extract_year(pub_date):
    if not pub_date:
        return None
    m = year_re.search(pub_date)
    if m:
        return int(m.group(1))
    return None

# Helper to parse cpc JSON string to list of codes
def parse_cpc_field(cpc_field):
    if not cpc_field:
        return []
    # Some entries may already be a list/dict; handle strings primarily
    if isinstance(cpc_field, list):
        arr = cpc_field
    else:
        try:
            arr = json.loads(cpc_field)
        except Exception:
            # try to fix common issues: single quotes -> double quotes
            try:
                arr = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                return []
    codes = []
    for entry in arr:
        if isinstance(entry, dict):
            code = entry.get('code')
            if code:
                codes.append(code)
        elif isinstance(entry, str):
            # if array of strings
            codes.append(entry)
    return codes

# Count occurrences per (group, year)
counts = defaultdict(lambda: defaultdict(int))
all_years = set()
for rec in pub_records:
    pub_date = rec.get('publication_date')
    year = extract_year(pub_date)
    if not year:
        continue
    all_years.add(year)
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        # extract group code as first 4 characters (e.g., C01B)
        if not isinstance(code, str) or len(code) < 3:
            continue
        group = code[:4]
        if group in level5_symbols:
            counts[group][year] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    # For each group compute EMA across years
    alpha = 0.2
    best_year_by_group = {}
    for group, year_counts in counts.items():
        # Build time series for all years (fill 0 for missing)
        ts = [year_counts.get(y, 0) for y in years]
        if not ts:
            continue
        # EMA initialization: use first value
        ema_vals = []
        ema = ts[0]
        ema_vals.append(ema)
        for x in ts[1:]:
            ema = alpha * x + (1 - alpha) * ema
            ema_vals.append(ema)
        # Find year of max EMA
        max_idx = max(range(len(years)), key=lambda i: ema_vals[i])
        best_year = years[max_idx]
        best_year_by_group[group] = best_year

    # Select groups whose best year is 2022
    result = sorted([g for g, y in best_year_by_group.items() if y == 2022])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3RJwBAtp6NVw1Vmx1jikSgmm': 'file_storage/call_3RJwBAtp6NVw1Vmx1jikSgmm.json', 'var_call_iyOqHsSbUsNSUsJcxleuLzY0': 'file_storage/call_iyOqHsSbUsNSUsJcxleuLzY0.json'}

exec(code, env_args)
