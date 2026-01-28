code = """import json
import re
from collections import defaultdict

# Load the large query result from publication_database
with open(var_call_2KWjt8JKvALQF3B1Xrp7spAo, 'r') as f:
    records = json.load(f)

# Filter for Germany and grant_date in Jul-Dec 2019
months_h2 = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

def is_germany(pi):
    if not pi:
        return False
    return re.search(r'\bDE\b', pi) is not None

filtered = []
for r in records:
    gd = (r.get('grant_date') or '').lower()
    if '2019' not in gd:
        continue
    if not any(m in gd for m in months_h2):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    filtered.append(r)

# Build counts per CPC level-4 group per filing year (unique family_id counted once per group-year)
group_year_family = defaultdict(lambda: defaultdict(set))

for r in filtered:
    fam = r.get('family_id')
    filing = r.get('filing_date') or ''
    m = re.search(r'(20\d{2}|19\d{2})', filing)
    if not m:
        continue
    year = int(m.group(1))
    cpc_field = r.get('cpc') or ''
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpc_fixed = cpc_field.replace("'", '"')
            cpcs = json.loads(cpc_fixed)
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or len(code) < 4:
            continue
        group = code[:4]
        group_year_family[group][year].add(fam)

# Convert to counts time series and compute EMA (alpha=0.1)
alpha = 0.1
results = []
for group, year_map in group_year_family.items():
    years = sorted(year_map.keys())
    if not years:
        continue
    counts = [len(year_map[y]) for y in years]
    # compute EMA series
    ema_values = []
    ema_prev = counts[0]
    ema_values.append(ema_prev)
    for x in counts[1:]:
        ema_curr = alpha * x + (1 - alpha) * ema_prev
        ema_values.append(ema_curr)
        ema_prev = ema_curr
    # find year with highest EMA
    best_idx = max(range(len(years)), key=lambda i: ema_values[i])
    results.append({
        'group_code': group,
        'years': years,
        'counts': counts,
        'ema_series': [round(v,6) for v in ema_values],
        'best_year': years[best_idx],
        'best_ema': round(ema_values[best_idx],6)
    })

# Prepare list of group codes for lookup
group_codes = sorted(list({r['group_code'] for r in results}))

out = {
    'groups': results,
    'group_codes': group_codes
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2KWjt8JKvALQF3B1Xrp7spAo': 'file_storage/call_2KWjt8JKvALQF3B1Xrp7spAo.json'}

exec(code, env_args)
