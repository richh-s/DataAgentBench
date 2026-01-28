code = """import json
import re
from collections import defaultdict

# Load tool results from files (paths provided in storage variables)
with open(var_call_BDWG1gqxQVQQrkLM8yYykV4n, 'r') as f:
    pubs = json.load(f)

with open(var_call_9otBi7buNaFT6mCTSVsOBr3p, 'r') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull
cpc_title = {row['symbol']: row.get('titleFull') for row in cpc_defs}

# Helper to extract year from filing_date
year_re = re.compile(r'(20\d{2}|19\d{2})')

rows = []
for rec in pubs:
    filing_date = rec.get('filing_date') or ''
    m = year_re.search(filing_date)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc') or ''
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        code = code.strip()
        # level 4 group symbol: take first 3 characters (e.g., 'B01', 'A61', 'H01')
        group = code[:3]
        if len(group) < 2:
            continue
        rows.append((group, year))

# Count filings per group per year
counts = defaultdict(lambda: defaultdict(int))
for group, year in rows:
    counts[group][year] += 1

alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    # compute EMA
    ema = None
    ema_by_year = {}
    for y in years:
        x = year_counts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    max_ema = ema_by_year[best_year]
    title = cpc_title.get(group)
    results.append({
        'group': group,
        'titleFull': title,
        'best_year': int(best_year),
        'max_ema': float(max_ema),
        'years_counts': dict(sorted(year_counts.items()))
    })

# Sort results by max_ema descending
results_sorted = sorted(results, key=lambda r: r['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_BDWG1gqxQVQQrkLM8yYykV4n': 'file_storage/call_BDWG1gqxQVQQrkLM8yYykV4n.json', 'var_call_9otBi7buNaFT6mCTSVsOBr3p': 'file_storage/call_9otBi7buNaFT6mCTSVsOBr3p.json'}

exec(code, env_args)
