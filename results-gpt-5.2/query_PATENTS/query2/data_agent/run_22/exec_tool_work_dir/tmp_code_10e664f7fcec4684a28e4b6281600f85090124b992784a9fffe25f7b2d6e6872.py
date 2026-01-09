code = """import json, re, pandas as pd
from datetime import datetime

# load records
path = var_call_TBZM4GbiRKvHit3ronCTbqFU
with open(path,'r',encoding='utf-8') as f:
    recs = json.load(f)

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_month(s):
    if not s: return None
    ms = s.lower()
    months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
    for k,v in months.items():
        if k in ms:
            return v
    return None

def is_germany(pi):
    return bool(re.search(r'\bfrom DE\b', pi or '')) or bool(re.search(r'\bDE-', pi or ''))

def title_from_localized(tl):
    if not tl: return None
    try:
        arr = json.loads(tl)
        if isinstance(arr,list) and arr:
            # prefer en then de then first
            for lang in ['en','de']:
                for o in arr:
                    if o.get('language')==lang and o.get('text'):
                        return o.get('text')
            for o in arr:
                if o.get('text'):
                    return o.get('text')
    except Exception:
        pass
    return None

def cpc_level4(code):
    if not code: return None
    c = code.strip()
    # remove spaces
    c = c.replace(' ','')
    if '/' not in c:
        return None
    pre, post = c.split('/',1)
    # level4 = first digit after slash
    if not post or not post[0].isdigit():
        # sometimes like 2400 etc, still digit
        return None
    return pre + '/' + post[0]

rows=[]
for r in recs:
    if not is_germany(r.get('Patents_info')):
        continue
    gy=parse_year(r.get('grant_date'))
    gm=parse_month(r.get('grant_date'))
    if gy!=2019 or gm is None or gm<7:
        continue
    fy=parse_year(r.get('filing_date'))
    if fy is None:
        continue
    title=title_from_localized(r.get('title_localized'))
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs=[]
    lvl4=set()
    for o in cpcs:
        code=o.get('code')
        l4=cpc_level4(code)
        if l4:
            lvl4.add(l4)
    for l4 in lvl4:
        rows.append({'cpc4':l4,'filing_year':fy,'title':title})

df=pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    counts=df.groupby(['cpc4','filing_year']).size().reset_index(name='n').sort_values(['cpc4','filing_year'])
    alpha=0.1
    best=[]
    for cpc4, g in counts.groupby('cpc4'):
        g=g.sort_values('filing_year')
        ema=None
        best_year=None
        best_val=None
        for _,row in g.iterrows():
            x=float(row['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if best_val is None or ema>best_val:
                best_val=ema
                best_year=int(row['filing_year'])
        best.append({'cpc4':cpc4,'best_year':best_year,'best_ema':best_val})
    best_df=pd.DataFrame(best).sort_values('best_ema',ascending=False)
    top=best_df.head(20)
    out=top.to_dict('records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_cPz7hBfbexTUglRXwdF9ZtMv': ['publicationinfo'], 'var_call_XeAyLAVzju4UqMrRw27HJewi': ['cpc_definition'], 'var_call_TBZM4GbiRKvHit3ronCTbqFU': 'file_storage/call_TBZM4GbiRKvHit3ronCTbqFU.json'}

exec(code, env_args)
