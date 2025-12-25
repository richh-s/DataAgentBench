code = """import json
import pandas as pd

# Load OrderItem data
with open(locals()['var_function-call-18146379666724150079'], 'r') as f:
    order_items = json.load(f)

# Load Case data
with open(locals()['var_function-call-1808321046090152926'], 'r') as f:
    cases = json.load(f)

df_order_items = pd.DataFrame(order_items)
df_cases = pd.DataFrame(cases)

def clean_id(x):
    if pd.isna(x):
        return ""
    x = str(x).strip()
    if x.startswith("#"):
        x = x[1:]
    return x

df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id_clean'] = df_order_items['Product2Id'].apply(clean_id)
df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)

target_product_id = "01tWt000006hVJdIAM"
target_order_items = df_order_items[df_order_items['Product2Id_clean'] == target_product_id]

info = {}
info['target_product_id'] = target_product_id
info['num_order_items'] = len(target_order_items)
info['sample_order_item_ids'] = target_order_items['Id_clean'].head().tolist()

target_ids = set(target_order_items['Id_clean'])
matching_cases = df_cases[df_cases['orderitemid_clean'].isin(target_ids)].copy()

info['num_matching_cases'] = len(matching_cases)

# Check date distribution of matching cases
matching_cases['createddate'] = pd.to_datetime(matching_cases['createddate'])
matching_cases['Month'] = matching_cases['createddate'].dt.strftime('%Y-%m')
monthly_counts = matching_cases.groupby('Month').size().to_dict()
info['monthly_counts'] = monthly_counts

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-18146379666724150079': 'file_storage/function-call-18146379666724150079.json', 'var_function-call-1808321046090152926': 'file_storage/function-call-1808321046090152926.json', 'var_function-call-14255137602280284402': [{'Month': '2020-09', 'MonthName': 'September', 'Count': 1}, {'Month': '2020-11', 'MonthName': 'November', 'Count': 2}, {'Month': '2021-01', 'MonthName': 'January', 'Count': 1}, {'Month': '2021-03', 'MonthName': 'March', 'Count': 1}], 'var_function-call-17720943828121859338': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
