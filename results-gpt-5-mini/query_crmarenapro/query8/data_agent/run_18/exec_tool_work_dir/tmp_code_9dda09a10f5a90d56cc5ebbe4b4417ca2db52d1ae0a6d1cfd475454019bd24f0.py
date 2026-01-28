code = """import pandas as pd
import json

df = pd.DataFrame(var_call_wox5BfFpJJlhHkYTU5FXIT9T)
# Clean function
def clean_id(x):
    if x is None:
        return None
    if not isinstance(x, str):
        x = str(x)
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    if x.lower() == 'none' or x == '':
        return None
    return x

for col in ['oldvalue__c', 'newvalue__c']:
    if col in df.columns:
        df[col] = df[col].apply(clean_id)
    else:
        df[col] = None

# handled_count: count of times agent appears as newvalue__c
handled = df[df['newvalue__c'].notnull()].groupby('newvalue__c').size().reset_index(name='handled_count')
handled = handled.rename(columns={'newvalue__c': 'agent_id'})

# transfer_count: count of times agent appears as oldvalue__c in a transfer (old not null and new not null)
transfers = df[(df['oldvalue__c'].notnull()) & (df['newvalue__c'].notnull())].groupby('oldvalue__c').size().reset_index(name='transfer_count')
transfers = transfers.rename(columns={'oldvalue__c': 'agent_id'})

# Merge
agg = pd.merge(handled, transfers, on='agent_id', how='left')
agg['transfer_count'] = agg['transfer_count'].fillna(0).astype(int)

# Filter agents who handled > 0 cases (handled_count > 0) - already the handled list
# Find agent(s) with minimum transfer_count
min_tc = agg['transfer_count'].min()
min_agents = agg[agg['transfer_count'] == min_tc]['agent_id'].tolist()

# Deterministic single agent choice: lexicographically smallest id
min_agents_sorted = sorted(min_agents)
result_id = min_agents_sorted[0] if len(min_agents_sorted) > 0 else None

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_s4YxHaaO0fa82KiAukNz2jar': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_OSdmX5xUgBw3USrPyTXpf82l': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_wox5BfFpJJlhHkYTU5FXIT9T': [{'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'caseid__c': '500Wt00000DDgLLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDPIsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDg8RIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'caseid__c': '500Wt00000DDYpHIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzxRIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzPZIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'caseid__c': '500Wt00000DDzqzIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzMLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzXeIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DE0LdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'caseid__c': '500Wt00000DDzNxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDxScIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDZJuIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzvqIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzoIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDPZ0IAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDg1zIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDxduIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0IPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzcTIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzSoIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'caseid__c': '500Wt00000DDfx8IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDQRsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzB4IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDZtKIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'caseid__c': '500Wt00000DDy8aIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DDxkMIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'caseid__c': '500Wt00000DDg20IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDsKuIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'caseid__c': '500Wt00000DDyRvIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DE0K1IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'caseid__c': '500Wt00000DE0FDIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0VJIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzJ8IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}]}

exec(code, env_args)
