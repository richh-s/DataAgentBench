code = """import json, re, pandas as pd
from datetime import datetime

# Load large results from files
with open(var_call_7efAjmWglTLqUppZobHoSDiQ, 'r') as f:
    pubs = json.load(f)
with open(var_call_r3H7hpKzjAPQgYm4FbqAMcVG, 'r') as f:
    cpc_defs = json.load(f)

# Helper to extract country code from Patents_info (assumes pattern "In XX," or "In US," etc. or "In Germany"; but we know it's US-focused text, so instead look for "In DE," or " in Germany"). Here, however, Patents_info structure in preview uses "In US, the application" or "holds the US patent"; country code is embedded like "US patent". To get Germany, search for "DE patent" or " In Germany" or "German". This dataset may not actually contain Germany patents, but we'll filter by pattern including " German " or "Germany" or " DE patent" or " DE-".

def is_germany(pinfo: str) -> bool:
    txt = pinfo.lower()
    if ' germany' in txt or ' german ' in txt:
        return True
    if ' de patent' in txt or ' de-20' in txt or ' de-10' in txt:
        return True
    if ' the de patent' in txt:
        return True
    return False

# Parse natural language grant_date, keep those in H2 2019

month_map = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

ord_map = {'st':'','nd':'','rd':'','th':''}


def parse_date(s):
    if not s or not isinstance(s,str):
        return None
    s = s.strip()
    s = s.replace('dated ','').replace('date of ','')
    # examples: "3rd August 2021", "21st of September, 2021", "6th October 2020"
    # remove commas
    s2 = s.replace(',', '')
    parts = s2.split()
    if len(parts) < 3:
        return None
    # find day (first token)
    day_token = parts[0]
    day = re.sub(r'(st|nd|rd|th)$','',day_token)
    try:
        day = int(day)
    except:
        return None
    # month is next word that matches a month
    month = None
    year = None
    for p in parts[1:]:
        if p in month_map:
            month = month_map[p]
        elif re.match(r'^\d{4}$', p):
            year = int(p)
    if not month or not year:
        return None
    try:
        return datetime(year, month, day)
    except:
        return None


filtered = []
for r in pubs:
    if not is_germany(r.get('Patents_info','')):
        continue
    d = parse_date(r.get('grant_date'))
    if not d:
        continue
    if d.year == 2019 and d.month >= 7:
        # second half 2019
        filtered.append({'date': d, 'cpc': r.get('cpc')})

# If no German patents in H2 2019, we'll handle later

# Parse CPC JSON-like field

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        return [e.get('code') for e in data if isinstance(e, dict) and e.get('code')]
    except Exception:
        return []

records = []
for r in filtered:
    codes = extract_cpc_codes(r['cpc'])
    year = r['date'].year
    for code in codes:
        # Level 4 group is the first 3 characters (section+class) like C01, B29, etc.
        group = code[:3]
        records.append({'year': year, 'group': group})

if not records:
    result = {'error': 'No German patents with grants in H2 2019 found in the dataset, so the requested analysis cannot be performed.'}
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['year','group']).size().reset_index(name='count')
    # sort by year
    counts = counts.sort_values(['group','year'])
    # compute EMA with alpha=0.1 per group over years
    ema_list = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_list.append({'group': g, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_list)
    # best year per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # join with cpc_defs to get titleFull
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    best = best.merge(defs_df[['symbol','titleFull']], left_on='group', right_on='symbol', how='left')
    best.rename(columns={'symbol':'cpc_group_code','titleFull':'title_full','year':'best_year','ema':'ema_value'}, inplace=True)
    best = best[['cpc_group_code','title_full','best_year','ema_value']].sort_values('ema_value', ascending=False)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7efAjmWglTLqUppZobHoSDiQ': 'file_storage/call_7efAjmWglTLqUppZobHoSDiQ.json', 'var_call_r3H7hpKzjAPQgYm4FbqAMcVG': 'file_storage/call_r3H7hpKzjAPQgYm4FbqAMcVG.json'}

exec(code, env_args)
