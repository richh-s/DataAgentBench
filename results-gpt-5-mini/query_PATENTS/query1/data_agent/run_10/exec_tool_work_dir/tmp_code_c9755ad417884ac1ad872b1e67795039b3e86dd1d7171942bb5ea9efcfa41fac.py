code = """import json
import re
from collections import defaultdict

cpc_defs_path = var_call_YE2zqtqcVqTWgh47MXYr8BqH
pubs_path = var_call_Mnu7ZA99v6zlg0eU5qFuAnGn

# Load CPC defs
with open(cpc_defs_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

level5_symbols = set()
for rec in cpc_defs:
    sym = rec.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Prepare symbols sorted by length desc for prefix matching
symbols_sorted = sorted(level5_symbols, key=lambda s: -len(s))

# regex for year
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.search(text)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

# parse cpc field

def parse_cpc_field(cpc_str):
    if not cpc_str or not isinstance(cpc_str, str):
        return []
    try:
        lst = json.loads(cpc_str)
        codes = [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
        return [c for c in codes if c]
    except Exception:
        # fallback regex: letters+digits+letter and optional /digits/groups
        codes = re.findall(r"[A-Z]\d{2}[A-Z]\d*(?:/\d+)?", cpc_str)
        return codes

# match code to level-5 symbol

def match_code_to_level5(code):
    if not code:
        return None
    code_no_slash = code.split('/')[0]
    # direct exact
    if code in level5_symbols:
        return code
    # try symbols as prefix of code or code_no_slash
    for s in symbols_sorted:
        if code.startswith(s) or code_no_slash.startswith(s):
            return s
    return None

# Stream parse publications JSON array to avoid loading whole file
counts = defaultdict(lambda: defaultdict(int))
min_year = None
max_year = None

with open(pubs_path, 'r', encoding='utf-8') as f:
    buf = ''
    in_obj = False
    brace_count = 0
    while True:
        chunk = f.read(65536)
        if not chunk:
            break
        for ch in chunk:
            if not in_obj:
                if ch == '{':
                    in_obj = True
                    brace_count = 1
                    buf = '{'
                else:
                    continue
            else:
                buf += ch
                if ch == '{':
                    brace_count += 1
                elif ch == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # complete object
                        try:
                            rec = json.loads(buf)
                        except Exception:
                            # skip malformed
                            buf = ''
                            in_obj = False
                            brace_count = 0
                            continue
                        filing = rec.get('filing_date')
                        year = extract_year(filing)
                        if year is not None:
                            if min_year is None or year < min_year:
                                min_year = year
                            if max_year is None or year > max_year:
                                max_year = year
                            cpc_field = rec.get('cpc')
                            codes = parse_cpc_field(cpc_field)
                            for code in codes:
                                sym = match_code_to_level5(code)
                                if sym:
                                    counts[sym][year] += 1
                        # reset
                        buf = ''
                        in_obj = False
                        brace_count = 0

# If no data
if not counts:
    result = []
else:
    # compute EMA per symbol over full year range
    alpha = 0.2
    symbols_with_best_year_2022 = []
    if min_year is None or max_year is None:
        symbols_with_best_year_2022 = []
    else:
        years_range = list(range(min_year, max_year+1))
        for sym, year_counts in counts.items():
            ema = None
            ema_by_year = {}
            for y in years_range:
                c = year_counts.get(y, 0)
                if ema is None:
                    ema = c
                else:
                    ema = alpha * c + (1 - alpha) * ema
                ema_by_year[y] = ema
            # find max EMA
            max_ema = max(ema_by_year.values())
            best_years = [y for y,v in ema_by_year.items() if abs(v-max_ema) < 1e-9]
            if 2022 in best_years:
                symbols_with_best_year_2022.append(sym)
        result = sorted(list(set(symbols_with_best_year_2022)))

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_KOAe9jSTh9Mbmi1RCVQS58Hp': ['publicationinfo'], 'var_call_tAgqIyi2aU92W9WzynRcveR3': ['cpc_definition'], 'var_call_YE2zqtqcVqTWgh47MXYr8BqH': 'file_storage/call_YE2zqtqcVqTWgh47MXYr8BqH.json', 'var_call_Mnu7ZA99v6zlg0eU5qFuAnGn': 'file_storage/call_Mnu7ZA99v6zlg0eU5qFuAnGn.json'}

exec(code, env_args)
