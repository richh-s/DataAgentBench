code = """import json, re, collections

# Load data from storage-provided file paths
pubs_path = var_call_rgCbKHskIacaX0xVvVaIOmml
level5_path = var_call_iPcq9nJIu60t6Nz07StOy22j

with open(pubs_path, 'r', encoding='utf-8') as f:
    publications = json.load(f)
with open(level5_path, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Prepare sorted symbols by length desc to match longest prefix first
sorted_symbols = sorted(level5_symbols, key=lambda s: len(s), reverse=True)

year_regex = re.compile(r"(19|20)\d{2}")

counts = collections.Counter()
min_year = None
max_year = None

for rec in publications:
    date_str = rec.get('filing_date') or ''
    m = year_regex.search(date_str)
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
    # try to parse cpc field as JSON
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # if parsing fails, skip
        continue
    if not isinstance(cpc_list, list):
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        matched = None
        for sym in sorted_symbols:
            if code.startswith(sym):
                matched = sym
                break
        if matched:
            counts[(matched, year)] += 1

# If no years found, return empty
if min_year is None:
    result = []
else:
    alpha = 0.2
    year_range = list(range(min_year, max_year + 1))
    best_year_by_symbol = {}
    for sym in level5_symbols:
        # build counts per year over full range
        counts_by_year = [counts.get((sym, y), 0) for y in year_range]
        if all(c == 0 for c in counts_by_year):
            continue
        # compute EMA
        ema_values = []
        ema_prev = counts_by_year[0]
        ema_values.append(ema_prev)
        for c in counts_by_year[1:]:
            ema_curr = alpha * c + (1 - alpha) * ema_prev
            ema_values.append(ema_curr)
            ema_prev = ema_curr
        # find year of max EMA (if multiple, take first occurrence)
        max_idx = max(range(len(ema_values)), key=lambda i: ema_values[i])
        best_year = year_range[max_idx]
        best_year_by_symbol[sym] = best_year

    # select symbols whose best year is 2022
    result = sorted([sym for sym, y in best_year_by_symbol.items() if y == 2022])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GvbZb7Ivoch36cnxrXMAcMEm': ['publicationinfo'], 'var_call_MLl8y02YPuoMLc74lDEMBppc': ['cpc_definition'], 'var_call_rgCbKHskIacaX0xVvVaIOmml': 'file_storage/call_rgCbKHskIacaX0xVvVaIOmml.json', 'var_call_iPcq9nJIu60t6Nz07StOy22j': 'file_storage/call_iPcq9nJIu60t6Nz07StOy22j.json'}

exec(code, env_args)
