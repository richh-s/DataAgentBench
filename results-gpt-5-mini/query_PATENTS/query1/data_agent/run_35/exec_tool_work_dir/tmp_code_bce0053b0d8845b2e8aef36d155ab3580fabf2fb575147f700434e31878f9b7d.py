code = """import json
import re
from collections import defaultdict

# Load the query results from storage files
with open(var_call_OLPprixqsT2cfw7tAI79YnQM, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_caEXGpG58q827HVOTfKeijy3, 'r', encoding='utf-8') as f:
    level5_rows = json.load(f)

# Build set of level 5 symbols
level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract year from filing_date string
year_re = re.compile(r'(19|20)\d{2}')
def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Count filings per group per year
counts = defaultdict(lambda: defaultdict(int))
for rec in pubs:
    cpc_field = rec.get('cpc')
    filing_date = rec.get('filing_date')
    year = extract_year(filing_date)
    if year is None:
        continue
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    # parse the cpc JSON-like string
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues: replace single quotes with double, or remove trailing commas
        try:
            fixed = cpc_field.replace("\"\"", '"')
            cpc_list = json.loads(fixed)
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for c in cpc_list:
        code = c.get('code') if isinstance(c, dict) else None
        if not code or not isinstance(code, str):
            continue
        group = code[:4]
        if group in level5_symbols:
            counts[group][year] += 1

# For each group, compute EMA across years sorted ascending with alpha=0.2
alpha = 0.2
best_years = {}
for group, year_counts in counts.items():
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
    # find year with highest EMA (if tie, pick latest year)
    max_ema = None
    max_year = None
    for y, e in ema_by_year.items():
        if max_ema is None or e > max_ema or (e == max_ema and y > max_year):
            max_ema = e
            max_year = y
    if max_year is not None:
        best_years[group] = max_year

# Filter groups whose best year is 2022
result = sorted([g for g, y in best_years.items() if y == 2022])

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_OLPprixqsT2cfw7tAI79YnQM': 'file_storage/call_OLPprixqsT2cfw7tAI79YnQM.json', 'var_call_caEXGpG58q827HVOTfKeijy3': 'file_storage/call_caEXGpG58q827HVOTfKeijy3.json'}

exec(code, env_args)
