code = """import json
import pandas as pd
# var_call_ChTdQtjC7kQkhRsSZHm6uPcH is available from previous query
records = var_call_ChTdQtjC7kQkhRsSZHm6uPcH
# Load into DataFrame
df = pd.DataFrame(records)
# Normalize values: strip whitespace, treat 'None' or None as None
for col in ['oldvalue__c','newvalue__c']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace({'None': None, 'none': None, 'nan': None, 'None.0': None})
# Compute handled counts (appearances as newvalue__c)
handled = df['newvalue__c'].dropna()
handled_counts = handled.value_counts().to_dict()
# Compute transfer counts (appearances as oldvalue__c) but only when oldvalue not None
oldvals = df['oldvalue__c'].dropna()
transfer_counts = oldvals.value_counts().to_dict()
# Create set of agents who handled >0 cases
agents_handled = set(handled_counts.keys())
# For each agent in agents_handled, get transfer count (default 0)
agent_stats = []
for agent in agents_handled:
    tcount = int(transfer_counts.get(agent, 0))
    hcount = int(handled_counts.get(agent, 0))
    if hcount > 0:
        agent_stats.append({'agent': agent, 'handled': hcount, 'transfers': tcount})
# If no agents, return None
if not agent_stats:
    result = None
else:
    # Find minimal transfers
    min_transfer = min(a['transfers'] for a in agent_stats)
    candidates = [a for a in agent_stats if a['transfers'] == min_transfer]
    # If tie, choose lexicographically smallest agent id
    candidates_sorted = sorted(candidates, key=lambda x: x['agent'])
    chosen = candidates_sorted[0]['agent']
    result = chosen
# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ChTdQtjC7kQkhRsSZHm6uPcH': [{'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDgLLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDPIsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDg8RIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDYpHIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzxRIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzPZIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzqzIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzMLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzXeIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE0LdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzNxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDxScIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDZJuIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzvqIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyzoIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDPZ0IAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDg1zIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDxduIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE0IPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzcTIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzSoIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDfx8IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDQRsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzB4IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDZtKIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDy8aIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDxkMIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDg20IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDsKuIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyRvIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE0K1IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE0FDIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE0VJIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzJ8IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
