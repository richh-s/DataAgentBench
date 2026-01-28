code = """import pandas as pd
import json

# Load data from previous query results available in storage
cases = pd.DataFrame(var_call_HvkQb0BOMaILSaSFulbzJtlU)
order_items = pd.DataFrame(var_call_MrzTdDfvalrEyVIeWFyFgQjT)

# Normalize ID-like fields by stripping whitespace and leading '#'
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#')

cases['orderitem_clean'] = cases['orderitemid__c'].apply(clean_id)
order_items['id_clean'] = order_items['Id'].apply(clean_id)

# Filter cases whose orderitemid__c is in the product order items
product_order_ids = set(order_items['id_clean'].tolist())
matched = cases[cases['orderitem_clean'].isin(product_order_ids)].copy()

# Parse createddate with utc timezone, then convert to naive by removing tzinfo
matched['created_dt'] = pd.to_datetime(matched['createddate'], errors='coerce', utc=True)
matched['created_dt'] = matched['created_dt'].dt.tz_convert(None)

# Define analysis window (past 10 months from 2021-04-10 as used in initial query)
start = pd.to_datetime('2020-06-10').tz_localize(None)
end = pd.to_datetime('2021-04-10').tz_localize(None)

# Generate list of month starts between start and end (inclusive)
month_starts = pd.date_range(start=start.normalize().replace(day=1), end=end, freq='MS')
# We'll consider months from the month of start to month of end inclusive
months = [(dt.year, dt.month) for dt in month_starts]

# Count matched cases per (year,month)
counts = {}
for y,m in months:
    counts[(y,m)] = 0

for _, row in matched.iterrows():
    dt = row['created_dt']
    if pd.isna(dt):
        continue
    # Only include if within window
    if dt < start or dt > end:
        continue
    key = (dt.year, dt.month)
    if key in counts:
        counts[key] += 1

# Prepare list of month labels and counts
month_labels = []
count_values = []
for (y,m) in months:
    label = pd.Timestamp(year=y, month=m, day=1).strftime('%B')
    month_labels.append(label)
    count_values.append(counts[(y,m)])

# Compute statistics
import math
n = len(count_values)
mean = sum(count_values)/n if n>0 else 0
# population std
variance = sum((x-mean)**2 for x in count_values)/n if n>0 else 0
std = math.sqrt(variance)
threshold = mean + 2*std

# Find months exceeding threshold
exceeding = []
for label, cnt, (y,m) in zip(month_labels, count_values, months):
    if cnt > threshold:
        # store (label, cnt, zscore)
        z = (cnt - mean) / std if std>0 else float('inf')
        exceeding.append((label, cnt, z, y, m))

result_month = None
if len(exceeding) == 1:
    result_month = exceeding[0][0]
elif len(exceeding) > 1:
    # pick highest z-score
    exceeding.sort(key=lambda x: x[2], reverse=True)
    result_month = exceeding[0][0]
else:
    result_month = None

# If none exceeded, return None
print("__RESULT__:")
print(json.dumps(result_month))"""

env_args = {'var_call_HvkQb0BOMaILSaSFulbzJtlU': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_MrzTdDfvalrEyVIeWFyFgQjT': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
