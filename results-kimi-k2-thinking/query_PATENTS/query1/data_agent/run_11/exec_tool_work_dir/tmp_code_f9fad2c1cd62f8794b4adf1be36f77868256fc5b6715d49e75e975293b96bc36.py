code = """import json, datetime

fp = locals()['var_functions.query_db:40']
with open(fp) as f:
    data = json.load(f)

cpc_counts = {}
years = set()

for r in data:
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
    except Exception:
        pass

alpha = 0.2
result = []

for cd, yc in cpc_counts.items():
    sy = sorted(list(years))
    ema = 0
    by = None
    be = 0
    for y in sy:
        c = yc.get(y, 0)
        ema = alpha * c + (1 - alpha) * ema
        if ema > be:
            be = ema
            by = y
    if by == 2022:
        result.append((cd, be))

result.sort(key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps([x[0] for x in result]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json'}

exec(code, env_args)
