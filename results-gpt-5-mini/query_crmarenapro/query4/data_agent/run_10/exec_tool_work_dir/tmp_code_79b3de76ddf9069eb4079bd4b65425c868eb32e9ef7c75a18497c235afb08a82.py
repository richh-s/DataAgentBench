code = """import json
import pandas as pd
from datetime import datetime

# load data from previous tool calls
cases = var_call_IzuN5BLQW7YB5zxrDm1DOUtQ
order_items = var_call_1wLIiiFwptuYZOSiEQUE1Fg4

# normalize ids: strip leading '#' and whitespace
for r in cases:
    if r.get('id'):
        r['id'] = r['id'].lstrip('#').strip()
    if r.get('orderitemid__c'):
        r['orderitemid__c'] = r['orderitemid__c'].lstrip('#').strip()
    # parse createddate
    try:
        r['created_dt'] = pd.to_datetime(r['createddate'])
    except Exception:
        r['created_dt'] = None

for r in order_items:
    if r.get('Id'):
        r['Id'] = r['Id'].lstrip('#').strip()

# build set of order item ids for the given product
product_order_ids = set([r['Id'] for r in order_items if r.get('Id')])

# Define analysis window: past 10 months relative to 2021-04-10
end_date = pd.to_datetime('2021-04-10')
# We'll consider the 10 full months prior to end_date's month: from 2020-06-01 to 2021-03-31
start_month = (end_date.replace(day=1) - pd.DateOffset(months=10))
start_date = start_month
# end of last full month
last_full_month_end = (end_date.replace(day=1) - pd.DateOffset(days=1)).replace(hour=23, minute=59, second=59)

# Filter cases for those linked to product order items and within the 10-month window
filtered = []
for r in cases:
    if not r.get('created_dt') or not r.get('orderitemid__c'):
        continue
    if r['orderitemid__c'] in product_order_ids:
        if r['created_dt'] >= start_date and r['created_dt'] <= last_full_month_end:
            filtered.append(r)

# Create month labels Jun 2020 .. Mar 2021
months = pd.date_range(start=start_date, end=last_full_month_end, freq='MS')
month_names = [dt.strftime('%B') for dt in months]
month_keys = [dt.strftime('%Y-%m') for dt in months]

# Count per month
counts = {k: 0 for k in month_keys}
for r in filtered:
    key = r['created_dt'].strftime('%Y-%m')
    if key in counts:
        counts[key] += 1

# Compute statistics
vals = list(counts.values())
import math
mean = sum(vals)/len(vals) if vals else 0
var = sum((x-mean)**2 for x in vals)/len(vals) if vals else 0
std = math.sqrt(var)

# Determine if any month significantly exceeds others: > mean + 2*std
significant_month = None
significant_value = None
threshold = mean + 2*std
for k, v in counts.items():
    if v > threshold:
        if significant_month is None or v > significant_value:
            significant_month = k
            significant_value = v

if significant_month:
    # convert to month name
    out = datetime.strptime(significant_month + '-01', '%Y-%m-%d').strftime('%B')
else:
    out = None

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nHuSh199l6lljnkBjF40nCj3': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_noJoH8IGF4QF3m2rPzXGUMSy': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_IzuN5BLQW7YB5zxrDm1DOUtQ': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_1wLIiiFwptuYZOSiEQUE1Fg4': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
