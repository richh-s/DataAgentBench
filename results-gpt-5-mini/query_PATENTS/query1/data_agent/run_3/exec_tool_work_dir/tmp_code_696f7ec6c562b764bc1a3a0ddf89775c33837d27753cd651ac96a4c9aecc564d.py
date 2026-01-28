code = """import json
import re
from collections import defaultdict, OrderedDict

# Load the large query results from storage file paths
pub_path = var_call_XLm6w9Kebpc0YMfZHyM8EcDt
cpc_symbols_path = var_call_NLkNkhb6Mu5NOcGKQZmvhQVz

with open(pub_path, 'r', encoding='utf-8') as f:
    publications = json.load(f)

with open(cpc_symbols_path, 'r', encoding='utf-8') as f:
    cpc_symbols_rows = json.load(f)

# Extract level-5 CPC symbols into a set
level5_symbols = set()
for r in cpc_symbols_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract year from filing_date text
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc JSON-like string for codes
def parse_cpc_field(cpc_field):
    if not cpc_field or not isinstance(cpc_field, str):
        return []
    try:
        arr = json.loads(cpc_field)
    except Exception:
        # fallback: try to fix single quotes
        try:
            arr = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            return []
    codes = []
    for item in arr:
        if isinstance(item, dict):
            code = item.get('code')
            if code and isinstance(code, str):
                codes.append(code.strip())
    return codes

# Build counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year] = count
all_years = set()

for rec in publications:
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    all_years.add(year)
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    # Deduplicate per publication per symbol
    symbols_in_pub = set()
    for code in codes:
        left = code.split('/')[0].strip()
        if len(left) >= 4:
            symbol = left[:4]
        else:
            symbol = left
        if symbol in level5_symbols:
            symbols_in_pub.add(symbol)
    for sym in symbols_in_pub:
        counts[sym][year] += 1

if not all_years:
    result = []
else:
    years_sorted = sorted(all_years)
    # Ensure consistent year ordering from earliest to latest
    # For EMA, we will iterate in ascending years
    alpha = 0.2
    symbols_with_best_year_2022 = []

    for sym, year_counts in counts.items():
        # build series for all years_sorted, fill missing with 0
        series = [year_counts.get(y, 0) for y in years_sorted]
        # compute EMA
        ema_values = []
        prev = None
        for val in series:
            if prev is None:
                ema = val
            else:
                ema = alpha * val + (1 - alpha) * prev
            ema_values.append(ema)
            prev = ema
        # find year index of max EMA
        if not ema_values:
            continue
        max_idx = int(max(range(len(ema_values)), key=lambda i: ema_values[i]))
        best_year = years_sorted[max_idx]
        if best_year == 2022:
            symbols_with_best_year_2022.append(sym)

    # Sort results for consistency
    result = sorted(symbols_with_best_year_2022)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_XLm6w9Kebpc0YMfZHyM8EcDt': 'file_storage/call_XLm6w9Kebpc0YMfZHyM8EcDt.json', 'var_call_NLkNkhb6Mu5NOcGKQZmvhQVz': 'file_storage/call_NLkNkhb6Mu5NOcGKQZmvhQVz.json'}

exec(code, env_args)
