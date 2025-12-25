code = """import json, re, pandas as pd

# Load full large results if needed
pub_file = var_call_4qWvRrGKEgebcoaqqVns2aFX
cpcdef_file = var_call_ZbXBjW4HD6aTUtoVoz3VQmbP

with open(pub_file, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_file, 'r') as f:
    cpcdef_data = json.load(f)

# Filter to Germany using Patents_info country code 'DE '
pat_de = []
for r in pub_data:
    if ' DE ' in r['Patents_info'] or ' DE-' in r['Patents_info']:
        pat_de.append(r)

# Parse grant year from natural language grant_date
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

from datetime import datetime

def parse_year(date_str):
    # find 4-digit year
    m = re.search(r'(19|20)\\d{2}', date_str)
    if m:
        return int(m.group(0))
    return None

# build dataframe with year and CPC codes
rows = []
for r in pat_de:
    y = parse_year(r.get('grant_date','') or '')
    if y is None:
        continue
    try:
        cpc_list = json.loads(r.get('cpc') or '[]')
    except Exception:
        continue
    codes = [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('code')]
    for code in codes:
        # level 4 group code approximation: first 3 chars (section+class)?? but CPC level 4 likely section+class; use first 3
        group = code.split('/')[0][:3]
        rows.append({'year': y, 'group': group})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='filings')
    # compute EMA per group over years sorted
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            if ema is None:
                ema = row['filings']
            else:
                ema = alpha*row['filings'] + (1-alpha)*ema
            ema_rows.append({'group': g, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # find best year (max ema) for each group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # attach titles from cpcdef level 4
    cpc_df = pd.DataFrame(cpcdef_data)
    cpc_df['symbol'] = cpc_df['symbol'].astype(str)
    best = best.merge(cpc_df[['symbol','titleFull']], left_on='group', right_on='symbol', how='left')
    best = best.sort_values('ema', ascending=False)
    result = best.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4qWvRrGKEgebcoaqqVns2aFX': 'file_storage/call_4qWvRrGKEgebcoaqqVns2aFX.json', 'var_call_ZbXBjW4HD6aTUtoVoz3VQmbP': 'file_storage/call_ZbXBjW4HD6aTUtoVoz3VQmbP.json', 'var_call_nE63h5KLATdS4hiwoWS4Dviq': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}]}

exec(code, env_args)
