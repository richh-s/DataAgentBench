code = """import json
import re

# Load data from previous query results (file paths are provided in variables)
with open(var_call_NrOxPJB0wn9tkToIWHiv5GZI, 'r', encoding='utf-8') as f:
    patents = json.load(f)
with open(var_call_V7ONosHXlW2jMqUbKx60BNED, 'r', encoding='utf-8') as f:
    cpc_level4 = json.load(f)

# Build symbol->title map for level 4
symbol_title = {r['symbol']: r.get('titleFull','') for r in cpc_level4}
symbols = list(symbol_title.keys())
# sort symbols by length descending to match longest prefix first
symbols_sorted = sorted(symbols, key=lambda s: -len(s))

# Helper to detect German patents from Patents_info
def is_german(patents_info):
    if not patents_info:
        return False
    # Common patterns: 'from DE', 'DE-', ' DE,', 'country DE', 'application (no. DE-...'
    if re.search(r'\bDE\b', patents_info):
        return True
    if re.search(r'DE-', patents_info):
        return True
    return False

# Helper to check grant_date in second half 2019
months_h2 = ['Jul','July','Aug','August','Sep','Sept','September','Oct','October','Nov','November','Dec','December']

def is_h2_2019(grant_date):
    if not grant_date:
        return False
    if '2019' not in grant_date:
        return False
    for m in months_h2:
        if m in grant_date:
            return True
    return False

# Extract filing year
def extract_year(text):
    if not text:
        return None
    m = re.search(r'(19|20)\d{2}', text)
    if m:
        return int(m.group(0))
    return None

# Parse CPC JSON string safely
import ast

def parse_cpc(cpc_str):
    if not cpc_str:
        return []
    try:
        return json.loads(cpc_str)
    except Exception:
        try:
            # fallback: use ast.literal_eval
            return ast.literal_eval(cpc_str)
        except Exception:
            return []

# Build counts per (symbol, year)
from collections import defaultdict
counts = defaultdict(int)

for rec in patents:
    pi = rec.get('Patents_info','')
    if not is_german(pi):
        continue
    gd = rec.get('grant_date','')
    if not is_h2_2019(gd):
        continue
    fy = extract_year(rec.get('filing_date','') or '')
    if fy is None:
        continue
    # parse cpc
    codes = parse_cpc(rec.get('cpc',''))
    for entry in codes:
        code = None
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, str):
            code = entry
        if not code:
            continue
        code = code.strip()
        # find matching level-4 symbol by longest prefix
        matched = None
        for sym in symbols_sorted:
            if code.startswith(sym):
                matched = sym
                break
        if matched:
            counts[(matched, fy)] += 1

# For each symbol, build year series and compute EMA (alpha=0.1)
alpha = 0.1
results = []
from collections import defaultdict
symbol_years = defaultdict(dict)
for (sym, yr), cnt in counts.items():
    symbol_years[sym][yr] = cnt

for sym, year_counts in symbol_years.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    # initialize EMA with first year's count
    ema_by_year = {}
    ema = year_counts[years[0]]
    ema_by_year[years[0]] = ema
    for y in years[1:]:
        cnt = year_counts.get(y, 0)
        ema = alpha * cnt + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA (if tie pick latest year)
    max_ema = None
    best_year = None
    for y, e in ema_by_year.items():
        if (max_ema is None) or (e > max_ema) or (e == max_ema and y > best_year):
            max_ema = e
            best_year = y
    results.append({'symbol': sym, 'titleFull': symbol_title.get(sym, ''), 'best_year': best_year, 'max_ema': max_ema})

# Sort results by max_ema desc
results_sorted = sorted(results, key=lambda r: - (r['max_ema'] if r['max_ema'] is not None else 0))

# Prepare output list with required fields (symbol, titleFull, best_year)
out = [{'symbol': r['symbol'], 'titleFull': r['titleFull'], 'best_year': r['best_year']} for r in results_sorted]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NqE2lEqlPPAoKQ7ZRfgVnYpO': ['publicationinfo'], 'var_call_fBCFMBPCVO0b4tC08WZRTPz7': ['cpc_definition'], 'var_call_sBRgSeQDZL39xZ2fkUbpmTn8': 'file_storage/call_sBRgSeQDZL39xZ2fkUbpmTn8.json', 'var_call_WJyshfST2ad2Wkhd3hoZP1wf': 'file_storage/call_WJyshfST2ad2Wkhd3hoZP1wf.json', 'var_call_V7ONosHXlW2jMqUbKx60BNED': 'file_storage/call_V7ONosHXlW2jMqUbKx60BNED.json', 'var_call_NrOxPJB0wn9tkToIWHiv5GZI': 'file_storage/call_NrOxPJB0wn9tkToIWHiv5GZI.json'}

exec(code, env_args)
