code = """import json
from collections import Counter

cases = var_call_ZucAgs927kawljwYkARjvKFE

owner_counts = Counter()
for row in cases:
    owner = row['ownerid'].strip() if isinstance(row['ownerid'], str) else row['ownerid']
    if owner:
        owner_counts[owner] += 1

# agents who handled more than 0 cases are all owners with count > 0
if owner_counts:
    min_count = min(owner_counts.values())
    # among those with >0 cases, min_count will naturally be >=1
    # get any one agent with this minimal count
    candidates = [owner for owner, cnt in owner_counts.items() if cnt == min_count]
    # deterministic: sort and pick first
    agent_id = sorted(candidates)[0]
else:
    agent_id = None

result = json.dumps(agent_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_v2ILZWNTySbD79cSnCWbGURV': [], 'var_call_ZucAgs927kawljwYkARjvKFE': [{'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}]}

exec(code, env_args)
