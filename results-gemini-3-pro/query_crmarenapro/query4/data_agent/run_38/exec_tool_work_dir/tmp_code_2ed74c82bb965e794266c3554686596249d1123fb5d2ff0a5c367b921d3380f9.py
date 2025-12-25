code = """import json
import pandas as pd

# Load files
with open(locals()['var_function-call-14046360423355083313'], 'r') as f:
    order_items = json.load(f)
with open(locals()['var_function-call-6667994660044802622'], 'r') as f:
    cases = json.load(f)

def clean_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#').strip()
    return x

target_product_id = "01tWt000006hVJdIAM"
valid_order_item_ids = set()

for item in order_items:
    pid = clean_id(item.get('Product2Id'))
    if pid == target_product_id:
        valid_order_item_ids.add(clean_id(item.get('Id')))

matched_cases = []
for case in cases:
    oid = clean_id(case.get('orderitemid__c'))
    if oid in valid_order_item_ids:
        matched_cases.append(case)

debug_info = {}
debug_info['total_valid_order_items'] = len(valid_order_item_ids)
debug_info['total_matched_cases'] = len(matched_cases)

monthly_counts_dict = {}
if matched_cases:
    df = pd.DataFrame(matched_cases)
    df['createddate'] = pd.to_datetime(df['createddate'])
    monthly_counts = df['createddate'].dt.to_period('M').value_counts().sort_index()
    monthly_counts_dict = {str(k): int(v) for k, v in monthly_counts.items()}

print("__RESULT__:")
print(json.dumps({"debug": debug_info, "monthly_counts": monthly_counts_dict}))"""

env_args = {'var_function-call-15147835606305365127': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-15147835606305361998': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6667994660044800741': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-6667994660044802622': 'file_storage/function-call-6667994660044802622.json', 'var_function-call-15954347864961491755': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-14046360423355084056': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-14046360423355083313': 'file_storage/function-call-14046360423355083313.json', 'var_function-call-6478380301174335294': {'counts': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'counts_named': {'January': 1, 'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-10765273189293179453': 'Done'}

exec(code, env_args)
