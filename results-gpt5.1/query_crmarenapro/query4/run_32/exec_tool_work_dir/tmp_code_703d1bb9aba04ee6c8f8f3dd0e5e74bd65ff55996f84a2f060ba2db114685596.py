code = """import json, pandas as pd
cases = pd.DataFrame(var_call_tHAAUKI9aVrJM2LuHKZ4siNa)
# load full order items
with open(var_call_sDp34dioT2fzzd52Y8ibfD65, 'r') as f:
    order_items = pd.DataFrame(json.load(f))
# normalize IDs by stripping leading '#'
cases['orderitemid__c_norm'] = cases['orderitemid__c'].str.lstrip('#')
order_items['OrderItemId_norm'] = order_items['OrderItemId'].str.lstrip('#')
order_items['Product2Id_norm'] = order_items['Product2Id'].str.lstrip('#')
# filter to target product
target_pid = '01tWt000006hVJdIAM'
order_items_target = order_items[order_items['Product2Id_norm'] == target_pid]
# join
merged = cases.merge(order_items_target, left_on='orderitemid__c_norm', right_on='OrderItemId_norm', how='inner')
if merged.empty:
    result = None
else:
    merged['createddate'] = pd.to_datetime(merged['createddate'])
    merged['month'] = merged['createddate'].dt.to_period('M')
    counts = merged.groupby('month').size().reset_index(name='case_count')
    # past 10 months from 2021-04-10 => 2020-07 to 2021-04 (exclusive of partial?) we'll just use what's there
    counts = counts.sort_values('month')
    # check if a month significantly exceeds others: define as more than mean+std
    mean = counts['case_count'].mean()
    std = counts['case_count'].std(ddof=0)
    threshold = mean + std
    significant = counts[counts['case_count'] > threshold]
    if significant.empty:
        # if none, pick max month
        max_row = counts.loc[counts['case_count'].idxmax()]
    else:
        # pick top significant
        max_row = significant.sort_values('case_count', ascending=False).iloc[0]
    month_name = max_row['month'].strftime('%B')
    result = month_name

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tHAAUKI9aVrJM2LuHKZ4siNa': [{'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_sDp34dioT2fzzd52Y8ibfD65': 'file_storage/call_sDp34dioT2fzzd52Y8ibfD65.json'}

exec(code, env_args)
