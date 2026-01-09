code = """import json, re, pandas as pd
from datetime import datetime

# load records
src = var_call_9OEKmGKMvbRnEjWC0oxH2Mwi
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

month_map = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not date_str: return None
    m = re.search(r'(19|20)\\d{2}', date_str)
    return int(m.group(0)) if m else None

def parse_month(date_str):
    if not date_str: return None
    for mn in month_map:
        if mn in date_str:
            return month_map[mn]
    return None

def country_from_info(info):
    if not info: return None
    m = re.search(r'The\\s+([A-Z]{2})\\s+patent application', info)
    if m: return m.group(1)
    m = re.search(r'^In\\s+([A-Z]{2}),', info)
    if m: return m.group(1)
    m = re.search(r'Application.*?from\\s+([A-Z]{2})', info)
    if m: return m.group(1)
    return None

def cpc_level4(code):
    # group at level 4 approximated as main group: e.g., A01B 1/00 => A01B1/00 ; F25B2339/047 => F25B2339/00
    if not code: return None
    code = code.strip()
    if '/' in code:
        left,right = code.split('/',1)
        return left + '/' + (right[:2] if len(right)>=2 else right).ljust(2,'0')
    return code

rows=[]
for r in recs:
    ctry = country_from_info(r.get('Patents_info'))
    if ctry != 'DE':
        continue
    gy = parse_year(r.get('grant_date'))
    gm = parse_month(r.get('grant_date'))
    if gy != 2019 or gm is None or gm < 7:
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    try:
        cpcs = json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs=[]
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lv4 = cpc_level4(code)
        if lv4:
            rows.append({'rowid': r.get('rowid'), 'filing_year': fy, 'cpc4': lv4})

df = pd.DataFrame(rows).drop_duplicates(subset=['rowid','cpc4'])
# counts per year per cpc4
ct = df.groupby(['cpc4','filing_year']).size().reset_index(name='n')

# compute EMA with alpha=0.1 per cpc4 across years from min to max (fill missing years with 0)
alpha=0.1
out=[]
for cpc4, g in ct.groupby('cpc4'):
    g = g.sort_values('filing_year')
    years = list(range(int(g.filing_year.min()), int(g.filing_year.max())+1))
    m = {int(y):int(n) for y,n in zip(g.filing_year, g.n)}
    ema=None
    for y in years:
        x = m.get(y,0)
        if ema is None:
            ema = x
        else:
            ema = alpha*x + (1-alpha)*ema
        out.append({'cpc4':cpc4,'year':y,'ema':float(ema)})

ema_df = pd.DataFrame(out)
# best year and max ema
best = ema_df.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').head(1)

# choose cpc groups with highest max ema overall
best_sorted = best.sort_values('ema', ascending=False)
# keep all tied for top? We'll return all groups with highest ema value
if len(best_sorted)==0:
    top=[]
else:
    top_ema = best_sorted.iloc[0].ema
    top = best_sorted[best_sorted.ema==top_ema]

res = top[['cpc4','year','ema']].rename(columns={'year':'best_year','ema':'best_year_ema'}).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_lX9bn6RInmeIFW0tKsKase89': ['publicationinfo'], 'var_call_4A65hqzVN8KwE4FDnsPiJwSB': ['cpc_definition'], 'var_call_9OEKmGKMvbRnEjWC0oxH2Mwi': 'file_storage/call_9OEKmGKMvbRnEjWC0oxH2Mwi.json'}

exec(code, env_args)
