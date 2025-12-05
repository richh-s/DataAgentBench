code = """import json, re, pandas as pd

path = var_call_uMgrK4I3aNzMoFdQ9pkMAooF
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def get_country(text):
    m = re.search(r'\b([A-Z]{2})\b', text)
    return m.group(1) if m else None

df['country'] = df['Patents_info'].apply(get_country)

df_de = df[df['country'] == 'DE'].copy()

from datetime import datetime

month_map = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', date_str)
    if m:
        return int(re.search(r'(20\d{2})', date_str).group(1))
    m = re.search(r'(\d{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December), (20\d{2})', date_str)
    if m:
        return int(m.group(4))
    m = re.search(r'(on )?(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)?, (20\d{2})', date_str)
    if m:
        return int(m.group(4))
    m = re.search(r'(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (20\d{2})', date_str)
    if m:
        return int(m.group(3))
    m = re.search(r'(20\d{2})', date_str)
    return int(m.group(1)) if m else None

# need earlier years too to compute EMA per year, filter to DE only but all years

records = []
for _, row in df_de.iterrows():
    year = parse_year(row['grant_date'])
    if year is None:
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        grp = code.split('/')[0][:4]
        records.append({'year': year, 'group4': grp})

pat_df = pd.DataFrame(records)

if pat_df.empty:
    result = []
else:
    counts = pat_df.groupby(['group4','year']).size().reset_index(name='count')
    alpha = 0.1
    ema_records = []
    for g, sub in counts.groupby('group4'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            if ema is None:
                ema = r['count']
            else:
                ema = alpha * r['count'] + (1-alpha) * ema
            ema_records.append({'group4': g, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    idx = ema_df.groupby('group4')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uMgrK4I3aNzMoFdQ9pkMAooF': 'file_storage/call_uMgrK4I3aNzMoFdQ9pkMAooF.json', 'var_call_MDdcyQVU1kGRYkaHuX65KDTK': 'file_storage/call_MDdcyQVU1kGRYkaHuX65KDTK.json', 'var_call_5xCH3QPkgavY1YwElQWkcFMJ': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
