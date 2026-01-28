code = """import json
import pandas as pd

# load data from previous tool calls
cases = pd.DataFrame(var_call_2QhwoGOmVfG7XNf40rrCL4HT)
orderitems = pd.DataFrame(var_call_O69nyfOVTevq93CwFrPWBH8j)

# Normalize ID-like fields by stripping leading '#'
cases['orderitemid_norm'] = cases['orderitemid__c'].astype(str).str.lstrip('#').str.strip()
orderitems['Id_norm'] = orderitems['Id'].astype(str).str.lstrip('#').str.strip()
orderitems['Product2Id_norm'] = orderitems['Product2Id'].astype(str).str.lstrip('#').str.strip()

# Target product id normalized
target_pid = '01tWt000006hVJdIAM'

# Find order item IDs linked to target product
target_order_ids = orderitems.loc[orderitems['Product2Id_norm'] == target_pid, 'Id_norm'].unique().tolist()

# Filter cases for those order items
cases_target = cases.loc[cases['orderitemid_norm'].isin(target_order_ids)].copy()

# If no cases, return None
if cases_target.empty:
    result = None
else:
    # Parse createddate and get month names
    cases_target['created_dt'] = pd.to_datetime(cases_target['createddate'], errors='coerce')
    cases_target = cases_target.dropna(subset=['created_dt'])
    cases_target['month_name'] = cases_target['created_dt'].dt.strftime('%B')

    # Count per month
    counts = cases_target['month_name'].value_counts().sort_index()

    # Compute mean and std
    mean = counts.mean()
    std = counts.std(ddof=0)  # population std

    # Determine significant if count > mean + 2*std
    if std == 0:
        # If std zero, no variance; then no significant month unless one count > mean
        significant = counts[counts > mean]
    else:
        threshold = mean + 2 * std
        significant = counts[counts > threshold]

    if significant.empty:
        result = None
    else:
        # pick month with highest z-score among significant
        z_scores = (counts - mean) / (std if std != 0 else 1)
        # select only months present in significant
        sig_month = z_scores[significant.index].idxmax()
        result = sig_month

# Prepare output
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2QhwoGOmVfG7XNf40rrCL4HT': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_O69nyfOVTevq93CwFrPWBH8j': [{'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795XwIAI', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt00000796JtIAI', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797r5IAA', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '802Wt00000798OvIAI', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '802Wt00000798aDIAQ', 'Product2Id': '01tWt000006hV58IAE'}, {'Id': '802Wt00000799uTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt0000079A2ZIAU', 'Product2Id': '01tWt000006hV57IAE'}]}

exec(code, env_args)
