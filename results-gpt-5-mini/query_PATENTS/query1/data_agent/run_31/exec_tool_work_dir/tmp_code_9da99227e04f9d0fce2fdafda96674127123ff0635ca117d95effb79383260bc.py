code = """import json
import re
from collections import defaultdict

# Load variables from storage
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

records = load_var(var_call_deRgmDhVVQXfGS4scAqVdZMs)
level5_rows = load_var(var_call_wK7WsskEZwVdX45SUSqyk6WM)

level5_symbols = [r.get('symbol') for r in level5_rows if r.get('symbol')]
# remove any None and ensure strings
level5_symbols = [s for s in level5_symbols if isinstance(s, str) and s]
# sort by length desc
level5_symbols_sorted = sorted(level5_symbols, key=lambda s: len(s), reverse=True)

# function to extract year
year_re = re.compile(r'(20\d{2}|19\d{2})')

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.findall(text)
    if m:
        return int(m[-1])
    return None

counts = defaultdict(lambda: defaultdict(int))

for rec in records:
    code_sample = rec.get('code_sample')
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None or not code_sample:
        continue
    code = code_sample.strip()
    # remove trailing non-alphanum (like slash)
    code = re.match(r'^([A-Z0-9]+)', code)
    if code:
        code = code.group(1)
    else:
        code = rec.get('code_sample').strip()
    mapped = set()
    for sym in level5_symbols_sorted:
        if code.startswith(sym.replace('/', '')):
            mapped.add(sym)
            break
    for sym in mapped:
        counts[sym][year] += 1

# compute EMA
alpha = 0.2
best_year_by_symbol = {}
for sym, yc in counts.items():
    years = sorted(yc.keys())
    prev = None
    emas = {}
    for y in years:
        x = yc[y]
        if prev is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * prev
        emas[y] = ema
        prev = ema
    # pick year with max ema, tie-breaker by year (larger)
    best = max(emas.items(), key=lambda kv: (kv[1], kv[0]))
    best_year_by_symbol[sym] = best[0]

result_symbols = sorted([s for s, y in best_year_by_symbol.items() if y == 2022])

import json as _json
print("__RESULT__:")
print(_json.dumps(result_symbols))"""

env_args = {'var_call_XVJDQgV7Lq135SV2qo0jDHC1': 'file_storage/call_XVJDQgV7Lq135SV2qo0jDHC1.json', 'var_call_wK7WsskEZwVdX45SUSqyk6WM': 'file_storage/call_wK7WsskEZwVdX45SUSqyk6WM.json', 'var_call_deRgmDhVVQXfGS4scAqVdZMs': 'file_storage/call_deRgmDhVVQXfGS4scAqVdZMs.json'}

exec(code, env_args)
