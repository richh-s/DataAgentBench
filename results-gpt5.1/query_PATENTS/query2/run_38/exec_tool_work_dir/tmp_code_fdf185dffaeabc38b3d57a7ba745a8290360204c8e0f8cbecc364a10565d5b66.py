code = """import json, re, pandas as pd, datetime
from dateutil import parser

# Load full publication data
path = var_call_VEJyxYN9tihKIjqlkpulOd5s
with open(path, 'r') as f:
    pubs = json.load(f)

# Filter German patents and parse grant_date
country_re = re.compile(r'\bDE[- ]|\bGermany\b|country_code\s*[:=]\s*DE')

def parse_date(text):
    if not text:
        return None
    try:
        return parser.parse(text, dayfirst=True, fuzzy=True)
    except Exception:
        return None

records = []
for row in pubs:
    info = row.get('Patents_info','') or ''
    if not country_re.search(info):
        continue
    gd = parse_date(row.get('grant_date'))
    if not gd or not (gd.year == 2019 and gd.month >= 7 and gd.month <= 12):
        continue
    cpc_raw = row.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        records.append({'year': gd.year, 'cpc_code': code})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # get yearly counts per CPC
    counts = df.groupby(['cpc_code','year']).size().reset_index(name='count')

    # Build full year range for EMA (we only have 2019 data, so EMA will be that year only)
    # Still, we can technically compute EMA over available years per group
    ema_rows = []
    alpha = 0.1
    for code, grp in counts.groupby('cpc_code'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            y, c = r['year'], r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'cpc_code': code, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)
    # best year per CPC
    idx = ema_df.groupby('cpc_code')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VEJyxYN9tihKIjqlkpulOd5s': 'file_storage/call_VEJyxYN9tihKIjqlkpulOd5s.json', 'var_call_tMBhGrJYDfK68X0BDKX1NMV1': 'file_storage/call_tMBhGrJYDfK68X0BDKX1NMV1.json'}

exec(code, env_args)
