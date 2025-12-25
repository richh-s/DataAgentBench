code = """import json
import pandas as pd
from dateutil import parser

# Load OrderItem data
with open(locals()['var_function-call-18146379666724150079'], 'r') as f:
    order_items = json.load(f)

# Load Case data
with open(locals()['var_function-call-1808321046090152926'], 'r') as f:
    cases = json.load(f)

df_order_items = pd.DataFrame(order_items)
df_cases = pd.DataFrame(cases)

# Clean IDs
def clean_id(x):
    if pd.isna(x):
        return ""
    x = str(x).strip()
    if x.startswith("#"):
        x = x[1:]
    return x

df_order_items['Id'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id'] = df_order_items['Product2Id'].apply(clean_id)

target_product_id = "01tWt000006hVJdIAM"
# Filter OrderItems for the target product
target_order_items = df_order_items[df_order_items['Product2Id'] == target_product_id]
target_order_item_ids = set(target_order_items['Id'].unique())

print(f"DEBUG: Found {len(target_order_item_ids)} OrderItem IDs for product {target_product_id}")

# Clean Case IDs
df_cases['orderitemid__c'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter Cases by valid OrderItem IDs
df_cases_filtered = df_cases[df_cases['orderitemid__c'].isin(target_order_item_ids)].copy()

print(f"DEBUG: Found {len(df_cases_filtered)} Cases linked to target product before date filtering")

# Parse dates
df_cases_filtered['createddate'] = pd.to_datetime(df_cases_filtered['createddate'])

# Filter for past 10 months from 2021-04-10
end_date = pd.Timestamp("2021-04-10").tz_localize('UTC') # Case dates seem to have timezone info or I should handle it.
# Check if case dates are tz-aware. The preview shows '2023-07-02T11:00:00.000+0000'.
# So they are tz-aware.

# Calculate start date (10 months ago)
# 10 months ago from April 10, 2021 is June 10, 2020.
start_date = end_date - pd.DateOffset(months=10)

print(f"DEBUG: Time range {start_date} to {end_date}")

df_cases_final = df_cases_filtered[
    (df_cases_filtered['createddate'] >= start_date) & 
    (df_cases_filtered['createddate'] <= end_date + pd.Timedelta(days=1)) # Inclusive of end date
]

# Group by Month
# We need to distinguish months. e.g. "2020-07", "2020-08".
df_cases_final['Month'] = df_cases_final['createddate'].dt.strftime('%Y-%m')
df_cases_final['MonthName'] = df_cases_final['createddate'].dt.strftime('%B')

monthly_counts = df_cases_final.groupby(['Month', 'MonthName']).size().reset_index(name='Count')
monthly_counts = monthly_counts.sort_values('Month')

print("__RESULT__:")
print(monthly_counts.to_json(orient='records'))"""

env_args = {'var_function-call-18146379666724150079': 'file_storage/function-call-18146379666724150079.json', 'var_function-call-1808321046090152926': 'file_storage/function-call-1808321046090152926.json'}

exec(code, env_args)
