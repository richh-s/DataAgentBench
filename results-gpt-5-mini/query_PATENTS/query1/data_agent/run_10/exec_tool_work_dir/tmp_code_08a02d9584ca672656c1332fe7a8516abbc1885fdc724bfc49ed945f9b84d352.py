code = """import json
import re
from collections import defaultdict

# Load data from storage-provided file paths
with open(var_call_YE2zqtqcVqTWgh47MXYr8BqH, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
with open(var_call_Mnu7ZA99v6zlg0eU5qFuAnGn, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Extract level-5 symbols set
level5_symbols = set()
for rec in cpc_defs:
    sym = rec.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Helper to extract year from filing_date
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc field string into list of codes

def parse_cpc_field(cpc_str):
    if not cpc_str or not isinstance(cpc_str, str):
        return []
    try:
        # Some fields are JSON-like strings; try to load
        lst = json.loads(cpc_str)
        codes = [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
        return [c for c in codes if c]
    except Exception:
        # fallback: try to extract occurrences of patterns like letters+digits+maybe / and digits
        codes = re.findall(r"[A-Z]\d{2}[A-Z]\d+(?:/\d+)?", cpc_str)
        return codes

# Matching function: find best matching level-5 symbol for a code

def match_code_to_level5(code, symbols_set):
    if not code:
        return None
    # direct exact match
    if code in symbols_set:
        return code
    # try prefixes: consider code and code before '/'
    code_no_slash = code.split('/')[0]
    candidates = [s for s in symbols_set if code.startswith(s)]
    if candidates:
        return max(candidates, key=len)
    candidates = [s for s in symbols_set if code_no_slash.startswith(s)]
    if candidates:
        return max(candidates, key=len)
    # sometimes symbols are shorter (like 'C01B33' vs 'C01B33/00'), try matching symbol as prefix of code_no_slash
    candidates = [s for s in symbols_set if code_no_slash.startswith(s)]
    if candidates:
        return max(candidates, key=len)
    # last resort: try matching by first 4 or 3 characters
    for l in (6,5,4,3):
        prefix = code_no_slash[:l]
        candidates = [s for s in symbols_set if s.startswith(prefix)]
        if candidates:
            return max(candidates, key=len)
    return None

# Build counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()
for rec in pubs:
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if not year:
        continue
    all_years.add(year)
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        sym = match_code_to_level5(code, level5_symbols)
        if sym:
            counts[sym][year] += 1

# For each symbol, compute yearly EMA with alpha=0.2
alpha = 0.2
symbols_with_best_year_2022 = []

for sym, year_counts in counts.items():
    # consider years in sorted order
    years = sorted(year_counts.keys())
    if not years:
        continue
    # compute EMA sequentially
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find max EMA value and corresponding years
    max_ema = max(ema_by_year.values())
    best_years = [y for y, v in ema_by_year.items() if abs(v - max_ema) < 1e-9]
    if 2022 in best_years:
        symbols_with_best_year_2022.append(sym)

# Sort result
symbols_with_best_year_2022 = sorted(list(set(symbols_with_best_year_2022)))

import json as _json
print("__RESULT__:")
print(_json.dumps(symbols_with_best_year_2022))"""

env_args = {'var_call_KOAe9jSTh9Mbmi1RCVQS58Hp': ['publicationinfo'], 'var_call_tAgqIyi2aU92W9WzynRcveR3': ['cpc_definition'], 'var_call_YE2zqtqcVqTWgh47MXYr8BqH': 'file_storage/call_YE2zqtqcVqTWgh47MXYr8BqH.json', 'var_call_Mnu7ZA99v6zlg0eU5qFuAnGn': 'file_storage/call_Mnu7ZA99v6zlg0eU5qFuAnGn.json'}

exec(code, env_args)
