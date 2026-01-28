code = """import json, re
import pandas as pd

# Load data from storage-provided variables
# var_call_fVdicR9IUrrzkzNwEB1rIAPr and var_call_gP1ejUL1tRWQ2G6k94uQDIKD are expected to be file paths (strings) to JSON files

pub_path = var_call_fVdicR9IUrrzkzNwEB1rIAPr
cpc_level5_path = var_call_gP1ejUL1tRWQ2G6k94uQDIKD

# Helper to load possibly-large JSON result
def load_json_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return x

pub_records = load_json_maybe_path(pub_path)
cpc_level5_records = load_json_maybe_path(cpc_level5_path)

# Extract level-5 symbols
level5_symbols = set()
for r in cpc_level5_records:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip().upper())

# Build counts per (group, year)
counts = {}  # {group: {year: count}}

year_regex = re.compile(r'(20\d{2}|19\d{2})')

for rec in pub_records:
    filing = rec.get('filing_date')
    if not filing or not isinstance(filing, str):
        continue
    m = year_regex.search(filing)
    if not m:
        continue
    year = int(m.group(0))

    cpc_field = rec.get('cpc')
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    # cpc_field is a JSON-like string representing a list of dicts
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues: replace single quotes with double quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    # collect unique groups for this publication
    groups = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper()
        if len(code) < 4:
            continue
        group = code[:4]
        if group in level5_symbols:
            groups.add(group)
    # increment counts
    for g in groups:
        counts.setdefault(g, {}).setdefault(year, 0)
        counts[g][year] += 1

# For each group, compute yearly EMA with alpha=0.2
alpha = 0.2
result_groups = []

for g, year_counts in counts.items():
    # Prepare time series from min to max year
    years = sorted(year_counts.keys())
    if not years:
        continue
    # Build series dict mapping year->value (0 if missing)
    start, end = years[0], years[-1]
    series_years = list(range(start, end+1))
    values = [year_counts.get(y, 0) for y in series_years]
    # compute EMA
    ema_values = {}
    ema_prev = None
    for y, v in zip(series_years, values):
        if ema_prev is None:
            ema = v
        else:
            ema = alpha * v + (1 - alpha) * ema_prev
        ema_values[y] = ema
        ema_prev = ema
    # find year with max EMA
    # If multiple years tie, choose the latest year among them
    max_ema = max(ema_values.values())
    best_years = [y for y, e in ema_values.items() if e == max_ema]
    best_year = max(best_years)
    if best_year == 2022:
        result_groups.append(g)

# Sort result
result_groups = sorted(result_groups)

import json
print("__RESULT__:")
print(json.dumps(result_groups))"""

env_args = {'var_call_fVdicR9IUrrzkzNwEB1rIAPr': 'file_storage/call_fVdicR9IUrrzkzNwEB1rIAPr.json', 'var_call_gP1ejUL1tRWQ2G6k94uQDIKD': 'file_storage/call_gP1ejUL1tRWQ2G6k94uQDIKD.json'}

exec(code, env_args)
