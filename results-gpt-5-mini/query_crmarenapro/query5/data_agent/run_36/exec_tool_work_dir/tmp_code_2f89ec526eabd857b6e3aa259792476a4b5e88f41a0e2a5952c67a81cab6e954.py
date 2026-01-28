code = """import json
import pandas as pd
from datetime import datetime

# Load order item ids from previous query result
order_items_raw = var_call_d7g4pk6sZzFB2IRqfNWTFUhA
order_item_ids = [str(r.get('Id','')).lstrip('#').strip() for r in order_items_raw if r.get('Id')]
order_item_set = set(order_item_ids)

# Load cases result (may be a large file path)
cases_raw = var_call_ev7FuwBmDElm26XnVPi0oKT2
if isinstance(cases_raw, str):
    # it's a filepath to JSON
    with open(cases_raw, 'r', encoding='utf-8') as f:
        cases = json.load(f)
else:
    cases = cases_raw

# Create DataFrame
df = pd.DataFrame(cases)
# Ensure expected columns exist
for col in ['issueid__c','orderitemid__c','createddate']:
    if col not in df.columns:
        df[col] = None

# Clean ids: remove leading # and surrounding whitespace
df['orderitemid_clean'] = df['orderitemid__c'].fillna('').astype(str).str.lstrip('#').str.strip()
df['issueid_clean'] = df['issueid__c'].fillna('').astype(str).str.strip()

# Parse dates as UTC-aware
df['created_dt'] = pd.to_datetime(df['createddate'], errors='coerce', utc=True)

# Define window: past five months from 2023-01-16 inclusive -> from 2022-08-16 to 2023-01-16
start = pd.Timestamp('2022-08-16', tz='UTC')
end = pd.Timestamp('2023-01-16', tz='UTC') + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

# Filter by date and orderitem id
mask = (df['created_dt'] >= start) & (df['created_dt'] <= end) & (df['orderitemid_clean'].isin(order_item_set))
df_filt = df[mask].copy()

# Count issue occurrences, ignoring empty issue ids
df_filt = df_filt[df_filt['issueid_clean'] != '']

if df_filt.empty:
    top_issue = ''
else:
    counts = df_filt['issueid_clean'].value_counts()
    top_issue = counts.idxmax()

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(top_issue))"""

env_args = {'var_call_d7g4pk6sZzFB2IRqfNWTFUhA': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXgIAI'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '802Wt0000078ypSIAQ'}, {'Id': '802Wt000007906mIAA'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt00000794bTIAQ'}, {'Id': '#802Wt00000794bXIAQ'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt000007959PIAQ'}, {'Id': '#802Wt00000795PSIAY'}, {'Id': '802Wt00000795UKIAY'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796IIIAY'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796lKIAQ'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796n0IAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt000007979WIAQ'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '802Wt00000797RGIAY'}, {'Id': '802Wt00000797SsIAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '#802Wt00000797nqIAA'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '#802Wt000007983xIAA'}, {'Id': '802Wt000007987CIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798NMIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '802Wt00000798iIIAQ'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799EaIAI'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '#802Wt00000799b7IAA'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079A7NIAU'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '#802Wt0000079AfJIAU'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_call_ev7FuwBmDElm26XnVPi0oKT2': 'file_storage/call_ev7FuwBmDElm26XnVPi0oKT2.json'}

exec(code, env_args)
