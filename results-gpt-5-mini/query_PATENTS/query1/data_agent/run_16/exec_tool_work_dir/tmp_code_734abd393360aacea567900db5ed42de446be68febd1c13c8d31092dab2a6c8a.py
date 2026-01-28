code = """import json
import re
from collections import defaultdict

# Load data from storage variables (file paths)
with open(var_call_4t7KTNuga3Vfvzgd7Fm4QSK1, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_napwtOc69FA4u2i6fRCAHGB7, 'r', encoding='utf-8') as f:
    defs = json.load(f)

# Build set of level-5 symbols from defs
level5_symbols = set()
for d in defs:
    sym = d.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract codes from cpc field
code_re = re.compile(r'"code"\s*:\s*"([^"]+)"')

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    # Try to parse as JSON
    try:
        obj = json.loads(cpc_str)
        codes = []
        if isinstance(obj, list):
            for entry in obj:
                if isinstance(entry, dict) and 'code' in entry and entry['code']:
                    codes.append(entry['code'].strip())
        return codes
    except Exception:
        # Fallback regex
        return code_re.findall(cpc_str)

# Helper to get year from filing_date
def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(\d{4})', date_str)
    if m:
        return int(m.group(1))
    return None

# Count unique publication contributions per (group, year)
counts = defaultdict(lambda: defaultdict(int))  # counts[group][year] = count
all_years = set()
for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    all_years.add(year)
    codes = extract_codes(cpc_field)
    groups = set()
    for code in codes:
        # extract level-5 group: pattern Letter + 2 digits + Letter (e.g., H01M)
        m = re.match(r'^([A-Z]\d{2}[A-Z])', code)
        if m:
            grp = m.group(1)
        else:
            grp = code[:4]
        groups.add(grp)
    for grp in groups:
        counts[grp][year] += 1

if not counts:
    result = []
else:
    years_sorted = sorted(all_years)
    alpha = 0.2
    best_year_per_group = {}
    for grp, year_counts in counts.items():
        # Only consider groups that exist in level5_symbols
        if grp not in level5_symbols:
            continue
        # Build series of counts for all years (fill 0 for missing)
        series = [year_counts.get(y, 0) for y in years_sorted]
        # Compute EMA
        ema_vals = []
        if series:
            ema = series[0]
            ema_vals.append(ema)
            for val in series[1:]:
                ema = alpha * val + (1 - alpha) * ema
                ema_vals.append(ema)
        # Determine year with max EMA (choose earliest year of max if multiple)
        if ema_vals:
            max_idx = max(range(len(ema_vals)), key=lambda i: (ema_vals[i], -years_sorted[i]))
            # Note: tie-breaker prefers later year? The key uses -years_sorted to prefer larger year when EMA equal
            best_year = years_sorted[max_idx]
            best_year_per_group[grp] = best_year

    # Filter groups whose best year is 2022
    result = sorted([grp for grp, yr in best_year_per_group.items() if yr == 2022])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4t7KTNuga3Vfvzgd7Fm4QSK1': 'file_storage/call_4t7KTNuga3Vfvzgd7Fm4QSK1.json', 'var_call_napwtOc69FA4u2i6fRCAHGB7': 'file_storage/call_napwtOc69FA4u2i6fRCAHGB7.json'}

exec(code, env_args)
