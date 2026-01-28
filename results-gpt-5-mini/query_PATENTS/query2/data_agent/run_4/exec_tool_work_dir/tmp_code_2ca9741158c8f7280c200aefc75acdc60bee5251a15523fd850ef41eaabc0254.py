code = """import json, re

# Load publication records
pub_path = var_call_T6EVN0wa6vXygggLELsEzSqf
if isinstance(pub_path, str):
    with open(pub_path, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = var_call_T6EVN0wa6vXygggLELsEzSqf

# Load CPC definitions
cpc_path = var_call_m1Hpssfn6VXXHXhXmjgyXmHg
if isinstance(cpc_path, str):
    with open(cpc_path, 'r', encoding='utf-8') as f:
        cpc_defs = json.load(f)
else:
    cpc_defs = var_call_m1Hpssfn6VXXHXhXmjgyXmHg

# Build symbol->title map for level-4 CPCs
level4_map = {row['symbol']: row.get('titleFull','') for row in cpc_defs}
level4_set = set(level4_map.keys())

# Helper to extract year from filing_date
year_re = re.compile(r"\b(19|20)\d{2}\b")

def extract_year(text):
    if not text:
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

# Build counts per group per year
from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))
years_set = set()

for rec in pubs:
    filing = rec.get('filing_date','')
    year = extract_year(filing)
    if not year:
        continue
    years_set.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field is JSON-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code')
        if not code or len(code) < 3:
            continue
        # normalize and take first 3 chars (letter + two digits)
        code_norm = code.replace(' ', '')
        group = code_norm[:3]
        if group in level4_set:
            counts[group][year] += 1

if not years_set:
    result = []
else:
    min_year = min(years_set)
    max_year = max(years_set)
    years = list(range(min_year, max_year+1))

    # Compute EMA per group
    alpha = 0.1
    results = []
    for group in sorted(counts.keys()):
        # build series across full year range
        series = [counts[group].get(y, 0) for y in years]
        # compute EMA
        ema_vals = []
        if series:
            ema = series[0]
            ema_vals.append(ema)
            for x in series[1:]:
                ema = alpha * x + (1 - alpha) * ema
                ema_vals.append(ema)
        # find year with max EMA
        if ema_vals:
            max_idx = max(range(len(ema_vals)), key=lambda i: ema_vals[i])
            best_year = years[max_idx]
            results.append({'symbol': group, 'titleFull': level4_map.get(group,''), 'best_year': best_year})
    result = results

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json'}

exec(code, env_args)
