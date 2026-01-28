code = """import pandas as pd
import json

cases = pd.DataFrame(var_call_vUW1gcsCnci6PMNsEiq8BHmu)
ch = pd.DataFrame(var_call_ZosqmIQTU3uvr9JcPoT6JC9k)

def clean(s):
    if pd.isna(s):
        return s
    return str(s).strip().lstrip('#')

for col in ['id', 'ownerid', 'createddate', 'closeddate']:
    if col in cases.columns:
        if col in ['id','ownerid']:
            cases[col] = cases[col].apply(clean)
        else:
            cases[col] = pd.to_datetime(cases[col])

for col in ['id','caseid__c','createddate','field__c','oldvalue__c','newvalue__c']:
    if col in ch.columns:
        if col in ['id','caseid__c','field__c','oldvalue__c','newvalue__c']:
            ch[col] = ch[col].apply(lambda x: clean(x) if pd.notna(x) else x)
        else:
            ch[col] = pd.to_datetime(ch[col])

case_ids = set(cases['id'].tolist())
ch_owner = ch[ch['field__c'] == 'Owner Assignment'].copy()
ch_owner = ch_owner[ch_owner['caseid__c'].isin(case_ids)].copy()

assign_counts = ch_owner.groupby('caseid__c').size().rename('assign_count')
assign_counts = assign_counts.reindex(list(case_ids), fill_value=0)

cases = cases.set_index('id')
cases['assign_count'] = assign_counts
cases = cases.reset_index()

pairs_from_history = ch_owner[['caseid__c','newvalue__c']].dropna().copy()
pairs_from_history.columns = ['caseid','agentid']

pairs_from_cases = cases[['id','ownerid']].dropna().copy()
pairs_from_cases.columns = ['caseid','agentid']

all_pairs = pd.concat([pairs_from_history, pairs_from_cases], ignore_index=True)
all_pairs['agentid'] = all_pairs['agentid'].apply(clean)
all_pairs = all_pairs.drop_duplicates()

processed_counts = all_pairs.groupby('agentid')['caseid'].nunique().rename('cases_processed')

agents_gt1 = processed_counts[processed_counts > 1].index.tolist()

non_transferred = cases[cases['assign_count'] <= 1].copy()
non_transferred['handle_seconds'] = (non_transferred['closeddate'] - non_transferred['createddate']).dt.total_seconds()

handle_by_agent = non_transferred.groupby('ownerid')['handle_seconds'].mean()

# Convert complex objects to JSON-serializable
out = {
    'processed_counts': processed_counts.to_dict(),
    'agents_gt1': agents_gt1,
    'handle_by_agent': {k: float(v) for k,v in handle_by_agent.to_dict().items()},
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wkYsMJb9Go3buaez4mGV0L7V': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_vUW1gcsCnci6PMNsEiq8BHmu': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_ZosqmIQTU3uvr9JcPoT6JC9k': [{'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'id': 'a04Wt00000533XzIAI', 'caseid__c': '500Wt00000DDzscIAD', 'createddate': '2023-05-03T00:11:47.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000534KMIAY', 'caseid__c': '500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000534aXIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000534p2IAA', 'caseid__c': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'id': 'a04Wt00000537LSIAY', 'caseid__c': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:59:42.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'id': 'a04Wt00000537TXIAY', 'caseid__c': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'id': 'a04Wt00000537a0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:54:02.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'id': 'a04Wt00000537msIAA', 'caseid__c': '500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000537rkIAA', 'caseid__c': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000537wXIAQ', 'caseid__c': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000537y9IAA', 'caseid__c': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO'}, {'id': 'a04Wt00000537zmIAA', 'caseid__c': '500Wt00000DE02HIAT', 'createddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG'}, {'id': '#a04Wt00000538J8IAI', 'caseid__c': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': '#a04Wt00000538O0IAI', 'caseid__c': '500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW'}, {'id': '#a04Wt00000538nlIAA', 'caseid__c': '500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'id': '#a04Wt00000538qzIAA', 'caseid__c': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'id': '#a04Wt000005390gIAA', 'caseid__c': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt000005392IIAQ', 'caseid__c': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt000005395XIAQ', 'caseid__c': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000539ALIAY', 'caseid__c': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T13:35:12.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG'}, {'id': 'a04Wt00000539GoIAI', 'caseid__c': '500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000539LfIAI', 'caseid__c': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T19:41:08.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW'}], 'var_call_yj64rcxE7yzRbymiFoqIsU60': None}

exec(code, env_args)
