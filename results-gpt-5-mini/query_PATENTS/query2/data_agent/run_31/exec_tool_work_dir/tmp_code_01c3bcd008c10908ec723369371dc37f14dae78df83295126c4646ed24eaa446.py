code = """import json
import re
from collections import defaultdict

# Load query results and CPC definitions from storage files
with open(var_call_uZa1YAddL2G235QwVR1W5aTE, 'r', encoding='utf-8') as f:
    records = json.load(f)

with open(var_call_8LtSxg1YgzD2it7B98AppNeW, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull for level 4 CPCs
cpc_title = {r['symbol']: r.get('titleFull') for r in cpc_defs}

# Helper to detect German patents in Patents_info
def is_germany(text):
    if not text:
        return False
    text = text.replace('\n', ' ')
    # common patterns: 'from DE', 'DE-', ' DE,', ' in DE', 'country code DE', 'Germany'
    patterns = [r'\bfrom\s+DE\b', r'\bDE-', r'\bDE,', r'\bin\s+DE\b', r'country\s*code\s*DE', r'\bGermany\b']
    for p in patterns:
        if re.search(p, text):
            return True
    return False

# Helper to extract year from filing_date or grant_date
def extract_year(text):
    if not text:
        return None
    m = re.search(r'(19|20)\d{2}', text)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc JSON-like field
def parse_cpc_field(cpc_field):
    if not cpc_field:
        return []
    try:
        lst = json.loads(cpc_field)
        codes = []
        for entry in lst:
            code = entry.get('code') if isinstance(entry, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # try to extract codes with regex as fallback
        return re.findall(r'"code"\s*:\s*"([A-Z0-9/]+)"', cpc_field)

# Aggregate counts per CPC level-4 symbol by filing year for German patents granted in H2 2019
alpha = 0.1
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year] = count

for rec in records:
    info = rec.get('Patents_info', '')
    if not is_germany(info):
        continue
    cpc_field = rec.get('cpc') or rec.get('CPC')
    filing = rec.get('filing_date') or rec.get('Filing_date')
    year = extract_year(filing)
    if year is None:
        # fallback to grant_date
        year = extract_year(rec.get('grant_date'))
    if year is None:
        continue
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        if not code or len(code) < 3:
            continue
        symbol = code[:3].upper()
        # ensure symbol looks like letter+2 digits
        if not re.match(r'^[A-Z]\d{2}$', symbol):
            # try first 3 chars fallback
            symbol = symbol
        counts[symbol][year] += 1

# For each symbol that is present and in level-4 definitions, compute EMA across years and find best year
results = []
for symbol, year_counts in counts.items():
    if symbol not in cpc_title:
        # skip symbols not in level-4 definitions
        continue
    # build sorted years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    # initialize EMA with first year's count
    first_year = years[0]
    ema = float(year_counts[first_year])
    ema_by_year[first_year] = ema
    for y in years[1:]:
        c = float(year_counts[y])
        ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    best_ema = ema_by_year[best_year]
    results.append({
        'cpc_group_code': symbol,
        'titleFull': cpc_title.get(symbol),
        'best_year': int(best_year),
        'best_ema': round(best_ema, 4)
    })

# Sort results by best_ema descending
results.sort(key=lambda x: (-x['best_ema'], x['cpc_group_code']))

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_EfRBax6hzCx2UiC0ghQYhdkm': ['publicationinfo'], 'var_call_QR3UjU0wikjaXaQBZgfcgCRB': ['cpc_definition'], 'var_call_G6o6GvXBMro9WbS516sSZ442': 'file_storage/call_G6o6GvXBMro9WbS516sSZ442.json', 'var_call_8LtSxg1YgzD2it7B98AppNeW': 'file_storage/call_8LtSxg1YgzD2it7B98AppNeW.json', 'var_call_uZa1YAddL2G235QwVR1W5aTE': 'file_storage/call_uZa1YAddL2G235QwVR1W5aTE.json'}

exec(code, env_args)
