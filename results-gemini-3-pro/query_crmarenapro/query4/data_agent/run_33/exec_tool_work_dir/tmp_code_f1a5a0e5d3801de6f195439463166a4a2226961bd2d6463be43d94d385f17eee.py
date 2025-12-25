code = """import pandas as pd
import json

# Load Order Items
order_items_data = locals()['var_function-call-10205882618145039242']
valid_order_item_ids = set()
for item in order_items_data:
    oid = item['Id']
    if oid:
        # Clean: remove leading # and whitespace
        clean_id = oid.lstrip('#').strip()
        valid_order_item_ids.add(clean_id)

print(f"DEBUG: Found {len(valid_order_item_ids)} valid order item IDs for the product.")
# print(list(valid_order_item_ids)[:5])

# Load Cases
cases_file_path = locals()['var_function-call-10205882618145039871']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

df_cases = pd.DataFrame(cases_data)

# Clean orderitemid__c
df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].astype(str).apply(lambda x: x.lstrip('#').strip())

# Filter by product
df_filtered = df_cases[df_cases['clean_order_item_id'].isin(valid_order_item_ids)].copy()
print(f"DEBUG: Found {len(df_filtered)} cases linked to this product (all time fetched).")

# Convert date
df_filtered['createddate'] = pd.to_datetime(df_filtered['createddate'])

# Group by Month-Year for all fetched data
df_filtered['MonthYear'] = df_filtered['createddate'].dt.to_period('M')
all_counts = df_filtered.groupby('MonthYear')['clean_order_item_id'].count()

print("__RESULT__:")
print(json.dumps({
    "all_counts": {str(k): v for k, v in all_counts.items()}
}))"""

env_args = {'var_function-call-9991664212149122767': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9991664212149123198': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-10205882618145039242': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10205882618145039871': 'file_storage/function-call-10205882618145039871.json', 'var_function-call-5641040536612995723': {'counts_by_month': {'January': 1, 'March': 1, 'November': 2, 'September': 1}, 'detailed_counts': {"(2020, 'November')": 2, "(2020, 'September')": 1, "(2021, 'January')": 1, "(2021, 'March')": 1}}, 'var_function-call-7098145903175548628': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
