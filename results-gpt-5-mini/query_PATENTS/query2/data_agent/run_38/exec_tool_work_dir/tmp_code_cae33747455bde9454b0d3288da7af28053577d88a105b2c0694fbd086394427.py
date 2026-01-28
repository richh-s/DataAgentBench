code = """import json, re
from collections import defaultdict

# Load the query results from storage-provided file paths
with open(var_call_PEhmuC9pMmqNCNpXLwOZ8oEL, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

with open(var_call_qbdyCS1kshXQ5AUjTT4soVfm, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull for level-4 CPC groups
cpc_title = {row['symbol']: row.get('titleFull') for row in cpc_defs}

# Helper to extract year from filing_date
year_re = re.compile(r'(19|20)\d{2}')
# Helper to detect Germany in Patents_info
country_re = re.compile(r'\bDE\b|DE-|GERMANY|GERMAN', re.IGNORECASE)

# Accumulate counts per group per year
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    pat_info = rec.get('Patents_info') or ''
    if not isinstance(pat_info, str):
        pat_info = str(pat_info)
    # Check for Germany
    if not country_re.search(pat_info):
        continue
    # Extract year from filing_date
    filing = rec.get('filing_date') or ''
    if filing is None:
        continue
    m = year_re.search(str(filing))
    if not m:
        continue
    year = int(m.group(0))
    # Parse CPC codes
    cpc_field = rec.get('cpc') or ''
    codes = []
    try:
        parsed = json.loads(cpc_field)
        if isinstance(parsed, list):
            for e in parsed:
                code = e.get('code') if isinstance(e, dict) else None
                if code:
                    codes.append(code)
    except Exception:
        # fallback: regex extract
        codes = re.findall(r'"code":\s*"([A-Z0-9]+[A-Z0-9/]*/?[0-9]*)"', cpc_field)
    # For each code, derive level-4 group symbol as first 3 characters (letter+2 digits)
    for code in codes:
        if len(code) < 3:
            continue
        symbol = code[:3]
        # ensure symbol matches pattern Letter + two digits
        if re.match(r'^[A-Z][0-9]{2}$', symbol):
            counts[symbol][year] += 1

# For each group, compute EMA across years and find best year
alpha = 0.1
results = []
for symbol, year_counts in counts.items():
    # Only consider groups present in cpc_definition level 4 (optional)
    title = cpc_title.get(symbol)
    # prepare sorted years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    best_year = None
    best_ema = -1
    for y in years:
        val = year_counts[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        if ema > best_ema:
            best_ema = ema
            best_year = y
    results.append({
        'symbol': symbol,
        'titleFull': title,
        'best_year': best_year
    })

# Sort results by symbol
results = sorted(results, key=lambda x: (x['symbol'] or ''))

# Output JSON string
out = json.dumps(results, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PjNn96gjT7rS9j2uwWB6HvSS': 'file_storage/call_PjNn96gjT7rS9j2uwWB6HvSS.json', 'var_call_qbdyCS1kshXQ5AUjTT4soVfm': 'file_storage/call_qbdyCS1kshXQ5AUjTT4soVfm.json', 'var_call_PEhmuC9pMmqNCNpXLwOZ8oEL': 'file_storage/call_PEhmuC9pMmqNCNpXLwOZ8oEL.json'}

exec(code, env_args)
