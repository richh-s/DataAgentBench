code = """import pandas as pd
import json

# load data from storage variables
cases = pd.DataFrame(var_call_kWQ4ysFcll9CevgImOzvwoAa)
orderitems = pd.DataFrame(var_call_roTQSNySkq7GCBiLLOZQJQ9Y)

# helper to clean IDs
def clean_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

cases['orderitemid__c_clean'] = cases['orderitemid__c'].apply(clean_id)
cases['createddate'] = pd.to_datetime(cases['createddate'], utc=True)
orderitems['Id_clean'] = orderitems['Id'].apply(clean_id)

# Define analysis window: July 2020 through April 2021 (10 months ending 2021-04-10)
start = pd.Timestamp('2020-07-01T00:00:00Z')
end = pd.Timestamp('2021-04-10T23:59:59Z')

# Filter cases in window
cases_window = cases[(cases['createddate'] >= start) & (cases['createddate'] <= end)].copy()

# Filter cases where orderitemid matches product's order items
oi_set = set(orderitems['Id_clean'].tolist())
matched = cases_window[cases_window['orderitemid__c_clean'].isin(oi_set)].copy()

# Create month-year column
matched['month_year'] = matched['createddate'].dt.to_period('M')

# Build ordered list of months from start to end inclusive
months = pd.period_range(start=pd.Period('2020-07', freq='M'), end=pd.Period('2021-04', freq='M'), freq='M')
month_names = [m.to_timestamp().strftime('%B') for m in months]
month_keys = [str(m) for m in months]

# Count per month, include zeros
counts = matched.groupby('month_year').size().reindex(months, fill_value=0)
counts_list = [int(x) for x in counts.tolist()]

# Determine if a month significantly exceeds others
import math

if len(counts_list) == 0:
    significant_month = None
else:
    max_count = max(counts_list)
    max_idx = counts_list.index(max_count)
    # second highest
    sorted_counts = sorted(counts_list, reverse=True)
    second = sorted_counts[1] if len(sorted_counts) > 1 else 0
    mean = sum(counts_list)/len(counts_list)
    variance = sum((x-mean)**2 for x in counts_list)/len(counts_list)
    std = math.sqrt(variance)
    # significance rules: either >= mean + 2*std or >= 2*second highest
    if (max_count >= mean + 2*std and max_count > 0) or (second>0 and max_count >= 2*second):
        significant_month = month_names[max_idx]
    else:
        significant_month = None

# Prepare output string (month name or None)
out = json.dumps(significant_month if significant_month is not None else None)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_kWQ4ysFcll9CevgImOzvwoAa': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_roTQSNySkq7GCBiLLOZQJQ9Y': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
