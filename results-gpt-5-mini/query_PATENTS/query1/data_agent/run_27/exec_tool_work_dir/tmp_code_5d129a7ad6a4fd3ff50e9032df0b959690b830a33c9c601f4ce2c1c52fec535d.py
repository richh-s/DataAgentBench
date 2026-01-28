code = """import json
from collections import defaultdict

file_symbols = 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json'
file_pubs = 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json'

with open(file_symbols, 'r') as f:
    symbols_records = json.load(f)

level5 = set()
for r in symbols_records:
    s = r.get('symbol')
    if s:
        level5.add(s.replace(' ', ''))

with open(file_pubs, 'r') as f:
    pubs = json.load(f)


def extract_year(fd):
    if not fd:
        return None
    s = str(fd)
    for i in range(len(s)-3):
        sub = s[i:i+4]
        if sub.isdigit():
            y = int(sub)
            if 1800 <= y <= 2050:
                return y
    return None

counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    cpc_text = rec.get('cpc')
    year = extract_year(rec.get('filing_date') or '')
    if year is None:
        continue
    try:
        entries = json.loads(cpc_text)
    except Exception:
        try:
            entries = json.loads((cpc_text or '').replace('\n',' '))
        except Exception:
            entries = []
    if not isinstance(entries, list):
        continue
    for e in entries:
        if not isinstance(e, dict):
            continue
        code = e.get('code')
        if not code:
            continue
        left = code.split('/')[0].replace(' ', '')
        # match any level5 symbol that exactly equals left or is prefix
        if left in level5:
            counts[left][year] += 1
        else:
            for L in range(len(left), 0, -1):
                pref = left[:L]
                if pref in level5:
                    counts[pref][year] += 1
                    break

alpha = 0.2
symbol_best = {}

for sym, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    ema = yc[years[0]]
    ema_by_year = {years[0]: ema}
    for y in years[1:]:
        x = yc[y]
        ema = alpha * x + (1 - alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    symbol_best[sym] = best_year

result = sorted([s for s, y in symbol_best.items() if y == 2022])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hhze6RW5Hrd7TvkcPLkzfc5S': 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json', 'var_call_OgklCS1GfZ5AQf9iW6lgvq6w': 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json', 'var_call_8do9cpvQuihKdifami9t5WEh': {'a': 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json', 'b': 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json'}}

exec(code, env_args)
