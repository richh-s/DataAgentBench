code = """import json
import pandas as pd

cases = pd.DataFrame(var_call_32FWeNM4GRQLaFMVMxALPUKz)

last_created = cases['createddate'].max()

# For this dataset, "last 4 quarters" relative to 2023-04-10 is 2022-04-10 to 2023-04-10, already filtered.
# Transfer counts are based on casehistory__c where field__c = 'Owner'. We'll recompute from the already fetched (but empty) history set.

history = pd.DataFrame(var_call_cpzeaq13gbAWt0mRK8b9LDTB)

# Normalize IDs by stripping leading '#'
for col in ['id', 'caseid__c', 'oldvalue__c', 'newvalue__c']:
    if col in history.columns:
        history[col] = history[col].astype(str).str.lstrip('#')

if not history.empty:
    transfers = history.groupby('oldvalue__c').size().reset_index(name='transfer_count')
else:
    transfers = pd.DataFrame(columns=['oldvalue__c', 'transfer_count'])

# Count cases handled by each agent in the period (initial owner only, per Case.ownerid). This is the number of cases they handled at least once via initial assignment.
cases['owner_norm'] = cases['ownerid'].astype(str).str.lstrip('#')
case_counts = cases.groupby('owner_norm').size().reset_index(name='case_count')

# Also count times an agent received a transfer as new owner (so they "handled" more cases).
if not history.empty:
    new_owner_counts = history.groupby('newvalue__c').size().reset_index(name='received_count')
else:
    new_owner_counts = pd.DataFrame(columns=['newvalue__c', 'received_count'])

# Merge to compute total handled cases (initial + received)
merged = case_counts.merge(new_owner_counts, left_on='owner_norm', right_on='newvalue__c', how='left')
merged['received_count'] = merged['received_count'].fillna(0)
merged['handled_cases'] = merged['case_count'] + merged['received_count']

# Add transfer counts (as old owner) per agent
merged = merged.merge(transfers, left_on='owner_norm', right_on='oldvalue__c', how='left')
merged['transfer_count'] = merged['transfer_count'].fillna(0)

# Filter agents who handled more than 0 cases (already true, but keep semantic)
eligible = merged[merged['handled_cases'] > 0].copy()

if eligible.empty:
    result_id = None
else:
    min_transfer = eligible['transfer_count'].min()
    # Among those with minimum transfer_count, pick any (e.g., first sorted by Id for determinism)
    candidates = eligible[eligible['transfer_count'] == min_transfer].sort_values('owner_norm')
    result_id = candidates['owner_norm'].iloc[0]

out = json.dumps(result_id)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cpzeaq13gbAWt0mRK8b9LDTB': [], 'var_call_32FWeNM4GRQLaFMVMxALPUKz': [{'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}]}

exec(code, env_args)
