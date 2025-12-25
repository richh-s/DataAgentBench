code = """history = locals()['var_function-call-313924085140625575']
import json

# Clean IDs function
def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

# Stats container
stats = {} # AgentId -> {'handled': 0, 'transfers': 0}

for rec in history:
    old_val = clean_id(rec['oldvalue__c'])
    new_val = clean_id(rec['newvalue__c'])
    
    # Handle New Value (Incoming Assignment -> Handled)
    if new_val:
        if new_val not in stats:
            stats[new_val] = {'handled': 0, 'transfers': 0}
        stats[new_val]['handled'] += 1
        
    # Handle Old Value (Outgoing Transfer -> Transfer Count)
    if old_val and old_val != 'None':
        if old_val not in stats:
            stats[old_val] = {'handled': 0, 'transfers': 0}
        stats[old_val]['transfers'] += 1
        # Note: If old_val was not in stats, it means they were assigned before the window?
        # But we need to make sure they are counted as "handled > 0"
        # If they transferred out, they must have handled it.
        # So we should increment handled? 
        # But "Handled" definition usually refers to Assignment count.
        # If I transfer out, I don't get a new assignment.
        # But I must have had one before.
        # If the assignment was before the window, do I count as "handled > 0" IN THE WINDOW?
        # If "Handled > 0" is a filter for active agents, then someone transferring a case IS active.
        # So I will ensure handled > 0 if transfer > 0.
        if stats[old_val]['handled'] == 0:
             stats[old_val]['handled'] = 1 # Assume at least 1 handled to allow transfer

# Filter Handled > 0
candidates = []
for agent, data in stats.items():
    if data['handled'] > 0:
        candidates.append({'id': agent, 'transfers': data['transfers'], 'handled': data['handled']})

# Sort by Transfer ASC, then Handled DESC
candidates.sort(key=lambda x: (x['transfers'], -x['handled']))

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-3635588617336801309': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12642860199555503233': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-3103648946183642204': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11174023430256808300': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-2975253429011362283': [{'count': '39'}], 'var_function-call-16050486677366106742': [{'count': '165'}], 'var_function-call-313924085140625575': [{'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}], 'var_function-call-14344896460135805658': [{'count': '12'}]}

exec(code, env_args)
