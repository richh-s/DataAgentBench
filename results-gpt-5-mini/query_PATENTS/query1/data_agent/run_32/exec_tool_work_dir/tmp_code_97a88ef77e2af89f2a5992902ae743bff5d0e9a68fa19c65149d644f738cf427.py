code = """import json
import re
from collections import defaultdict

# To avoid timeout, process in streaming fashion
with open(var_call_v1OtkJfTUeC5VXQY072oZ9zT, 'r', encoding='utf-8') as f:
    level5 = json.load(f)
symbols = [r['symbol'] for r in level5 if r.get('symbol')]
symbols_sorted = sorted(symbols, key=lambda x: -len(x))

# Prepare counts
counts = defaultdict(lambda: defaultdict(int))

year_re = re.compile(r'(19|20)\d{2}')

# Stream-read publications to avoid building large list
import io
with open(var_call_0pHvLmRFOFeI8zjaOCjRnq9R, 'r', encoding='utf-8') as f:
    data = json.load(f)

for row in data:
    cpc_field = row.get('cpc')
    filing_date = row.get('filing_date') or ''
    m = year_re.search(filing_date)
    if not m:
        continue
    year = int(m.group(0))
    if not cpc_field:
        continue
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        continue
    for item in cpc_list:
        code = (item.get('code') or '').strip()
        if not code:
            continue
        for s in symbols_sorted:
            if code.startswith(s):
                counts[s][year] += 1
                break

# Compute EMA
alpha = 0.2
result_symbols = []
for s, ycounts in counts.items():
    years = sorted(ycounts.keys())
    if not years:
        continue
    S = None
    ema_by_year = {}
    for y in years:
        c = ycounts[y]
        if S is None:
            S = c
        else:
            S = alpha * c + (1 - alpha) * S
        ema_by_year[y] = S
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        result_symbols.append(s)

result_symbols = sorted(result_symbols)
print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_call_v1OtkJfTUeC5VXQY072oZ9zT': 'file_storage/call_v1OtkJfTUeC5VXQY072oZ9zT.json', 'var_call_0pHvLmRFOFeI8zjaOCjRnq9R': 'file_storage/call_0pHvLmRFOFeI8zjaOCjRnq9R.json'}

exec(code, env_args)
