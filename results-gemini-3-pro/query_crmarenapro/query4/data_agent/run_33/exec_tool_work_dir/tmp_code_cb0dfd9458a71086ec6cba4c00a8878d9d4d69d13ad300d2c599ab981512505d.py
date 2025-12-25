code = """import pandas as pd
import json

# Load Order Items
order_items_data = locals()['var_function-call-10205882618145039242']
# Clean IDs
valid_order_item_ids = set()
for item in order_items_data:
    oid = item['Id']
    if oid:
        valid_order_item_ids.add(oid.lstrip('#'))

# Load Cases
cases_file_path = locals()['var_function-call-10205882618145039871']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

df_cases = pd.DataFrame(cases_data)

# Clean orderitemid__c
df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].astype(str).apply(lambda x: x.lstrip('#'))

# Filter by product
df_filtered = df_cases[df_cases['clean_order_item_id'].isin(valid_order_item_ids)].copy()

# Convert date
df_filtered['createddate'] = pd.to_datetime(df_filtered['createddate'])

# Filter date range (Past 10 months from 2021-04-10)
start_date = pd.Timestamp('2020-06-10').tz_localize('UTC')
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')

# Ensure createddate is timezone aware or handle comparison correctly
# The preview shows "2023-07-02T11:00:00.000+0000", so it has timezone.

df_filtered = df_filtered[(df_filtered['createddate'] >= start_date) & (df_filtered['createddate'] <= end_date)]

# Extract Month
df_filtered['Month'] = df_filtered['createddate'].dt.month_name()
df_filtered['Year'] = df_filtered['createddate'].dt.year
df_filtered['YearMonth'] = df_filtered['createddate'].dt.to_period('M')

# Count
counts = df_filtered.groupby('Month')['clean_order_item_id'].count()
counts_detailed = df_filtered.groupby(['Year', 'Month'])['clean_order_item_id'].count()

print("__RESULT__:")
print(json.dumps({
    "counts_by_month": counts.to_dict(),
    "detailed_counts": {str(k): v for k, v in counts_detailed.items()}
}))"""

env_args = {'var_function-call-9991664212149122767': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9991664212149123198': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-10205882618145039242': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10205882618145039871': 'file_storage/function-call-10205882618145039871.json'}

exec(code, env_args)
