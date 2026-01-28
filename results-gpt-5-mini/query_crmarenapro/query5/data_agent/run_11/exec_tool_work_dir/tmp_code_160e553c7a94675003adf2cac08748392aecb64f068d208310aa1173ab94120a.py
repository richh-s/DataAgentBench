code = """import json
import pandas as pd
from datetime import datetime

# Load cases result which may be a filepath or a list
cases_var = var_call_UcamNkwmwaixPwQe0Ph6FpWT
if isinstance(cases_var, str):
    with open(cases_var, 'r', encoding='utf-8') as f:
        cases = json.load(f)
else:
    cases = cases_var

orderitems = var_call_qpVduQcj2mBXMQj5a4OSK4Mr

# Create DataFrames
df_cases = pd.DataFrame(cases)
df_order = pd.DataFrame(orderitems)

# Normalization function
def norm(x):
    if pd.isna(x):
        return x
    if not isinstance(x, str):
        x = str(x)
    return x.strip().lstrip('#').strip()

# Normalize relevant id fields
for col in ['orderitemid__c', 'issueid__c', 'id']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].apply(norm)

# Parse createddate to naive datetime (drop tz)
if 'createddate' in df_cases.columns:
    df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
    # convert to naive by removing tzinfo
    df_cases['createddate'] = df_cases['createddate'].dt.tz_convert(None) if df_cases['createddate'].dt.tz is not None else df_cases['createddate']

# Normalize order item ids
if 'Id' in df_order.columns:
    df_order['Id_norm'] = df_order['Id'].apply(norm)
else:
    df_order['Id_norm'] = df_order['Id'].apply(norm)

# Determine date range: past 5 months from 2023-01-16 -> >= 2022-08-16 and <= 2023-01-16
start = pd.to_datetime('2022-08-16')
end = pd.to_datetime('2023-01-16')

# Make sure createddate is naive
# If createddate contains timezone-aware datetimes, convert to naive by astype('datetime64[ns]')
if df_cases['createddate'].dtype == 'datetime64[ns, UTC]':
    df_cases['createddate'] = df_cases['createddate'].dt.tz_convert(None)

# Filter cases by date range
df_cases_range = df_cases[(df_cases['createddate'] >= start) & (df_cases['createddate'] <= end)].copy()

# Filter cases linked to product via orderitem id
order_ids_set = set(df_order['Id_norm'].tolist())

if 'orderitemid__c' in df_cases_range.columns:
    df_cases_range['orderitem_norm'] = df_cases_range['orderitemid__c']
else:
    df_cases_range['orderitem_norm'] = None

df_matched = df_cases_range[df_cases_range['orderitem_norm'].isin(order_ids_set)].copy()

# Count frequency of issueid__c
if df_matched.empty:
    result = None
else:
    # normalize issueid
    df_matched['issue_norm'] = df_matched['issueid__c'].apply(lambda x: norm(x) if pd.notna(x) else x)
    freq = df_matched['issue_norm'].value_counts()
    if freq.empty:
        result = None
    else:
        result = freq.idxmax()

# Prepare output as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UcamNkwmwaixPwQe0Ph6FpWT': 'file_storage/call_UcamNkwmwaixPwQe0Ph6FpWT.json', 'var_call_qpVduQcj2mBXMQj5a4OSK4Mr': [{'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'OrderId': '#801Wt00000PGjNsIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'OrderId': '801Wt00000PHLzNIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'OrderId': '801Wt00000PGbDQIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'OrderId': '801Wt00000PGoc0IAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'OrderId': '#801Wt00000PGzVrIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'OrderId': '801Wt00000PGoc1IAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'OrderId': '#801Wt00000PGbdMIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'OrderId': '801Wt00000PGyzXIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794JmIAI', 'OrderId': '801Wt00000PHRVKIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794YFIAY', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794YJIAY', 'OrderId': '#801Wt00000PGzikIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007959OIAQ', 'OrderId': '801Wt00000PGzikIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795akIAA', 'OrderId': '801Wt00000PGzFlIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795ywIAA', 'OrderId': '801Wt00000PGaCTIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007962JIAQ', 'OrderId': '801Wt00000PGXwBIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968hIAA', 'OrderId': '801Wt00000PGGlcIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968iIAA', 'OrderId': '801Wt00000PGijTIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796F5IAI', 'OrderId': '801Wt00000PFyIUIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796N7IAI', 'OrderId': '801Wt00000PFtAmIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796NAIAY', 'OrderId': '801Wt00000PGR7WIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796RzIAI', 'OrderId': '#801Wt00000PGtQPIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S0IAI', 'OrderId': '801Wt00000PGyzYIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S1IAI', 'OrderId': '801Wt00000PH4FMIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796VDIAY', 'OrderId': '801Wt00000PHWY9IAP', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YPIAY', 'OrderId': '801Wt00000PGzijIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YQIAY', 'OrderId': '801Wt00000PGz4MIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796a1IAA', 'OrderId': '801Wt00000PGHEdIAP', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796dFIAQ', 'OrderId': '801Wt00000PGbDPIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796dIIAQ', 'OrderId': '801Wt00000PGj2uIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796jiIAA', 'OrderId': '801Wt00000PGtQRIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796myIAA', 'OrderId': '801Wt00000PHHhCIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796oaIAA', 'OrderId': '801Wt00000PHVdiIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796rlIAA', 'OrderId': '801Wt00000PGoP6IAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796tTIAQ', 'OrderId': '801Wt00000PGxnKIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796v0IAA', 'OrderId': '801Wt00000PGnZVIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wbIAA', 'OrderId': '#801Wt00000PHVlmIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wcIAA', 'OrderId': '801Wt00000PHWUwIAP', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797FxIAI', 'OrderId': '801Wt00000PGj2sIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797MQIAY', 'OrderId': '#801Wt00000PHRFAIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797O5IAI', 'OrderId': '801Wt00000PHVqhIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797axIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797e9IAA', 'OrderId': '801Wt00000PGotiIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797hNIAQ', 'OrderId': '801Wt00000PGYHFIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797j0IAA', 'OrderId': '801Wt00000PGdjpIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797mDIAQ', 'OrderId': '801Wt00000PHWczIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797nsIAA', 'OrderId': '801Wt00000PHHnfIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797pSIAQ', 'OrderId': '801Wt00000PH48HIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797sfIAA', 'OrderId': '801Wt00000PFyITIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797z8IAA', 'OrderId': '801Wt00000PGdGmIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007982LIAQ', 'OrderId': '#801Wt00000PHVqfIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IUIAY', 'OrderId': '#801Wt00000PGHg8IAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IVIAY', 'OrderId': '#801Wt00000PGQrZIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798NKIAY', 'OrderId': '801Wt00000PHWgDIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798S9IAI', 'OrderId': '801Wt00000PFtAnIAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798nBIAQ', 'OrderId': '801Wt00000PGeG6IAL', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798rxIAA', 'OrderId': '801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798wpIAA', 'OrderId': '801Wt00000PHLZXIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007991dIAA', 'OrderId': '801Wt00000PGXXxIAP', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079987IAA', 'OrderId': '#801Wt00000PHWptIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EZIAY', 'OrderId': '801Wt00000PGizbIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799HoIAI', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799JPIAY', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799T3IAI', 'OrderId': '801Wt00000PGY0yIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799ckIAA', 'OrderId': '#801Wt00000PGtLXIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799fxIAA', 'OrderId': '#801Wt00000PHVieIAH', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799srIAA', 'OrderId': '801Wt00000PFyIVIA1', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799w5IAA', 'OrderId': '#801Wt00000PHHMFIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079A0wIAE', 'OrderId': '#801Wt00000PGGhBIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A2aIAE', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A49IAE', 'OrderId': '801Wt00000PFt7UIAT', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AgrIAE', 'OrderId': '#801Wt00000PGizaIAD', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AqXIAU', 'OrderId': '801Wt00000PHRYVIA5', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079As9IAE', 'OrderId': '#801Wt00000PHWjTIAX', 'Product2Id': '01tWt000006hV8LIAU'}]}

exec(code, env_args)
