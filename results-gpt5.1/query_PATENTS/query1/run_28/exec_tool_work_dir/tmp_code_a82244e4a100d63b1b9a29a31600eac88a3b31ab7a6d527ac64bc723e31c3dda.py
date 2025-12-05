code = """import json, pandas as pd, re

path_pub = var_call_1RbwDUJZe12ISm53GfQrS8PR
path_level5 = var_call_OiLeVa9e6mKVSjBtqw0EgdrO

with open(path_pub, 'r') as f:
    pub = json.load(f)
with open(path_level5, 'r') as f:
    lvl5 = json.load(f)

pub_df = pd.DataFrame(pub)
pub_df = pub_df.dropna(subset=['publication_date', 'cpc'])

months = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}

def to_year(s):
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(st|nd|rd|th)?,\s*(\d{4})', s)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{1,2}(st|nd|rd|th)?,\s*(\d{4})', s)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{1,2}(st|nd|rd|th)?[,]?\s*(\d{4})', s)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{1,2}[a-z]{2},\s*(\d{4})', s)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{1,2},\s*(\d{4})', s)
    if not m:
        m = re.search(r'(\w+)\s+\d{1,2}[a-z]{2},\s*(\d{4})', s)
    if not m:
        m = re.search(r'(\w+)\s+\d{1,2}[a-z]{2}\s*(\d{4})', s)
    if not m:
        m = re.search(r'\b(\d{4})\b', s)
        if not m:
            return None
        return int(m.group(1))
    year = m.group(len(m.groups()))
    return int(year)

pub_df['year'] = pub_df['publication_date'].apply(to_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

lvl5_set = set([r['symbol'] for r in lvl5])

records = []
for _, row in pub_df.iterrows():
    try:
        cps = json.loads(row['cpc'])
    except Exception:
        continue
    y = row['year']
    for entry in cps:
        code = entry.get('code')
        if code in lvl5_set:
            records.append({'symbol': code, 'year': y})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    yearly = df.groupby(['symbol','year']).size().reset_index(name='count')
    years = sorted(yearly['year'].unique())
    alpha = 0.2
    ema_records = []
    for sym, grp in yearly.groupby('symbol'):
        g = grp.set_index('year')['count']
        g = g.reindex(years, fill_value=0)
        ema = None
        for yr in years:
            c = g.loc[yr]
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            ema_records.append({'symbol': sym, 'year': yr, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    best = ema_df.loc[ema_df.groupby('symbol')['ema'].idxmax()].reset_index(drop=True)
    best_2022 = best[best['year']==2022]
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _j
out = _j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1RbwDUJZe12ISm53GfQrS8PR': 'file_storage/call_1RbwDUJZe12ISm53GfQrS8PR.json', 'var_call_OiLeVa9e6mKVSjBtqw0EgdrO': 'file_storage/call_OiLeVa9e6mKVSjBtqw0EgdrO.json', 'var_call_HQxUjZHUXAtuh8ufYxRWchg3': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}]}

exec(code, env_args)
