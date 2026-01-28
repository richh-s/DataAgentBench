code = """import json, re, pandas as pd

# Load data from storage file paths
path_level5 = var_call_DC5goInbH4wtr4Tyj3ekeUna
path_pub = var_call_GFynDXJBCT7UezxVAXkKIhAo
with open(path_level5, 'r', encoding='utf-8') as f:
    level5_data = json.load(f)
with open(path_pub, 'r', encoding='utf-8') as f:
    pub_data = json.load(f)

# Build set of level-5 symbols
level5_symbols = set()
for r in level5_data:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip().upper())

# Regex patterns
year_re = re.compile(r"(19|20)\d{2}")
group_re = re.compile(r"^([A-Z]\d{2}[A-Z])")

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
    # parse cpc JSON string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace('\n',''))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for item in cpcs:
        if isinstance(item, dict):
            code = item.get('code')
        else:
            code = None
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

rows = []
for (g,y),cnt in counts.items():
    rows.append({'group': g, 'year': int(y), 'count': int(cnt)})

selected = []
if rows:
    df = pd.DataFrame(rows)
    all_groups = sorted(df['group'].unique())
    years = list(range(min_year, max_year+1))
    full_rows = []
    for g in all_groups:
        for y in years:
            c = int(df[(df['group']==g)&(df['year']==y)]['count'].sum())
            full_rows.append({'group': g, 'year': int(y), 'count': c})
    full_df = pd.DataFrame(full_rows)
    alpha = 0.2
    for g in all_groups:
        ser = full_df[full_df['group']==g].sort_values('year')
        counts_series = ser['count'].astype(float).reset_index(drop=True)
        ema = counts_series.ewm(alpha=alpha, adjust=False).mean()
        ser = ser.reset_index(drop=True)
        ser['ema'] = ema
        idx = ser['ema'].idxmax()
        best_year = int(ser.loc[idx, 'year'])
        if best_year == 2022:
            selected.append(g)

selected = sorted(selected)
print("__RESULT__:")
print(json.dumps(selected))"""

env_args = {'var_call_DC5goInbH4wtr4Tyj3ekeUna': 'file_storage/call_DC5goInbH4wtr4Tyj3ekeUna.json', 'var_call_GFynDXJBCT7UezxVAXkKIhAo': 'file_storage/call_GFynDXJBCT7UezxVAXkKIhAo.json', 'var_call_UmhGy9Sr0LmqG1hbvew6OqLC': {'level5_count': 677, 'pub_count': 277813}}

exec(code, env_args)
