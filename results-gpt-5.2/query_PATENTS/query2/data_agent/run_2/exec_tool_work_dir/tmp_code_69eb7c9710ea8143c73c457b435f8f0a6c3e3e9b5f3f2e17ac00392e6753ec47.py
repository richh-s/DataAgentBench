code = """import json, re, pandas as pd
from datetime import datetime

# load records from file if needed
path = var_call_yfmgTYsGCSf4u0WA7OJevGvX
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

months = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(text):
    if not text:
        return None
    m = re.search(r'(19|20)\\d{2}', text)
    return int(m.group(0)) if m else None

def parse_grant_month(text):
    if not text:
        return None
    for m,mi in months.items():
        if m in text:
            return mi
    return None

def extract_country(info):
    if not info:
        return None
    # pattern like 'The DK patent application' or 'Application ... from EP'
    m = re.search(r'The\\s+([A-Z]{2})\\s+patent application', info)
    if m:
        return m.group(1)
    m = re.search(r'Application .* from\\s+([A-Z]{2})', info)
    if m:
        return m.group(1)
    # sometimes 'In KR,'
    m = re.search(r'In\\s+([A-Z]{2})\\s*,', info)
    if m:
        return m.group(1)
    # sometimes contains 'number DE-'
    m = re.search(r'\bDE-\d', info)
    if m:
        return 'DE'
    return None

def parse_cpc_list(cpc_str):
    if not cpc_str:
        return []
    try:
        lst = json.loads(cpc_str)
        return [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
    except Exception:
        return []

def cpc_level4(code):
    # level 4 as class+subclass+main group (e.g., A61K 38)
    if not code:
        return None
    m = re.match(r'^([A-HY][0-9]{2}[A-Z])\s*(\d+)', code.replace(' ',''))
    if not m:
        return None
    return f"{m.group(1)}{m.group(2)}"  # no slash

rows=[]
for r in recs:
    gtext=r.get('grant_date')
    gy=parse_year(gtext)
    gm=parse_grant_month(gtext)
    if gy!=2019 or gm is None or gm<7:
        continue
    if extract_country(r.get('Patents_info'))!='DE':
        continue
    fy=parse_year(r.get('filing_date'))
    if fy is None:
        continue
    codes=parse_cpc_list(r.get('cpc'))
    lvl4=set(filter(None,(cpc_level4(c) for c in codes)))
    for c4 in lvl4:
        rows.append({'cpc4':c4,'filing_year':fy})

df=pd.DataFrame(rows)
if df.empty:
    out={'error':'No DE patents granted in H2 2019 found with parsable filing_year/CPC.'}
else:
    counts=df.groupby(['cpc4','filing_year']).size().reset_index(name='filings').sort_values(['cpc4','filing_year'])
    alpha=0.1
    res=[]
    for cpc4, g in counts.groupby('cpc4'):
        g=g.sort_values('filing_year')
        ema=None
        best_year=None
        best_ema=-1
        for _,row in g.iterrows():
            x=float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if ema>best_ema:
                best_ema=ema
                best_year=int(row['filing_year'])
        res.append({'cpc_group_code':cpc4,'best_year':best_year,'best_ema':best_ema})
    res_df=pd.DataFrame(res).sort_values(['best_ema','cpc_group_code'], ascending=[False,True])
    top=res_df.head(20)
    out=top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vZrDOLIHfW9dlOdw3MYzm4C2': ['publicationinfo'], 'var_call_jO4ZMQloc2z16UQOYwgNqPEk': ['cpc_definition'], 'var_call_UCf7Z4QIMTSExuLabWT4eoX8': [], 'var_call_raMtB9lmUWv0ZwZf1IcnvP6F': 'file_storage/call_raMtB9lmUWv0ZwZf1IcnvP6F.json', 'var_call_yfmgTYsGCSf4u0WA7OJevGvX': 'file_storage/call_yfmgTYsGCSf4u0WA7OJevGvX.json'}

exec(code, env_args)
