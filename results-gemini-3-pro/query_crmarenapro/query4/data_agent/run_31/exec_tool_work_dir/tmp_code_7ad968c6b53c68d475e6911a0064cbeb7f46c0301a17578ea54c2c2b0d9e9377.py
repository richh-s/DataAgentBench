code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load cases
cases_file = locals()['var_function-call-18208661459881045691']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)

# Load order items
order_items_data = locals()['var_function-call-18208661459881044318']

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs function
def clean_id(x):
    if x is None:
        return ""
    return str(x).replace('#', '').strip()

# Clean Case columns
df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])

# Clean Order Item columns
df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id_clean'] = df_order_items['Product2Id'].apply(clean_id)

# Filter Order Items for the specific product
target_product_id = '01tWt000006hVJdIAM'
target_order_items = df_order_items[df_order_items['Product2Id_clean'] == target_product_id]
valid_order_item_ids = set(target_order_items['Id_clean'])

# Filter Cases for these order items
relevant_cases = df_cases[df_cases['orderitemid_clean'].isin(valid_order_item_ids)]

# Filter for the past 10 months from 2021-04-10
current_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = current_date - pd.DateOffset(months=10)

# Filter by date range (ensure timezone awareness compatibility)
# Cases createddate is likely timezone aware.
relevant_cases = relevant_cases[relevant_cases['createddate'] >= start_date]
relevant_cases = relevant_cases[relevant_cases['createddate'] <= current_date]

# Group by month
relevant_cases['month_year'] = relevant_cases['createddate'].dt.to_period('M')
monthly_counts = relevant_cases['month_year'].value_counts().sort_index()

# Convert Period to str for JSON serialization
monthly_counts_str = monthly_counts.index.astype(str).tolist()
monthly_counts_values = monthly_counts.values.tolist()
result = dict(zip(monthly_counts_str, monthly_counts_values))

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-18323367245867218532': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-18323367245867220441': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-18208661459881045691': 'file_storage/function-call-18208661459881045691.json', 'var_function-call-18208661459881044318': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
