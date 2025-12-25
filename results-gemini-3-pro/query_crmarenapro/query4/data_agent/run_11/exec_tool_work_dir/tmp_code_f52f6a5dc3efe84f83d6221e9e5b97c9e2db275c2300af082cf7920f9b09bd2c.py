code = """import json
import pandas as pd

# Load Order Items
order_items = locals()['var_function-call-8635919969418049399'] # Using the second query result which had wildcards, same content though

# Clean OrderItem Ids
valid_order_item_ids = set()
for item in order_items:
    oid = str(item['Id']).strip()
    if oid.startswith('#'):
        oid = oid[1:]
    valid_order_item_ids.add(oid)

print(f"DEBUG: Found {len(valid_order_item_ids)} valid OrderItem IDs.")
print(f"DEBUG: Sample OrderItem IDs: {list(valid_order_item_ids)[:5]}")

# Load Cases
cases_path = locals()['var_function-call-2782911535086019411']
with open(cases_path, 'r') as f:
    cases = json.load(f)

df_cases = pd.DataFrame(cases)

# Clean orderitemid__c
def clean_id(x):
    if pd.isna(x):
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter
matched_cases = df_cases[df_cases['clean_order_item_id'].isin(valid_order_item_ids)].copy()
print(f"DEBUG: Found {len(matched_cases)} cases matching the product.")

# Date Filter
matched_cases['createddate'] = pd.to_datetime(matched_cases['createddate'])
ref_date = pd.Timestamp("2021-04-10").replace(tzinfo=matched_cases['createddate'].dt.tz)
start_date = ref_date - pd.DateOffset(months=10)

print(f"DEBUG: Date range {start_date} to {ref_date}")

filtered_cases = matched_cases[(matched_cases['createddate'] >= start_date) & (matched_cases['createddate'] <= ref_date)]
print(f"DEBUG: {len(filtered_cases)} cases in date range.")

# Group by Month
filtered_cases['month'] = filtered_cases['createddate'].dt.strftime('%B')
filtered_cases['year_month'] = filtered_cases['createddate'].dt.strftime('%Y-%m')

counts = filtered_cases.groupby('year_month')['month'].value_counts()
print("DEBUG: Monthly counts:")
print(counts)

# Prepare result
result = counts.to_json() # simple serialization for now
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14108611946275025966': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-14108611946275028411': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2782911535086022320': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2782911535086019411': 'file_storage/function-call-2782911535086019411.json', 'var_function-call-9973046957187302705': [{'month': 'September', 'year_month': '2020-09', 'count': 1}, {'month': 'November', 'year_month': '2020-11', 'count': 2}, {'month': 'January', 'year_month': '2021-01', 'count': 1}, {'month': 'March', 'year_month': '2021-03', 'count': 1}], 'var_function-call-8635919969418049399': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-17923261169044884893': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
