code = """import pandas as pd
import json

df_cases = pd.DataFrame(var_call_eGrCxCZnxOQ0HvGoCyer5DY5)
df_orderitems = pd.DataFrame(var_call_3WMin5WyeQjiWejfl2g8Veb9)

# Clean IDs by removing leading # and trailing whitespace
for col in ['id','orderitemid__c']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].astype(str).str.strip().str.lstrip('#')

if 'Id' in df_orderitems.columns:
    df_orderitems['Id'] = df_orderitems['Id'].astype(str).str.strip().str.lstrip('#')
if 'Product2Id' in df_orderitems.columns:
    df_orderitems['Product2Id'] = df_orderitems['Product2Id'].astype(str).str.strip().str.lstrip('#')

# Merge cases with orderitems on order item id
merged = df_cases.merge(df_orderitems, left_on='orderitemid__c', right_on='Id', how='left')

# Filter for the target product id
target = '01tWt000006hVJdIAM'
merged_target = merged[merged['Product2Id'] == target].copy()

# If no records, result is None
if merged_target.empty:
    result = None
else:
    # parse createddate and extract month name
    merged_target['createddate'] = pd.to_datetime(merged_target['createddate'], errors='coerce')
    merged_target = merged_target.dropna(subset=['createddate'])
    merged_target['month'] = merged_target['createddate'].dt.strftime('%B')
    counts = merged_target['month'].value_counts().to_dict()
    # Compute if any month significantly exceeds others: > mean + 2*std
    import math
    vals = list(counts.values())
    mean = sum(vals)/len(vals)
    std = (sum((x-mean)**2 for x in vals)/len(vals))**0.5 if len(vals)>0 else 0
    threshold = mean + 2*std
    # Find months above threshold
    above = {m:c for m,c in counts.items() if c > threshold}
    if above:
        # choose the month with highest count among above
        month = max(above.items(), key=lambda x: (x[1], x[0]))[0]
        result = month
    else:
        # No significant month
        result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eGrCxCZnxOQ0HvGoCyer5DY5': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_3WMin5WyeQjiWejfl2g8Veb9': [{'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795XwIAI', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt00000796JtIAI', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797r5IAA', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '802Wt00000798OvIAI', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '802Wt00000798aDIAQ', 'Product2Id': '01tWt000006hV58IAE'}, {'Id': '802Wt00000799uTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt0000079A2ZIAU', 'Product2Id': '01tWt000006hV57IAE'}]}

exec(code, env_args)
