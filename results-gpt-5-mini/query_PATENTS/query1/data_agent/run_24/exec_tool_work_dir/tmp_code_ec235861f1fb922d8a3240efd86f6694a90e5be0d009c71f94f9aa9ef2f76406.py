code = """import json, re, pandas as pd

# Load data from provided storage file paths
with open(var_call_DC5goInbH4wtr4Tyj3ekeUna, 'r', encoding='utf-8') as f:
    level5_data = json.load(f)
with open(var_call_GFynDXJBCT7UezxVAXkKIhAo, 'r', encoding='utf-8') as f:
    pub_data = json.load(f)

level5_symbols = set()
for r in level5_data:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Helper to extract year
year_re = re.compile(r'(19|20)\d{2}')
# Helper to extract group code (first 4 chars like A01B)
group_re = re.compile(r'^([A-Z]\d{2}[A-Z])')

counts = {}
min_year = 9999
max_year = 0
for rec in pub_data:
    fd = rec.get('filing_date') or ''
    m = year_re.search(fd)
    if not m:
        continue
    year = int(m.group(0))
    if year < min_year: min_year = year
    if year > max_year: max_year = year
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\n", ""))
        except Exception:
            continue
    for item in cpcs:
        code = item.get('code') if isinstance(item, dict) else None
        if not code:
            continue
        code = code.strip().upper()
        m2 = group_re.match(code)
        if m2:
            group = m2.group(1)
        else:
            group = code[:4]
        if group in level5_symbols:
            counts[(group, year)] = counts.get((group, year), 0) + 1

# Build DataFrame
rows = []
for (group, year), cnt in counts.items():
    rows.append({'group': group, 'year': year, 'count': cnt})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Ensure all groups have entries for all years between global min and max
    all_groups = df['group'].unique().tolist()
    years = list(range(min_year, max_year+1))
    full_rows = []
    for g in all_groups:
        for y in years:
            c = int(df[(df['group']==g)&(df['year']==y)]['count'].sum())
            full_rows.append({'group': g, 'year': y, 'count': c})
    full_df = pd.DataFrame(full_rows)
    results = []
    alpha = 0.2
    for g in all_groups:
        ser = full_df[full_df['group']==g].sort_values('year')
        counts_series = ser['count'].astype(float).reset_index(drop=True)
        # compute EMA with pandas
        ema = counts_series.ewm(alpha=alpha, adjust=False).mean()
        ser = ser.reset_index(drop=True)
        ser['ema'] = ema
        # find year with max ema
        idx = ser['ema'].idxmax()
        best_year = int(ser.loc[idx, 'year'])
        best_ema = float(ser.loc[idx, 'ema'])
        results.append({'group': g, 'best_year': best_year, 'best_ema': best_ema})
    # select groups whose best_year is 2022
    selected = [r['group'] for r in results if r['best_year']==2022]
    selected = sorted(selected)
    result = selected

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DC5goInbH4wtr4Tyj3ekeUna': 'file_storage/call_DC5goInbH4wtr4Tyj3ekeUna.json', 'var_call_GFynDXJBCT7UezxVAXkKIhAo': 'file_storage/call_GFynDXJBCT7UezxVAXkKIhAo.json'}

exec(code, env_args)
