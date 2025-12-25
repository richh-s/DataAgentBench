code = """import pandas as pd
import json

# Load Order Items
order_items = locals()['var_function-call-6371179236710566905']
df_oi = pd.DataFrame(order_items)

# Clean Order Item Id
# Remove leading '#' and strip whitespace
df_oi['clean_id'] = df_oi['Id'].astype(str).str.strip().str.lstrip('#')

# Load Cases
cases_file = locals()['var_function-call-6371179236710566180']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)
df_cases = pd.DataFrame(cases_data)

# Clean Case orderitemid__c
# Remove leading '#' and strip whitespace
# Handle None/NaN if any
df_cases['clean_orderitemid'] = df_cases['orderitemid__c'].astype(str).str.strip().str.lstrip('#')

# Join
# Inner join to find cases associated with the product
merged = pd.merge(df_cases, df_oi, left_on='clean_orderitemid', right_on='clean_id', how='inner')

# Filter by date
# Today: 2021-04-10
# Past 10 months: From roughly 2020-06-10 to 2021-04-10
# Let's convert createddate to datetime
merged['created_dt'] = pd.to_datetime(merged['createddate'])

# Define range
start_date = pd.Timestamp('2020-06-10').tz_localize('UTC')
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')

# Filter
filtered = merged[(merged['created_dt'] >= start_date) & (merged['created_dt'] <= end_date)].copy()

# Extract Month Name and Year
filtered['month_name'] = filtered['created_dt'].dt.month_name()
filtered['year'] = filtered['created_dt'].dt.year
filtered['month_year'] = filtered['created_dt'].dt.to_period('M')

# Count cases per month
monthly_counts = filtered.groupby('month_name').size()
monthly_counts_ordered = filtered.groupby('month_year').size()

print("__RESULT__:")
print(json.dumps({
    "monthly_counts": monthly_counts.to_dict(),
    "monthly_counts_ordered": {str(k): v for k, v in monthly_counts_ordered.items()},
    "total_cases_found": len(filtered)
}))"""

env_args = {'var_function-call-15577878570648328': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15577878570649663': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-6371179236710566180': 'file_storage/function-call-6371179236710566180.json', 'var_function-call-6371179236710566905': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
