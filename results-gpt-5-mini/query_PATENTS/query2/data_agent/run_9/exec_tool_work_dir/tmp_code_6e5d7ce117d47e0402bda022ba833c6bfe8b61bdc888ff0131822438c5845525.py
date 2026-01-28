code = """import json
import re
from collections import defaultdict, OrderedDict

# Load the query results files
with open(var_call_9tKMcZKRri9YGKd2eDqkAxcZ, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_TLR9qTMDAy8wttpBIhYRwFef, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build title lookup for level 4 symbols
title_lookup = {row['symbol']: row['titleFull'] for row in cpc_defs}

# Months in second half
months_h2 = ['Jul','July','Aug','August','Sep','Sept','September','Oct','October','Nov','November','Dec','December']

# Helper to extract year
year_re = re.compile(r'(20\d{2}|19\d{2})')

# Accumulate counts per level4 symbol per filing year
counts = defaultdict(lambda: defaultdict(int))

for row in pubs:
    pat_info = row.get('Patents_info','') or ''
    grant_date = row.get('grant_date','') or ''
    # Filter for Germany in Patents_info (simple check)
    if 'DE' not in pat_info and 'de,' not in pat_info.lower():
        continue
    # Must be in 2019 and in second half by month substring
    if '2019' not in grant_date:
        continue
    if not any(m in grant_date for m in months_h2):
        continue
    # Get filing year
    filing = row.get('filing_date','') or ''
    m = year_re.search(filing)
    if not m:
        # try publication fields or grant_date
        m = year_re.search(grant_date)
    if not m:
        continue
    year = int(m.group(1))
    # Parse CPC field
    cpc_field = row.get('cpc','') or ''
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean and find codes via regex
        codes = re.findall(r'"code":\s*"([A-Z]\d{2}[A-Z]?)', cpc_field)
        cpcs = [{'code': c} for c in codes]
    # For each unique level4 symbol in this patent
    symbols = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else entry
        if not code or len(code) < 3:
            continue
        sym = code[:3]
        symbols.add(sym)
    for sym in symbols:
        counts[sym][year] += 1

# For each symbol, compute EMA across years sorted
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find peak ema and its year (earliest if tie)
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], -kv[0]))[0]
    peak_ema = ema_by_year[best_year]
    title = title_lookup.get(sym, None)
    results.append({'symbol': sym, 'titleFull': title, 'best_year': int(best_year), 'peak_ema': float(peak_ema), 'year_counts': {str(k): int(v) for k,v in year_counts.items()}})

# Sort results by peak_ema desc
results_sorted = sorted(results, key=lambda r: r['peak_ema'], reverse=True)

# Prepare output
out = results_sorted

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_PoSBjFfctIckOvdFmTFlACfy': 'file_storage/call_PoSBjFfctIckOvdFmTFlACfy.json', 'var_call_9tKMcZKRri9YGKd2eDqkAxcZ': 'file_storage/call_9tKMcZKRri9YGKd2eDqkAxcZ.json', 'var_call_TLR9qTMDAy8wttpBIhYRwFef': 'file_storage/call_TLR9qTMDAy8wttpBIhYRwFef.json'}

exec(code, env_args)
