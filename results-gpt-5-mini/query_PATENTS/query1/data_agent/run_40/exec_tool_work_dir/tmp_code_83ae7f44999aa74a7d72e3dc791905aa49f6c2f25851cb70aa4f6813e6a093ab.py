code = """import json
import re
from collections import defaultdict

with open(var_call_HYw0mq3FJgEmyLi1r5g9UqG0, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_Ok9PC4fVy4QsRKC8pQR33FCM, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

level5_symbols = set(r.get('symbol') for r in level5_rows if r.get('symbol'))

year_re = re.compile(r"\b(19|20)\d{2}\b")
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    y = int(m.group(0))
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace('\n', '').strip())
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code')
        if not code or len(code) < 4:
            continue
        lvl5 = code[:4]
        if lvl5 in level5_symbols:
            counts[lvl5][y] += 1

alpha = 0.2
best_codes = []
for code, yd in counts.items():
    years = sorted(yd.keys())
    ema = None
    ema_by_year = {}
    for yr in years:
        cnt = yd[yr]
        if ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        ema_by_year[yr] = ema
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        best_codes.append(code)

best_codes_sorted = sorted(best_codes)
import json as _json
print("__RESULT__:")
print(_json.dumps(best_codes_sorted))"""

env_args = {'var_call_HYw0mq3FJgEmyLi1r5g9UqG0': 'file_storage/call_HYw0mq3FJgEmyLi1r5g9UqG0.json', 'var_call_Ok9PC4fVy4QsRKC8pQR33FCM': 'file_storage/call_Ok9PC4fVy4QsRKC8pQR33FCM.json', 'var_call_YZJzI8gJqMUmC0b8RIkAO0au': [277813, 677]}

exec(code, env_args)
