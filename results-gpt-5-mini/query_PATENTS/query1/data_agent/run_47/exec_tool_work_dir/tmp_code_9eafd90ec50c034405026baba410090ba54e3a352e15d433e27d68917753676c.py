code = """import json, re
from collections import defaultdict

# Load the query results from storage files
with open(var_call_wqwdFhTOsn4QYnZQgvj5tFoP, 'r') as f:
    level5_records = json.load(f)
with open(var_call_9IV1pcLw7WWEdP169MSVwRmm, 'r') as f:
    pub_records = json.load(f)

# Build set of level-5 CPC symbols
level5_symbols = set()
for r in level5_records:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract year from filing_date string
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Count occurrences per group per year
counts = defaultdict(lambda: defaultdict(int))
for rec in pub_records:
    cpc_field = rec.get('cpc')
    filing_date = rec.get('filing_date')
    year = extract_year(filing_date)
    if year is None:
        continue
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # sometimes already a list
        try:
            cpc_list = cpc_field
        except Exception:
            continue
    # cpc_list should be a list of dicts
    if not isinstance(cpc_list, list):
        continue
    seen_groups = set()
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or not isinstance(code, str):
            continue
        # Extract first four characters that form group symbol: letters+digits+letter
        # e.g., 'C01B33/00' -> 'C01B', 'H01M10/0565' -> 'H01M'
        # We'll extract leading pattern: one letter, two digits, one letter (like C01B)
        m = re.match(r'([A-Z]\d{2}[A-Z])', code)
        if m:
            group = m.group(1)
        else:
            # fallback: take first 4 chars upper
            group = code[:4].upper()
        if group in level5_symbols and (group, year) not in seen_groups:
            counts[group][year] += 1
            seen_groups.add((group, year))

# Get global set of years
all_years = set()
for g in counts:
    all_years.update(counts[g].keys())
if not all_years:
    result = []
else:
    years_sorted = sorted(all_years)
    alpha = 0.2
    # Compute EMA per group per year
    ema = defaultdict(dict)
    for g in counts:
        # For years missing, treat count as 0
        # iterate through years_sorted chronologically
        prev = None
        for y in years_sorted:
            cnt = counts[g].get(y, 0)
            if prev is None:
                val = float(cnt)
            else:
                val = alpha * cnt + (1 - alpha) * prev
            ema[g][y] = val
            prev = val

    # For each group, find the year(s) where EMA is maximum
    groups_with_best2022 = []
    for g in ema:
        year_vals = ema[g]
        # find max value
        max_val = max(year_vals.values()) if year_vals else None
        if max_val is None:
            continue
        # find years with this max
        best_years = [y for y, v in year_vals.items() if abs(v - max_val) < 1e-12]
        if 2022 in best_years:
            groups_with_best2022.append(g)

    result = sorted(groups_with_best2022)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wqwdFhTOsn4QYnZQgvj5tFoP': 'file_storage/call_wqwdFhTOsn4QYnZQgvj5tFoP.json', 'var_call_9IV1pcLw7WWEdP169MSVwRmm': 'file_storage/call_9IV1pcLw7WWEdP169MSVwRmm.json'}

exec(code, env_args)
