code = """import json
import pandas as pd

# Load files
with open(var_call_DC5goInbH4wtr4Tyj3ekeUna, 'r', encoding='utf-8') as f:
    level5_data = json.load(f)
with open(var_call_GFynDXJBCT7UezxVAXkKIhAo, 'r', encoding='utf-8') as f:
    pub_data = json.load(f)

# Build set of level-5 symbols
level5_symbols = set()
for r in level5_data:
    s = r.get('symbol')
    if s:
        level5_symbols.add(s.strip().upper())

# helper to find a year in a text: look for any 4-digit substring starting with 19 or 20
def extract_year(text):
    if not isinstance(text, str):
        return None
    L = len(text)
    for i in range(L-3):
        part = text[i:i+4]
        if (part.startswith('19') or part.startswith('20')) and part.isdigit():
            return int(part)
    return None

counts = {}
min_year = 9999
max_year = 0

for rec in pub_data:
    fd = rec.get('filing_date') or ''
    year = extract_year(fd)
    if year is None:
        continue
    if year < min_year:
        min_year = year
    if year > max_year:
        max_year = year
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # parse cpc JSON
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace(chr(10), ''))
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
        # group is first 4 chars like A01B
        if len(code) >= 4:
            group = code[:4]
        else:
            continue
        if (group[0].isalpha() and group[1].isdigit() and group[2].isdigit() and group[3].isalpha()):
            pass
        else:
            # fall back to first 4 chars anyway
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
