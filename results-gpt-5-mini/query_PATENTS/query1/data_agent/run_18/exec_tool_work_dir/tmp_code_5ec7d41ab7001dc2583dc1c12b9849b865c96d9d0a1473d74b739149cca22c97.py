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

# Year extractor
year_re = re.compile(r"\b(19|20)\d{2}\b")

# Counts: symbol -> year -> count
counts = defaultdict(lambda: defaultdict(int))

for pub in pubs:
    filing = pub.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = pub.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace(chr(10), '').replace(chr(9), ''))
        except Exception:
            continue
    matched = set()
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code:
            continue
        code = code.strip()
        for sym in level5_symbols:
            if code.upper().startswith(sym.upper()):
                matched.add(sym)
    for sym in matched:
        counts[sym][year] += 1

# Compute EMA
alpha = 0.2
ema_by_sym = {}
for sym, year_counts in counts.items():
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

# Best year by symbol
best_year_by_sym = {}
for sym, ema_series in ema_by_sym.items():
    max_val = None
    max_year = None
    for y, v in ema_series.items():
        if (max_val is None) or (v > max_val) or (v == max_val and (max_year is None or y > max_year)):
            max_val = v
            max_year = y
    best_year_by_sym[sym] = max_year

# Select symbols whose best year is 2022
result_syms = sorted([sym for sym, y in best_year_by_sym.items() if y == 2022])

print("__RESULT__:")
print(json.dumps(result_syms))"""

env_args = {'var_call_1g2Nu9PWCE2MNzzzwx7KtorW': 'file_storage/call_1g2Nu9PWCE2MNzzzwx7KtorW.json', 'var_call_ZNXDanpw45vtkmCpITD5ZCPZ': 'file_storage/call_ZNXDanpw45vtkmCpITD5ZCPZ.json'}

exec(code, env_args)
