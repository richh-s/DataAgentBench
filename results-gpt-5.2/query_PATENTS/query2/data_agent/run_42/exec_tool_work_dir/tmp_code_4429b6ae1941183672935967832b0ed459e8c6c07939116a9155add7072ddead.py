code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_Z5gY8vUJ0Siopbkwx5YsNrWf)
cpc4 = load_records(var_call_1zwQH43GOG18NKoK1sh1MsxA)

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def parse_grant_date(s):
    # return (year, month)
    if not s: return (None, None)
    months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
    sl = s.lower()
    y = parse_year(sl)
    m = None
    for name,num in months.items():
        if name in sl:
            m = num
            break
    return (y,m)

def extract_country(pi):
    if not pi: return None
    m = re.search(r'\b([A-Z]{2})\b', pi)
    # try explicit country_code
    m2 = re.search(r'country_code\s*[:=]\s*([A-Z]{2})', pi)
    if m2: return m2.group(1)
    # heuristic: look for 'In XX,'
    m3 = re.search(r'\bIn\s+([A-Z]{2})\b', pi)
    if m3: return m3.group(1)
    return None

rows=[]
for r in pub:
    gy, gm = parse_grant_date(r.get('grant_date'))
    if gy==2019 and gm is not None and gm>=7:
        cc = extract_country(r.get('Patents_info',''))
        if cc=='DE':
            fy = parse_year(r.get('filing_date'))
            if fy is None: 
                continue
            cpc_str = r.get('cpc')
            if not cpc_str: 
                continue
            try:
                cpcs = json.loads(cpc_str)
            except Exception:
                continue
            codes=set()
            for entry in cpcs:
                code = entry.get('code')
                if not code: 
                    continue
                m = re.match(r'^([A-HY]\\d{2})', code)
                if m:
                    codes.add(m.group(1))
            for c in codes:
                rows.append({'cpc4':c,'filing_year':fy})

df = pd.DataFrame(rows)
if df.empty:
    out = {'error':'No matching German patents granted in H2 2019 found with parsable data.'}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='filings')

def ema_for_group(g):
    g = g.sort_values('filing_year')
    alpha=0.1
    ema=[]
    prev=None
    for x in g['filings']:
        prev = x if prev is None else alpha*x + (1-alpha)*prev
        ema.append(prev)
    g = g.copy()
    g['ema']=ema
    return g

ema_df = counts.groupby('cpc4', group_keys=False).apply(ema_for_group)
# best year per group by max EMA (tie -> latest year)
ema_df = ema_df.sort_values(['cpc4','ema','filing_year'], ascending=[True,False,False])
best = ema_df.groupby('cpc4').head(1).reset_index(drop=True)

cpc4_df = pd.DataFrame(cpc4)
cpc4_df['level']=cpc4_df['level'].astype(float).astype(int)
# map symbol to title
best = best.merge(cpc4_df[['symbol','titleFull']], left_on='cpc4', right_on='symbol', how='left')
best['titleFull'] = best['titleFull'].fillna('')
# find highest EMA overall and filter to those (ties)
max_ema = best['ema'].max()
top = best[best['ema']==max_ema].copy()
# sort by code
top = top.sort_values('cpc4')
res = top[['titleFull','cpc4','filing_year','ema']].rename(columns={'cpc4':'cpc_group_code_level4','filing_year':'best_year','ema':'best_year_ema'}).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'results':res, 'max_ema':float(max_ema), 'num_groups':int(best.shape[0])}, ensure_ascii=False))"""

env_args = {'var_call_Z5gY8vUJ0Siopbkwx5YsNrWf': 'file_storage/call_Z5gY8vUJ0Siopbkwx5YsNrWf.json', 'var_call_BwXSVN2WSg5Sg1j4tynhonMz': [], 'var_call_1zwQH43GOG18NKoK1sh1MsxA': 'file_storage/call_1zwQH43GOG18NKoK1sh1MsxA.json'}

exec(code, env_args)
