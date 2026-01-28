code = """import json
import re
from collections import defaultdict

# Load level-5 symbols
with open(var_call_v1OtkJfTUeC5VXQY072oZ9zT, 'r', encoding='utf-8') as f:
    level5 = json.load(f)
symbols = [r['symbol'] for r in level5 if r.get('symbol')]
# Sort symbols by length descending to help longest-prefix matching
symbols_sorted = sorted(symbols, key=lambda x: -len(x))

# Load publication records
with open(var_call_0pHvLmRFOFeI8zjaOCjRnq9R, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year] = count

year_re = re.compile(r'(19|20)\d{2}')

for row in pubs:
    cpc_field = row.get('cpc')
    filing_date = row.get('filing_date') or ''
    m = year_re.search(filing_date)
    if not m:
        continue
    year = int(m.group(0))
    if not cpc_field:
        continue
    # cpc_field is a JSON-like string
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    for item in cpc_list:
        code = (item.get('code') or '').strip()
        if not code:
            continue
        # Find longest matching level-5 symbol that is a prefix of code
        matched = None
        for s in symbols_sorted:
            if code.startswith(s):
                matched = s
                break
        if matched:
            counts[matched][year] += 1

# Compute EMA with alpha=0.2 for each symbol across its years
alpha = 0.2
result_symbols = []

for s, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    # Build list of (year, count)
    yc = [(y, year_counts[y]) for y in years]
    # Compute EMA sequentially
    ema_by_year = {}
    S = None
    for y, c in yc:
        if S is None:
            S = c
        else:
            S = alpha * c + (1 - alpha) * S
        ema_by_year[y] = S
    # Determine best year (year with max EMA)
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        result_symbols.append(s)

# Sort result for consistency
result_symbols = sorted(result_symbols)

import json as _json
print("__RESULT__:")
print(_json.dumps(result_symbols))"""

env_args = {'var_call_v1OtkJfTUeC5VXQY072oZ9zT': 'file_storage/call_v1OtkJfTUeC5VXQY072oZ9zT.json', 'var_call_0pHvLmRFOFeI8zjaOCjRnq9R': 'file_storage/call_0pHvLmRFOFeI8zjaOCjRnq9R.json'}

exec(code, env_args)
