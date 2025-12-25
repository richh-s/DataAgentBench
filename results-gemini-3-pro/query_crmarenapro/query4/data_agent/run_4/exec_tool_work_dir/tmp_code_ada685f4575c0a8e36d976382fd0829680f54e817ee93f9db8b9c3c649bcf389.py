code = """import json
import pandas as pd

# Load Cases
with open(var_function_call_1880255598136818696, 'r') as f:
    cases_data = json.load(f)

# Load OrderItems
order_items_data = var_function_call_16523067176860182723

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs function
def clean_id(x):
    if x is None:
        return ""
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Clean OrderItems
df_order_items['Id'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id'] = df_order_items['Product2Id'].apply(clean_id)

# Filter OrderItems for the specific ProductId
target_product_id = "01tWt000006hVJdIAM"
target_order_items = df_order_items[df_order_items['Product2Id'] == target_product_id]['Id'].unique()

# Clean Cases
df_cases['orderitemid__c'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter Cases by OrderItemId
df_target_cases = df_cases[df_cases['orderitemid__c'].isin(target_order_items)].copy()

# Date filtering
df_target_cases['createddate'] = pd.to_datetime(df_target_cases['createddate'])
end_date = pd.to_datetime('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

# Ensure createddate is timezone aware/compatible. The sample output shows +0000, so it is timezone aware (UTC).
# If errors occur, I will handle tz.
df_target_cases = df_target_cases[
    (df_target_cases['createddate'] >= start_date) & 
    (df_target_cases['createddate'] <= end_date + pd.Timedelta(days=1)) # include the end date fully
]

# Group by Month
df_target_cases['Month'] = df_target_cases['createddate'].dt.strftime('%B')
df_target_cases['YearMonth'] = df_target_cases['createddate'].dt.strftime('%Y-%m')

monthly_counts = df_target_cases.groupby('YearMonth')['id'].count()
monthly_counts_name = df_target_cases.groupby('Month')['id'].count() # Use this if months are unique across years in the window?
# Wait, June 2020 and April 2021. No overlap in month names except maybe if range was > 12 months.
# 10 months: June 2020 to April 2021.
# Months: Jun, Jul, Aug, Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr.
# Each name appears once.

print("__RESULT__:")
print(json.dumps({
    "monthly_counts": monthly_counts.to_dict(),
    "monthly_counts_name": monthly_counts_name.to_dict()
}))"""

env_args = {'var_function-call-16523067176860182723': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-1880255598136818696': 'file_storage/function-call-1880255598136818696.json'}

exec(code, env_args)
