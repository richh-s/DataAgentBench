code = """import json,re

pub_var = var_call_MDlcivTJXFIfR2vKR26j59aM
cpcdef_var = var_call_5Gw88oI4JpttA2mAkVduidzd

def load(x):
    if isinstance(x,str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

pubs = load(pub_var)
cpcdefs = load(cpcdef_var)

level5 = set()
for r in cpcdefs:
    s = r.get('symbol')
    if s:
        level5.add(s.strip())

year_re = re.compile(r'(19|20)\d{2}')
year_counts = {}
all_years = set()
for rec in pubs:
    fd = rec.get('filing_date')
    cpc = rec.get('cpc')
    if not fd or not cpc:
        continue
    m = year_re.search(fd)
    if not m:
        continue
    y = int(m.group(0))
    all_years.add(y)
    # parse cpc
    try:
        cpcs = json.loads(cpc)
    except Exception:
        try:
            import ast
            cpcs = ast.literal_eval(cpc)
        except Exception:
            continue
    if not isinstance(cpcs,list):
        continue
    groups = set()
    for e in cpcs:
        if not isinstance(e,dict):
            continue
        code = e.get('code')
        if not code or len(code)<4:
            continue
        groups.add(code[:4])
    if not groups:
        continue
    yc = year_counts.setdefault(y,{})
    for g in groups:
        yc[g] = yc.get(g,0)+1

result = []
if year_counts:
    miny = min(all_years)
    maxy = max(all_years)
    years = list(range(miny,maxy+1))
    groups = set()
    for yc in year_counts.values():
        groups.update(yc.keys())
    groups = sorted([g for g in groups if g in level5])
    counts = {g:[] for g in groups}
    for y in years:
        yc = year_counts.get(y,{})
        for g in groups:
            counts[g].append(int(yc.get(g,0)))
    alpha = 0.2
    best = {}
    for g in groups:
        s = counts[g]
        if not s:
            continue
        ema = s[0]
        emalist = [ema]
        for v in s[1:]:
            ema = alpha*v + (1-alpha)*ema
            emalist.append(ema)
        idx = max(range(len(emalist)), key=lambda i: emalist[i])
        best[g] = years[idx]
    result = [g for g,y in best.items() if y==2022]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MDlcivTJXFIfR2vKR26j59aM': 'file_storage/call_MDlcivTJXFIfR2vKR26j59aM.json', 'var_call_5Gw88oI4JpttA2mAkVduidzd': 'file_storage/call_5Gw88oI4JpttA2mAkVduidzd.json'}

exec(code, env_args)
