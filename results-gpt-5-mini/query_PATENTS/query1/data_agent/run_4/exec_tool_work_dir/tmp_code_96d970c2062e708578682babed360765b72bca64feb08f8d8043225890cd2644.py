code = """import json, re, collections

# Load the large query results from files provided in storage variables
with open(var_call_HeFAsblEstgEkHuqI2gk7FJK, 'r', encoding='utf-8') as f:
    records = json.load(f)

with open(var_call_4EwcyWmAo7FAt6AHsQfuPI3h, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)

level5_set = set([r['symbol'].upper() for r in level5_list if 'symbol' in r])

# Count occurrences per level5 group and year
counts = collections.Counter()
all_years = set()
for rec in records:
    pubdate = rec.get('publication_date') or ''
    m = re.search(r'(\d{4})', pubdate)
    if not m:
        continue
    year = m.group(1)
    all_years.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpc_entries = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpc_entries = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpc_entries, list):
        continue
    for entry in cpc_entries:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or len(code) < 4:
            continue
        group = code[:4].upper()
        # only consider groups that are in the level5 definition list
        if group in level5_set:
            counts[(group, year)] += 1

if not counts:
    result = []
else:
    years_sorted = sorted(all_years)

    # Build per-group time series and compute EMA with alpha=0.2
    alpha = 0.2
    group_year_ema = {}  # group -> {year: ema}
    groups = sorted({g for (g,y) in counts.keys()})
    for g in groups:
        # ensure all years in chronological order
        series = [counts.get((g, y), 0) for y in years_sorted]
        emas = []
        if series:
            ema_prev = series[0]
            emas.append(ema_prev)
            for x in series[1:]:
                ema = alpha * x + (1 - alpha) * ema_prev
                emas.append(ema)
                ema_prev = ema
        # map years to emas
        group_year_ema[g] = {year: float(emas[i]) for i, year in enumerate(years_sorted)}

    # For each group, find the year with maximum EMA
    result_groups = []
    for g, ym in group_year_ema.items():
        # find year(s) with max ema
        max_year = max(ym.items(), key=lambda kv: (kv[1], kv[0]))[0]
        if max_year == '2022':
            result_groups.append(g)

    result = sorted(result_groups)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HeFAsblEstgEkHuqI2gk7FJK': 'file_storage/call_HeFAsblEstgEkHuqI2gk7FJK.json', 'var_call_4EwcyWmAo7FAt6AHsQfuPI3h': 'file_storage/call_4EwcyWmAo7FAt6AHsQfuPI3h.json'}

exec(code, env_args)
