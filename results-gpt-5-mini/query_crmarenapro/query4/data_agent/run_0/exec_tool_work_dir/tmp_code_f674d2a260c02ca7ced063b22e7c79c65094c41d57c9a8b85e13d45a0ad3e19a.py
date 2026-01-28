code = """import json
from datetime import datetime
import pandas as pd

# load data from storage
cases = var_call_8JV2qbPDI06gQEQYga2oQbiZ
orderitems = var_call_VX7xN4seBImGeoACIhbewWnm

# normalize ids helper
def norm_id(s):
    if s is None:
        return s
    return s.strip().lstrip('#')

order_ids = set(norm_id(r['Id']) for r in orderitems)

# parse cases and filter by orderitem id
rows = []
for r in cases:
    oid = r.get('orderitemid__c')
    if oid is None:
        continue
    if norm_id(oid) in order_ids:
        cd = r.get('createddate')
        try:
            dt = datetime.strptime(cd[:19], '%Y-%m-%dT%H:%M:%S')
        except Exception:
            # try alternative formats
            try:
                dt = datetime.fromisoformat(cd)
            except Exception:
                continue
        rows.append({'created': dt, 'orderitemid': norm_id(oid)})

if not rows:
    result = ''
else:
    df = pd.DataFrame(rows)
    # determine past 10 months relative to 2021-04-10
    end_date = datetime(2021,4,10)
    # months from 2020-07 to 2021-04 inclusive
    months = []
    start_year = 2020
    start_month = 7
    for i in range(10):
        m = start_month + i
        y = start_year + (m-1)//12
        mm = ((m-1)%12)+1
        months.append((y, mm))
    # build month labels
    month_labels = { (y,m): datetime(y,m,1).strftime('%B') for (y,m) in months }

    # count occurrences per month-year
    counts = { (y,m): 0 for (y,m) in months }
    for dt in df['created']:
        key = (dt.year, dt.month)
        if key in counts:
            counts[key] += 1
    # prepare sorted list
    items = sorted(counts.items(), key=lambda x: (x[0][0], x[0][1]))
    # find top and second
    sorted_by_count = sorted(items, key=lambda x: x[1], reverse=True)
    top_count = sorted_by_count[0][1]
    top_key = sorted_by_count[0][0]
    second_count = sorted_by_count[1][1] if len(sorted_by_count) > 1 else 0

    # significance rule: top >= 1.5 * second OR second == 0 and top >=2
    significant = False
    if second_count == 0:
        if top_count >= 2:
            significant = True
    else:
        if top_count >= 1.5 * second_count:
            significant = True

    if significant and top_count>0:
        result = month_labels.get(top_key, '')
    else:
        result = ''

# print result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8JV2qbPDI06gQEQYga2oQbiZ': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_VX7xN4seBImGeoACIhbewWnm': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
