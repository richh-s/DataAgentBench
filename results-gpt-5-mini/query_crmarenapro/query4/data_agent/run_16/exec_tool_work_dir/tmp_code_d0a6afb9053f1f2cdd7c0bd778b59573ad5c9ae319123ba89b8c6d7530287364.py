code = """import pandas as pd
import json

# Access the stored query results
cases = var_call_AvJaP42I2M8Qz01WWSC02b0L
order_items = var_call_6wfwxdz2lwbeEgV0X0LMmmyE

# Create DataFrames
df_cases = pd.DataFrame(cases)
df_orders = pd.DataFrame(order_items)

# Helper to normalize IDs by stripping leading '#'
strip_hash = lambda x: x.lstrip('#') if isinstance(x, str) else x

# Normalize ID fields
if 'orderitemid__c' in df_cases.columns:
    df_cases['orderitemid__c_norm'] = df_cases['orderitemid__c'].astype(str).map(strip_hash)
else:
    df_cases['orderitemid__c_norm'] = None

if 'Id' in df_orders.columns:
    df_orders['Id_norm'] = df_orders['Id'].astype(str).map(strip_hash)
else:
    df_orders['Id_norm'] = None

# Filter cases to only those that match product order items
product_order_ids = set(df_orders['Id_norm'].tolist())

# Parse dates
# Parse without timezone, then localize naive
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
if df_cases['createddate'].dt.tz is not None:
    # convert to naive UTC
    df_cases['createddate'] = df_cases['createddate'].dt.tz_convert(None)

# Define date range (past 10 months as used in original query): 2020-06-10 to 2021-04-10
start_date = pd.to_datetime('2020-06-10')
end_date = pd.to_datetime('2021-04-10')

# Ensure createddate is naive datetime for comparison
if df_cases['createddate'].dt.tz is not None:
    df_cases['createddate'] = df_cases['createddate'].dt.tz_convert(None)

# Filter by date range
df_cases = df_cases[(df_cases['createddate'] >= start_date) & (df_cases['createddate'] <= end_date)]

# Keep only cases linked to the product order items
df_cases = df_cases[df_cases['orderitemid__c_norm'].isin(product_order_ids)].copy()

# If no matching cases, return None
if df_cases.empty:
    result = None
else:
    # Compute month name
    df_cases['month'] = df_cases['createddate'].dt.month_name()
    # Count per month in the period
    ordered_months = ['June','July','August','September','October','November','December','January','February','March','April']
    counts = df_cases.groupby('month').size().reindex(ordered_months, fill_value=0)
    counts_list = counts.tolist()
    months = counts.index.tolist()
    # Compute statistics
    import math
    import statistics
    mean = statistics.mean(counts_list)
    stdev = statistics.pstdev(counts_list) if len(counts_list)>0 else 0
    # Identify max
    max_count = max(counts_list)
    max_idx = counts_list.index(max_count)
    max_month = months[max_idx]
    # Decide significance: max >= mean + 2*stdev
    significant = False
    if stdev == 0:
        significant = False
    else:
        significant = (max_count >= mean + 2*stdev)
    result = max_month if significant else None

# Print result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AvJaP42I2M8Qz01WWSC02b0L': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_6wfwxdz2lwbeEgV0X0LMmmyE': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
