code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItem data (stored in var_call_JyQ6PRZy1ca5mGgfcy4rijrD)
data_path_orderitems = var_call_JyQ6PRZy1ca5mGgfcy4rijrD
if isinstance(data_path_orderitems, str):
    with open(data_path_orderitems, 'r') as f:
        orderitems = json.load(f)
else:
    orderitems = data_path_orderitems

# Load Case data (stored in var_call_PAyPrPMbJ7FlRM8p7vItmmSG)
data_path_cases = var_call_PAyPrPMbJ7FlRM8p7vItmmSG
if isinstance(data_path_cases, str):
    with open(data_path_cases, 'r') as f:
        cases = json.load(f)
else:
    cases = data_path_cases

# Create DataFrames
df_items = pd.DataFrame(orderitems)
df_cases = pd.DataFrame(cases)

# Normalize ID-like fields by stripping leading '#' and whitespace
def clean_id(x):
    if pd.isna(x):
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

for col in ['Id', 'Product2Id']:
    if col in df_items.columns:
        df_items[col] = df_items[col].apply(clean_id)

if 'orderitemid__c' in df_cases.columns:
    df_cases['orderitemid__c'] = df_cases['orderitemid__c'].apply(clean_id)
if 'issueid__c' in df_cases.columns:
    df_cases['issueid__c'] = df_cases['issueid__c'].apply(clean_id)
if 'createddate' in df_cases.columns:
    # parse dates where possible
    df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

# Filter order items to the target product id
target_product = '01tWt000006hV8LIAU'
df_items_target = df_items[df_items['Product2Id'] == target_product].copy()

# Prepare set of relevant order item ids
relevant_item_ids = set(df_items_target['Id'].dropna().astype(str).tolist())

# Filter cases to date range past five months relative to 2023-01-16 (inclusive): 2022-08-16 to 2023-01-16
start = pd.to_datetime('2022-08-16')
end = pd.to_datetime('2023-01-16') + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

mask_date = df_cases['createddate'].notna() & (df_cases['createddate'] >= start) & (df_cases['createddate'] <= end)
mask_orderitem = df_cases['orderitemid__c'].notna() & df_cases['orderitemid__c'].astype(str).isin(relevant_item_ids)

df_filtered = df_cases[mask_date & mask_orderitem].copy()

# Count issueid__c occurrences
counts = df_filtered['issueid__c'].dropna().astype(str).value_counts()

most_issue_id = None
if not counts.empty:
    # get highest count; if multiple, pick the one with smallest lexicographic id to be deterministic
    max_count = counts.iloc[0]
    candidate_ids = counts[counts == max_count].index.tolist()
    candidate_ids.sort()
    most_issue_id = candidate_ids[0]

import json
print("__RESULT__:")
print(json.dumps(most_issue_id))"""

env_args = {'var_call_6CtGANBJ8hlHbYpRTvggO9y4': [], 'var_call_roYC5ipqF90PKkdKZT7JWdeA': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_Nl9WDaNN0zeuR0eXwGKPDUC7': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}], 'var_call_JyQ6PRZy1ca5mGgfcy4rijrD': 'file_storage/call_JyQ6PRZy1ca5mGgfcy4rijrD.json', 'var_call_PAyPrPMbJ7FlRM8p7vItmmSG': 'file_storage/call_PAyPrPMbJ7FlRM8p7vItmmSG.json'}

exec(code, env_args)
