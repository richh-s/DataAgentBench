code = """import pandas as pd
import json

# Load OrderItems
with open(locals()['var_function-call-15112027591336911943'], 'r') as f:
    order_items_data = json.load(f)

# Load Cases
with open(locals()['var_function-call-1629989200070721134'], 'r') as f:
    cases_data = json.load(f)

df_oi = pd.DataFrame(order_items_data)
df_cases = pd.DataFrame(cases_data)

# Helper cleanup function
def clean_id(x):
    if x is None: return ""
    return str(x).replace('#', '').strip()

# Target Product ID
target_product_id = "01tWt000006hVJdIAM"

# Process OrderItems
df_oi['clean_product_id'] = df_oi['Product2Id'].apply(clean_id)
df_oi['clean_id'] = df_oi['Id'].apply(clean_id)

# Filter for target product
target_ois = df_oi[df_oi['clean_product_id'] == target_product_id]
target_oi_ids = set(target_ois['clean_id'])

# Process Cases
df_cases['clean_orderitemid'] = df_cases['orderitemid__c'].apply(clean_id)
# Handle date parsing
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

# Filter by product association
matched_cases = df_cases[df_cases['clean_orderitemid'].isin(target_oi_ids)].copy()

# Filter by date range (past 10 months from 2021-04-10)
# Ref date: 2021-04-10
ref_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
start_date = ref_date - pd.DateOffset(months=10)

matched_cases = matched_cases[(matched_cases['createddate'] <= ref_date) & (matched_cases['createddate'] >= start_date)]

# Group by Month Name
matched_cases['month_name'] = matched_cases['createddate'].dt.strftime('%B')
matched_cases['month_year'] = matched_cases['createddate'].dt.strftime('%Y-%m')

counts = matched_cases['month_year'].value_counts().sort_index()

print("__RESULT__:")
print(json.dumps(counts.to_dict()))"""

env_args = {'var_function-call-15112027591336911943': 'file_storage/function-call-15112027591336911943.json', 'var_function-call-1629989200070721134': 'file_storage/function-call-1629989200070721134.json'}

exec(code, env_args)
