code = """import json
import pandas as pd

cases_file_path = locals()['var_function-call-1880255598136818696']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

order_items_data = locals()['var_function-call-16523067176860182723']

df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

def clean_id(x):
    if x is None:
        return ""
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

df_order_items['Id'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id'] = df_order_items['Product2Id'].apply(clean_id)

target_product_id = "01tWt000006hVJdIAM"
target_order_items = df_order_items[df_order_items['Product2Id'] == target_product_id]['Id'].unique()

df_cases['orderitemid__c'] = df_cases['orderitemid__c'].apply(clean_id)
df_target_cases = df_cases[df_cases['orderitemid__c'].isin(target_order_items)].copy()
df_target_cases['createddate'] = pd.to_datetime(df_target_cases['createddate'])

# Filter date
end_date = pd.to_datetime('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)
df_filtered = df_target_cases[
    (df_target_cases['createddate'] >= start_date) & 
    (df_target_cases['createddate'] <= end_date + pd.Timedelta(days=1))
]

print("__RESULT__:")
print(json.dumps(
    df_filtered[['id', 'createddate', 'orderitemid__c']].astype(str).to_dict(orient='records')
))"""

env_args = {'var_function-call-16523067176860182723': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-1880255598136818696': 'file_storage/function-call-1880255598136818696.json', 'var_function-call-15727989274279356713': {'monthly_counts': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'monthly_counts_name': {'January': 1, 'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-11418672449548713438': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-3116201958146513868': {'all_monthly_counts': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1, '2023-06': 1}, 'target_order_items': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797awIAA', '802Wt00000797z7IAA', '802Wt00000798VPIAY', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt0000079B6gIAE']}}

exec(code, env_args)
