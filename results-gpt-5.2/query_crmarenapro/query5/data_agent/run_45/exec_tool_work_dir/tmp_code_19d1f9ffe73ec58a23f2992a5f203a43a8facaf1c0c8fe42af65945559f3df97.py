code = """import json, pandas as pd
from datetime import datetime

# Load order items for the product
orderitems = pd.DataFrame(var_call_Drnsek70NbE8HGpaTxqOFeBs)
order_set = set(orderitems['orderitem_id_clean'].astype(str))

# Load cases (large) from file
path = var_call_AeaI15YmHzr8UyXwalc0gaDG
with open(path, 'r') as f:
    cases_raw = json.load(f)

df = pd.DataFrame(cases_raw)
# Clean ids
for col in ['issue_id','orderitemid__c']:
    df[col] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Parse createddate and filter last 5 months from 2023-01-16 => >= 2022-08-16
cutoff = pd.Timestamp('2022-08-16T00:00:00Z')
df['created_ts'] = pd.to_datetime(df['createddate'], errors='coerce', utc=True)

filt = df['orderitemid__c'].isin(order_set) & (df['created_ts'] >= cutoff) & df['issue_id'].notna() & (df['issue_id']!='None')
df_f = df.loc[filt, ['issue_id']]

counts = df_f.value_counts().reset_index(name='cnt')
counts = counts.sort_values(['cnt','issue_id'], ascending=[False, True])
issue_id = counts.iloc[0]['issue_id'] if len(counts) else None

print('__RESULT__:')
print(json.dumps({'issue_id': issue_id}))"""

