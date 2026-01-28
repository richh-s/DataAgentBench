code = """import json
from collections import defaultdict, OrderedDict
import re

# Load input data from storage variables
# var_call_REXK1X7tGAMD8oDC6nRpGCr7 and var_call_XC02b47QYtx3SRyHXC5tZWck are provided by the tool calls

def load_maybe_path(var):
    if isinstance(var, str):
        # assume it's a file path to json
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

records = load_maybe_path(var_call_REXK1X7tGAMD8oDC6nRpGCr7)
cpc_defs = load_maybe_path(var_call_XC02b47QYtx3SRyHXC5tZWck)

# build title lookup for level-4 symbols
title_lookup = {r['symbol']: r.get('titleFull') for r in cpc_defs}

# helper to extract year and month from natural-language date strings
month_map = {
    'jan':1,'january':1,'feb':2,'february':2,'mar':3,'march':3,'apr':4,'april':4,'may':5,'jun':6,'june':6,
    'jul':7,'july':7,'aug':8,'august':8,'sep':9,'september':9,'oct':10,'october':10,'nov':11,'november':11,
    'dec':12,'december':12
}

def parse_date(text):
    if not text or not isinstance(text, str):
        return None, None
    text_low = text.lower()
    year_match = re.search(r'(20\d{2}|19\d{2})', text_low)
    year = int(year_match.group(1)) if year_match else None
    month = None
    # find month name
    for name, num in month_map.items():
        if name in text_low:
            month = num
            break
    # also check for numeric month patterns like 2019-10-31
    num_month_match = re.search(r'-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01])', text_low)
    if num_month_match and not month:
        month = int(num_month_match.group(1))
    return year, month

# helper to parse cpc field which is a JSON-like string

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    # cpc_field may already be list/dict
    if isinstance(cpc_field, list):
        objs = cpc_field
    else:
        try:
            objs = json.loads(cpc_field)
        except Exception:
            # try fixing common issues: single quotes -> double quotes
            try:
                objs = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                return []
    codes = []
    for o in objs:
        if isinstance(o, dict) and 'code' in o:
            codes.append(o['code'])
        elif isinstance(o, str):
            codes.append(o)
    return codes

# regex to extract level-4 symbol: letter + two digits (e.g., G06 -> 'G06', A61 -> 'A61')
symbol_re = re.compile(r'^([A-Z]\d{2})')

# Build counts per (symbol, filing_year) for patents that were granted in Jul-Dec 2019 and are from Germany (records already filtered by DE)
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year] = count

for rec in records:
    grant_date = rec.get('grant_date')
    year, month = parse_date(grant_date)
    if year != 2019 or (month is None) or month < 7 or month > 12:
        continue
    # parse filing year
    filing_date = rec.get('filing_date') or ''
    fyear_match = re.search(r'(20\d{2}|19\d{2})', str(filing_date))
    if not fyear_match:
        # try priority_date
        fyear_match = re.search(r'(20\d{2}|19\d{2})', str(rec.get('priority_date','')))
    if not fyear_match:
        continue
    fyear = int(fyear_match.group(1))
    # extract cpc codes
    codes = extract_cpc_codes(rec.get('cpc'))
    symbols = set()
    for code in codes:
        m = symbol_re.match(code)
        if m:
            symbols.add(m.group(1))
    for sym in symbols:
        counts[sym][fyear] += 1

# For each symbol, compute yearly EMA with alpha=0.1
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    # sort years ascending
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = float(c)
        else:
            ema = alpha * float(c) + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find best year where ema is max
    best_year = max(ema_by_year.items(), key=lambda kv: kv[1])[0]
    max_ema = ema_by_year[best_year]
    results.append({'symbol': sym, 'titleFull': title_lookup.get(sym), 'best_year': best_year, 'max_ema': round(max_ema, 6)})

# sort results by max_ema descending
results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)

# Output JSON string
out = json.dumps(results_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_L1duTcvgEWRATMKr4v3d5GW1': 'file_storage/call_L1duTcvgEWRATMKr4v3d5GW1.json', 'var_call_XC02b47QYtx3SRyHXC5tZWck': 'file_storage/call_XC02b47QYtx3SRyHXC5tZWck.json', 'var_call_REXK1X7tGAMD8oDC6nRpGCr7': 'file_storage/call_REXK1X7tGAMD8oDC6nRpGCr7.json'}

exec(code, env_args)
