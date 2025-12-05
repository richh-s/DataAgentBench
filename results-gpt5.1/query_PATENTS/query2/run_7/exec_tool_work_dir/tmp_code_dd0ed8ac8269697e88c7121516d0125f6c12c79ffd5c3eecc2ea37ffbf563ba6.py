code = """import json, re, pandas as pd
from datetime import datetime

path_pubs = var_call_jGZ0YzApr2ZRj9WKloXR68ji
path_cpc = var_call_Vodkb5polttWei6SsAns05ei

with open(path_pubs,'r') as f:
    pubs = json.load(f)
with open(path_cpc,'r') as f:
    cpcdefs = json.load(f)

pubs_df = pd.DataFrame(pubs)

def extract_country(text):
    m = re.search(r'\b([A-Z]{2})\b', text)
    return m.group(1) if m else None

pubs_df['country'] = pubs_df['Patents_info'].apply(extract_country)

month_map = {m: i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}

def parse_date(text):
    if not isinstance(text,str) or not text.strip():
        return None
    text = text.replace('dated ','').replace('on ','').replace('of ','')
    text = re.sub(r'(st|nd|rd|th)','',text)
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', text)
    if not m:
        return None
    month = m.group(1)
    parts = re.split(r'\s+', text.strip())
    try:
        if parts[0].isdigit():
            day = int(parts[0])
            year = int(parts[-1])
        else:
            day = int(parts[1])
            year = int(parts[-1])
        return datetime(year, month_map[month], day)
    except Exception:
        return None

pubs_df['grant_dt'] = pubs_df['grant_date'].apply(parse_date)

mask = pubs_df['country'].eq('DE') & pubs_df['grant_dt'].notna() & (pubs_df['grant_dt'].dt.year==2019) & (pubs_df['grant_dt'].dt.month>=7)
sub = pubs_df[mask].copy()

sub = sub[sub['cpc'].notna() & sub['cpc'].str.strip().ne('')]

records = []
for _,row in sub.iterrows():
    try:
        codes = json.loads(row['cpc'])
    except Exception:
        continue
    year = row['grant_dt'].year
    for c in codes:
        code = c.get('code')
        if not code:
            continue
        m = re.match(r'^[A-HY]\d+[A-Z]\d+/?\d*', code)
        grp = m.group(0) if m else code
        records.append({'group': grp, 'year': year})

out = []
if records:
    df = pd.DataFrame(records)
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    years = sorted(counts['year'].unique())
    alpha = 0.1
    ema_rows = []
    for g, gdf in counts.groupby('group'):
        ema = None
        best_year = None
        best_ema = None
        for y in years:
            c = int(gdf[gdf['year']==y]['count'].sum()) if y in gdf['year'].values else 0
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            if best_ema is None or ema>best_ema:
                best_ema = ema
                best_year = y
        ema_rows.append({'group': g, 'best_year': best_year, 'best_ema': best_ema})
    ema_df = pd.DataFrame(ema_rows)
    cpc_df = pd.DataFrame(cpcdefs)[['symbol','titleFull']]
    merged = ema_df.merge(cpc_df, left_on='group', right_on='symbol', how='left')
    merged = merged.sort_values('best_ema', ascending=False)
    for _,r in merged.iterrows():
        out.append({'cpc_group_code': r['group'], 'titleFull': r['titleFull'], 'best_year': int(r['best_year']), 'best_ema': r['best_ema']})

import json as js
res = js.dumps(out)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_jGZ0YzApr2ZRj9WKloXR68ji': 'file_storage/call_jGZ0YzApr2ZRj9WKloXR68ji.json', 'var_call_Vodkb5polttWei6SsAns05ei': 'file_storage/call_Vodkb5polttWei6SsAns05ei.json'}

exec(code, env_args)
