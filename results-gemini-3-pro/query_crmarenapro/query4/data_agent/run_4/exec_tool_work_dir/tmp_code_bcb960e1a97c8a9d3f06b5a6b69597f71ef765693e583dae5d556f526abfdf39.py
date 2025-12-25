code = """import json
import pandas as pd

# Load previous results
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

print(f"Target OrderItem Count: {len(target_order_items)}")

df_cases['orderitemid__c'] = df_cases['orderitemid__c'].apply(clean_id)
df_target_cases = df_cases[df_cases['orderitemid__c'].isin(target_order_items)].copy()

print(f"Matched Cases Count (Total): {len(df_target_cases)}")

df_target_cases['createddate'] = pd.to_datetime(df_target_cases['createddate'])

# Check distribution over all time
df_target_cases['Month'] = df_target_cases['createddate'].dt.strftime('%Y-%m')
all_counts = df_target_cases.groupby('Month')['id'].count()

print("__RESULT__:")
print(json.dumps({
    "all_monthly_counts": all_counts.to_dict(),
    "target_order_items": list(target_order_items)
}))"""

env_args = {'var_function-call-16523067176860182723': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-1880255598136818696': 'file_storage/function-call-1880255598136818696.json', 'var_function-call-15727989274279356713': {'monthly_counts': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'monthly_counts_name': {'January': 1, 'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-11418672449548713438': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
