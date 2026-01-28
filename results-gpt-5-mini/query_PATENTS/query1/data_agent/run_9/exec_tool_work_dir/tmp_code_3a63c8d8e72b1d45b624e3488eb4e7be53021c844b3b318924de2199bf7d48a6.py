code = """import json, re
from collections import defaultdict

# Load publication filing data
path_pub = var_call_hBfothRiKjoGpWtxJ06WoEhS
if isinstance(path_pub, str):
    with open(path_pub, 'r', encoding='utf-8') as f:
        pub_records = json.load(f)
else:
    pub_records = var_call_hBfothRiKjoGpWtxJ06WoEhS

# Load level-5 CPC symbols
path_cpc = var_call_Y86WtWrYxxe4UMu5nTKB7VZs
if isinstance(path_cpc, str):
    with open(path_cpc, 'r', encoding='utf-8') as f:
        cpc_records = json.load(f)
else:
    cpc_records = var_call_Y86WtWrYxxe4UMu5nTKB7VZs

level5_symbols = [r.get('symbol') for r in cpc_records if 'symbol' in r]
# Sort symbols by length desc to match longest prefix first
level5_symbols_sorted = sorted(level5_symbols, key=lambda s: -len(s))

# Regex to extract year
year_re = re.compile(r"\b(19|20)\d{2}\b")

# Count occurrences per symbol per year
counts = defaultdict(lambda: defaultdict(int))

for rec in pub_records:
    filing_date = rec.get('filing_date')
    if not filing_date:
        continue
    m = year_re.search(filing_date)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # parse cpc field which is JSON-like
    parsed = None
    try:
        parsed = json.loads(cpc_field)
    except Exception:
        try:
            import ast
            parsed = ast.literal_eval(cpc_field)
        except Exception:
            parsed = None
    if not parsed:
        continue
    for item in parsed:
        # item might be dict with 'code'
        code = None
        if isinstance(item, dict):
            code = item.get('code')
        elif isinstance(item, str):
            code = item
        if not code or not isinstance(code, str):
            continue
        # find best matching level5 symbol
        match = None
        for s in level5_symbols_sorted:
            if code.startswith(s):
                match = s
                break
        if match:
            counts[match][year] += 1

# Compute EMA per symbol per year with alpha=0.2
alpha = 0.2
best_year_by_symbol = {}

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
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
    if not ema_by_year:
        continue
    # if multiple years have same EMA, choose the latest year
    max_ema = max(ema_by_year.values())
    # get years with max_ema
    candidate_years = [y for y, v in ema_by_year.items() if v == max_ema]
    best_year = max(candidate_years)
    best_year_by_symbol[sym] = best_year

# Select symbols whose best year is 2022
result_symbols = sorted([s for s, y in best_year_by_symbol.items() if y == 2022])

import json
print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_call_YETBLr7P9i7F0gSOavpaS1AB': 'file_storage/call_YETBLr7P9i7F0gSOavpaS1AB.json', 'var_call_hBfothRiKjoGpWtxJ06WoEhS': 'file_storage/call_hBfothRiKjoGpWtxJ06WoEhS.json', 'var_call_Y86WtWrYxxe4UMu5nTKB7VZs': 'file_storage/call_Y86WtWrYxxe4UMu5nTKB7VZs.json'}

exec(code, env_args)
