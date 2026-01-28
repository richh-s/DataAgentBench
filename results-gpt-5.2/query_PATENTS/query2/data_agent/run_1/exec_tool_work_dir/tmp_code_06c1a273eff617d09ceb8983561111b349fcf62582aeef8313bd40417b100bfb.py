code = """import json, re
import pandas as pd
from datetime import datetime

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_WsAjyPFt4M2aLOCM9DMAioYs)
defs = load_records(var_call_bW30R6oKqU6GU3BFQD2k1hnD)

def parse_year(s):
    if s is None:
        return None
    s2 = str(s)
    m = re.search(r'(19|20)\d{2}', s2)
    return int(m.group(0)) if m else None

def parse_grant_date(s):
    if s is None:
        return None
    s2 = str(s)
    m = re.search(r'(19|20)\d{2}', s2)
    if not m:
        return None
    year = int(m.group(0))
    # month detection
    months = {
        'jan':1,'january':1,
        'feb':2,'february':2,
        'mar':3,'march':3,
        'apr':4,'april':4,
        'may':5,
        'jun':6,'june':6,
        'jul':7,'july':7,
        'aug':8,'august':8,
        'sep':9,'sept':9,'september':9,
        'oct':10,'october':10,
        'nov':11,'november':11,
        'dec':12,'december':12
    }
    s_lower = s2.lower()
    month = None
    for k,v in months.items():
        if k in s_lower:
            month = v
            break
    if month is None:
        # formats like 2019 on Jul 12th handled above; still month found.
        # if only year, cannot decide half-year
        return None
    return (year, month)

def is_germany(patents_info):
    if patents_info is None:
        return False
    return bool(re.search(r'\bfrom\s+DE\b', patents_info)) or bool(re.search(r'\bDE-', patents_info))

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        data = json.loads(cpc_field)
        codes = []
        for entry in data:
            code = entry.get('code')
            if code:
                codes.append(code)
        return codes
    except Exception:
        return []

# filter patents granted in H2 2019 and from Germany
rows=[]
for r in pub:
    gm = parse_grant_date(r.get('grant_date'))
    if not gm:
        continue
    gy, gmo = gm
    if gy != 2019 or gmo < 7:
        continue
    if not is_germany(r.get('Patents_info')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    for code in extract_cpc_codes(r.get('cpc')):
        # map to level4 group: take first 3 chars if like A61B...
        if len(code) >= 3:
            grp = code[:3]
            if re.match(r'^[A-HY]\d\d$', grp):
                rows.append((grp, fy))

df = pd.DataFrame(rows, columns=['cpc_group','filing_year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc_group','filing_year']).size().reset_index(name='filings')
    # compute EMA per group across years
    alpha=0.1
    best_rows=[]
    for grp, gdf in counts.groupby('cpc_group'):
        gdf2 = gdf.sort_values('filing_year')
        ema=None
        best_ema=-1
        best_year=None
        for y, f in zip(gdf2['filing_year'], gdf2['filings']):
            ema = f if ema is None else alpha*f + (1-alpha)*ema
            if ema > best_ema:
                best_ema=ema
                best_year=int(y)
        best_rows.append({'cpc_group':grp,'best_year':best_year,'best_ema':float(best_ema)})
    best = pd.DataFrame(best_rows)
    # join titles
    ddf = pd.DataFrame(defs)
    ddf = ddf.rename(columns={'symbol':'cpc_group','titleFull':'title'})
    merged = best.merge(ddf[['cpc_group','title']], on='cpc_group', how='left')
    merged = merged.sort_values(['best_ema','cpc_group'], ascending=[False,True])
    out = merged[['title','cpc_group','best_year','best_ema']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_WsAjyPFt4M2aLOCM9DMAioYs': 'file_storage/call_WsAjyPFt4M2aLOCM9DMAioYs.json', 'var_call_s90PUFxGfLtgD1FexovUHUZ8': [], 'var_call_erEHfwcM3t1OKmfaeAwVSSAp': ['cpc_definition'], 'var_call_yUjUspl6iqu6RjZnY9LvrLxu': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'status': 'published'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'status': 'published'}], 'var_call_bW30R6oKqU6GU3BFQD2k1hnD': 'file_storage/call_bW30R6oKqU6GU3BFQD2k1hnD.json'}

exec(code, env_args)
