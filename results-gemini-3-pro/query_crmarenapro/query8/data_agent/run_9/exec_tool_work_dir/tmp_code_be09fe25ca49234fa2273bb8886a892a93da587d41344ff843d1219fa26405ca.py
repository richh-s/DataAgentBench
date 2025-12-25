code = """import json
from datetime import datetime

# Load data
with open(locals()['var_function-call-726124146613183122'], 'r') as f:
    history = json.load(f)

end_date = datetime(2023, 4, 10)
start_date = datetime(2022, 4, 10)

agent_handled_cases = {}
agent_transferred_count = {}

for record in history:
    cdate_str = record['createddate']
    try:
        dt = datetime.strptime(cdate_str[:19], "%Y-%m-%dT%H:%M:%S")
    except:
        continue

    if start_date <= dt <= end_date:
        old_val = record['oldvalue__c']
        new_val = record['newvalue__c']
        case_id = record.get('caseid__c')
        
        if old_val:
            old_val = old_val.strip().lstrip('#')
        if new_val:
            new_val = new_val.strip().lstrip('#')
            
        # Count Handled (Set of Case IDs)
        # Agent in newvalue__c handled this case.
        if new_val and new_val != 'None':
            if new_val not in agent_handled_cases:
                agent_handled_cases[new_val] = set()
            agent_handled_cases[new_val].add(case_id)
            
        # Count Transferred (Counter)
        # Agent in oldvalue__c transferred this case OUT.
        if old_val and old_val != 'None':
            agent_transferred_count[old_val] = agent_transferred_count.get(old_val, 0) + 1

# Filter
eligible = []
for agent, cases in agent_handled_cases.items():
    if len(cases) > 0:
        t_count = agent_transferred_count.get(agent, 0)
        eligible.append({'id': agent, 'handled_count': len(cases), 'transferred': t_count})

# Sort
# Primary: Fewest transfers
# Secondary: Most handled cases (tie-breaker)
eligible.sort(key=lambda x: (x['transferred'], -x['handled_count']))

print("__RESULT__:")
print(json.dumps(eligible))"""

env_args = {'var_function-call-14614809315977098220': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1916479405294806639': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4651257634675235691': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005389SIAQ', 'caseid__c': '500Wt00000DDfvXIAT', 'oldvalue__c': '005Wt000003NHg0IAG', 'newvalue__c': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T20:27:15.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538NzIAI', 'caseid__c': '500Wt00000DDz6FIAT', 'oldvalue__c': '005Wt000003NDqFIAW', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T13:07:23.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538m9IAA', 'caseid__c': '500Wt00000DDYpGIAX', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T13:52:45.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000539blIAA', 'caseid__c': '500Wt00000DDTERIA5', 'oldvalue__c': '005Wt000003NJ6fIAG', 'newvalue__c': '005Wt000003NIk5IAG', 'createddate': '2022-03-10T11:37:09.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-8419406847472328550': [{'count': '165'}], 'var_function-call-9224824487569700459': 'file_storage/function-call-9224824487569700459.json', 'var_function-call-17717598133814413129': [{'id': '005Wt000003NDqFIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NEzqIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NEGhIAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJ6gIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIVZIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NBcAIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NHsrIAG', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NFr4IAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NINVIA4', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NJhlIAG', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NHpeIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NI2XIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJTFIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJoDIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIc2IAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NBykIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJD9IAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJrRIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NDsUIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIwzIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJ8HIAW', 'handled': 3, 'transferred': 0}, {'id': '005Wt000003NFKoIAO', 'handled': 3, 'transferred': 0}, {'id': '005Wt000003NIaQIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NDJ1IAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIvNIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NISLIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJEjIAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NGjuIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJ0DIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NInLIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIliIAG', 'handled': 2, 'transferred': 1}], 'var_function-call-11673333647238537141': [{'id': '005Wt000003NJ8HIAW', 'handled': 3, 'transferred': 0}, {'id': '005Wt000003NFKoIAO', 'handled': 3, 'transferred': 0}, {'id': '005Wt000003NHsrIAG', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NINVIA4', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NJhlIAG', 'handled': 2, 'transferred': 0}, {'id': '005Wt000003NDqFIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NEzqIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NEGhIAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJ6gIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIVZIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NBcAIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NFr4IAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NHpeIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NI2XIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJTFIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJoDIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIc2IAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NBykIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJD9IAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJrRIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NDsUIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIwzIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIaQIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NDJ1IAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NIvNIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NISLIA4', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJEjIAO', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NGjuIAG', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NJ0DIAW', 'handled': 1, 'transferred': 0}, {'id': '005Wt000003NInLIAW', 'handled': 1, 'transferred': 0}], 'var_function-call-726124146613183122': 'file_storage/function-call-726124146613183122.json'}

exec(code, env_args)
