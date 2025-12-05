code = """import json, re, pandas as pd

# Load publication data
path = var_call_iAwRHFnOxEckZmShIBh3Qok2
with open(path, 'r') as f:
    pubs = json.load(f)

# Filter for Germany using Patents_info country code 'DE-'
pat_de = re.compile(r'\bDE-')
pubs_de = [r for r in pubs if pat_de.search(r.get('Patents_info',''))]

# Parse grant year and build yearly counts per CPC code (full code string)
month_map = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)|((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*)', date_str)
    y = re.search(r'(19|20)\d{2}', date_str)
    if not y:
        return None
    return int(y.group(0))

records = []
for r in pubs_de:
    year = extract_year(r.get('grant_date',''))
    if year is None:
        continue
    cpc_raw = r.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    codes = {c.get('code') for c in cpc_list if c.get('code')}
    for code in codes:
        # Derive level-4 group as first 3 characters (section+class) for lack of better mapping
        lvl4 = code[:3]
        records.append({'year': year, 'cpc_group4': lvl4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # yearly counts per group
    counts = df.groupby(['cpc_group4','year']).size().reset_index(name='count')
    # ensure continuous years per group
    out_rows = []
    alpha = 0.1
    for grp, g in counts.groupby('cpc_group4'):
        years = list(range(g['year'].min(), g['year'].max()+1))
        year_counts = {int(y): int(c) for y,c in zip(g['year'], g['count'])}
        ema = None
        for y in years:
            c = year_counts.get(y, 0)
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            out_rows.append({'cpc_group4': grp, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(out_rows)
    # for each group, pick year with max EMA
    idx = ema_df.groupby('cpc_group4')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iAwRHFnOxEckZmShIBh3Qok2': 'file_storage/call_iAwRHFnOxEckZmShIBh3Qok2.json', 'var_call_w1JXhL7giUTxZf7AYH8jwBdg': 'file_storage/call_w1JXhL7giUTxZf7AYH8jwBdg.json'}

exec(code, env_args)
