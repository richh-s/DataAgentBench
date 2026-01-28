code = """import json, re

# Load level-5 symbols
with open(var_call_YE2zqtqcVqTWgh47MXYr8BqH, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
level5 = set(rec.get('symbol') for rec in cpc_defs if rec.get('symbol'))
# Prepare sorted symbols by length desc
symbols_sorted = sorted(level5, key=lambda s: -len(s))

# Load 2022 publications cpc fields
with open(var_call_HKhiFOFs3nWlSQqAZCYYOhPt, 'r', encoding='utf-8') as f:
    pubs2022 = json.load(f)

# function to parse cpc field
import json

def parse_cpc_field(cpc_str):
    if not cpc_str or not isinstance(cpc_str, str):
        return []
    try:
        lst = json.loads(cpc_str)
        return [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
    except Exception:
        return re.findall(r"[A-Z]\d{2}[A-Z]\d*(?:/\d+)?", cpc_str)

# Match code to level5 symbol

def match_code(code):
    if not code:
        return None
    code_no_slash = code.split('/')[0]
    for s in symbols_sorted:
        if code.startswith(s) or code_no_slash.startswith(s):
            return s
    return None

symbols_in_2022 = set()
for rec in pubs2022:
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        sym = match_code(code)
        if sym:
            symbols_in_2022.add(sym)

import json as _json
print("__RESULT__:")
print(_json.dumps(sorted(list(symbols_in_2022))))"""

env_args = {'var_call_KOAe9jSTh9Mbmi1RCVQS58Hp': ['publicationinfo'], 'var_call_tAgqIyi2aU92W9WzynRcveR3': ['cpc_definition'], 'var_call_YE2zqtqcVqTWgh47MXYr8BqH': 'file_storage/call_YE2zqtqcVqTWgh47MXYr8BqH.json', 'var_call_Mnu7ZA99v6zlg0eU5qFuAnGn': 'file_storage/call_Mnu7ZA99v6zlg0eU5qFuAnGn.json', 'var_call_HKhiFOFs3nWlSQqAZCYYOhPt': 'file_storage/call_HKhiFOFs3nWlSQqAZCYYOhPt.json'}

exec(code, env_args)
