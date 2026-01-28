code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        # assume file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_bBfYdt6KQ8sln8ezNnwuqDD2)
defs = load_records(var_call_wjIpy3xP5pd73QvLuzhX5YKH)

df_pub = pd.DataFrame(pub)

# Germany filter from Patents_info: look for ' DE' country mention or 'from DE' or '(number DE-' etc.
# Use regex for word boundary DE or pattern ' DE-' ' DE,' ' DE.' 'from DE' 'The DE'
pat = re.compile(r'\bDE\b|\bDE-[0-9]|\(number DE-|from DE', re.IGNORECASE)
mask_de = df_pub['Patents_info'].fillna('').apply(lambda s: bool(pat.search(s)))
df_pub = df_pub[mask_de].copy()

# parse filing year
month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not date_str or not isinstance(date_str,str):
        return None
    m = re.search(r'(19|20)\d{2}', date_str)
    if not m:
        return None
    return int(m.group(0))

def parse_grant(date_str):
    if not date_str or not isinstance(date_str,str):
        return None
    y = parse_year(date_str)
    mo = None
    for name,num in month_map.items():
        if name in date_str.lower():
            mo = num
            break
    return (y, mo)

# second half 2019
mask_h2_2019 = df_pub['grant_date'].fillna('').apply(lambda s: (lambda ym: ym[0]==2019 and (ym[1] is not None and ym[1]>=7))(parse_grant(s)) if parse_grant(s) else False)
df_pub = df_pub[mask_h2_2019].copy()

# explode CPC codes; cpc field is json-like string

def extract_codes(cpc_str):
    if not cpc_str or not isinstance(cpc_str,str):
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z0-9/]+)"', cpc_str)

# level 4 group: first 3 chars before '/' (e.g., A61B) and for section-only like 'B04' treat as itself

def to_level4(code):
    if not code:
        return None
    code = code.strip()
    # remove spaces
    code = code.replace(' ', '')
    if '/' in code:
        pre = code.split('/')[0]
        return pre[:4]
    return code[:4]

rows = []
for _,r in df_pub.iterrows():
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    for c in extract_codes(r.get('cpc')):
        lv4 = to_level4(c)
        if lv4:
            rows.append((lv4, fy))

df = pd.DataFrame(rows, columns=['cpc4','year'])
if df.empty:
    out = []
else:
    # count filings per year per cpc4
    cnt = df.groupby(['cpc4','year']).size().reset_index(name='filings')

    # compute EMA alpha=0.1 per cpc4 over years sorted
    alpha=0.1
    ema_rows=[]
    for cpc4, sub in cnt.groupby('cpc4'):
        sub = sub.sort_values('year')
        ema=None
        for _,sr in sub.iterrows():
            x = float(sr['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            ema_rows.append({'cpc4':cpc4,'year':int(sr['year']),'filings':int(sr['filings']),'ema':float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    # for each year, find cpc4 with max ema
    idx = ema_df.groupby('year')['ema'].idxmax()
    top_by_year = ema_df.loc[idx].copy().sort_values('year')

    # attach titles from definitions: exact match symbol==cpc4, else None
    df_defs = pd.DataFrame(defs)
    df_defs['symbol']=df_defs['symbol'].astype(str)
    title_map = dict(zip(df_defs['symbol'], df_defs['titleFull']))
    top_by_year['titleFull'] = top_by_year['cpc4'].map(title_map)

    # best year for each cpc group based on max ema
    best_idx = ema_df.groupby('cpc4')['ema'].idxmax()
    best_year = ema_df.loc[best_idx, ['cpc4','year','ema']].rename(columns={'year':'best_year','ema':'best_ema'})

    merged = pd.merge(top_by_year, best_year, on='cpc4', how='left')
    merged = merged[['year','cpc4','titleFull','ema','best_year','best_ema']]

    out = merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_bBfYdt6KQ8sln8ezNnwuqDD2': 'file_storage/call_bBfYdt6KQ8sln8ezNnwuqDD2.json', 'var_call_wjIpy3xP5pd73QvLuzhX5YKH': 'file_storage/call_wjIpy3xP5pd73QvLuzhX5YKH.json'}

exec(code, env_args)
