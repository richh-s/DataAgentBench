code = """import json, re

# Load data from the previous query results (file paths are stored in variables)
with open(var_call_KK1SeAJD0N0UxZDsC54zncBT, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)
with open(var_call_UQxymh5GMYrbQ5W27fxOhYDG, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Extract set of level-5 symbols
level5_symbols = set()
for rec in level5_list:
    sym = rec.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract year
year_re = re.compile(r'(\d{4})')
# Helper to extract level-5 prefix from a CPC code: pattern Letter + 2 digits + Letter
pref_re = re.compile(r'^([A-Z]\d{2}[A-Z])')

# Count occurrences per (group, year)
counts = {}
all_years = set()
for rec in pubs:
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(1))
    all_years.add(year)
    cpc_field = rec.get('cpc') or ''
    # parse cpc field which is JSON-like string
    try:
        codes = json.loads(cpc_field)
    except Exception:
        # skip if can't parse
        continue
    # For each code object, extract code string
    for cobj in codes:
        code = cobj.get('code') if isinstance(cobj, dict) else None
        if not code or not isinstance(code, str):
            continue
        pm = pref_re.match(code)
        if not pm:
            continue
        grp = pm.group(1)
        counts.setdefault(grp, {}).setdefault(year, 0)
        counts[grp][year] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    alpha = 0.2
    # Compute EMA per group per year
    ema_by_group = {}
    best_year_by_group = {}
    for grp, year_counts in counts.items():
        # Build time series of counts aligned to years
        series = [year_counts.get(y, 0) for y in years]
        ema_series = []
        ema = None
        for val in series:
            if ema is None:
                ema = val
            else:
                ema = alpha * val + (1 - alpha) * ema
            ema_series.append(ema)
        # find max ema and corresponding year (if multiple, pick latest year)
        max_ema = None
        max_year = None
        for y, e in zip(years, ema_series):
            if (max_ema is None) or (e > max_ema) or (e == max_ema and y > max_year):
                max_ema = e
                max_year = y
        ema_by_group[grp] = dict(zip([str(y) for y in years], ema_series))
        best_year_by_group[grp] = max_year

    # Filter groups to level-5 symbols and whose best year is 2022
    result = sorted([grp for grp, by in best_year_by_group.items() if by == 2022 and grp in level5_symbols])

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KK1SeAJD0N0UxZDsC54zncBT': 'file_storage/call_KK1SeAJD0N0UxZDsC54zncBT.json', 'var_call_UQxymh5GMYrbQ5W27fxOhYDG': 'file_storage/call_UQxymh5GMYrbQ5W27fxOhYDG.json'}

exec(code, env_args)
