code = """import pandas as pd
import json

target_product_id = "01tWt000006hVJdIAM"

# Load ALL Order Items
order_items_file = locals()['var_function-call-1469869314428591067']
with open(order_items_file, 'r') as f:
    order_items_data = json.load(f)

valid_order_item_ids = set()
for item in order_items_data:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    if pid and oid:
        # Clean Product ID
        clean_pid = pid.lstrip('#').strip()
        if clean_pid == target_product_id:
            # Clean Order Item ID and add to set
            clean_oid = oid.lstrip('#').strip()
            valid_order_item_ids.add(clean_oid)

print(f"DEBUG: Found {len(valid_order_item_ids)} valid order item IDs for the product.")
# print(list(valid_order_item_ids))

# Load Cases
cases_file_path = locals()['var_function-call-10205882618145039871']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

df_cases = pd.DataFrame(cases_data)

# Clean orderitemid__c
df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].astype(str).apply(lambda x: x.lstrip('#').strip())

# Filter by product
df_filtered = df_cases[df_cases['clean_order_item_id'].isin(valid_order_item_ids)].copy()

# Convert date
df_filtered['createddate'] = pd.to_datetime(df_filtered['createddate'])

# Filter date range (Past 10 months from 2021-04-10)
# Start: 2020-06-10
start_date = pd.Timestamp('2020-06-10').tz_localize('UTC')
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')

# Ensure timezone match (cases data has timezone)
# If case data is tz-aware (which it is), we are good.

df_in_range = df_filtered[(df_filtered['createddate'] >= start_date) & (df_filtered['createddate'] <= end_date)].copy()

# Group by Month-Year
df_in_range['MonthName'] = df_in_range['createddate'].dt.month_name()
df_in_range['YearMonth'] = df_in_range['createddate'].dt.to_period('M')

counts = df_in_range.groupby('MonthName')['clean_order_item_id'].count()
detailed = df_in_range.groupby('YearMonth')['clean_order_item_id'].count()

print("__RESULT__:")
print(json.dumps({
    "valid_order_item_ids_count": len(valid_order_item_ids),
    "total_cases_in_range": len(df_in_range),
    "counts_by_month": counts.to_dict(),
    "detailed_counts": {str(k): v for k, v in detailed.items()}
}))"""

env_args = {'var_function-call-9991664212149122767': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9991664212149123198': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-10205882618145039242': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10205882618145039871': 'file_storage/function-call-10205882618145039871.json', 'var_function-call-5641040536612995723': {'counts_by_month': {'January': 1, 'March': 1, 'November': 2, 'September': 1}, 'detailed_counts': {"(2020, 'November')": 2, "(2020, 'September')": 1, "(2021, 'January')": 1, "(2021, 'March')": 1}}, 'var_function-call-7098145903175548628': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-7098145903175546035': {'all_counts': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1, '2023-06': 1}}, 'var_function-call-17724000434272448015': [{'count': '5'}], 'var_function-call-17724000434272444806': [{'orderitemid__c': '802Wt00000797r4IAA'}, {'orderitemid__c': '802Wt00000798aDIAQ'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt00000797r3IAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt0000078xAFIAY'}, {'orderitemid__c': '802Wt0000079ATyIAM'}, {'orderitemid__c': '802Wt00000794bXIAQ'}, {'orderitemid__c': '802Wt00000796yFIAQ'}], 'var_function-call-14822656254729422224': [{'count(*)': '689'}], 'var_function-call-1469869314428591067': 'file_storage/function-call-1469869314428591067.json'}

exec(code, env_args)
