code = """import json, re
import pandas as pd

# Load publication records (may be a path)
pubs = var_call_7mftjHcZkwaIbi8yRMnZoe9p
if isinstance(pubs, str):
    with open(pubs, 'r', encoding='utf-8') as f:
        pubs = json.load(f)

cpc_defs = var_call_0SeCxnWIdKksFb7R3RiJXVEI

# Helpers
month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_month(s):
    if not s: return None
    s2 = s.lower()
    for name,num in month_map.items():
        if name in s2:
            return num
    return None

def is_grant_in_h2_2019(s):
    y = parse_year(s)
    if y != 2019: return False
    mo = parse_month(s)
    return mo is not None and 7 <= mo <= 12

def extract_country_code(pi):
    if not pi: return None
    m = re.search(r'country_code\s*"?\s*:?\s*([A-Z]{2})', pi)
    if m: return m.group(1)
    # fallback: look for 'In <CC>,'
    m = re.search(r'\bIn\s+([A-Z]{2})\b', pi)
    if m: return m.group(1)
    return None

def parse_cpc_list(cpc_str):
    if not cpc_str: return []
    try:
        lst = json.loads(cpc_str)
        codes = []
        for x in lst:
            code = x.get('code') if isinstance(x, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        return []

def to_level4(code):
    # CPC group at level 4 ~ subclass + main group: e.g., H01M10/00
    m = re.match(r'^([A-HY]\d{2}[A-Z])\s*(\d+)/(\d+)$', code.replace(' ',''))
    if not m:
        return None
    subclass = m.group(1)
    main = m.group(2)
    return f"{subclass}{main}/00"

# Build counts per year per level4 CPC for Germany, for patents granted H2 2019
rows = []
for r in pubs:
    if not is_grant_in_h2_2019(r.get('grant_date')):
        continue
    if extract_country_code(r.get('Patents_info')) != 'DE':
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    codes = parse_cpc_list(r.get('cpc'))
    lvl4 = {to_level4(c) for c in codes}
    lvl4.discard(None)
    for c4 in lvl4:
        rows.append({'cpc4': c4, 'year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = []
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

counts = df.groupby(['cpc4','year']).size().reset_index(name='filings')

# Compute EMA per cpc4 over years
alpha = 0.1
result_rows = []
for cpc4, g in counts.groupby('cpc4'):
    g2 = g.sort_values('year')
    ema = None
    for _, row in g2.iterrows():
        x = float(row['filings'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        result_rows.append({'cpc4': cpc4, 'year': int(row['year']), 'ema': float(ema)})

ema_df = pd.DataFrame(result_rows)
# Best year (highest EMA) per cpc4
best = ema_df.sort_values(['cpc4','ema','year'], ascending=[True,False,False]).groupby('cpc4').head(1)

# Determine highest EMA each year across CPC groups
best_each_year = ema_df.sort_values(['year','ema'], ascending=[True,False]).groupby('year').head(1)

# CPC titles: cpc_defs came empty; return without titles
best_each_year = best_each_year.merge(best[['cpc4','year']].rename(columns={'year':'best_year'}), on='cpc4', how='left')

out = best_each_year.sort_values('year').to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7mftjHcZkwaIbi8yRMnZoe9p': 'file_storage/call_7mftjHcZkwaIbi8yRMnZoe9p.json', 'var_call_0SeCxnWIdKksFb7R3RiJXVEI': []}

exec(code, env_args)
