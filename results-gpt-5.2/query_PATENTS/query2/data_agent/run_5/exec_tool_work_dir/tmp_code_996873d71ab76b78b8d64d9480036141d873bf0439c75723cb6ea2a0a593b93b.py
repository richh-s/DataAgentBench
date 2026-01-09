code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_Zqf930h923rNLOnb7mQ6I2r3
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_h2_2019(grant_str):
    s = (grant_str or '').lower()
    # quick year check
    y = parse_year(s)
    if y != 2019:
        return False
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
        'dec':12,'december':12,
    }
    mon = None
    for k,v in months.items():
        if k in s:
            mon = v
            break
    if mon is None:
        # try numeric month patterns like 2019-07-12 or 12/07/2019 etc
        m = re.search(r'(?:\b2019\b[^0-9]{0,3})(\d{1,2})', s)
        if m:
            try:
                mon = int(m.group(1))
            except:
                mon = None
    return (mon is not None) and (7 <= mon <= 12)

def is_germany(patents_info):
    return bool(re.search(r'\bfrom\s+DE\b', patents_info or ''))

def extract_level4(code):
    if not code:
        return None
    code = code.strip()
    # level 4 as class/subclass + main group (before '/')
    if '/' in code:
        return code.split('/')[0] + '/' + '00'
    return code

def parse_title(title_localized):
    if not title_localized:
        return None
    try:
        arr = json.loads(title_localized)
        if isinstance(arr, list) and arr:
            # prefer en then de then first
            for pref in ['en','de']:
                for it in arr:
                    if it.get('language')==pref and it.get('text'):
                        return it.get('text')
            for it in arr:
                if it.get('text'):
                    return it.get('text')
    except:
        return str(title_localized)
    return None

rows=[]
for r in records:
    if not (is_germany(r.get('Patents_info')) and is_h2_2019(r.get('grant_date'))):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    title = parse_title(r.get('title_localized'))
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except:
        continue
    for c in cpcs if isinstance(cpcs,list) else []:
        code = c.get('code')
        lvl4 = extract_level4(code)
        if lvl4:
            rows.append({'lvl4':lvl4,'filing_year':fy,'title':title})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    # count filings per year per lvl4 (unique patents would require id; not available; count rows as filings assignments)
    counts = df.groupby(['lvl4','filing_year']).size().reset_index(name='n')
    # compute EMA per lvl4 over years (sorted)
    alpha=0.1
    best=[]
    for lvl4, g in counts.groupby('lvl4'):
        g = g.sort_values('filing_year')
        ema=None
        best_year=None
        best_ema=None
        for _,row in g.iterrows():
            n=row['n']
            if ema is None:
                ema = n
            else:
                ema = alpha*n + (1-alpha)*ema
            if (best_ema is None) or (ema>best_ema):
                best_ema=ema
                best_year=int(row['filing_year'])
        best.append({'cpc_group_code':lvl4,'best_year':best_year,'best_ema':float(best_ema)})
    best_df = pd.DataFrame(best).sort_values(['best_ema','cpc_group_code'], ascending=[False, True])
    top = best_df.head(20)
    # fetch titles from CPCDefinition DB in next step; here output codes+best_year
    out = top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_XVuBEZ2DgHu1EMguchNguYfD': ['publicationinfo'], 'var_call_L09bT4D6JohGY9TmzWsgVkmU': ['cpc_definition'], 'var_call_Zqf930h923rNLOnb7mQ6I2r3': 'file_storage/call_Zqf930h923rNLOnb7mQ6I2r3.json'}

exec(code, env_args)
