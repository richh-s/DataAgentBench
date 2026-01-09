code = """import json, re, pandas as pd

raw = var_call_AaeA2pHkjJXWtyG1xBm7JCt0
if isinstance(raw, str):
    with open(raw,'r',encoding='utf-8') as f:
        records=json.load(f)
else:
    records=raw

def parse_year(s):
    if not s: return None
    m=re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def cpc_level4(code):
    if not code: return None
    code=code.strip().split(' ')[0]
    if '/' not in code: return code
    pre, post = code.split('/',1)
    digits=''.join(ch for ch in post if ch.isdigit())
    if not digits: return pre
    lvl=digits[:4] if len(digits)>=4 else digits
    return pre+'/'+lvl

rows=[]
for r in records:
    # DE is jurisdiction marker at start like 'The DE '
    if not (r.get('Patents_info','').startswith('The DE') or ' from DE' in r.get('Patents_info','') or 'The DE ' in r.get('Patents_info','')):
        continue
    fy=parse_year(r.get('filing_date'))
    if fy is None: continue
    try:
        cpcs=json.loads(r.get('cpc')) if r.get('cpc') else []
    except Exception:
        cpcs=[]
    for e in cpcs:
        if isinstance(e,dict) and e.get('code'):
            lvl4=cpc_level4(e['code'])
            if lvl4:
                rows.append({'lvl4':lvl4,'filing_year':fy})

df=pd.DataFrame(rows)
if df.empty:
    print('__RESULT__:')
    print(json.dumps({'error':'No rows after DE filter and parsing'}))
    raise SystemExit

cnt=df.groupby(['lvl4','filing_year']).size().reset_index(name='filings').sort_values(['lvl4','filing_year'])
alpha=0.1
emas=[]
for lvl4,g in cnt.groupby('lvl4'):
    ema=None
    for _,row in g.sort_values('filing_year').iterrows():
        x=float(row['filings'])
        ema = x if ema is None else alpha*x+(1-alpha)*ema
        emas.append({'lvl4':lvl4,'year':int(row['filing_year']),'ema':float(ema)})
ema_df=pd.DataFrame(emas)
best=ema_df.sort_values(['lvl4','ema','year'],ascending=[True,False,True]).groupby('lvl4').head(1)
top=best.sort_values('ema',ascending=False).head(10)
print('__RESULT__:')
print(json.dumps({'top':top.to_dict('records'), 'symbols':sorted(top['lvl4'].unique().tolist())}))"""

env_args = {'var_call_KtpJrgGjCQAScV8aiuSnhhAo': ['publicationinfo'], 'var_call_PdaBkhXROFG7raA0T0FkaSFu': ['cpc_definition'], 'var_call_OWtkZbNyowygBowaTEKzrfvj': [], 'var_call_OlEoAyjMSjsS9CmUmq6pTKsO': 'file_storage/call_OlEoAyjMSjsS9CmUmq6pTKsO.json', 'var_call_HEE0uTfggdQoTJPVL0IpCFKH': 'file_storage/call_HEE0uTfggdQoTJPVL0IpCFKH.json', 'var_call_TV2JwEGCJ2O6VlwXUjhqETNq': {'error': 'No DE granted H2 2019 records with parsable filing_year/CPC.'}, 'var_call_AaeA2pHkjJXWtyG1xBm7JCt0': 'file_storage/call_AaeA2pHkjJXWtyG1xBm7JCt0.json'}

exec(code, env_args)