env_args = {'var_call_Drnsek70NbE8HGpaTxqOFeBs': [{'orderitem_id_clean': '802Wt0000078wz5IAA'}, {'orderitem_id_clean': '802Wt0000078xAAIAY'}, {'orderitem_id_clean': '802Wt0000078yXgIAI'}, {'orderitem_id_clean': '802Wt0000078yXiIAI'}, {'orderitem_id_clean': '802Wt0000078ypSIAQ'}, {'orderitem_id_clean': '802Wt000007906mIAA'}, {'orderitem_id_clean': '802Wt00000790WEIAY'}, {'orderitem_id_clean': '802Wt00000792gDIAQ'}, {'orderitem_id_clean': '802Wt00000792zTIAQ'}, {'orderitem_id_clean': '802Wt0000079315IAA'}, {'orderitem_id_clean': '802Wt00000793sTIAQ'}, {'orderitem_id_clean': '802Wt00000794F3IAI'}, {'orderitem_id_clean': '802Wt00000794F4IAI'}, {'orderitem_id_clean': '802Wt00000794JmIAI'}, {'orderitem_id_clean': '802Wt00000794YFIAY'}, {'orderitem_id_clean': '802Wt00000794YJIAY'}, {'orderitem_id_clean': '802Wt00000794bTIAQ'}, {'orderitem_id_clean': '802Wt00000794bXIAQ'}, {'orderitem_id_clean': '802Wt000007959OIAQ'}, {'orderitem_id_clean': '802Wt000007959PIAQ'}, {'orderitem_id_clean': '802Wt00000795PSIAY'}, {'orderitem_id_clean': '802Wt00000795UKIAY'}, {'orderitem_id_clean': '802Wt00000795akIAA'}, {'orderitem_id_clean': '802Wt00000795ywIAA'}, {'orderitem_id_clean': '802Wt000007962JIAQ'}, {'orderitem_id_clean': '802Wt000007968hIAA'}, {'orderitem_id_clean': '802Wt000007968iIAA'}, {'orderitem_id_clean': '802Wt00000796F5IAI'}, {'orderitem_id_clean': '802Wt00000796IIIAY'}, {'orderitem_id_clean': '802Wt00000796N7IAI'}, {'orderitem_id_clean': '802Wt00000796NAIAY'}, {'orderitem_id_clean': '802Wt00000796RzIAI'}, {'orderitem_id_clean': '802Wt00000796S0IAI'}, {'orderitem_id_clean': '802Wt00000796S1IAI'}, {'orderitem_id_clean': '802Wt00000796VDIAY'}, {'orderitem_id_clean': '802Wt00000796YPIAY'}, {'orderitem_id_clean': '802Wt00000796YQIAY'}, {'orderitem_id_clean': '802Wt00000796a1IAA'}, {'orderitem_id_clean': '802Wt00000796dFIAQ'}, {'orderitem_id_clean': '802Wt00000796dIIAQ'}, {'orderitem_id_clean': '802Wt00000796jiIAA'}, {'orderitem_id_clean': '802Wt00000796lKIAQ'}, {'orderitem_id_clean': '802Wt00000796myIAA'}, {'orderitem_id_clean': '802Wt00000796n0IAA'}, {'orderitem_id_clean': '802Wt00000796oaIAA'}, {'orderitem_id_clean': '802Wt00000796rlIAA'}, {'orderitem_id_clean': '802Wt00000796tTIAQ'}, {'orderitem_id_clean': '802Wt00000796v0IAA'}, {'orderitem_id_clean': '802Wt00000796wbIAA'}, {'orderitem_id_clean': '802Wt00000796wcIAA'}, {'orderitem_id_clean': '802Wt000007979WIAQ'}, {'orderitem_id_clean': '802Wt00000797FxIAI'}, {'orderitem_id_clean': '802Wt00000797MQIAY'}, {'orderitem_id_clean': '802Wt00000797O5IAI'}, {'orderitem_id_clean': '802Wt00000797RGIAY'}, {'orderitem_id_clean': '802Wt00000797SsIAI'}, {'orderitem_id_clean': '802Wt00000797axIAA'}, {'orderitem_id_clean': '802Wt00000797e9IAA'}, {'orderitem_id_clean': '802Wt00000797hNIAQ'}, {'orderitem_id_clean': '802Wt00000797j0IAA'}, {'orderitem_id_clean': '802Wt00000797mDIAQ'}, {'orderitem_id_clean': '802Wt00000797nqIAA'}, {'orderitem_id_clean': '802Wt00000797nsIAA'}, {'orderitem_id_clean': '802Wt00000797pSIAQ'}, {'orderitem_id_clean': '802Wt00000797sfIAA'}, {'orderitem_id_clean': '802Wt00000797z8IAA'}, {'orderitem_id_clean': '802Wt000007982LIAQ'}, {'orderitem_id_clean': '802Wt000007983xIAA'}, {'orderitem_id_clean': '802Wt000007987CIAQ'}, {'orderitem_id_clean': '802Wt00000798IUIAY'}, {'orderitem_id_clean': '802Wt00000798IVIAY'}, {'orderitem_id_clean': '802Wt00000798NKIAY'}, {'orderitem_id_clean': '802Wt00000798NMIAY'}, {'orderitem_id_clean': '802Wt00000798S9IAI'}, {'orderitem_id_clean': '802Wt00000798iIIAQ'}, {'orderitem_id_clean': '802Wt00000798nBIAQ'}, {'orderitem_id_clean': '802Wt00000798rxIAA'}, {'orderitem_id_clean': '802Wt00000798wpIAA'}, {'orderitem_id_clean': '802Wt000007991dIAA'}, {'orderitem_id_clean': '802Wt0000079987IAA'}, {'orderitem_id_clean': '802Wt00000799EZIAY'}, {'orderitem_id_clean': '802Wt00000799EaIAI'}, {'orderitem_id_clean': '802Wt00000799HoIAI'}, {'orderitem_id_clean': '802Wt00000799JPIAY'}, {'orderitem_id_clean': '802Wt00000799T3IAI'}, {'orderitem_id_clean': '802Wt00000799b7IAA'}, {'orderitem_id_clean': '802Wt00000799ckIAA'}, {'orderitem_id_clean': '802Wt00000799fxIAA'}, {'orderitem_id_clean': '802Wt00000799srIAA'}, {'orderitem_id_clean': '802Wt00000799w5IAA'}, {'orderitem_id_clean': '802Wt0000079A0wIAE'}, {'orderitem_id_clean': '802Wt0000079A2aIAE'}, {'orderitem_id_clean': '802Wt0000079A49IAE'}, {'orderitem_id_clean': '802Wt0000079A7NIAU'}, {'orderitem_id_clean': '802Wt0000079AU1IAM'}, {'orderitem_id_clean': '802Wt0000079AfJIAU'}, {'orderitem_id_clean': '802Wt0000079AgrIAE'}, {'orderitem_id_clean': '802Wt0000079AqXIAU'}, {'orderitem_id_clean': '802Wt0000079As9IAE'}], 'var_call_AeaI15YmHzr8UyXwalc0gaDG': 'file_storage/call_AeaI15YmHzr8UyXwalc0gaDG.json'}

exec(code, env_args)
