code = """import json
import re
from collections import defaultdict

# Load data from storage variables (file paths)
with open(var_call_HYw0mq3FJgEmyLi1r5g9UqG0, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_Ok9PC4fVy4QsRKC8pQR33FCM, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# helper to extract year
year_re = re.compile(r'(19|20)\d{2}')

# counts[code][year] = count
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    # extract year
    y = None
    if filing:
        m = year_re.search(filing)
        if m:
            y = int(m.group(0))
    if y is None:
        continue
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean stray newlines/spaces
        try:
            cpcs = json.loads(cpc_field.replace("\n", "").strip())
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code')
        if not code or len(code) < 4:
            continue
        lvl5 = code[:4]
        if lvl5 in level5_symbols:
            counts[lvl5][y] += 1

# For each code, compute EMA time series sorted by year
alpha = 0.2
best_codes = []

for code, year_dict in counts.items():
    # sort years
    years = sorted(year_dict.keys())
    if not years:
        continue
    # compute EMA
    ema = None
    ema_by_year = {}
    for yr in years:
        cnt = year_dict[yr]
        if ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        ema_by_year[yr] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        best_codes.append(code)

# Sort result
best_codes_sorted = sorted(best_codes)

import json as _json
print("__RESULT__:")
print(_json.dumps(best_codes_sorted))"""

env_args = {'var_call_HYw0mq3FJgEmyLi1r5g9UqG0': 'file_storage/call_HYw0mq3FJgEmyLi1r5g9UqG0.json', 'var_call_Ok9PC4fVy4QsRKC8pQR33FCM': 'file_storage/call_Ok9PC4fVy4QsRKC8pQR33FCM.json'}

exec(code, env_args)
