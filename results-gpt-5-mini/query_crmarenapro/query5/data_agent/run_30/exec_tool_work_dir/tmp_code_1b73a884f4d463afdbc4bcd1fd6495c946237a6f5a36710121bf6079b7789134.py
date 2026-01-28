code = """import pandas as pd
import json
from datetime import datetime

# Load the cases data from the file path in var_call_8CG6hOqrNKH4siY1Cb5pl8JY
import json as _json
with open(var_call_8CG6hOqrNKH4siY1Cb5pl8JY, 'r') as f:
    cases_raw = _json.load(f)

# Load order items from var_call_1sHKgNYRd1cRkIVXZl3v9pbB (it's already a list)
oi_raw = var_call_1sHKgNYRd1cRkIVXZl3v9pbB

# Create dataframes
df_cases = pd.DataFrame(cases_raw)
df_oi = pd.DataFrame(oi_raw)

# cleaning function
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Clean relevant columns
if not df_cases.empty:
    df_cases['orderitem_clean'] = df_cases['orderitemid__c'].apply(clean_id)
    df_cases['issueid_clean'] = df_cases['issueid__c'].apply(lambda x: clean_id(x) if pd.notnull(x) else None)
    df_cases['created_dt'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

if not df_oi.empty:
    df_oi['Id_clean'] = df_oi['Id'].apply(clean_id)
    df_oi['Product2Id_clean'] = df_oi['Product2Id'].apply(clean_id)

# Target product id cleaned
target_pid = '01tWt000006hV8LIAU'

# Get set of orderitem ids for this product
oi_set = set(df_oi.loc[df_oi['Product2Id_clean'] == target_pid, 'Id_clean'].dropna().unique())

# Filter cases linked to these order items
df_linked = df_cases[df_cases['orderitem_clean'].isin(oi_set)].copy()

# Define window: past five months from 2023-01-16 -> from 2022-08-16 (inclusive) to 2023-01-16
start_dt = pd.to_datetime('2022-08-16T00:00:00Z')
end_dt = pd.to_datetime('2023-01-16T23:59:59Z')

if not df_linked.empty:
    df_linked = df_linked[(df_linked['created_dt'] >= start_dt) & (df_linked['created_dt'] <= end_dt)]

# Count issue occurrences
counts = {}
if not df_linked.empty:
    for v in df_linked['issueid_clean'].dropna():
        vs = v.strip()
        if vs == '':
            continue
        counts[vs] = counts.get(vs, 0) + 1

# Determine most frequent issue id
if counts:
    max_count = max(counts.values())
    # get all with max_count and pick lexicographically smallest to be deterministic
    candidates = sorted([k for k,v in counts.items() if v==max_count])
    most_freq = candidates[0]
else:
    most_freq = ""

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(most_freq))"""

