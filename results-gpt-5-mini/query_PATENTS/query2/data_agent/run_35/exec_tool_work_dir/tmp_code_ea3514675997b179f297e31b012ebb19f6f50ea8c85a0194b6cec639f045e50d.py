code = """import json, re
# Load data from previous tool results
with open(var_call_uX35j8swiDeRTrhkqYrZ3t7S, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_7yMwBGdeJJXK2ZKHMVmTmgWn, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level-4 map symbol -> titleFull
cpc_map = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Aggregate counts per group (level-4 symbol) per filing year
from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))  # counts[group][year] = count

for rec in pubs:
    # Ensure grant_date in second half 2019
    gd = rec.get('grant_date','')
    if '2019' not in gd:
        continue
    if not any(m in gd for m in ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']):
        continue
    # Extract filing year
    fd = rec.get('filing_date','')
    m = re.search(r'(20\d{2}|19\d{2})', fd)
    if not m:
        # try grant_date as fallback
        m = re.search(r'(20\d{2}|19\d{2})', gd)
    if not m:
        continue
    year = int(m.group(1))
    # Parse CPC field
    cpc_field = rec.get('cpc','')
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'","\""))
        except Exception:
            continue
    for entry in cpcs:
        code = entry.get('code')
        if not code:
            continue
        # Extract level-4 symbol (letter + two digits)
        m2 = re.match(r'^([A-Z]\d{2})', code)
        if not m2:
            # try first 3 chars
            group = code[:3]
        else:
            group = m2.group(1)
        if group in cpc_map:
            counts[group][year] += 1

# For each group compute EMA across years with alpha=0.1
alpha = 0.1
results = []
for group, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        cnt = year_counts.get(y,0)
        if ema is None:
            ema = float(cnt)
        else:
            ema = alpha * cnt + (1-alpha) * ema
        ema_by_year[y] = ema
    # Find best year by EMA
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    results.append({
        'symbol': group,
        'titleFull': cpc_map.get(group,'') ,
        'best_year': int(best_year),
        'best_ema': round(float(best_ema),3),
        'years_considered': len(years)
    })

# Sort by best_ema descending and take top 10
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)
top_results = results_sorted[:10]

import json
print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_call_VrLjYDKCzlPz4wvziBWhrxsY': 'file_storage/call_VrLjYDKCzlPz4wvziBWhrxsY.json', 'var_call_uX35j8swiDeRTrhkqYrZ3t7S': 'file_storage/call_uX35j8swiDeRTrhkqYrZ3t7S.json', 'var_call_H43HOmSBNUjo7iHO18cuHoOk': 'file_storage/call_H43HOmSBNUjo7iHO18cuHoOk.json', 'var_call_7yMwBGdeJJXK2ZKHMVmTmgWn': 'file_storage/call_7yMwBGdeJJXK2ZKHMVmTmgWn.json'}

exec(code, env_args)
