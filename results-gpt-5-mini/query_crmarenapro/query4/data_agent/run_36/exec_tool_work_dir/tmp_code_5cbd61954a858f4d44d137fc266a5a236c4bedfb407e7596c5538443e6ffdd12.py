code = """import pandas as pd
import json
from datetime import datetime

# load data from previous calls
cases = var_call_mk9Z6sEKCzfNsmGyUSpK6VjW
orderitems = var_call_SWSZho9pPxXZdK5VKvmGe4WQ

# Helper to normalize ids (strip whitespace and leading #)
def norm_id(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s.lstrip('#')
    return s.strip()

orderitem_ids = set(norm_id(r.get('Id')) for r in orderitems)

# Build DataFrame for cases
df = pd.DataFrame(cases)
if df.empty:
    result = ""
else:
    # normalize orderitemid__c
    df['orderitem_norm'] = df['orderitemid__c'].apply(norm_id)
    # filter cases linked to given product's order items
    df = df[df['orderitem_norm'].isin(orderitem_ids)].copy()
    if df.empty:
        result = ""
    else:
        # parse createddate
        def parse_dt(s):
            try:
                # handle ISO with timezone
                return datetime.fromisoformat(s.replace('Z', '+00:00'))
            except Exception:
                try:
                    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f%z')
                except Exception:
                    return None
        df['dt'] = df['createddate'].apply(parse_dt)
        df = df[df['dt'].notnull()].copy()
        if df.empty:
            result = ""
        else:
            # Only keep within the 10-month window (2020-06-10 to 2021-04-10)
            start = datetime(2020,6,10)
            end = datetime(2021,4,10,23,59,59)
            df = df[(df['dt'] >= start) & (df['dt'] <= end)].copy()
            if df.empty:
                result = ""
            else:
                # aggregate by year-month
                df['year_month'] = df['dt'].dt.to_period('M')
                counts = df.groupby('year_month').size().reset_index(name='count')
                # compute month names
                counts['year'] = counts['year_month'].dt.year
                counts['month'] = counts['year_month'].dt.month
                counts['month_name'] = counts['dt'] = counts.apply(lambda r: datetime(int(r['year']), int(r['month']), 1).strftime('%B'), axis=1)
                # find top
                counts_sorted = counts.sort_values('count', ascending=False).reset_index(drop=True)
                max_count = int(counts_sorted.loc[0,'count'])
                top_month_name = counts_sorted.loc[0,'month_name']
                # compute statistics
                arr = counts['count'].astype(float)
                mean = arr.mean()
                std = arr.std(ddof=0)
                second = counts_sorted.loc[1,'count'] if len(counts_sorted) > 1 else 0
                significant = False
                if max_count >= mean + 2*std:
                    significant = True
                if second>0 and max_count >= 1.5 * second:
                    significant = True
                result = top_month_name if significant else ""

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mk9Z6sEKCzfNsmGyUSpK6VjW': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_SWSZho9pPxXZdK5VKvmGe4WQ': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
