code = """import json
import pandas as pd

# Load data
cases_file = locals()['var_function-call-18208661459881045691']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)
df_cases = pd.DataFrame(cases_data)

order_items_data = locals()['var_function-call-18208661459881044318']
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs
def clean_id(x):
    if x is None: return ""
    return str(x).replace('#', '').strip()

df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)
df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id_clean'] = df_order_items['Product2Id'].apply(clean_id)

target_product_id = '01tWt000006hVJdIAM'
valid_items = df_order_items[df_order_items['Product2Id_clean'] == target_product_id]
valid_ids = set(valid_items['Id_clean'])

# Match
matched_cases = df_cases[df_cases['orderitemid_clean'].isin(valid_ids)].copy()
matched_cases['createddate'] = pd.to_datetime(matched_cases['createddate'])

# Stats
print("__RESULT__:")
print(json.dumps({
    "total_cases_loaded": len(df_cases),
    "total_order_items_loaded": len(df_order_items),
    "matching_order_items": len(valid_ids),
    "matched_cases_total": len(matched_cases),
    "matched_cases_dates": matched_cases['createddate'].dt.to_period('M').astype(str).value_counts().to_dict()
}))"""

env_args = {'var_function-call-18323367245867218532': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-18323367245867220441': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-18208661459881045691': 'file_storage/function-call-18208661459881045691.json', 'var_function-call-18208661459881044318': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-8853160959091589246': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-5944713814642297141': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
