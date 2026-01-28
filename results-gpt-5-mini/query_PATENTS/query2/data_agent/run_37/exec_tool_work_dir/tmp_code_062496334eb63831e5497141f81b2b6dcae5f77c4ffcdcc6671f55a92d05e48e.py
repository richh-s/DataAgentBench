code = """import json, re
from collections import defaultdict

# Load the large query result file path variable provided by previous query
path = var_call_C1mviJjloTwFfejDEpxwxHRn
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

alpha = 0.1

# helper to extract year
year_re = re.compile(r'(19|20)\d{2}')
country_re = re.compile(r'\bDE\b|Germany|German', re.IGNORECASE)

# aggregate counts per level4 code per filing year for Germany
counts = defaultdict(lambda: defaultdict(int))

for r in records:
    info = r.get('Patents_info','') or ''
    if not country_re.search(info):
        continue
    filing = r.get('filing_date','') or ''
    m = year_re.search(filing)
    if not m:
        # try grant_date as fallback
        gd = r.get('grant_date','') or ''
        m = year_re.search(gd)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = r.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # skip if parsing fails
        continue
    for item in cpcs:
        code = item.get('code')
        if not code:
            continue
        code = code.strip()
        # level 4 = first 4 characters (e.g., A61B)
        level4 = code[:4]
        counts[level4][year] += 1

# compute EMA per group
result = []
level4_list = []
for level4, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find best year = year with highest ema
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    best_ema = ema_by_year[best_year]
    result.append({
        'level4': level4,
        'counts': dict(sorted(year_counts.items())),
        'ema': {str(k): v for k, v in sorted(ema_by_year.items())},
        'best_year': int(best_year),
        'best_ema': float(best_ema)
    })
    level4_list.append(level4)

output = {'groups': result, 'level4_list': sorted(list(set(level4_list)))}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_EG3jYgEy7mbMHgDYp7xJmNPY': 'file_storage/call_EG3jYgEy7mbMHgDYp7xJmNPY.json', 'var_call_C1mviJjloTwFfejDEpxwxHRn': 'file_storage/call_C1mviJjloTwFfejDEpxwxHRn.json'}

exec(code, env_args)
