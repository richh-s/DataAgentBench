code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_vJZYSjVsxJJOYaISowzBlj3l
with open(path, 'r') as f:
    pubs = json.load(f)

def parse_country(info):
    m = re.search(r'\b([A-Z]{2})\b', info)
    return m.group(1) if m else None

def parse_date(nl):
    if not nl:
        return None
    nl = nl.replace('dated ','').replace('the ','')
    nl = nl.replace('st','').replace('nd','').replace('rd','').replace('th','')
    for fmt in ['%d %B %Y','%B %d %Y','%d %B, %Y','%B %d, %Y','%d %b %Y','%Y-%m-%d']:
        try:
            return datetime.strptime(nl.strip(), fmt).date()
        except Exception:
            continue
    return None

records = []
for p in pubs:
    country = parse_country(p.get('Patents_info',''))
    if country != 'DE':
        continue
    gd = parse_date(p.get('grant_date'))
    if not gd or gd.year != 2019 or gd.month < 7:
        continue
    cpcs = p.get('cpc')
    if not cpcs:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpcs)]
    except Exception:
        continue
    year = gd.year
    for code in set(codes):
        lvl4 = code[0:3]
        records.append({'year': year,'lvl4': lvl4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['lvl4','year']).size().reset_index(name='count')
    years = sorted(counts['year'].unique())
    alpha = 0.1
    rows = []
    for lvl4, grp in counts.groupby('lvl4'):
        ema = None
        best_ema = None
        best_year = None
        for y in years:
            c = int(grp[grp['year']==y]['count'].iloc[0]) if y in set(grp['year']) else 0
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            if best_ema is None or ema>best_ema:
                best_ema, best_year = ema, y
        rows.append({'lvl4':lvl4,'best_year':best_year,'best_ema':best_ema})
    top = pd.DataFrame(rows).sort_values('best_ema',ascending=False).head(20)
    result = top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vJZYSjVsxJJOYaISowzBlj3l': 'file_storage/call_vJZYSjVsxJJOYaISowzBlj3l.json', 'var_call_mAM7Mt06jb2Uv5bnHfHaZKzI': 'file_storage/call_mAM7Mt06jb2Uv5bnHfHaZKzI.json'}

exec(code, env_args)
