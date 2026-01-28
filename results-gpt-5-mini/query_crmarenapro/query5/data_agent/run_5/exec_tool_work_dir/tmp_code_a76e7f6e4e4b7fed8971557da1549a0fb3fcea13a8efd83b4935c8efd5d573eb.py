code = """import json
import pandas as pd
from datetime import datetime

# Load variables from storage
orderitems = var_call_Kzf9SvbsWT1PyXIuk07vGngL
cases_path = var_call_BmayfSGA739oPJyJxuQLoQBt

# Read cases JSON file
with open(cases_path, 'r') as f:
    cases = json.load(f)

# Convert to DataFrames
df_orders = pd.DataFrame(orderitems)
df_cases = pd.DataFrame(cases)

# Cleaning function for IDs and text
def clean_id(x):
    if x is None:
        return None
    s = str(x)
    s = s.strip()
    # remove leading '#' characters
    while s.startswith('#'):
        s = s[1:]
    return s.strip()

# Apply cleaning
for col in ['Id', 'Product2Id']:
    if col in df_orders.columns:
        df_orders[col+'_clean'] = df_orders[col].apply(clean_id)

for col in ['id', 'issueid__c', 'orderitemid__c', 'createddate']:
    if col in df_cases.columns:
        if col.startswith('created'):
            # leave createddate as is for parsing
            df_cases['createddate_parsed'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
        else:
            df_cases[col+'_clean'] = df_cases[col].apply(clean_id)

# Filter orderitems for the product id (cleaned)
target_product = '01tWt000006hV8LIAU'
matched_orders = df_orders[df_orders['Product2Id_clean'] == target_product]
matched_order_ids = set(matched_orders['Id_clean'].tolist())

# Define date window: past five months relative to 2023-01-16 -> from 2022-08-16 to 2023-01-16 inclusive
start_date = pd.to_datetime('2022-08-16')
end_date = pd.to_datetime('2023-01-16')

# Filter cases in date range and matching order item ids
if 'orderitemid__c_clean' in df_cases.columns and 'createddate_parsed' in df_cases.columns:
    df_cases_matched = df_cases[
        df_cases['orderitemid__c_clean'].isin(matched_order_ids) &
        (df_cases['createddate_parsed'] >= start_date) &
        (df_cases['createddate_parsed'] <= end_date)
    ].copy()
else:
    df_cases_matched = pd.DataFrame()

# Clean issue ids and count
if not df_cases_matched.empty and 'issueid__c_clean' in df_cases_matched.columns:
    df_cases_matched = df_cases_matched[df_cases_matched['issueid__c_clean'].notna()]
    counts = df_cases_matched['issueid__c_clean'].value_counts().reset_index()
    counts.columns = ['issueid', 'count']
    if not counts.empty:
        # Sort by count desc, then issueid lexicographically to break ties
        counts = counts.sort_values(by=['count', 'issueid'], ascending=[False, True])
        top_issue = counts.iloc[0]['issueid']
    else:
        top_issue = None
else:
    top_issue = None

# Prepare output
output = json.dumps(top_issue)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_9Ce1zlbrgn4sKmtKpZe6QIHS': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_Kzf9SvbsWT1PyXIuk07vGngL': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007906mIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794JmIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794YFIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794YJIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794bXIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007959OIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007959PIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000795PSIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795UKIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795akIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795ywIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007962JIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968hIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968iIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796F5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796IIIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796N7IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796NAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796RzIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S0IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S1IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796VDIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796a1IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796dFIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796dIIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796jiIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796lKIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796myIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796n0IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796oaIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796rlIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796tTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796v0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wbIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wcIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007979WIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797FxIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797MQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797O5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797RGIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797SsIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797axIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797e9IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797hNIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797j0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797mDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797nqIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797nsIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797pSIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797sfIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797z8IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007982LIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt000007983xIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007987CIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IUIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IVIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798NKIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798NMIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798S9IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798iIIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798nBIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798rxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798wpIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007991dIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079987IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EZIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EaIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799HoIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799JPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799T3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799b7IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799ckIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799fxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799srIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799w5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079A0wIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A2aIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A49IAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A7NIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079AfJIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AgrIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AqXIAU', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079As9IAE', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_call_BmayfSGA739oPJyJxuQLoQBt': 'file_storage/call_BmayfSGA739oPJyJxuQLoQBt.json'}

exec(code, env_args)
