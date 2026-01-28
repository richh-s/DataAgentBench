code = """import json
from collections import defaultdict

with open(var_call_HYw0mq3FJgEmyLi1r5g9UqG0, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_Ok9PC4fVy4QsRKC8pQR33FCM, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

def extract_year(s):
    if not s:
        return None
    for i in range(len(s) - 3):
        sub = s[i:i+4]
        if sub.isdigit() and (sub.startswith('19') or sub.startswith('20')):
            return int(sub)
    return None

counts = defaultdict(lambda: defaultdict(int))
for rec in pubs:
    filing = rec.get('filing_date') or ''
    y = extract_year(filing)
    if not y:
        continue
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cleaned = cpc_field.replace(chr(10), '').strip()
            cpcs = json.loads(cleaned)
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if not isinstance(entry, dict):
            continue
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
    if not years:
        continue
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
print('__RESULT__:')
print(json.dumps(best_codes_sorted))"""

env_args = {'var_call_HYw0mq3FJgEmyLi1r5g9UqG0': 'file_storage/call_HYw0mq3FJgEmyLi1r5g9UqG0.json', 'var_call_Ok9PC4fVy4QsRKC8pQR33FCM': 'file_storage/call_Ok9PC4fVy4QsRKC8pQR33FCM.json', 'var_call_YZJzI8gJqMUmC0b8RIkAO0au': [277813, 677]}

exec(code, env_args)
