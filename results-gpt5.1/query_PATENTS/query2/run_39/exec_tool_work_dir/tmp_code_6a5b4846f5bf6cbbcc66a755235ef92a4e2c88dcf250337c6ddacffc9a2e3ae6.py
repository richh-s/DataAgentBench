code = """import json, re, pandas as pd
from datetime import datetime

path_pubs = var_call_KJYXEAWioXdPdzLmmmtbhrNl
path_def = var_call_UqDU82U7I3z2IXv6vTuKYr3o

with open(path_pubs, 'r') as f:
    pubs = json.load(f)
with open(path_def, 'r') as f:
    defs = json.load(f)

pubs_df = pd.DataFrame(pubs)

pubs_df = pubs_df.dropna(subset=['grant_date','cpc','Patents_info'])

pubs_df = pubs_df[pubs_df['Patents_info'].str.contains(' country code DE', regex=False, na=False)]

def parse_date(s):
    s = s.strip().replace('dated ','')
    s = s.replace('the ','').replace('of ','')
    s = re.sub(r'(st|nd|rd|th)', '', s)
    for fmt in ['%d %B %Y','%B %d %Y','%d %b %Y','%Y-%m-%d']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return None

pubs_df['grant_dt'] = pubs_df['grant_date'].apply(parse_date)

pubs_df = pubs_df.dropna(subset=['grant_dt'])

start = datetime(2019,7,1)
end = datetime(2019,12,31,23,59,59)

pubs_df = pubs_df[(pubs_df['grant_dt']>=start) & (pubs_df['grant_dt']<=end)]

codes = []
for _, row in pubs_df.iterrows():
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for ent in cpc_list:
        code = ent.get('code')
        if not code:
            continue
        m = re.match(r'([A-Z]\d\d[A-Z])', code)
        if not m:
            continue
        lvl4 = m.group(1)
        codes.append({'lvl4': lvl4, 'year': row['grant_dt'].year})

if not codes:
    result = []
else:
    codes_df = pd.DataFrame(codes)
    counts = codes_df.groupby(['lvl4','year']).size().reset_index(name='count')
    years_sorted = sorted(counts['year'].unique())
    alpha = 0.1
    records = []
    for lvl4, grp in counts.groupby('lvl4'):
        grp = grp.set_index('year').reindex(years_sorted, fill_value=0)
        ema = None
        for y in years_sorted:
            c = grp.loc[y,'count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            records.append({'lvl4': lvl4, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(records)
    idx = ema_df.groupby('lvl4')['ema'].idxmax()
    best = ema_df.loc[idx].copy()
    best.rename(columns={'year':'best_year','ema':'best_ema'}, inplace=True)

    defs_df = pd.DataFrame(defs)
    defs_df['level'] = defs_df['level'].astype(float)
    defs_df4 = defs_df[defs_df['level']==4.0][['symbol','titleFull']]

    merged = best.merge(defs_df4, left_on='lvl4', right_on='symbol', how='left')
    merged = merged.sort_values('best_ema', ascending=False)
    final = merged[['lvl4','titleFull','best_year','best_ema']].to_dict(orient='records')
    result = final

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KJYXEAWioXdPdzLmmmtbhrNl': 'file_storage/call_KJYXEAWioXdPdzLmmmtbhrNl.json', 'var_call_UqDU82U7I3z2IXv6vTuKYr3o': 'file_storage/call_UqDU82U7I3z2IXv6vTuKYr3o.json'}

exec(code, env_args)
