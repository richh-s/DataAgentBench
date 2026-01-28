code = """import json,re
from collections import defaultdict
with open('file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json','r',encoding='utf-8') as f:
    pubs=json.load(f)
with open('file_storage/call_iWKlRsPXFz8VehE93rIAy156.json','r',encoding='utf-8') as f:
    cpc_defs=json.load(f)
# build level4 map
level4={}
for r in cpc_defs:
    sym=r.get('symbol')
    lvl=r.get('level')
    try:
        if int(float(lvl))==4 and sym:
            level4[sym]=r.get('titleFull')
    except Exception:
        pass
# filter pubs for Germany and grant in H2 2019
def is_germany(s):
    if not s:
        return False
    if 'DE-' in s or 'from DE' in s:
        return True
    if re.search(r"\bDE\b", s):
        return True
    return False

def has_h2_2019(gd):
    if not gd:
        return False
    g=gd.lower()
    if '2019' not in g:
        return False
    for m in ('jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december'):
        if m in g:
            return True
    return False
filtered=[]
for p in pubs:
    if not is_germany(p.get('Patents_info','')):
        continue
    if has_h2_2019(p.get('grant_date','')):
        filtered.append(p)
# aggregate counts per level4 per filing year
def find_year(s):
    if not s:
        return None
    m=re.search(r'(20\d{2}|19\d{2})', s)
    return int(m.group(1)) if m else None
counts=defaultdict(lambda: defaultdict(int))
for p in filtered:
    cpcf=p.get('cpc')
    if not cpcf:
        continue
    try:
        cpcs=json.loads(cpcf)
    except Exception:
        try:
            cpcs=json.loads(cpcf.replace("'","\""))
        except Exception:
            continue
    fy=find_year(p.get('filing_date') or p.get('publication_date') or '')
    if not fy:
        continue
    for e in cpcs:
        if isinstance(e, dict):
            code=e.get('code')
        else:
            code=None
        if not code or len(code)<3:
            continue
        lvl4=code[:3]
        if lvl4 in level4:
            counts[lvl4][fy]+=1
# compute EMA
alpha=0.1
results=[]
for sym,yc in counts.items():
    years=sorted(yc.keys())
    ema=None
    emaval={}
    for y in years:
        v=yc[y]
        if ema is None:
            ema=v
        else:
            ema=alpha*v+(1-alpha)*ema
        emaval[y]=ema
    best=max(emaval.keys(), key=lambda yy: emaval[yy])
    results.append({'symbol':sym,'titleFull':level4.get(sym),'best_year':int(best),'peak_ema':round(float(emaval[best]),4),'year_counts':{str(y):int(yc[y]) for y in years}})
results_sorted=sorted(results, key=lambda r: r['peak_ema'], reverse=True)
print('__RESULT__:')
print(json.dumps(results_sorted, ensure_ascii=False))"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json', 'var_call_HJBw0WnBcgg79MIUSqCfldCG': {'var1': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var2': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}}

exec(code, env_args)
