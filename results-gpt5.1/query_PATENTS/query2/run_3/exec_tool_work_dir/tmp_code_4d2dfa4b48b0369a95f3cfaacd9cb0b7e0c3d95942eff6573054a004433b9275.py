code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_6pf3cTsXt2rNzl3xbHUBVr4K
with open(path, 'r') as f:
    pubs = json.load(f)

pub_df = pd.DataFrame(pubs)

country_pattern = re.compile(r'\b(DE)\b')
pub_df = pub_df[pub_df['Patents_info'].astype(str).str.contains(country_pattern)]

months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_date(s):
    if not isinstance(s, str):
        return None
    s = s.strip()
    s = re.sub(r'^(dated|on)\s+', '', s)
    s = s.replace('of ', '')
    s = s.replace(',', '')
    s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
    parts = s.split()
    if len(parts) == 3:
        if parts[0].isalpha():
            month = parts[0]
            day = parts[1]
        else:
            day = parts[0]
            month = parts[1]
        try:
            if month in months:
                m = months[month]
            else:
                dt = datetime.strptime(month, '%b')
                m = dt.month
            return datetime(int(parts[2]), m, int(day))
        except Exception:
            return None
    return None

pub_df['grant_dt'] = pub_df['grant_date'].apply(parse_date)

pub_df = pub_df[pub_df['grant_dt'].notna()]

mask = (pub_df['grant_dt'] >= datetime(2019,7,1)) & (pub_df['grant_dt'] <= datetime(2019,12,31))
sub = pub_df[mask].copy()
sub = sub[sub['cpc'].notna()]

sub['year'] = sub['grant_dt'].apply(lambda x: x.year)

def level4(code):
    return code[:3]

records = []
for _, row in sub.iterrows():
    try:
        cpcs = json.loads(row['cpc'])
    except Exception:
        continue
    for ent in cpcs:
        code = ent.get('code')
        if not code:
            continue
        grp = level4(code)
        records.append({'group': grp, 'year': row['year']})

cpc_df = pd.DataFrame(records)

if cpc_df.empty:
    out = []
else:
    counts = cpc_df.groupby(['group','year']).size().reset_index(name='count')
    alpha = 0.1
    ema_rows = []
    for grp, g in counts.groupby('group'):
        g = g.sort_values('year')
        ema = None
        for _, r in g.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'group': grp, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    cpc_defs = pd.DataFrame(var_call_PH5gwB2MahmArTyp1ZQU3ZnW)
    cpc_defs['level_num'] = cpc_defs['level'].astype(float)
    level4_defs = cpc_defs[cpc_defs['level_num'] == 4.0][['symbol','titleFull']]

    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    result = best.merge(level4_defs, left_on='group', right_on='symbol', how='left')
    result = result.sort_values('ema', ascending=False)

    out = []
    for _, r in result.iterrows():
        out.append({
            'cpc_group_code': r['group'],
            'titleFull': r.get('titleFull'),
            'best_year': r['year'],
            'max_ema_filings': r['ema']
        })

    out = sorted(out, key=lambda x: x['max_ema_filings'], reverse=True)[:20]

res_json = json.dumps(out)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_6pf3cTsXt2rNzl3xbHUBVr4K': 'file_storage/call_6pf3cTsXt2rNzl3xbHUBVr4K.json', 'var_call_PH5gwB2MahmArTyp1ZQU3ZnW': 'file_storage/call_PH5gwB2MahmArTyp1ZQU3ZnW.json', 'var_call_0WOtW4jnLouyzYiPT4BnRxD4': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
