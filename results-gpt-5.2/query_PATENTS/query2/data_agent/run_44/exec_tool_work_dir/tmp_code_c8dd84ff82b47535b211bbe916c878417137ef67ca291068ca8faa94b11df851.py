code = """import json, re
from datetime import datetime
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

recs = load_records(var_call_zjFBClOwm2DRLmM4t3iplz5m)

months_h2 = {'july','august','september','october','november','december'}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def in_h2_2019(grant_date):
    if not grant_date:
        return False
    s = grant_date.lower()
    if '2019' not in s:
        return False
    return any(mon in s for mon in months_h2)

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        arr = json.loads(cpc_field)
        codes = [o.get('code') for o in arr if isinstance(o, dict) and o.get('code')]
        return codes
    except Exception:
        return []

def level4(code):
    # normalize: remove spaces
    code = code.strip()
    # level-4 as class+subclass+main group number (before '/')
    if '/' in code:
        pre = code.split('/')[0]
    else:
        pre = code
    return pre

rows=[]
for r in recs:
    if not in_h2_2019(r.get('grant_date')):
        continue
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    for c in codes:
        rows.append({'year': y, 'cpc4': level4(c)})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    # count filings per year per cpc4
    cnt = df.groupby(['cpc4','year']).size().reset_index(name='n').sort_values(['cpc4','year'])
    alpha = 0.1
    # compute EMA per group
    def ema_group(g):
        g = g.sort_values('year').copy()
        ema=[]
        prev=None
        for v in g['n'].tolist():
            if prev is None:
                prev = v
            else:
                prev = alpha*v + (1-alpha)*prev
            ema.append(prev)
        g['ema'] = ema
        return g
    ema = cnt.groupby('cpc4', group_keys=False).apply(ema_group)
    # best year per cpc4 (max ema)
    best = ema.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').head(1)
    # among cpc4 choose those with highest ema per best year? interpret as overall highest per year? We'll return ranked list by ema desc
    best = best.sort_values('ema', ascending=False)
    out = best[['cpc4','year','ema']].rename(columns={'cpc4':'cpc_group_code','year':'best_year','ema':'best_year_ema'}).to_dict('records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_aSG8ybRCb4ixYiNVq3wbRnuz': ['publicationinfo'], 'var_call_3h3AEY3yILY4iZor7rW05LOe': ['cpc_definition'], 'var_call_QuYk8va0hnKk9YfK9cVqdFoX': [], 'var_call_RVrtZnIpq649ZJLOK9RTrNTv': 'file_storage/call_RVrtZnIpq649ZJLOK9RTrNTv.json', 'var_call_BPXLwcnU61nKeB0pEzHgTk8V': 'file_storage/call_BPXLwcnU61nKeB0pEzHgTk8V.json', 'var_call_zjFBClOwm2DRLmM4t3iplz5m': 'file_storage/call_zjFBClOwm2DRLmM4t3iplz5m.json'}

exec(code, env_args)
