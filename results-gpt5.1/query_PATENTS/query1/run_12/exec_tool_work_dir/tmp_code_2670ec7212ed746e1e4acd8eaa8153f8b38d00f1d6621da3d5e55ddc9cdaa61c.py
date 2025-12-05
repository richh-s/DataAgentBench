code = """import json, pandas as pd, re, os
from datetime import datetime

path = var_call_XaIsOM9dH6FjPH9PTT2AbHm7
with open(path, 'r') as f:
    data = json.load(f)

months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}

rows = []
for rec in data:
    dstr = rec['publication_date']
    if not dstr:
        continue
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)', dstr)
    y = re.search(r'(20[0-2][0-9])', dstr)
    if not y:
        continue
    year = int(y.group(1))
    if year>2022 or year<2000:
        continue
    month = 1
    if m:
        mon = m.group(1)
        mon_full = {'Jan':'January','Feb':'February','Mar':'March','Apr':'April','Jun':'June','Jul':'July','Aug':'August','Sep':'September','Sept':'September','Oct':'October','Nov':'November','Dec':'December'}.get(mon,mon)
        month = months.get(mon_full,1)
    try:
        cpcs = json.loads(rec['cpc'])
    except:
        continue
    for c in cpcs:
        code = c.get('code')
        if not code:
            continue
        rows.append({'year':year,'code':code})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['year','code']).size().reset_index(name='count')
    years = sorted(counts['year'].unique())
    alpha = 0.2
    records = []
    for code, g in counts.groupby('code'):
        g = g.set_index('year').reindex(years, fill_value=0)
        ema = None
        for y in years:
            c = g.loc[y,'count']
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            records.append({'code':code,'year':y,'ema':ema})
    ema_df = pd.DataFrame(records)
    idx = ema_df.groupby('code')['ema'].idxmax()
    best = ema_df.loc[idx]
    best_2022 = best[best['year']==2022]
    codes_2022 = sorted(best_2022['code'].unique())
    result = codes_2022

import json as _j
print("__RESULT__:")
print(_j.dumps(result))"""

env_args = {'var_call_pSn9f1c4ijx25IEKBYNHZCRC': 'file_storage/call_pSn9f1c4ijx25IEKBYNHZCRC.json', 'var_call_wSFZcXxVm5fstNPLa85nH4Nj': ['publicationinfo'], 'var_call_ZCo69geLxy1ghdtlXyIt7R0B': ['cpc_definition'], 'var_call_XaIsOM9dH6FjPH9PTT2AbHm7': 'file_storage/call_XaIsOM9dH6FjPH9PTT2AbHm7.json'}

exec(code, env_args)
