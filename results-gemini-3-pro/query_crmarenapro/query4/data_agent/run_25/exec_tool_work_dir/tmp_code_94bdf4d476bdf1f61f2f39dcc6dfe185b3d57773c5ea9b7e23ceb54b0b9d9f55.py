code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-2269822306977592115'], 'r') as f:
    cases_data = json.load(f)

order_items_data = locals()['var_function-call-2269822306977591614']

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#')

df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)
df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)

# Filter cases by OrderItems related to the product
target_order_item_ids = set(df_order_items['Id_clean'])
df_cases_filtered = df_cases[df_cases['orderitemid_clean'].isin(target_order_item_ids)].copy()

# Convert date
df_cases_filtered['createddate'] = pd.to_datetime(df_cases_filtered['createddate'])

# Define date range: Past 10 months from 2021-04-10
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC') # Ensure timezone awareness if data is aware
start_date = end_date - pd.DateOffset(months=10)

# Ensure createddate is timezone aware/compatible. 
# The string format "2023-07-02T11:00:00.000+0000" is timezone aware.
# pd.to_datetime should handle it.

# Filter by date range
df_cases_in_range = df_cases_filtered[(df_cases_filtered['createddate'] >= start_date) & (df_cases_filtered['createddate'] <= end_date)]

# Group by month
df_cases_in_range['month_year'] = df_cases_in_range['createddate'].dt.strftime('%Y-%m')
df_cases_in_range['month_name'] = df_cases_in_range['createddate'].dt.month_name()
monthly_counts = df_cases_in_range.groupby(['month_year', 'month_name']).size().reset_index(name='count')

print("__RESULT__:")
print(monthly_counts.to_json(orient='records'))"""

env_args = {'var_function-call-5265069770845645301': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5265069770845645176': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2269822306977592115': 'file_storage/function-call-2269822306977592115.json', 'var_function-call-2269822306977591614': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
