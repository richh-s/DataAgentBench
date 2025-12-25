code = """import json
import pandas as pd
import datetime

# Load Order Items
order_items = locals()['var_function-call-6667994660044800741']
# Load Cases
with open(locals()['var_function-call-6667994660044802622'], 'r') as f:
    cases = json.load(f)

# Create DataFrames
df_order_items = pd.DataFrame(order_items)
df_cases = pd.DataFrame(cases)

# Clean IDs
def clean_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter Cases by date range [2020-06-10, 2021-04-10]
today = pd.to_datetime("2021-04-10").tz_localize('UTC')
start_date = today - pd.DateOffset(months=10)

df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])

# Filter cases
mask_date = (df_cases['createddate'] >= start_date) & (df_cases['createddate'] <= today + pd.Timedelta(days=1))
df_cases_filtered = df_cases[mask_date].copy()

# Join
merged = pd.merge(df_cases_filtered, df_order_items, left_on='orderitemid_clean', right_on='Id_clean', how='inner')

# Extract Month Name and YearMonth
merged['Month'] = merged['createddate'].dt.month_name()
merged['YearMonth'] = merged['createddate'].dt.to_period('M')

# Count by YearMonth
monthly_counts = merged.groupby('YearMonth').size()

# Convert to string for JSON
monthly_counts_dict = {str(k): int(v) for k, v in monthly_counts.items()}

print("__RESULT__:")
print(json.dumps(monthly_counts_dict))"""

env_args = {'var_function-call-15147835606305365127': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-15147835606305361998': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6667994660044800741': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-6667994660044802622': 'file_storage/function-call-6667994660044802622.json'}

exec(code, env_args)
