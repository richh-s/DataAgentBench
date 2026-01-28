code = """import json
import re
from collections import defaultdict

# Load data from previous tool results
# var_call_gu3AUm2swDvdT5J346b0c3Sm and var_call_9kgKnxIPQPNIX0leZtwNWv9l

# Determine if these are file paths or direct lists
pub_path = var_call_gu3AUm2swDvdT5J346b0c3Sm
cpcdef_path = var_call_9kgKnxIPQPNIX0leZtwNWv9l

with open(pub_path, 'r', encoding='utf-8') as f:
    publications = json.load(f)

with open(cpcdef_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level-5 symbol set
level5_symbols = set()
for row in cpc_defs:
    sym = row.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Collect counts per symbol per year
counts = defaultdict(int)
all_years = set()

for rec in publications:
    fdate = rec.get('filing_date')
    cpc_field = rec.get('cpc')
    if not fdate or not cpc_field:
        continue
    # extract year as last 4-digit group
    years_found = re.findall(r"(\d{4})", fdate)
    if not years_found:
        continue
    year = int(years_found[-1])
    all_years.add(year)
    # parse cpc field which should be a JSON string
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues: single quotes to double
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or len(code) < 3:
            continue
        # derive group code as first 4 characters (or full code if shorter)
        group = code[:4]
        if group in level5_symbols:
            counts[(group, year)] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    # For each symbol, build series over full year range, filling zeros
    symbol_years = defaultdict(list)
    symbols = sorted({k[0] for k in counts.keys()})
    for sym in symbols:
        for y in years:
            symbol_years[sym].append(counts.get((sym, y), 0))

    alpha = 0.2
    best_year_by_sym = {}
    for sym, series in symbol_years.items():
        # compute EMA with first observation as initial
        ema_values = []
        if not series:
            continue
        ema = series[0]
        ema_values.append(ema)
        for val in series[1:]:
            ema = alpha * val + (1 - alpha) * ema
            ema_values.append(ema)
        # find index of max ema
        max_idx = max(range(len(ema_values)), key=lambda i: ema_values[i])
        best_year = years[max_idx]
        best_year_by_sym[sym] = best_year

    # select symbols whose best_year is 2022
    result = sorted([sym for sym, y in best_year_by_sym.items() if y == 2022])

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sHEDsGNVHUpmwqoMumzOoz3H': ['publicationinfo'], 'var_call_nfcKt9ztC8W8fJW9s0wQe4IV': ['cpc_definition'], 'var_call_gu3AUm2swDvdT5J346b0c3Sm': 'file_storage/call_gu3AUm2swDvdT5J346b0c3Sm.json', 'var_call_9kgKnxIPQPNIX0leZtwNWv9l': 'file_storage/call_9kgKnxIPQPNIX0leZtwNWv9l.json'}

exec(code, env_args)
