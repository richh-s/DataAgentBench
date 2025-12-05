code = """import json, pandas as pd
from datetime import datetime

order_items = var_call_spQhIIf2eYNHpORsLrbA07Ee

with open(var_call_cF5MfDIHMXBGEZYe4vHqicxr, 'r') as f:
    cases = json.load(f)

oi_ids = set()
for r in order_items:
    oid = r['Id']
    oi_ids.add(oid)
    if oid.startswith('#'):
        oi_ids.add(oid[1:])
    else:
        oi_ids.add('#' + oid)

filtered = []
for c in cases:
    if c['orderitemid__c'] in oi_ids:
        dt = datetime.strptime(c['createddate'], '%Y-%m-%dT%H:%M:%S.%f%z')
        if datetime(2020,6,10,tzinfo=dt.tzinfo) <= dt < datetime(2021,4,11,tzinfo=dt.tzinfo):
            filtered.append({'createddate': c['createddate']})

if not filtered:
    result = None
else:
    df = pd.DataFrame(filtered)
    df['dt'] = pd.to_datetime(df['createddate'])
    df['month'] = df['dt'].dt.to_period('M')
    counts = df.groupby('month').size().reset_index(name='n').sort_values('month')
    if len(counts) < 2:
        top_month_name = counts.iloc[0]['month'].strftime('%B')
    else:
        counts = counts.sort_values('n', ascending=False).reset_index(drop=True)
        top = counts.iloc[0]
        second = counts.iloc[1]
        if top['n'] >= second['n'] + 5:
            top_month_name = top['month'].strftime('%B')
        else:
            top_month_name = None
    result = top_month_name

import json as _json
out = _json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_spQhIIf2eYNHpORsLrbA07Ee': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_cF5MfDIHMXBGEZYe4vHqicxr': 'file_storage/call_cF5MfDIHMXBGEZYe4vHqicxr.json'}

exec(code, env_args)
