code = """import json
import re
from collections import defaultdict, OrderedDict

# Load data from storage files
with open(var_call_1g2Nu9PWCE2MNzzzwx7KtorW, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)

with open(var_call_ZNXDanpw45vtkmCpITD5ZCPZ, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Extract level-5 symbols
level5_symbols = [row.get('symbol') for row in level5_list if row.get('symbol')]
level5_symbols_set = set(level5_symbols)

# Year extractor
year_re = re.compile(r"\b(19|20)\d{2}\b")

# Counts: symbol -> year -> count (unique patents per publication)
counts = defaultdict(lambda: defaultdict(int))

for pub in pubs:
    filing = pub.get('filing_date') or ''
    # find year
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    # parse cpc field
    cpc_field = pub.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean up common issues
        try:
            cpcs = json.loads(cpc_field.replace("\n", "").replace("\t", ""))
        except Exception:
            continue
    # determine which level5 symbols apply to this publication
    matched = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        code = code.strip()
        # try to match by prefix: if a level5 symbol is a prefix of code
        # check all level5 symbols; optimize by checking prefixes of code
        # generate possible prefixes from code by progressively truncating after letters/numbers and slash
        # But simplest: check any symbol that is prefix of code
        for sym in level5_symbols:
            if code.upper().startswith(sym.upper()):
                matched.add(sym)
    for sym in matched:
        counts[sym][year] += 1

# For each symbol, compute EMA across years
alpha = 0.2
ema_by_sym = {}

for sym, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_series = OrderedDict()
    ema_prev = None
    for y in years:
        c = year_counts[y]
        if ema_prev is None:
            ema = float(c)
        else:
            ema = alpha * c + (1 - alpha) * ema_prev
        ema_series[y] = ema
        ema_prev = ema
    ema_by_sym[sym] = ema_series

# For each symbol, find the year with highest EMA
best_year_by_sym = {}
for sym, ema_series in ema_by_sym.items():
    # find year with max ema; if multiple choose earliest year? choose the year with max value, tie -> latest year
    max_val = None
    max_year = None
    for y, v in ema_series.items():
        if (max_val is None) or (v > max_val) or (v == max_val and y > max_year):
            max_val = v
            max_year = y
    best_year_by_sym[sym] = max_year

# Select symbols at level 5 whose best year is 2022
result_syms = sorted([sym for sym, y in best_year_by_sym.items() if y == 2022])

# Print result as JSON string
import json
print("__RESULT__:")
print(json.dumps(result_syms))"""

env_args = {'var_call_1g2Nu9PWCE2MNzzzwx7KtorW': 'file_storage/call_1g2Nu9PWCE2MNzzzwx7KtorW.json', 'var_call_ZNXDanpw45vtkmCpITD5ZCPZ': 'file_storage/call_ZNXDanpw45vtkmCpITD5ZCPZ.json'}

exec(code, env_args)
