code = """import pandas as pd
import json
from collections import defaultdict

# Load records from the previous query
records = var_call_DxKld1UNiCYQfNbb7g92ju5

# Create DataFrame
df = pd.DataFrame(records)

# Cleaning function for IDs (remove leading '#', strip whitespace, convert 'None' to None)
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    # remove leading '#'
    while s.startswith('#'):
        s = s[1:]
    if s == '' or s.lower() == 'none':
        return None
    return s

# Apply cleaning
df['old_clean'] = df['oldvalue__c'].apply(clean_id)
df['new_clean'] = df['newvalue__c'].apply(clean_id)
# Clean case id as well
def clean_case(x):
    if x is None:
        return None
    s = str(x).strip()
    while s.startswith('#'):
        s = s[1:]
    return s

df['case_clean'] = df['caseid__c'].apply(clean_case)

# Compute transfer counts: rows where old_clean is not None (a transfer from old -> new)
transfers = df[df['old_clean'].notnull()]
transfer_counts = transfers.groupby('old_clean').size().to_dict()

# Compute handled cases per agent: any appearance in old_clean or new_clean for a case
handled_cases = defaultdict(set)
for _, row in df.iterrows():
    case = row['case_clean']
    if case is None:
        continue
    if row['old_clean'] is not None:
        handled_cases[row['old_clean']].add(case)
    if row['new_clean'] is not None:
        handled_cases[row['new_clean']].add(case)

# Build eligible agents: those who handled > 0 cases
eligible = {}
for agent, cases in handled_cases.items():
    cnt = len(cases)
    if cnt > 0:
        transfers_cnt = int(transfer_counts.get(agent, 0))
        eligible[agent] = {'handled': cnt, 'transfers': transfers_cnt}

if not eligible:
    result = None
else:
    # find min transfer count among eligible agents
    min_transfers = min(v['transfers'] for v in eligible.values())
    agents_min = sorted([agent for agent, v in eligible.items() if v['transfers'] == min_transfers])
    # if single agent, return string, else return list
    if len(agents_min) == 1:
        result = agents_min[0]
    else:
        result = agents_min

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dDtHJIHJsAmaHl52E5R0fGo5': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_hxXMEsngPV0sIn3NBISyPWcz': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_DxKld1UNiCYQfNbb7g92ju5f': [{'id': 'a04Wt00000532wtIAA', 'caseid__c': '500Wt00000DDZtLIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': 'a04Wt00000534XJIAY', 'caseid__c': '500Wt00000DDgLLIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'id': 'a04Wt00000535bQIAQ', 'caseid__c': '500Wt00000DDPIsIAP', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': 'a04Wt00000536Z6IAI', 'caseid__c': '500Wt00000DDzvpIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'id': 'a04Wt00000536m0IAA', 'caseid__c': '500Wt00000DDg8RIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'id': 'a04Wt00000536pCIAQ', 'caseid__c': '500Wt00000DDYpHIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#a04Wt000005376xIAA', 'caseid__c': '500Wt00000DDzxRIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': 'a04Wt00000537GcIAI', 'caseid__c': '500Wt00000DDzPZIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': 'a04Wt00000537ZyIAI', 'caseid__c': '500Wt00000DDzqzIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': 'a04Wt00000537bZIAQ', 'caseid__c': '500Wt00000DDzMLIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': 'a04Wt00000537bbIAA', 'caseid__c': '500Wt00000DDzXeIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': 'a04Wt00000537dFIAQ', 'caseid__c': '500Wt00000DE0LdIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'id': 'a04Wt00000537enIAA', 'caseid__c': '500Wt00000DDzNxIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'id': 'a04Wt00000537gQIAQ', 'caseid__c': '500Wt00000DDxScIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '#a04Wt00000537lHIAQ', 'caseid__c': '500Wt00000DDZJuIAP', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': 'a04Wt00000537mtIAA', 'caseid__c': '500Wt00000DDzvqIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': 'a04Wt00000537oUIAQ', 'caseid__c': '500Wt00000DDyzoIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'id': '#a04Wt00000537oVIAQ', 'caseid__c': '500Wt00000DDPZ0IAP', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': 'a04Wt000005381PIAQ', 'caseid__c': '500Wt00000DDg1zIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'id': 'a04Wt000005382zIAA', 'caseid__c': '500Wt00000DDxduIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': 'a04Wt0000053830IAA', 'caseid__c': '500Wt00000DE0IPIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'id': 'a04Wt00000538PZIAY', 'caseid__c': '500Wt00000DDzcTIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'id': '#a04Wt00000538SnIAI', 'caseid__c': '500Wt00000DDzSoIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'id': 'a04Wt00000538ZGIAY', 'caseid__c': '500Wt00000DDfx8IAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': 'a04Wt00000538arIAA', 'caseid__c': '500Wt00000DDQRsIAP', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'id': 'a04Wt00000538fhIAA', 'caseid__c': '500Wt00000DDzhJIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'id': 'a04Wt00000538xRIAQ', 'caseid__c': '500Wt00000DDzB4IAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': 'a04Wt00000538xSIAQ', 'caseid__c': '500Wt00000DDZtKIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': 'a04Wt000005392HIAQ', 'caseid__c': '500Wt00000DDy8aIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'id': 'a04Wt000005395VIAQ', 'caseid__c': '500Wt00000DDxkMIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': 'a04Wt000005398jIAA', 'caseid__c': '500Wt00000DDg20IAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': 'a04Wt00000539aBIAQ', 'caseid__c': '500Wt00000DDsKuIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'id': 'a04Wt00000539aCIAQ', 'caseid__c': '500Wt00000DDyRvIAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': 'a04Wt00000539ezIAA', 'caseid__c': '500Wt00000DE0K1IAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '#a04Wt00000539iDIAQ', 'caseid__c': '500Wt00000DDZtLIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'id': '#a04Wt00000539jrIAA', 'caseid__c': '500Wt00000DDPsPIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'id': 'a04Wt00000539zyIAA', 'caseid__c': '500Wt00000DE0FDIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'id': '#a04Wt0000053A6PIAU', 'caseid__c': '500Wt00000DE0VJIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'id': '#a04Wt0000053A81IAE', 'caseid__c': '500Wt00000DDzJ8IAL', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}]}

exec(code, env_args)
