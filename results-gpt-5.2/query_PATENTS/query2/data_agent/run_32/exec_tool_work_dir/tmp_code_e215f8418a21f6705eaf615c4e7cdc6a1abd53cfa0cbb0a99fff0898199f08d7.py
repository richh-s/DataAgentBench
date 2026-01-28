code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_r6STpnZ5CgXIW8Zbkkx6EN5O
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_country(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    return None

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str: str):
    if not date_str:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', date_str)
    return int(m.group(1)) if m else None

def parse_date(date_str: str):
    if not date_str:
        return None
    s = date_str.strip()
    s2 = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s, flags=re.I)
    s2 = s2.replace(',', ' ')
    s2 = re.sub(r'\bon\b', ' ', s2, flags=re.I)
    s2 = re.sub(r'\bthe\b', ' ', s2, flags=re.I)
    s2 = re.sub(r'\s+', ' ', s2).strip()
    # try formats
    for fmt in ['%d %b %Y','%b %d %Y','%d %B %Y','%B %d %Y','%Y %b %d','%Y %B %d','%Y %m %d','%Y %B','%B %Y','%Y']:
        try:
            dt = datetime.strptime(s2, fmt)
            return dt.date()
        except Exception:
            pass
    # handle "2019 on Jul 12" like patterns with month token
    y = parse_year(s2)
    if y is None:
        return None
    mm = None
    dd = 1
    m = re.search(r'\b([A-Za-z]{3,9})\b', s2)
    if m:
        token = m.group(1).lower()
        if token in month_map:
            mm = month_map[token]
    m2 = re.search(r'\b(\d{1,2})\b', s2)
    if m2:
        dd = int(m2.group(1))
    if mm is None:
        return datetime(y,1,1).date()
    return datetime(y,mm,dd).date()

rows=[]
for r in recs:
    if extract_country(r.get('Patents_info'))!='DE':
        continue
    gd = parse_date(r.get('grant_date'))
    if not gd or gd.year!=2019 or gd.month<7:
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    title = None
    tl = r.get('title_localized')
    if tl:
        try:
            arr = json.loads(tl)
            # prefer en then any
            if isinstance(arr, list) and arr:
                en = next((x.get('text') for x in arr if x.get('language')=='en' and x.get('text')), None)
                title = en or arr[0].get('text')
        except Exception:
            title = tl
    cpc_list=[]
    cpc = r.get('cpc')
    if cpc:
        try:
            arr = json.loads(cpc)
            for e in arr:
                code=e.get('code')
                if code:
                    cpc_list.append(code)
        except Exception:
            pass
    if not cpc_list:
        continue
    rows.append({'filing_year':fy,'cpc_codes':cpc_list})

df = pd.DataFrame(rows)
# explode codes
edf = df.explode('cpc_codes').rename(columns={'cpc_codes':'cpc'})
# level 4 group: take part before '/', then ensure at least 4 chars and strip spaces
edf['cpc4'] = edf['cpc'].str.split('/').str[0].str.replace(' ','', regex=False)
# some may include extra like H04L12 etc; ensure first 4 chars
edf['cpc4'] = edf['cpc4'].str.slice(0,4)

# count filings per year per cpc4
counts = edf.groupby(['cpc4','filing_year']).size().reset_index(name='n')
# compute EMA per cpc4 over years
alpha=0.1
best=[]
for cpc4, g in counts.groupby('cpc4'):
    g2 = g.sort_values('filing_year')
    ema=None
    for _, row in g2.iterrows():
        x=row['n']
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        best.append({'cpc4':cpc4,'year':int(row['filing_year']),'ema':float(ema)})

best_df = pd.DataFrame(best)
# pick best year per cpc4 by max ema then latest year tie
best_year = best_df.sort_values(['cpc4','ema','year'], ascending=[True,False,False]).groupby('cpc4').head(1)
# overall highest EMA among groups
max_ema = best_year['ema'].max() if not best_year.empty else None
if max_ema is None:
    out=[]
else:
    top = best_year[best_year['ema']==max_ema].copy()
    out = top[['cpc4','year','ema']].to_dict('records')

print('__RESULT__:')
print(json.dumps({'top_groups': out, 'all_best': best_year.to_dict('records')}, ensure_ascii=False))"""

env_args = {'var_call_wDXBInynToPM386rOQ3vXCLr': ['publicationinfo'], 'var_call_vANRYZkTCM7Rk9tLo4XhkzQO': ['cpc_definition'], 'var_call_r6STpnZ5CgXIW8Zbkkx6EN5O': 'file_storage/call_r6STpnZ5CgXIW8Zbkkx6EN5O.json'}

exec(code, env_args)
