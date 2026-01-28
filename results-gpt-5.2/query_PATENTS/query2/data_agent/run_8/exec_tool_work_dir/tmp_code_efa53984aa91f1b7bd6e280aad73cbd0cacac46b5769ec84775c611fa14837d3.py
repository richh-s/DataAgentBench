code = """import json, re
import pandas as pd

# load records
path = var_call_RRBLygdtp1C7FFkuGkd9d6kr
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_germany(pinfo):
    if not pinfo: return False
    return ('country_code' in pinfo and 'DE' in pinfo) or (' DE' in pinfo) or ('Germany' in pinfo)

def cpc_level4(code):
    # level 4 = subclass + main group (no subgroup)
    if not code or '/' not in code:
        return None
    pre, post = code.split('/', 1)
    main = re.match(r'\d+', post)
    if not main:
        return None
    return f"{pre}/{main.group(0)}"

rows=[]
for r in recs:
    if not is_germany(r.get('Patents_info')):
        continue
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    # parse cpc json-like
    cpc_str = r.get('cpc')
    try:
        cpcs = json.loads(cpc_str) if cpc_str else []
    except Exception:
        cpcs = []
    lvl4=set()
    for c in cpcs:
        code=c.get('code')
        l4=cpc_level4(code)
        if l4:
            lvl4.add(l4)
    for l4 in lvl4:
        rows.append({'year': y, 'cpc4': l4})

df=pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    counts=df.groupby(['cpc4','year']).size().reset_index(name='filings')
    # compute EMA per cpc4 over years
    alpha=0.1
    res=[]
    for cpc4, g in counts.sort_values(['cpc4','year']).groupby('cpc4'):
        g=g.sort_values('year').copy()
        ema=None
        for _, row in g.iterrows():
            x=row['filings']
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            res.append({'cpc4': cpc4, 'year': int(row['year']), 'ema': float(ema)})
    ema_df=pd.DataFrame(res)
    # pick best year per cpc4
    best=ema_df.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').head(1)
    # now find highest EMA across cpc4s (using their best year)
    max_ema=best['ema'].max()
    top=best[best['ema']==max_ema].copy()
    out=top.sort_values(['ema','cpc4']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'top': out}, ensure_ascii=False))"""

env_args = {'var_call_v1CpXqNsrdoQjjAXi5FLWbrp': ['publicationinfo'], 'var_call_NEa2KVzzn9B1BcGwQ2xpGZnO': ['cpc_definition'], 'var_call_RRBLygdtp1C7FFkuGkd9d6kr': 'file_storage/call_RRBLygdtp1C7FFkuGkd9d6kr.json'}

exec(code, env_args)
