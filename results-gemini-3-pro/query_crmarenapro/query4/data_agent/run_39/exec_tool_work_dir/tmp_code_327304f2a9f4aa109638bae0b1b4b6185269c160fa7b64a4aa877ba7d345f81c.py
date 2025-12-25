code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15112027591336911943'], 'r') as f:
    order_items_data = json.load(f)
with open(locals()['var_function-call-1629989200070721134'], 'r') as f:
    cases_data = json.load(f)

df_oi = pd.DataFrame(order_items_data)
df_cases = pd.DataFrame(cases_data)

def clean_id(x):
    if x is None: return ""
    return str(x).replace('#', '').strip()

target_product_id = "01tWt000006hVJdIAM"

# Process OrderItems
df_oi['clean_product_id'] = df_oi['Product2Id'].apply(clean_id)
df_oi['clean_id'] = df_oi['Id'].apply(clean_id)

target_ois = df_oi[df_oi['clean_product_id'] == target_product_id]
target_oi_ids = set(target_ois['clean_id'])

print(f"DEBUG: Total OrderItems: {len(df_oi)}")
print(f"DEBUG: Target Product ID: {target_product_id}")
print(f"DEBUG: Matching OrderItems: {len(target_ois)}")

# Process Cases
df_cases['clean_orderitemid'] = df_cases['orderitemid__c'].apply(clean_id)
df_cases['createddate_dt'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

print(f"DEBUG: Total Cases: {len(df_cases)}")
print(f"DEBUG: Cases with invalid date: {df_cases['createddate_dt'].isna().sum()}")

# Filter by product
matched_cases = df_cases[df_cases['clean_orderitemid'].isin(target_oi_ids)].copy()
print(f"DEBUG: Cases linked to target product (all time): {len(matched_cases)}")

# Check date range
ref_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
start_date = ref_date - pd.DateOffset(months=10)

matched_cases_period = matched_cases[(matched_cases['createddate_dt'] <= ref_date) & (matched_cases['createddate_dt'] >= start_date)]
print(f"DEBUG: Cases in 10 month window: {len(matched_cases_period)}")

# Group by month
matched_cases['month'] = matched_cases['createddate_dt'].dt.strftime('%Y-%m')
all_time_counts = matched_cases['month'].value_counts().sort_index()

print("__RESULT__:")
print(json.dumps(all_time_counts.to_dict()))"""

env_args = {'var_function-call-15112027591336911943': 'file_storage/function-call-15112027591336911943.json', 'var_function-call-1629989200070721134': 'file_storage/function-call-1629989200070721134.json', 'var_function-call-3934149717266984374': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-7611884811353004601': [{'Name': 'SecureAnalytics Pro', 'Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
