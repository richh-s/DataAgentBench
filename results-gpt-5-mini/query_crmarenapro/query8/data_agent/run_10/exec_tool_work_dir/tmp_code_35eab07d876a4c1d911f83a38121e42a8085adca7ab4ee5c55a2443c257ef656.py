code = """import json
# var_call_VUmBvodirkDGyh3LRHjxcWmb is available from previous query
records = var_call_VUmBvodirkDGyh3LRHjxcWmb

def clean_id(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.lower() == 'none' or s == '':
        return None
    # remove leading # characters
    while s.startswith('#'):
        s = s[1:]
    return s

# prepare structures
handled_cases = {}  # agent_id -> set of case ids
transfer_counts = {}  # agent_id -> int

for r in records:
    caseid = clean_id(r.get('caseid__c'))
    oldv = clean_id(r.get('oldvalue__c'))
    newv = clean_id(r.get('newvalue__c'))

    # if oldv present, it's a transfer from oldv to newv (unless oldv is None meaning initial assignment)
    if oldv is not None:
        transfer_counts.setdefault(oldv, 0)
        transfer_counts[oldv] += 1
        handled_cases.setdefault(oldv, set()).add(caseid)
    # newv is an assignment to newv (counts as handled)
    if newv is not None:
        handled_cases.setdefault(newv, set()).add(caseid)
        transfer_counts.setdefault(newv, 0)  # ensure present with 0 if never transferred away

# Filter agents who handled more than 0 cases
agents_with_handled = {aid: len(cases) for aid, cases in handled_cases.items() if len(cases) > 0}

if not agents_with_handled:
    result = None
else:
    # consider only agents with handled>0
    candidates = list(agents_with_handled.keys())
    # compute min transfer count among candidates
    min_count = None
    for a in candidates:
        cnt = transfer_counts.get(a, 0)
        if min_count is None or cnt < min_count:
            min_count = cnt
    # get agents with this min_count
    min_agents = [a for a in candidates if transfer_counts.get(a, 0) == min_count]
    # choose lexicographically smallest for determinism
    chosen = sorted(min_agents)[0]
    result = chosen

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KtUgc6INDrSbSt9fOKAgo3Qe': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_VUmBvodirkDGyh3LRHjxcWmb': [{'id': '#a04Wt00000532wsIAA', 'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000'}, {'id': 'a04Wt00000532wtIAA', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': 'a04Wt00000534XJIAY', 'caseid__c': '500Wt00000DDgLLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'id': 'a04Wt00000535bQIAQ', 'caseid__c': '500Wt00000DDPIsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': 'a04Wt00000536m0IAA', 'caseid__c': '500Wt00000DDg8RIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'id': 'a04Wt00000536pCIAQ', 'caseid__c': '500Wt00000DDYpHIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#a04Wt000005376xIAA', 'caseid__c': '500Wt00000DDzxRIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': 'a04Wt00000537GcIAI', 'caseid__c': '500Wt00000DDzPZIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': 'a04Wt00000537ZyIAI', 'caseid__c': '500Wt00000DDzqzIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': 'a04Wt00000537bZIAQ', 'caseid__c': '500Wt00000DDzMLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': 'a04Wt00000537bbIAA', 'caseid__c': '500Wt00000DDzXeIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': 'a04Wt00000537dFIAQ', 'caseid__c': '500Wt00000DE0LdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'id': 'a04Wt00000537enIAA', 'caseid__c': '500Wt00000DDzNxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'id': 'a04Wt00000537gQIAQ', 'caseid__c': '500Wt00000DDxScIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '#a04Wt00000537lHIAQ', 'caseid__c': '500Wt00000DDZJuIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': 'a04Wt00000537mtIAA', 'caseid__c': '500Wt00000DDzvqIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': 'a04Wt00000537oUIAQ', 'caseid__c': '500Wt00000DDyzoIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'id': '#a04Wt00000537oVIAQ', 'caseid__c': '500Wt00000DDPZ0IAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': 'a04Wt000005381PIAQ', 'caseid__c': '500Wt00000DDg1zIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'id': 'a04Wt000005382zIAA', 'caseid__c': '500Wt00000DDxduIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': 'a04Wt0000053830IAA', 'caseid__c': '500Wt00000DE0IPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'id': 'a04Wt00000538PZIAY', 'caseid__c': '500Wt00000DDzcTIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'id': '#a04Wt00000538SnIAI', 'caseid__c': '500Wt00000DDzSoIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'id': 'a04Wt00000538ZGIAY', 'caseid__c': '500Wt00000DDfx8IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': 'a04Wt00000538arIAA', 'caseid__c': '500Wt00000DDQRsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'id': 'a04Wt00000538fhIAA', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'id': 'a04Wt00000538xRIAQ', 'caseid__c': '500Wt00000DDzB4IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': 'a04Wt00000538xSIAQ', 'caseid__c': '500Wt00000DDZtKIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': 'a04Wt000005392HIAQ', 'caseid__c': '500Wt00000DDy8aIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'id': 'a04Wt000005395VIAQ', 'caseid__c': '500Wt00000DDxkMIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': 'a04Wt000005398jIAA', 'caseid__c': '500Wt00000DDg20IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': 'a04Wt00000539aBIAQ', 'caseid__c': '500Wt00000DDsKuIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'id': 'a04Wt00000539aCIAQ', 'caseid__c': '500Wt00000DDyRvIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': 'a04Wt00000539ezIAA', 'caseid__c': '500Wt00000DE0K1IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '#a04Wt00000539iDIAQ', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'id': 'a04Wt00000539zyIAA', 'caseid__c': '500Wt00000DE0FDIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'id': '#a04Wt0000053A6PIAU', 'caseid__c': '500Wt00000DE0VJIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'id': '#a04Wt0000053A81IAE', 'caseid__c': '500Wt00000DDzJ8IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}]}

exec(code, env_args)
