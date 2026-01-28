code = """import json,re
with open(var_call_uX35j8swiDeRTrhkqYrZ3t7S,'r',encoding='utf-8') as f:
    pubs=json.load(f)
with open(var_call_7yMwBGdeJJXK2ZKHMVmTmgWn,'r',encoding='utf-8') as f:
    cpc_defs=json.load(f)

cpc_map={it['symbol']:it['titleFull'] for it in cpc_defs}
from collections import defaultdict
counts=defaultdict(lambda:defaultdict(int))
for rec in pubs:
    gd=rec.get('grant_date','')
    if '2019' not in gd: continue
    if not any(m in gd for m in ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']): continue
    fd=rec.get('filing_date','')
    m=re.search(r'(20\d{2}|19\d{2})',fd)
    if not m:
        m=re.search(r'(20\d{2}|19\d{2})',gd)
    if not m: continue
    year=int(m.group(1))
    cpc_field=rec.get('cpc','')
    try:
        cpcs=json.loads(cpc_field)
    except Exception:
        try:
            cpcs=json.loads(cpc_field.replace("'","\""))
        except Exception:
            continue
    for entry in cpcs:
        code=entry.get('code')
        if not code: continue
        m2=re.match(r'^([A-Z]\d{2})',code)
        group=m2.group(1) if m2 else code[:3]
        if group in cpc_map:
            counts[group][year]+=1

alpha=0.1
results=[]
for group,yc in counts.items():
    years=sorted(yc.keys())
    if not years: continue
    ema=None
    ema_by_year={}
    for y in years:
        cnt=yc.get(y,0)
        if ema is None:
            ema=float(cnt)
        else:
            ema=alpha*cnt+(1-alpha)*ema
        ema_by_year[y]=ema
    best_year=max(ema_by_year.items(),key=lambda x:x[1])[0]
    best_ema=ema_by_year[best_year]
    results.append({'symbol':group,'titleFull':cpc_map.get(group,''),'best_year':int(best_year),'best_ema':round(float(best_ema),3),'years_considered':len(years)})

results_sorted=sorted(results,key=lambda x:x['best_ema'],reverse=True)
print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_VrLjYDKCzlPz4wvziBWhrxsY': 'file_storage/call_VrLjYDKCzlPz4wvziBWhrxsY.json', 'var_call_uX35j8swiDeRTrhkqYrZ3t7S': 'file_storage/call_uX35j8swiDeRTrhkqYrZ3t7S.json', 'var_call_H43HOmSBNUjo7iHO18cuHoOk': 'file_storage/call_H43HOmSBNUjo7iHO18cuHoOk.json', 'var_call_7yMwBGdeJJXK2ZKHMVmTmgWn': 'file_storage/call_7yMwBGdeJJXK2ZKHMVmTmgWn.json', 'var_call_ZoxDuyfmA0ExiNj3X6GL6mWl': {'pubs': 72, 'cpcs': 137}}

exec(code, env_args)
