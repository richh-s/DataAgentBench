code = """import json
import pandas as pd

cases = locals()['var_function-call-12556149855108314420']
history_path = locals()['var_function-call-4118261784160134371']

with open(history_path, 'r') as f:
    history = json.load(f)

df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

debug_info = {}
debug_info['cases_count'] = len(df_cases)
debug_info['history_total'] = len(df_history)

relevant_ids = set(df_cases['id'])
df_hist_rel = df_history[df_history['caseid__c'].isin(relevant_ids)]
debug_info['relevant_history_count'] = len(df_hist_rel)

counts = df_hist_rel.groupby('caseid__c').size().to_dict()
debug_info['history_counts_sample'] = list(counts.items())[:5]

agent_counts = {}
for _, case in df_cases.iterrows():
    cid = case['id']
    owner = case['ownerid']
    hist_owners = df_hist_rel[df_hist_rel['caseid__c'] == cid]['newvalue__c'].unique()
    owners = set()
    owners.add(owner)
    owners.update(hist_owners)
    for o in owners:
        agent_counts[o] = agent_counts.get(o, 0) + 1

debug_info['agents_gt_1'] = [k for k,v in agent_counts.items() if v > 1]

eligible_cases = []
for _, case in df_cases.iterrows():
    cid = case['id']
    h_count = len(df_hist_rel[df_hist_rel['caseid__c'] == cid])
    if h_count <= 1:
        eligible_cases.append(cid)

debug_info['eligible_cases_count'] = len(eligible_cases)
debug_info['eligible_cases_sample'] = eligible_cases[:5]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9241346808285847141': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-12556149855108314420': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-4118261784160134371': 'file_storage/function-call-4118261784160134371.json', 'var_function-call-6205398845989989636': 'No matching agent', 'var_function-call-4495172818801594668': 'debug_done'}

exec(code, env_args)
