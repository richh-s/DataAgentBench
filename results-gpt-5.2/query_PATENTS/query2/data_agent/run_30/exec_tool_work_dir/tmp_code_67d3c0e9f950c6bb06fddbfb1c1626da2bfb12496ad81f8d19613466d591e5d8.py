code = """import json, re
from datetime import datetime
import pandas as pd

# load records
rec = var_call_tfKvXA8L4MCE3nDyjQMJaAGU
if isinstance(rec, str):
    with open(rec, 'r', encoding='utf-8') as f:
        rec = json.load(f)

df = pd.DataFrame(rec)

# filter Germany by looking for country_code DE in Patents_info
mask_de = df['Patents_info'].fillna('').str.contains(r'country_code\"\s*:\s*\"DE\"') | df['Patents_info'].fillna('').str.contains(r'\bcountry_code\b.*\bDE\b')
df = df[mask_de].copy()

# parse grant_date and filing_date
months = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_nl_date(s):
    if not isinstance(s,str) or not s.strip():
        return None
    s2 = s.replace(',', ' ')
    # find year
    m = re.search(r'(19\d{2}|20\d{2})', s2)
    if not m:
        return None
    year = int(m.group(1))
    # find month name
    mon = None
    for name,num in months.items():
        if re.search(r'\b'+re.escape(name)+r'\b', s2, flags=re.I):
            mon = num
            break
    if mon is None:
        return datetime(year,1,1)
    # find day
    md = re.search(r'\b(\d{1,2})(st|nd|rd|th)?\b', s2)
    day = 1
    if md:
        d = int(md.group(1))
        if 1 <= d <= 31:
            day = d
    try:
        return datetime(year, mon, day)
    except:
        return datetime(year, mon, 1)


df['grant_dt'] = df['grant_date'].apply(parse_nl_date)
df['filing_dt'] = df['filing_date'].apply(parse_nl_date)

# second half of 2019 grants
start = datetime(2019,7,1)
end = datetime(2019,12,31,23,59,59)
df = df[df['grant_dt'].between(start,end)].copy()

# extract CPC codes and map to level-4 group (first 4 chars + main group number)
# level-4 here interpreted as subclass+main group, e.g., A61M1/00, A61M1/34 etc. We'll keep part before '/' plus one-digit? Actually main group is before '/', keep full before '/'.

def extract_codes(cpc_field):
    if not isinstance(cpc_field,str) or not cpc_field.strip():
        return []
    try:
        arr = json.loads(cpc_field)
        codes = [x.get('code') for x in arr if isinstance(x,dict) and x.get('code')]
    except:
        codes = re.findall(r'"code"\s*:\s*"([A-Z]\d\d[A-Z][0-9A-Z]?[^\"]*)"', cpc_field)
    # dedupe
    out=[]
    seen=set()
    for c in codes:
        if c not in seen:
            seen.add(c); out.append(c)
    return out

def to_level4(code):
    # normalize: remove spaces
    c = code.strip().replace(' ', '')
    if '/' in c:
        pre = c.split('/')[0]
        return pre  # subclass+main group number
    return c

rows=[]
for _,r in df.iterrows():
    for code in extract_codes(r.get('cpc')):
        rows.append({'rowid': r['rowid'], 'filing_year': r['filing_dt'].year if pd.notnull(r['filing_dt']) else None,
                     'level4': to_level4(code)})

cpc_df = pd.DataFrame(rows)
cpc_df = cpc_df.dropna(subset=['filing_year','level4'])

# counts per year per cpc group
counts = cpc_df.groupby(['level4','filing_year']).size().reset_index(name='n').sort_values(['level4','filing_year'])

alpha=0.1
# compute EMA per group over years in ascending order

def ema_for_group(sub):
    sub = sub.sort_values('filing_year').copy()
    ema=[]
    prev=None
    for v in sub['n']:
        if prev is None:
            prev = v
        else:
            prev = alpha*v + (1-alpha)*prev
        ema.append(prev)
    sub['ema']=ema
    return sub

ema_df = counts.groupby('level4', group_keys=False).apply(ema_for_group)

# best year per group (max ema)
best = ema_df.sort_values(['level4','ema','filing_year'], ascending=[True,False,True]).groupby('level4').head(1)
# find overall highest EMA groups
best = best.sort_values('ema', ascending=False)

# top groups (if many, return top 10)
topn = 10
best_top = best.head(topn).copy()

# fetch titles for these symbols from PostgreSQL
symbols = best_top['level4'].tolist()
# create query string for IN clause
in_list = ','.join(["'"+s.replace("'","''")+"'" for s in symbols])
query = f"SELECT symbol, \"titleFull\" FROM cpc_definition WHERE symbol IN ({in_list});"

import sqlite3, os

print('__RESULT__:')
print(json.dumps({'symbols':symbols,'title_query':query,'best_top':best_top.to_dict(orient='records')}, ensure_ascii=False))"""

env_args = {'var_call_67L1IauZYR9XooXgernt3yFm': ['publicationinfo'], 'var_call_uUD5NRuMClCnrgwpdh0DJnDA': ['cpc_definition'], 'var_call_rq5xMKOLJuqk9A1u7R1eGoB0': [], 'var_call_tfKvXA8L4MCE3nDyjQMJaAGU': 'file_storage/call_tfKvXA8L4MCE3nDyjQMJaAGU.json'}

exec(code, env_args)
