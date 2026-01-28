code = """import json, re, collections

pubs_path = var_call_rgCbKHskIacaX0xVvVaIOmml
level5_path = var_call_iPcq9nJIu60t6Nz07StOy22j

with open(level5_path, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# compute unique prefix lengths
lengths = sorted({len(s) for s in level5_symbols}, reverse=True)

year_regex = re.compile(r"(19|20)\d{2}")

counts = collections.Counter()
min_year = None
max_year = None

# process publications in streaming fashion to be efficient
with open(pubs_path, 'r', encoding='utf-8') as f:
    publications = json.load(f)

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
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        continue
    if not isinstance(cpc_list, list):
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        matched = None
        # check prefixes by length
        for L in lengths:
            pref = code[:L]
            if pref in level5_symbols:
                matched = pref
                break
        if matched:
            counts[(matched, year)] += 1

if min_year is None:
    result = []
else:
    alpha = 0.2
    year_range = list(range(min_year, max_year + 1))
    best_year_by_symbol = {}
    for sym in level5_symbols:
        counts_by_year = [counts.get((sym, y), 0) for y in year_range]
        if all(c == 0 for c in counts_by_year):
            continue
        ema_prev = counts_by_year[0]
        ema_values = [ema_prev]
        for c in counts_by_year[1:]:
            ema_curr = alpha * c + (1 - alpha) * ema_prev
            ema_values.append(ema_curr)
            ema_prev = ema_curr
        max_idx = max(range(len(ema_values)), key=lambda i: ema_values[i])
        best_year = year_range[max_idx]
        best_year_by_symbol[sym] = best_year
    result = sorted([sym for sym, y in best_year_by_symbol.items() if y == 2022])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GvbZb7Ivoch36cnxrXMAcMEm': ['publicationinfo'], 'var_call_MLl8y02YPuoMLc74lDEMBppc': ['cpc_definition'], 'var_call_rgCbKHskIacaX0xVvVaIOmml': 'file_storage/call_rgCbKHskIacaX0xVvVaIOmml.json', 'var_call_iPcq9nJIu60t6Nz07StOy22j': 'file_storage/call_iPcq9nJIu60t6Nz07StOy22j.json'}

exec(code, env_args)
