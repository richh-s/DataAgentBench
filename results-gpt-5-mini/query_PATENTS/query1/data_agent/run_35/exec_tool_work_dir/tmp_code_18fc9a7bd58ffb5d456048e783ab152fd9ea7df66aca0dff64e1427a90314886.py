code = """import json
import re
from collections import defaultdict

# Load data from storage-provided file paths
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

# Year extraction
year_re = re.compile(r"(19|20)\d{2}")
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
        # attempt a simple fix: replace single quotes with double quotes
        try:
            fixed = cpc_field.replace("'", '"')
            cpc_list = json.loads(fixed)
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for c in cpc_list:
        if not isinstance(c, dict):
            continue
        code = c.get('code')
        if not code or not isinstance(code, str):
            continue
        group = code[:4]
        if group in level5_symbols:
            counts[group][year] += 1

# Compute EMA with alpha=0.2 per group over sorted years
alpha = 0.2
best_years = {}
for group, yc in counts.items():
    years = sorted(yc.keys())
    ema = None
    ema_by_year = {}
    for y in years:
        c = yc[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA, tie-breaker latest year
    max_e = None
    max_y = None
    for y, e in ema_by_year.items():
        if max_e is None or e > max_e or (e == max_e and y > max_y):
            max_e = e
            max_y = y
    if max_y is not None:
        best_years[group] = max_y

# Filter groups where best year is 2022
result = sorted([g for g, y in best_years.items() if y == 2022])

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OLPprixqsT2cfw7tAI79YnQM': 'file_storage/call_OLPprixqsT2cfw7tAI79YnQM.json', 'var_call_caEXGpG58q827HVOTfKeijy3': 'file_storage/call_caEXGpG58q827HVOTfKeijy3.json'}

exec(code, env_args)
