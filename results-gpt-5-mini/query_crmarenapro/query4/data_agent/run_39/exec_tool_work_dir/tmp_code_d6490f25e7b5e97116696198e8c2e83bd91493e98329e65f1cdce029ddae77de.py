code = """import pandas as pd
import json
from datetime import datetime
import calendar

# Load data from storage variables
cases = pd.DataFrame(var_call_FixzM2mxsZLguKyFyVZRGAPB)
orderitems = pd.DataFrame(var_call_KEIxFDzdLfTaQsTWjFY3QuwE)

# Normalize IDs: strip leading '#' and whitespace
cases['orderitem_norm'] = cases['orderitemid__c'].astype(str).str.strip().str.lstrip('#')
orderitems['Id_norm'] = orderitems['Id'].astype(str).str.strip().str.lstrip('#')

# Create set of relevant order item ids
relevant_ids = set(orderitems['Id_norm'].unique())

# Filter cases linked to these order items
cases['is_relevant'] = cases['orderitem_norm'].isin(relevant_ids)
relevant_cases = cases[cases['is_relevant']].copy()

# Parse createddate
relevant_cases['created_dt'] = pd.to_datetime(relevant_cases['createddate'], errors='coerce')

# Define the 10-month range based on provided hint: using the queried range 2020-06-10 to 2021-04-10
start = datetime(2020, 6, 1)
end = datetime(2021, 4, 30)

# Build list of months from start to end inclusive
months = []
cur_year = start.year
cur_month = start.month
while (cur_year < end.year) or (cur_year == end.year and cur_month <= end.month):
    months.append((cur_year, cur_month))
    if cur_month == 12:
        cur_month = 1
        cur_year += 1
    else:
        cur_month += 1

# Count relevant cases per month
counts = []
for y, m in months:
    cnt = int(relevant_cases[(relevant_cases['created_dt'].dt.year == y) & (relevant_cases['created_dt'].dt.month == m)].shape[0])
    counts.append({'year': y, 'month': m, 'month_name': calendar.month_name[m], 'count': cnt})

# Compute statistics
counts_df = pd.DataFrame(counts)
mean = counts_df['count'].mean()
std = counts_df['count'].std(ddof=0)  # population std

# Identify month(s) significantly above mean+2*std
threshold = mean + 2 * std
candidates = counts_df[counts_df['count'] > threshold]

if not candidates.empty:
    # choose the month with highest z-score (count - mean) / std
    candidates = candidates.copy()
    if std == 0:
        # if std is zero, any month with count > mean qualifies; pick highest count
        chosen = candidates.sort_values(['count'], ascending=False).iloc[0]
    else:
        candidates['z'] = (candidates['count'] - mean) / std
        chosen = candidates.sort_values('z', ascending=False).iloc[0]
    result = chosen['month_name']
else:
    result = None

# Print result as required
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OsNYLPz9ZBZ53mbesVWBkfC9': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_FixzM2mxsZLguKyFyVZRGAPB': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_tFvhPkBztWhdcpjZhEP838NV': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_KEIxFDzdLfTaQsTWjFY3QuwE': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
