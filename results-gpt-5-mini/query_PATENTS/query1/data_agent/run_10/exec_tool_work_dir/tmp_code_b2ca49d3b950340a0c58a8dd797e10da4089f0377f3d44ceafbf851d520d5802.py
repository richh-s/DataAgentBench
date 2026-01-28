code = """import json
import re
from collections import defaultdict

# Load smaller slices to avoid timeout; open files and stream parse

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

cpc_defs = load_json(var_call_YE2zqtqcVqTWgh47MXYr8BqH)
# Only load first 50k records of publications to limit time? But we need all. We'll process streaming.

# For large file, stream by reading and parsing manually
pubs_path = var_call_Mnu7ZA99v6zlg0eU5qFuAnGn

# Extract level-5 symbols set
level5_symbols = set()
for rec in cpc_defs:
    sym = rec.get('symbol')
    if sym:
        level5_symbols.add(sym)

# regex and helpers
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None


def parse_cpc_field(cpc_str):
    if not cpc_str or not isinstance(cpc_str, str):
        return []
    try:
        lst = json.loads(cpc_str)
        codes = [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
        return [c for c in codes if c]
    except Exception:
        codes = re.findall(r"[A-Z]\d{2}[A-Z]\d+(?:/\d+)?", cpc_str)
        return codes


def match_code_to_level5(code, symbols_set):
    if not code:
        return None
    if code in symbols_set:
        return code
    code_no_slash = code.split('/')[0]
    candidates = [s for s in symbols_set if code.startswith(s)]
    if candidates:
        return max(candidates, key=len)
    candidates = [s for s in symbols_set if code_no_slash.startswith(s)]
    if candidates:
        return max(candidates, key=len)
    for l in (6,5,4,3):
        prefix = code_no_slash[:l]
        candidates = [s for s in symbols_set if s.startswith(prefix)]
        if candidates:
            return max(candidates, key=len)
    return None

# Process publications file streaming to avoid loading all into memory
counts = defaultdict(lambda: defaultdict(int))

with open(pubs_path, 'r', encoding='utf-8') as f:
    buf = f.read()
    pubs = json.loads(buf)

for rec in pubs:
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if not year:
        continue
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        sym = match_code_to_level5(code, level5_symbols)
        if sym:
            counts[sym][year] += 1

# Compute EMA
alpha = 0.2
symbols_with_best_year_2022 = []
for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    max_ema = max(ema_by_year.values())
    best_years = [y for y, v in ema_by_year.items() if abs(v - max_ema) < 1e-9]
    if 2022 in best_years:
        symbols_with_best_year_2022.append(sym)

symbols_with_best_year_2022 = sorted(list(set(symbols_with_best_year_2022)))

import json as _json
print("__RESULT__:")
print(_json.dumps(symbols_with_best_year_2022))"""

env_args = {'var_call_KOAe9jSTh9Mbmi1RCVQS58Hp': ['publicationinfo'], 'var_call_tAgqIyi2aU92W9WzynRcveR3': ['cpc_definition'], 'var_call_YE2zqtqcVqTWgh47MXYr8BqH': 'file_storage/call_YE2zqtqcVqTWgh47MXYr8BqH.json', 'var_call_Mnu7ZA99v6zlg0eU5qFuAnGn': 'file_storage/call_Mnu7ZA99v6zlg0eU5qFuAnGn.json'}

exec(code, env_args)
