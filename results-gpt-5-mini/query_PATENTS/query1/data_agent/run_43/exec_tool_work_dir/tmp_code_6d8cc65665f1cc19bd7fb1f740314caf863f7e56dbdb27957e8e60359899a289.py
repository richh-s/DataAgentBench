code = """import json
import pandas as pd
import re

# Load data from previous query results stored as files
pub_path = var_call_20WdpNZEVpgoOoPy60v5OVQ4
lvl5_path = var_call_ysvsKOBXxfGeTodHnN7eYfB2

with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

with open(lvl5_path, 'r', encoding='utf-8') as f:
    lvl5_rows = json.load(f)

lvl5_symbols = set(r.get('symbol') for r in lvl5_rows if r.get('symbol'))

rows = []
year_pattern = re.compile(r'(19|20)\d{2}')
code_pattern = re.compile(r'"code"\s*:\s*"([^"]+)"')

for rec in pubs:
    filing = rec.get('filing_date')
    cpc_field = rec.get('cpc')
    if not filing or not cpc_field:
        continue
    y_match = year_pattern.search(filing)
    if not y_match:
        continue
    year = int(y_match.group(0))
    # try parsing cpc field as json
    codes = []
    try:
        parsed = json.loads(cpc_field)
        for item in parsed:
            code = item.get('code')
            if code:
                codes.append(code)
    except Exception:
        # fallback: regex
        for m in code_pattern.finditer(cpc_field):
            codes.append(m.group(1))
    for code in codes:
        code = code.strip()
        if len(code) < 4:
            continue
        group = code[:4].upper()
        if group in lvl5_symbols:
            rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # count filings per group per year
    counts = df.groupby(['group', 'year']).size().reset_index(name='count')
    # full year range
    min_year = int(counts['year'].min())
    max_year = int(counts['year'].max())
    years = list(range(min_year, max_year+1))

    alpha = 0.2
    group_best_year = {}

    for group, gdf in counts.groupby('group'):
        # build series across years
        year_counts = {int(r['year']): int(r['count']) for _, r in gdf.iterrows()}
        ema = None
        ema_by_year = {}
        for y in years:
            cnt = year_counts.get(y, 0)
            if ema is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1 - alpha) * ema
            ema_by_year[y] = ema
        # find year where ema is max
        best_year = max(ema_by_year.items(), key=lambda x: (x[1], -x[0]))[0]
        group_best_year[group] = {'best_year': best_year, 'ema_by_year': ema_by_year}

    # select groups whose best_year == 2022
    result = sorted([g for g, v in group_best_year.items() if v['best_year'] == 2022])

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_Dg4yvPtc3wgSzHICI4ee8p4z': [], 'var_call_ysvsKOBXxfGeTodHnN7eYfB2': 'file_storage/call_ysvsKOBXxfGeTodHnN7eYfB2.json', 'var_call_20WdpNZEVpgoOoPy60v5OVQ4': 'file_storage/call_20WdpNZEVpgoOoPy60v5OVQ4.json'}

exec(code, env_args)
