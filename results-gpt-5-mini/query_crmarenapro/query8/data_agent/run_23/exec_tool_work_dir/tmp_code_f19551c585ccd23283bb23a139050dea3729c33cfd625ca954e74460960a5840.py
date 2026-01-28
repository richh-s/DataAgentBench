code = """import json
# var_call_QPqihLTPv81m2yxat0KSU9Lm is available
records = var_call_QPqihLTPv81m2yxat0KSU9Lm

def normalize_id(v):
    if v is None:
        return None
    if isinstance(v, str):
        s = v.strip()
        if s == '' or s.lower() == 'none':
            return None
        # remove leading # if present
        if s.startswith('#'):
            s = s[1:]
        return s
    return str(v)

handled_cases = {}  # agent -> set(caseids)
transfers_out = {}  # agent -> count

for r in records:
    caseid = r.get('caseid__c')
    old = normalize_id(r.get('oldvalue__c'))
    new = normalize_id(r.get('newvalue__c'))
    # normalize caseid as well
    if caseid is not None:
        caseid = caseid.strip()
        if caseid.startswith('#'):
            caseid = caseid[1:]
    # count handled (as new owner) unique cases
    if new is not None:
        handled_cases.setdefault(new, set()).add(caseid)
    # count transfers out for old owners (transfers from old to new)
    if old is not None:
        # Only count if actually transferred (new different or present)
        # If new is None, it's odd but we'll still count as transfer out if old present
        transfers_out[old] = transfers_out.get(old, 0) + 1

# Build list of agents who handled >0 cases (unique case count >0)
agents = []
for agent, cases in handled_cases.items():
    if len([c for c in cases if c is not None]) > 0:
        agents.append(agent)

if not agents:
    result = None
else:
    # compute transfers for these agents (default 0)
    agent_transfer_pairs = [(agent, transfers_out.get(agent, 0)) for agent in agents]
    # find minimum transfer count
    min_count = min(cnt for a, cnt in agent_transfer_pairs)
    # get agents with min_count
    min_agents = [a for a, cnt in agent_transfer_pairs if cnt == min_count]
    # tie-breaker: lexicographically smallest id
    selected = sorted(min_agents)[0]
    result = selected

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4sFIf4TAwVFLRJwYA3EF2Dwh': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_H18X5KLK06dUdIVNssXWkZNR': [{'field__c': 'Owner Assignment'}, {'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}], 'var_call_opn1GHanFsQ9StWdulXcFh01': 'file_storage/call_opn1GHanFsQ9StWdulXcFh01.json', 'var_call_QPqihLTPv81m2yxat0KSU9Lm': [{'caseid__c': '500Wt00000DDzxRIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDg1zIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDPZ0IAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDg8RIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'caseid__c': '500Wt00000DDgLLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'caseid__c': '500Wt00000DDsKuIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'caseid__c': '500Wt00000DDzSoIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'caseid__c': '500Wt00000DDzcTIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDPIsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0IPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzJ8IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'caseid__c': '500Wt00000DDYpHIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzXeIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDxduIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'caseid__c': '500Wt00000DDxScIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DE0K1IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDg20IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDfx8IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDZtKIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'caseid__c': '500Wt00000DDzqzIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzoIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDZJuIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDxkMIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'caseid__c': '500Wt00000DDy8aIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0LdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'caseid__c': '500Wt00000DDzvqIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzB4IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDQRsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'caseid__c': '500Wt00000DDzMLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzNxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzPZIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'caseid__c': '500Wt00000DDyRvIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DE0FDIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0VJIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'caseid__c': '500Wt00000DDzvpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}]}

exec(code, env_args)
