code = """import pandas as pd
import json

# Use the new OrderItem result
order_items = locals()['var_function-call-12382592923587961148']
cases_file_path = locals()['var_function-call-2618497939888766397']

# Clean OrderItem IDs
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        oid = oid.strip()
        if oid.startswith('#'):
            oid = oid[1:]
        target_order_item_ids.add(oid)

# Load cases
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

cases_df = pd.DataFrame(cases_data)

# Clean Case OrderItem IDs
def clean_id(x):
    if x is None:
        return ""
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

cases_df['clean_orderitemid'] = cases_df['orderitemid__c'].apply(clean_id)

# Filter cases by product (join logic)
matched_cases = cases_df[cases_df['clean_orderitemid'].isin(target_order_item_ids)].copy()

# Parse dates
matched_cases['createddate'] = pd.to_datetime(matched_cases['createddate'])
if matched_cases['createddate'].dt.tz is None:
    matched_cases['createddate'] = matched_cases['createddate'].dt.tz_localize('UTC')
else:
    matched_cases['createddate'] = matched_cases['createddate'].dt.tz_convert('UTC')

# Filter date range: Past 10 months from 2021-04-10
# 2020-06-10 to 2021-04-10
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

matched_cases = matched_cases[(matched_cases['createddate'] >= start_date) & (matched_cases['createddate'] <= end_date)]

# Group by Month
matched_cases['month_year'] = matched_cases['createddate'].dt.to_period('M').astype(str)
matched_cases['month_name'] = matched_cases['createddate'].dt.month_name()

counts = matched_cases.groupby(['month_year', 'month_name']).size().reset_index(name='count')

print("__RESULT__:")
print(counts.to_json(orient='records'))"""

env_args = {'var_function-call-1163680895361236878': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-2618497939888766397': 'file_storage/function-call-2618497939888766397.json', 'var_function-call-1376755387683017809': [{'month_year': '2020-09', 'month_name': 'September', 'count': 1}, {'month_year': '2020-11', 'month_name': 'November', 'count': 2}, {'month_year': '2021-03', 'month_name': 'March', 'count': 1}], 'var_function-call-10338897396762162419': [], 'var_function-call-10338897396762163682': [{'month_year': '2020-09', 'count': 1}, {'month_year': '2020-11', 'count': 2}, {'month_year': '2021-03', 'count': 1}, {'month_year': '2023-06', 'count': 1}], 'var_function-call-9241081437086555383': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-12382592923587961148': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
