code = """import json
import re
from collections import defaultdict

# Load query results from storage keys
with open(var_call_VI7hTvYfFCFSvKSG2STTSOWI, 'r', encoding='utf-8') as f:
    records = json.load(f)

with open(var_call_jOwsDWVVvMdGEkaM2ADUFmCY, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping for level-4 CPC symbols to titleFull
cpc_map = {row['symbol']: row.get('titleFull') for row in cpc_defs}

# Helper to extract year from filing_date
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc JSON-like string and extract codes

def extract_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        parsed = json.loads(cpc_field)
        codes = []
        for entry in parsed:
            code = entry.get('code')
            if code and isinstance(code, str):
                codes.append(code.strip())
        return codes
    except Exception:
        # fallback: find code-like patterns
        return re.findall(r"[A-HY]\d{2}", cpc_field)

# Aggregate counts per group (first 3 chars of code) per filing year
counts = defaultdict(lambda: defaultdict(int))

for rec in records:
    filing_date = rec.get('filing_date')
    year = extract_year(filing_date)
    if year is None:
        continue
    cpc_field = rec.get('cpc')
    codes = extract_codes(cpc_field)
    for code in codes:
        # Extract level-4 group: first letter and two digits
        m = re.match(r'([A-Z][0-9]{2})', code)
        if m:
            group = m.group(1)
            counts[group][year] += 1

# For each group, compute EMA across years sorted ascending, alpha=0.1
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        cnt = year_counts[y]
        if ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    title = cpc_map.get(group)
    results.append({
        'cpc_group_code': group,
        'titleFull': title if title is not None else None,
        'best_year': best_year,
        'best_ema_value': round(best_ema, 4)
    })

# Sort results by best_ema_value descending
results.sort(key=lambda x: x['best_ema_value'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_Wv3rlUttpTXWiZKaWDRV2xkr': ['publicationinfo'], 'var_call_nGHY6mLzTVQucE6avyHEJOrR': ['cpc_definition'], 'var_call_7aD7DrIhbUSWNQv3P7ghYxRx': 'file_storage/call_7aD7DrIhbUSWNQv3P7ghYxRx.json', 'var_call_rUXcBsySx0FBLTGdZU4Iepn8': 'file_storage/call_rUXcBsySx0FBLTGdZU4Iepn8.json', 'var_call_jOwsDWVVvMdGEkaM2ADUFmCY': 'file_storage/call_jOwsDWVVvMdGEkaM2ADUFmCY.json', 'var_call_VI7hTvYfFCFSvKSG2STTSOWI': 'file_storage/call_VI7hTvYfFCFSvKSG2STTSOWI.json'}

exec(code, env_args)
