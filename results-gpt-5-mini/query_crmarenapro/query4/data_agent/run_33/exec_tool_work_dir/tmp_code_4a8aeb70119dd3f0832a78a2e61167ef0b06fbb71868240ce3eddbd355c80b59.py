code = """import json
import pandas as pd
from collections import Counter

# Load previous tool results from storage variables
cases = var_call_L8xUNfVSc4n9NvkII8em3KQY
orderitems_path = var_call_iODsxluEu1rLKnNMfksbVsrp

# Read the OrderItem full result from file
with open(orderitems_path, 'r') as f:
    orderitems = json.load(f)

# Normalize function to strip leading # and whitespace and make exact
def norm_id(x):
    if x is None:
        return None
    if not isinstance(x, str):
        x = str(x)
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Target product id
target = '01tWt000006hVJdIAM'

# Build set of OrderItem Ids for target product
orderitems_df = pd.DataFrame(orderitems)
orderitems_df['norm_Product2Id'] = orderitems_df['Product2Id'].apply(norm_id)
orderitems_df['norm_Id'] = orderitems_df['Id'].apply(norm_id)
matched_orderitem_ids = set(orderitems_df.loc[orderitems_df['norm_Product2Id'] == target, 'norm_Id'].tolist())

# Process cases
cases_df = pd.DataFrame(cases)
# Normalize orderitemid__c
if 'orderitemid__c' not in cases_df.columns:
    cases_df['orderitemid__c'] = None
cases_df['norm_orderitemid'] = cases_df['orderitemid__c'].apply(norm_id)
# Filter cases that reference matched order items
matched_cases = cases_df[cases_df['norm_orderitemid'].isin(matched_orderitem_ids)].copy()

# Parse createddate to datetime and extract month name
matched_cases['createddate'] = pd.to_datetime(matched_cases['createddate'], errors='coerce')
matched_cases = matched_cases.dropna(subset=['createddate'])
matched_cases['month_name'] = matched_cases['createddate'].dt.strftime('%B')
matched_cases['month_year'] = matched_cases['createddate'].dt.strftime('%Y-%m')

# Count per month (month_year) and keep month name
counts = matched_cases.groupby(['month_year','month_name']).size().reset_index(name='count')
# Sort by month_year chronologically
counts = counts.sort_values('month_year')

# Determine if any month significantly exceeds others: use threshold mean + 2*std
counts_only = counts['count'].astype(float)
mean = counts_only.mean() if len(counts_only)>0 else 0.0
std = counts_only.std(ddof=0) if len(counts_only)>0 else 0.0
threshold = mean + 2*std

# Find months meeting threshold
sig = counts[counts['count'] >= threshold]

# Choose result month_name: if any significant, pick the one with highest count; else pick the month with max count if exists
result_month = None
if len(sig) > 0:
    # pick highest count among significant
    top = sig.sort_values(['count','month_year'], ascending=[False, True]).iloc[0]
    result_month = top['month_name']
else:
    if len(counts) > 0:
        top = counts.sort_values(['count','month_year'], ascending=[False, True]).iloc[0]
        # But only return it if it's noticeably higher than others: require it > mean + std
        if top['count'] > mean + std:
            result_month = top['month_name']
        else:
            result_month = None

# Prepare output string
out = result_month if result_month is not None else "None"

# Print according to required format
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_L8xUNfVSc4n9NvkII8em3KQY': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_xRSlnCjGQT8ebcF3CxdEaMdA': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_iODsxluEu1rLKnNMfksbVsrp': 'file_storage/call_iODsxluEu1rLKnNMfksbVsrp.json'}

exec(code, env_args)
