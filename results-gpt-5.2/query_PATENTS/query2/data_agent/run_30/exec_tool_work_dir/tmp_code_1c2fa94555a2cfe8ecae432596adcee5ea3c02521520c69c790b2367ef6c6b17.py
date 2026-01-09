code = """import json, re
from datetime import datetime
import pandas as pd

rec = var_call_tfKvXA8L4MCE3nDyjQMJaAGU
if isinstance(rec, str):
    with open(rec, 'r', encoding='utf-8') as f:
        rec = json.load(f)

df = pd.DataFrame(rec)
mask_de = df['Patents_info'].fillna('').str.contains(r'country_code') & df['Patents_info'].fillna('').str.contains('DE')
df = df[mask_de].copy()

months = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_nl_date(s):
    if not isinstance(s,str) or not s.strip():
        return None
    s2 = s.replace(',', ' ')
    m = re.search(r'(19\d{2}|20\d{2})', s2)
    if not m:
        return None
    year = int(m.group(1))
    mon = None
    for name,num in months.items():
        if re.search(r'\b'+re.escape(name)+r'\b', s2, flags=re.I):
            mon = num
            break
    if mon is None:
        return datetime(year,1,1)
    md = re.search(r'\b(\d{1,2})(st|nd|rd|th)?\b', s2)
    day = int(md.group(1)) if md else 1
    try:
        return datetime(year, mon, day)
    except:
        return datetime(year, mon, 1)


df['grant_dt'] = df['grant_date'].apply(parse_nl_date)
df['filing_dt'] = df['filing_date'].apply(parse_nl_date)

start = datetime(2019,7,1)
end = datetime(2019,12,31,23,59,59)
df = df[df['grant_dt'].between(start,end)].copy()


def extract_codes(cpc_field):
    if not isinstance(cpc_field,str) or not cpc_field.strip():
        return []
    try:
        arr = json.loads(cpc_field)
        codes = [x.get('code') for x in arr if isinstance(x,dict) and x.get('code')]
    except:
        codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
    return list(dict.fromkeys([c.strip() for c in codes if c]))

def to_level4(code):
    c = code.strip().replace(' ', '')
    return c.split('/')[0] if '/' in c else c

rows=[]
for _,r in df.iterrows():
    fy = r['filing_dt'].year if pd.notnull(r['filing_dt']) else None
    for code in extract_codes(r.get('cpc')):
        rows.append({'filing_year': fy, 'level4': to_level4(code)})

cpc_df = pd.DataFrame(rows).dropna(subset=['filing_year','level4'])
counts = cpc_df.groupby(['level4','filing_year']).size().reset_index(name='n').sort_values(['level4','filing_year'])

alpha=0.1

def ema_for_group(sub):
    sub = sub.sort_values('filing_year').copy()
    prev=None
    ema=[]
    for v in sub['n'].tolist():
        prev = v if prev is None else alpha*v + (1-alpha)*prev
        ema.append(prev)
    sub['ema']=ema
    return sub

ema_df = counts.groupby('level4', group_keys=False).apply(ema_for_group)
best = ema_df.sort_values(['level4','ema','filing_year'], ascending=[True,False,True]).groupby('level4').head(1)
best = best.sort_values('ema', ascending=False).head(10)

symbols = best['level4'].tolist()
in_list = ','.join(["'"+s.replace("'","''")+"'" for s in symbols])
q = "SELECT symbol, \"titleFull\" FROM cpc_definition WHERE symbol IN (" + in_list + ");"

print('__RESULT__:')
print(json.dumps({'best':best.to_dict(orient='records'),'title_query':q}, ensure_ascii=False))"""

env_args = {'var_call_67L1IauZYR9XooXgernt3yFm': ['publicationinfo'], 'var_call_uUD5NRuMClCnrgwpdh0DJnDA': ['cpc_definition'], 'var_call_rq5xMKOLJuqk9A1u7R1eGoB0': [], 'var_call_tfKvXA8L4MCE3nDyjQMJaAGU': 'file_storage/call_tfKvXA8L4MCE3nDyjQMJaAGU.json'}

exec(code, env_args)
