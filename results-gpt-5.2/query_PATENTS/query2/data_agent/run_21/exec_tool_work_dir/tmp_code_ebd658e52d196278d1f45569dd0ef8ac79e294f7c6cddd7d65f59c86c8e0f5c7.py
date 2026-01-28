code = """import json, re
import pandas as pd

# Load records from storage (may be a file path)
src = var_call_QTOX5BFF3YvIJjP6nvkmOJuT
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def in_h2_2019(s):
    if not s:
        return False
    sl = s.lower()
    y = parse_year(sl)
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
        'dec':12,'december':12
    }
    mon = None
    for k,v in months.items():
        if k in sl:
            mon = v
            break
    if mon is None:
        # try numeric formats like 2019-07-15 or 15/07/2019
        m = re.search(r'\b(\d{1,2})[\-/](\d{1,2})[\-/]((?:19|20)\d{2})\b', sl)
        if m:
            # assume month is second if first>12 else ambiguous; take second as month if <=12
            a,b,_ = m.groups()
            a=int(a); b=int(b)
            mon = b if 1<=b<=12 else (a if 1<=a<=12 else None)
        else:
            m = re.search(r'\b((?:19|20)\d{2})[\-/](\d{1,2})[\-/](\d{1,2})\b', sl)
            if m:
                mon = int(m.group(2))
    return mon is not None and mon >= 7 and mon <= 12

def is_germany(patents_info):
    if not patents_info:
        return False
    # Heuristic: look for country_code DE or ' from DE' or 'Germany'
    s = patents_info
    return ('country_code' in s and 'DE' in s) or re.search(r'\bDE\b', s) or ('Germany' in s)

def cpc_level4(code):
    if not code:
        return None
    code = code.strip()
    m = re.match(r'^([A-HY]\d{2}[A-Z])\s*(\d+)(?:/(\d+))?$', code)
    if not m:
        return None
    main = m.group(1)
    cls = m.group(2)
    sub = m.group(3)
    if sub is None:
        return f"{main}{cls}/00"
    # level 4: keep first 2 digits of subgroup (or pad)
    sub2 = (sub + '0'*2)[:2]
    return f"{main}{cls}/{sub2}"

rows=[]
for r in recs:
    if not is_germany(r.get('Patents_info')):
        continue
    if not in_h2_2019(r.get('grant_date')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_str = r.get('cpc')
    try:
        cpcs = json.loads(cpc_str) if isinstance(cpc_str,str) else (cpc_str or [])
    except Exception:
        continue
    codes=set()
    for c in cpcs:
        code = c.get('code') if isinstance(c,dict) else None
        lv4 = cpc_level4(code)
        if lv4:
            codes.add(lv4)
    for lv4 in codes:
        rows.append({'year':fy,'cpc4':lv4})

df=pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    counts=df.groupby(['cpc4','year']).size().reset_index(name='filings')
    # compute EMA alpha=0.1 per cpc4 over years
    alpha=0.1
    best=[]
    for cpc4,g in counts.groupby('cpc4'):
        g=g.sort_values('year')
        ema=None
        for _,row in g.iterrows():
            x=row['filings']
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            best.append({'cpc4':cpc4,'year':int(row['year']),'ema':float(ema)})
    best_df=pd.DataFrame(best)
    idx=best_df.groupby('cpc4')['ema'].idxmax()
    winners=best_df.loc[idx].copy()
    # for overall highest, sort by ema desc
    winners=winners.sort_values(['ema','cpc4'],ascending=[False,True])
    out=winners.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Mbpn7fq1c6KmlusSvLF2XWtm': ['publicationinfo'], 'var_call_4cMNUeOLtWG92c7Cac2kBs4e': ['cpc_definition'], 'var_call_lbiXOMk5cItGmhjTcXXPVnlN': [], 'var_call_QTOX5BFF3YvIJjP6nvkmOJuT': 'file_storage/call_QTOX5BFF3YvIJjP6nvkmOJuT.json'}

exec(code, env_args)
