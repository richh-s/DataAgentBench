code = """import json
import pandas as pd
import datetime

# Load data
with open(locals()['var_function-call-15237146713433936160'], 'r') as f:
    cases_data = json.load(f)

order_items_data = locals()['var_function-call-15237146713433937959']

# Convert to DataFrames
df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs function
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Clean OrderItems
df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id_clean'] = df_order_items['Product2Id'].apply(clean_id)

# Filter OrderItems for the specific product
target_product_id = '01tWt000006hVJdIAM'
valid_order_items = df_order_items[df_order_items['Product2Id_clean'] == target_product_id]['Id_clean'].tolist()

# Clean Cases
df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter Cases by valid OrderItems
df_cases_filtered = df_cases[df_cases['orderitemid_clean'].isin(valid_order_items)].copy()

# Parse dates with UTC
df_cases_filtered['createddate'] = pd.to_datetime(df_cases_filtered['createddate'], utc=True)

# Filter by date range (past 10 months from 2021-04-10)
# Make end_date UTC
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

df_cases_final = df_cases_filtered[(df_cases_filtered['createddate'] >= start_date) & (df_cases_filtered['createddate'] <= end_date)]

# Group by Month
# Convert to period (will lose timezone but that's fine for grouping)
df_cases_final['MonthYear'] = df_cases_final['createddate'].dt.to_period('M')

monthly_counts = df_cases_final.groupby('MonthYear').size().reset_index(name='Count')
monthly_counts['MonthName'] = monthly_counts['MonthYear'].dt.strftime('%B')
monthly_counts['MonthYearStr'] = monthly_counts['MonthYear'].astype(str)

print("__RESULT__:")
print(json.dumps(monthly_counts[['MonthName', 'Count', 'MonthYearStr']].to_dict(orient='records')))"""

env_args = {'var_function-call-5222737157604988371': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5222737157604988016': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-15237146713433936160': 'file_storage/function-call-15237146713433936160.json', 'var_function-call-15237146713433937959': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