env_args = {'var_call_5QpEcYsclONDfyK6v2cTSe9P': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_K8qz2oB1QyPns91IkzMwORu3': 'file_storage/call_K8qz2oB1QyPns91IkzMwORu3.json', 'var_call_NU1WjvykAD9Fz8ZpnNaIRdpY': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}], 'var_call_1sHKgNYRd1cRkIVXZl3v9pbB': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHQuFIAX'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGHg7IAH'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHWjUIAX'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGjNsIAL'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHHMIIA5'}, {'Id': '802Wt000007906mIAA', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGdVHIA1'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHLzNIAX'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGbDQIA1'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGoc0IAD'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGzVrIAL'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGoc1IAD'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGbdMIAT'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGyzXIAT'}, {'Id': '#802Wt00000794JmIAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHRVKIA5'}, {'Id': '#802Wt00000794YFIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PH4FLIA1'}, {'Id': '802Wt00000794YJIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGzikIAD'}, {'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGj2tIAD'}, {'Id': '#802Wt00000794bXIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PH8vfIAD'}, {'Id': '802Wt000007959OIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGzikIAD'}, {'Id': '802Wt000007959PIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGXwDIAX'}, {'Id': '#802Wt00000795PSIAY', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGRpDIAX'}, {'Id': '802Wt00000795UKIAY', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHHMGIA5'}, {'Id': '802Wt00000795akIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGzFlIAL'}, {'Id': '802Wt00000795ywIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGaCTIA1'}, {'Id': '802Wt000007962JIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGXwBIAX'}, {'Id': '802Wt000007968hIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGGlcIAH'}, {'Id': '802Wt000007968iIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGijTIAT'}, {'Id': '802Wt00000796F5IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFyIUIA1'}, {'Id': '#802Wt00000796IIIAY', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGYqdIAH'}, {'Id': '#802Wt00000796N7IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFtAmIAL'}, {'Id': '802Wt00000796NAIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGR7WIAX'}, {'Id': '802Wt00000796RzIAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGtQPIA1'}, {'Id': '802Wt00000796S0IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGyzYIAT'}, {'Id': '802Wt00000796S1IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PH4FMIA1'}, {'Id': '802Wt00000796VDIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHWY9IAP'}, {'Id': '802Wt00000796YPIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGzijIAD'}, {'Id': '802Wt00000796YQIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGz4MIAT'}, {'Id': '802Wt00000796a1IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGHEdIAP'}, {'Id': '802Wt00000796dFIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGbDPIA1'}, {'Id': '#802Wt00000796dIIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGj2uIAD'}, {'Id': '#802Wt00000796jiIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGtQRIA1'}, {'Id': '802Wt00000796lKIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHLhaIAH'}, {'Id': '802Wt00000796myIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHHhCIAX'}, {'Id': '802Wt00000796n0IAA', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGGTwIAP'}, {'Id': '802Wt00000796oaIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHVdiIAH'}, {'Id': '802Wt00000796rlIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGoP6IAL'}, {'Id': '802Wt00000796tTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGxnKIAT'}, {'Id': '802Wt00000796v0IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGnZVIA1'}, {'Id': '802Wt00000796wbIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHVlmIAH'}, {'Id': '802Wt00000796wcIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHWUwIAP'}, {'Id': '802Wt000007979WIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGzApIAL'}, {'Id': '802Wt00000797FxIAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGj2sIAD'}, {'Id': '802Wt00000797MQIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHRFAIA5'}, {'Id': '#802Wt00000797O5IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHVqhIAH'}, {'Id': '802Wt00000797RGIAY', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHWZlIAP'}, {'Id': '802Wt00000797SsIAI', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHVidIAH'}, {'Id': '#802Wt00000797axIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGRh3IAH'}, {'Id': '802Wt00000797e9IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGotiIAD'}, {'Id': '802Wt00000797hNIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGYHFIA5'}, {'Id': '802Wt00000797j0IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGdjpIAD'}, {'Id': '#802Wt00000797mDIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHWczIAH'}, {'Id': '#802Wt00000797nqIAA', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHRVKIA5'}, {'Id': '802Wt00000797nsIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHHnfIAH'}, {'Id': '#802Wt00000797pSIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PH48HIAT'}, {'Id': '802Wt00000797sfIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFyITIA1'}, {'Id': '802Wt00000797z8IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGdGmIAL'}, {'Id': '802Wt000007982LIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHVqfIAH'}, {'Id': '#802Wt000007983xIAA', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGyzWIAT'}, {'Id': '802Wt000007987CIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGQrYIAX'}, {'Id': '802Wt00000798IUIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGHg8IAH'}, {'Id': '802Wt00000798IVIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGQrZIAX'}, {'Id': '802Wt00000798NKIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHWgDIAX'}, {'Id': '#802Wt00000798NMIAY', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHVicIAH'}, {'Id': '#802Wt00000798S9IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFtAnIAL'}, {'Id': '802Wt00000798iIIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHRTiIAP'}, {'Id': '#802Wt00000798nBIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGeG6IAL'}, {'Id': '802Wt00000798rxIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGVJJIA5'}, {'Id': '802Wt00000798wpIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHLZXIA5'}, {'Id': '802Wt000007991dIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGXXxIAP'}, {'Id': '802Wt0000079987IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHWptIAH'}, {'Id': '802Wt00000799EZIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGizbIAD'}, {'Id': '802Wt00000799EaIAI', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGtQSIA1'}, {'Id': '802Wt00000799HoIAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHQz1IAH'}, {'Id': '#802Wt00000799JPIAY', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGe00IAD'}, {'Id': '802Wt00000799T3IAI', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGY0yIAH'}, {'Id': '#802Wt00000799b7IAA', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '801Wt00000PGyWWIA1'}, {'Id': '802Wt00000799ckIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGtLXIA1'}, {'Id': '#802Wt00000799fxIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHVieIAH'}, {'Id': '802Wt00000799srIAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFyIVIA1'}, {'Id': '802Wt00000799w5IAA', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHHMFIA5'}, {'Id': '#802Wt0000079A0wIAE', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGGhBIAX'}, {'Id': '802Wt0000079A2aIAE', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHVkDIAX'}, {'Id': '802Wt0000079A49IAE', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PFt7UIAT'}, {'Id': '802Wt0000079A7NIAU', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHWl3IAH'}, {'Id': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHRYWIA5'}, {'Id': '#802Wt0000079AfJIAU', 'Product2Id': '#01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHQuGIAX'}, {'Id': '802Wt0000079AgrIAE', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PGizaIAD'}, {'Id': '802Wt0000079AqXIAU', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '801Wt00000PHRYVIA5'}, {'Id': '802Wt0000079As9IAE', 'Product2Id': '01tWt000006hV8LIAU', 'OrderId': '#801Wt00000PHWjTIAX'}], 'var_call_8CG6hOqrNKH4siY1Cb5pl8JY': 'file_storage/call_8CG6hOqrNKH4siY1Cb5pl8JY.json'}

exec(code, env_args)
