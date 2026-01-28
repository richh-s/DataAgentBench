code = """import json
import pandas as pd
from datetime import datetime

# Load data from previous tool calls
cases = pd.DataFrame(var_call_OsX7i763HAVK1Iw4ZvI26X1E)
orderitems = pd.DataFrame(var_call_HcZAhgT8EuZC8IWhacErMDMH)

# Normalize IDs: strip leading '#' and whitespace
cases['orderitemid_norm'] = cases['orderitemid__c'].astype(str).str.strip().str.lstrip('#')
orderitems['Id_norm'] = orderitems['Id'].astype(str).str.strip().str.lstrip('#')
orderitems['Product2Id_norm'] = orderitems['Product2Id'].astype(str).str.strip().str.lstrip('#')

# Merge cases with orderitem product mapping
merged = cases.merge(orderitems, left_on='orderitemid_norm', right_on='Id_norm', how='left')

# Target product id
target = '01tWt000006hVJdIAM'

# Filter to target product (after normalizing)
filtered = merged[merged['Product2Id_norm'] == target].copy()

# If no filtered rows, result is None
if filtered.empty:
    result = 'None'
else:
    # Parse createddate
    filtered['created_dt'] = pd.to_datetime(filtered['createddate'], errors='coerce')
    # Restrict to past 10 months window: 2020-07-01 to 2021-04-10 (inclusive)
    start = datetime(2020,7,1)
    end = datetime(2021,4,10,23,59,59)
    filtered = filtered[(filtered['created_dt'] >= start) & (filtered['created_dt'] <= end)]

    # Build list of month periods (YYYY-MM) for the 10-month span
    months = []
    cur = datetime(2020,7,1)
    while cur <= datetime(2021,4,1):
        months.append(cur.strftime('%Y-%m'))
        # advance one month
        if cur.month == 12:
            cur = datetime(cur.year+1, 1, 1)
        else:
            cur = datetime(cur.year, cur.month+1, 1)

    # Count cases per month
    filtered['period'] = filtered['created_dt'].dt.strftime('%Y-%m')
    counts = filtered.groupby('period').size().reindex(months, fill_value=0)

    # Statistical test: significant if count > mean + 2*std
    mean = counts.mean()
    std = counts.std(ddof=0)
    threshold = mean + 2*std
    significant = counts[counts > threshold]

    if significant.empty:
        result = 'None'
    else:
        # pick month with highest count among significant ones
        top_period = significant.idxmax()
        year, mon = top_period.split('-')
        month_name = datetime(int(year), int(mon), 1).strftime('%B')
        result = month_name

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OsX7i763HAVK1Iw4ZvI26X1E': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_HcZAhgT8EuZC8IWhacErMDMH': [{'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795XwIAI', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt00000796JtIAI', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797r5IAA', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '802Wt00000798OvIAI', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '802Wt00000798aDIAQ', 'Product2Id': '01tWt000006hV58IAE'}, {'Id': '802Wt00000799uTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt0000079A2ZIAU', 'Product2Id': '01tWt000006hV57IAE'}]}

exec(code, env_args)
