code = """import pandas as pd
import json
import calendar

# Data from previous queries
cases = pd.DataFrame(var_call_NLMD7hODCYfE1WPziV51Y4lQ)
orderitems = pd.DataFrame(var_call_ldwHLsFvZU7AmqgFc8M3FEtt)

# Clean potential leading '#' in ids
cases['orderitemid_clean'] = cases['orderitemid__c'].astype(str).str.lstrip('#')
orderitems['Id_clean'] = orderitems['Id'].astype(str).str.lstrip('#')
orderitems['Product2Id_clean'] = orderitems['Product2Id'].astype(str).str.lstrip('#')

# Target product id
target_pid = '01tWt000006hVJdIAM'

# Find order item ids that map to target product
oi_for_target = set(orderitems.loc[orderitems['Product2Id_clean'] == target_pid, 'Id_clean'].tolist())

# Filter cases whose orderitem matches
cases_target = cases[cases['orderitemid_clean'].isin(oi_for_target)].copy()

# Parse createddate
cases_target['createddate_parsed'] = pd.to_datetime(cases_target['createddate'], errors='coerce')

# Define the 10-month window: from 2020-06 to 2021-03 inclusive
months = []
start_year, start_month = 2020, 6
for i in range(10):
    y = start_year + (start_month - 1 + i) // 12
    m = (start_month - 1 + i) % 12 + 1
    months.append((y, m))

# Count per month
counts = []
for y, m in months:
    cnt = int(((cases_target['createddate_parsed'].dt.year == y) & (cases_target['createddate_parsed'].dt.month == m)).sum())
    counts.append({'year': y, 'month': m, 'count': cnt})

# Compute significance: month count > mean + 2*std
import math
vals = [c['count'] for c in counts]
mean = sum(vals)/len(vals) if len(vals)>0 else 0
std = (sum((v-mean)**2 for v in vals)/len(vals))**0.5 if len(vals)>0 else 0

significant_month = None
if std > 0:
    threshold = mean + 2*std
    # find months exceeding threshold
    candidates = []
    for c in counts:
        if c['count'] > threshold:
            z = (c['count'] - mean) / std
            candidates.append((z, c))
    if candidates:
        # pick highest z
        candidates.sort(reverse=True, key=lambda x: x[0])
        best = candidates[0][1]
        significant_month = calendar.month_name[best['month']]
else:
    significant_month = None

# If none found, result should be None
result = significant_month if significant_month is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NLMD7hODCYfE1WPziV51Y4lQ': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_ldwHLsFvZU7AmqgFc8M3FEtt': [{'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795XwIAI', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt00000796JtIAI', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797r5IAA', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '802Wt00000798OvIAI', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '802Wt00000798aDIAQ', 'Product2Id': '01tWt000006hV58IAE'}, {'Id': '802Wt00000799uTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt0000079A2ZIAU', 'Product2Id': '01tWt000006hV57IAE'}]}

exec(code, env_args)
