code = """"""
import json, datetime
fp = locals()['var_functions.query_db:40']
with open(fp, 'r') as f:
    d = json.load(f)
cpc_counts = {}
years = set()
for r in d:
    try:
        ds = r['publication_date']
        for sfx in ['st,', 'nd,', 'rd,', 'th,']:
            ds = ds.replace(sfx, ',')
        yr = datetime.datetime.strptime(ds.strip(), '%b %d, %Y').year
        years.add(yr)
        for itm in json.loads(r['cpc']):
            cd = itm.get('code', '')
            if '/' in cd and len(cd.split('/')[1]) >= 3:
                if cd not in cpc_counts:
                    cpc_counts[cd] = {}
                cpc_counts[cd][yr] = cpc_counts[cd].get(yr, 0) + 1
    except: pass
alpha=0.2
res=[]
for cd,yc in cpc_counts.items():
    sy=sorted(list(years))
    ema=0; best_yr=None; best_ema=0
    for y in sy:
        cnt=yc.get(y,0)
        ema=alpha*cnt+(1-alpha)*ema
        if ema>best_ema:
            best_ema=ema; best_yr=y
    if best_yr==2022:
        res.append((cd,best_ema))
res.sort(key=lambda x:x[1], reverse=True)
print('\n__RESULT__:')
print(json.dumps([x[0] for x in res]))
""""""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
