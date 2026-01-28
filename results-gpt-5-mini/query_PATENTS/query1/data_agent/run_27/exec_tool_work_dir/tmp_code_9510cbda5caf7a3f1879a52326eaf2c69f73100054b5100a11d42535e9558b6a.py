code = """import json
import re
from collections import defaultdict

file_symbols = var_call_hhze6RW5Hrd7TvkcPLkzfc5S
file_pubs = var_call_OgklCS1GfZ5AQf9iW6lgvq6w

with open(file_symbols, 'r') as f:
    symbols_records = json.load(f)

level5_symbols = set()
for r in symbols_records:
    s = r.get('symbol')
    if s:
        level5_symbols.add(s.replace(' ', ''))

with open(file_pubs, 'r') as f:
    pubs = json.load(f)

pat = re.compile('[12][0-9]{3}')

def extract_year(s):
    if not s:
        return None
    m = pat.findall(s)
    if not m:
        return None
    for candidate in m:
        y = int(candidate)
        if 1800 <= y <= 2050:
            return y
    return None

counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    cpc_text = rec.get('cpc')
    year = extract_year(rec.get('filing_date'))
    if year is None:
        continue
    try:
        entries = json.loads(cpc_text)
    except Exception:
        try:
            entries = json.loads(cpc_text.replace('\n', ' '))
        except Exception:
            entries = []
    if not isinstance(entries, list):
        continue
    for e in entries:
        code = e.get('code') if isinstance(e, dict) else None
        if not code:
            continue
        code = code.replace(' ', '')
        left = code.split('/')[0]
        matched = None
        # find a level5 symbol that is prefix of left
        for sym in level5_symbols:
            if left.startswith(sym):
                matched = sym
                break
        if matched:
            counts[matched][year] += 1

alpha = 0.2
symbol_year_ema = {}
symbol_best_year = {}

for sym, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    ema_by_year = {}
    ema = yc[years[0]]
    ema_by_year[years[0]] = ema
    for y in years[1:]:
        x = yc[y]
        ema = alpha * x + (1 - alpha) * ema
        ema_by_year[y] = ema
    symbol_year_ema[sym] = ema_by_year
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    symbol_best_year[sym] = best_year

result_syms = sorted([sym for sym, yr in symbol_best_year.items() if yr == 2022])

print("__RESULT__:")
print(json.dumps(result_syms))"""

env_args = {'var_call_hhze6RW5Hrd7TvkcPLkzfc5S': 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json', 'var_call_OgklCS1GfZ5AQf9iW6lgvq6w': 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json'}

exec(code, env_args)
