code = """import json
import pandas as pd
from datetime import datetime

# Load previous tool results
# var_call_rBGLVLhOKVcJMjw7ywXmCfq5 may be a filepath to a .json (large result)
cases_raw = None
if isinstance(var_call_rBGLVLhOKVcJMjw7ywXmCfq5, str):
    # It's a path to a JSON file
    with open(var_call_rBGLVLhOKVcJMjw7ywXmCfq5, 'r', encoding='utf-8') as f:
        cases_raw = json.load(f)
else:
    cases_raw = var_call_rBGLVLhOKVcJMjw7ywXmCfq5

order_items_raw = var_call_IuBEWqhgyN09gTEF0DJIfa80

# Create DataFrames
df_cases = pd.DataFrame(cases_raw)
df_orders = pd.DataFrame(order_items_raw)

# Normalization function: strip whitespace and leading '#'
def norm(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Apply normalization
if 'orderitemid__c' in df_cases.columns:
    df_cases['orderitem_norm'] = df_cases['orderitemid__c'].apply(norm)
else:
    df_cases['orderitem_norm'] = None

if 'issueid__c' in df_cases.columns:
    df_cases['issue_norm'] = df_cases['issueid__c'].apply(norm)
else:
    df_cases['issue_norm'] = None

if 'createddate' in df_cases.columns:
    # Parse createddate without timezone to naive datetime
    df_cases['created_parsed'] = pd.to_datetime(df_cases['createddate'], errors='coerce').dt.tz_convert(None)
else:
    df_cases['created_parsed'] = pd.NaT

if 'Id' in df_orders.columns:
    df_orders['Id_norm'] = df_orders['Id'].apply(norm)
else:
    df_orders['Id_norm'] = []

order_ids_set = set(df_orders['Id_norm'].dropna().unique())

# Define the 5-month window relative to 2023-01-16
start = pd.to_datetime('2022-08-16')
end = pd.to_datetime('2023-01-16T23:59:59')

# Ensure created_parsed is naive
# If still tz-aware, remove tz
if df_cases['created_parsed'].dtype == 'datetime64[ns, tz]':
    df_cases['created_parsed'] = df_cases['created_parsed'].dt.tz_convert(None)

# Filter cases by date and matching orderitem
df_filtered = df_cases[
    df_cases['orderitem_norm'].isin(order_ids_set) &
    df_cases['created_parsed'].notna() &
    (df_cases['created_parsed'] >= start) &
    (df_cases['created_parsed'] <= end)
]

# Count frequencies of issue_norm
counts = df_filtered['issue_norm'].dropna().value_counts()

if counts.empty:
    result = None
else:
    max_count = counts.iloc[0]
    top_issues = counts[counts == max_count].index.tolist()
    # deterministic choice: lexicographically smallest
    top_issue = sorted(top_issues)[0]
    result = top_issue

# Output must be a JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rBGLVLhOKVcJMjw7ywXmCfq5': 'file_storage/call_rBGLVLhOKVcJMjw7ywXmCfq5.json', 'var_call_dgsFRYaOfA1ArFFNznXRAWUT': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_IuBEWqhgyN09gTEF0DJIfa80': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007906mIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794JmIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794YFIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794YJIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794bXIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007959OIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007959PIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000795PSIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795UKIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795akIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795ywIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007962JIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968hIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968iIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796F5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796IIIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796N7IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796NAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796RzIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S0IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S1IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796VDIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796a1IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796dFIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796dIIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796jiIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796lKIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796myIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796n0IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796oaIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796rlIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796tTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796v0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wbIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wcIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007979WIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797FxIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797MQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797O5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797RGIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797SsIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797axIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797e9IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797hNIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797j0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797mDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797nqIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797nsIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797pSIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797sfIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797z8IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007982LIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt000007983xIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007987CIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IUIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IVIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798NKIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798NMIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798S9IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798iIIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798nBIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798rxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798wpIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007991dIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079987IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EZIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EaIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799HoIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799JPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799T3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799b7IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799ckIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799fxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799srIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799w5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079A0wIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A2aIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A49IAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A7NIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079AfJIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AgrIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AqXIAU', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079As9IAE', 'Product2Id': '01tWt000006hV8LIAU'}]}

exec(code, env_args)
