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
    for fmt in ['%d %b %Y','%b %d %Y','%d %B %Y','%B %d %Y','%Y %b %d','%Y %B %d','%Y %m %d','%Y %B','%B %Y','%Y']:
        try:
            return datetime.strptime(s2, fmt).date()
        except Exception:
            pass
    y = parse_year(s2)
    if y is None:
        return None
    mm = None
    dd = 1
    m = re.search(r'\b(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\b', s2, flags=re.I)
    if m:
        token = m.group(1).lower()
        token = token[:3] if len(token)>3 else token
        # map using first 3 letters
        map3 = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
        mm = map3.get(token[:3])
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
    cpc_list=[]
    cpc = r.get('cpc')
    if cpc:
        try:
            arr = json.loads(cpc)
            if isinstance(arr, list):
                for e in arr:
                    code=e.get('code') if isinstance(e, dict) else None
                    if code:
                        cpc_list.append(code)
        except Exception:
            pass
    if not cpc_list:
        continue
    rows.append({'filing_year':fy,'cpc_codes':cpc_list})

if not rows:
    result = {'top_groups': [], 'all_best': []}
    print('__RESULT__:')
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit

df = pd.DataFrame(rows)

edf = df.explode('cpc_codes').rename(columns={'cpc_codes':'cpc'})
edf['cpc4'] = edf['cpc'].astype(str).str.split('/').str[0].str.replace(' ','', regex=False).str.slice(0,4)

counts = edf.groupby(['cpc4','filing_year']).size().reset_index(name='n')
alpha=0.1
best_records=[]
for cpc4, g in counts.groupby('cpc4'):
    g2 = g.sort_values('filing_year')
    ema=None
    for _, row in g2.iterrows():
        x=int(row['n'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        best_records.append({'cpc4':cpc4,'year':int(row['filing_year']),'ema':float(ema)})

best_df = pd.DataFrame(best_records)
best_year = best_df.sort_values(['cpc4','ema','year'], ascending=[True,False,False]).groupby('cpc4').head(1)
max_ema = best_year['ema'].max()
top = best_year[best_year['ema']==max_ema].copy()
result = {'top_groups': top[['cpc4','year','ema']].to_dict('records'), 'all_best': best_year.to_dict('records')}
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_wDXBInynToPM386rOQ3vXCLr': ['publicationinfo'], 'var_call_vANRYZkTCM7Rk9tLo4XhkzQO': ['cpc_definition'], 'var_call_r6STpnZ5CgXIW8Zbkkx6EN5O': 'file_storage/call_r6STpnZ5CgXIW8Zbkkx6EN5O.json'}

exec(code, env_args)
