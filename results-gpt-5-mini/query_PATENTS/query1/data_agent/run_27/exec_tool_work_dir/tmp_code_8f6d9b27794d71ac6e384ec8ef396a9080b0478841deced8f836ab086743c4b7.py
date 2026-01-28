code = """import json, re
from collections import defaultdict

# Load inputs from storage variables
file_symbols = var_call_hhze6RW5Hrd7TvkcPLkzfc5S
file_pubs = var_call_OgklCS1GfZ5AQf9iW6lgvq6w

# Read JSON files
with open(file_symbols, 'r') as f:
    symbols_records = json.load(f)
level5_symbols = set([r['symbol'] for r in symbols_records if 'symbol' in r and r['symbol']])

with open(file_pubs, 'r') as f:
    pubs = json.load(f)

# Helper to extract year from filing_date
year_re = re.compile(r'(20\d{2}|19\d{2})')

def extract_year(fd):
    if not fd:
        return None
    m = year_re.search(fd)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc JSON text
def parse_cpc(cpc_text):
    try:
        return json.loads(cpc_text)
    except Exception:
        # try to fix common single quotes or trailing commas
        try:
            fixed = cpc_text.replace("\n", " ").strip()
            return json.loads(fixed)
        except Exception:
            return []

# Build counts per level5 symbol per year
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    cpc_text = rec.get('cpc')
    fd = rec.get('filing_date')
    year = extract_year(fd)
    if year is None:
        continue
    entries = parse_cpc(cpc_text)
    if not isinstance(entries, list):
        continue
    for e in entries:
        code = e.get('code')
        if not code:
            continue
        code = code.replace(' ', '')
        # split at slash
        left = code.split('/')[0]
        # generate prefixes from longest to shortest
        match = None
        for L in range(len(left), 0, -1):
            pref = left[:L]
            if pref in level5_symbols:
                match = pref
                break
        if match:
            counts[match][year] += 1

# For each symbol, compute EMA across sorted years
alpha = 0.2
symbol_year_ema = {}  # symbol -> {year: ema}
symbol_best_year = {}

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    # initialize with first year's count
    first_year = years[0]
    ema = year_counts[first_year]
    ema_by_year[first_year] = ema
    for y in years[1:]:
        x = year_counts[y]
        ema = alpha * x + (1 - alpha) * ema
        ema_by_year[y] = ema
    # store
    symbol_year_ema[sym] = ema_by_year
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    symbol_best_year[sym] = best_year

# Now determine, for each year, which symbol has the highest EMA that year
# Build years set
all_years = set()
for d in symbol_year_ema.values():
    all_years.update(d.keys())
all_years = sorted(all_years)

year_top_symbol = {}
for y in all_years:
    top_sym = None
    top_ema = None
    for sym, emad in symbol_year_ema.items():
        ema = emad.get(y)
        if ema is None:
            continue
        if (top_ema is None) or (ema > top_ema):
            top_ema = ema
            top_sym = sym
    if top_sym:
        year_top_symbol[y] = (top_sym, top_ema)

# Finally, return only level-5 symbols whose best year is 2022
result_syms = [sym for sym, by in symbol_best_year.items() if by == 2022]
result_syms_sorted = sorted(result_syms)

import json
print("__RESULT__:")
print(json.dumps(result_syms_sorted))"""

env_args = {'var_call_hhze6RW5Hrd7TvkcPLkzfc5S': 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json', 'var_call_OgklCS1GfZ5AQf9iW6lgvq6w': 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json'}

exec(code, env_args)
