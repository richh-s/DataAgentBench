code = """import json
import pandas as pd

with open(locals()['var_function-call-8139464499209271755'], 'r') as f:
    history = json.load(f)

def clean_id(val):
    if val and isinstance(val, str):
        val = val.strip()
        if val.startswith('#'):
            return val[1:]
        return val
    return val

assignments = [r for r in history if r.get('field__c') == 'Owner Assignment']

# Calendar Quarters: Q2 2022 to Q1 2023
start_date = pd.Timestamp('2022-04-01', tz='UTC')
end_date = pd.Timestamp('2023-03-31 23:59:59', tz='UTC')

handled_counts = {}
transfer_counts = {}

for r in assignments:
    try:
        dt = pd.to_datetime(r['createddate'])
    except:
        continue
    
    in_window = (dt >= start_date) and (dt <= end_date)
    
    new_agent = clean_id(r.get('newvalue__c'))
    old_agent = clean_id(r.get('oldvalue__c'))
    
    if new_agent == 'None': new_agent = None
    if old_agent == 'None': old_agent = None
    
    if new_agent and in_window:
        handled_counts[new_agent] = handled_counts.get(new_agent, 0) + 1
        
    if old_agent and in_window:
        transfer_counts[old_agent] = transfer_counts.get(old_agent, 0) + 1

candidates = []
for agent, h_count in handled_counts.items():
    if h_count > 0:
        t_count = transfer_counts.get(agent, 0)
        candidates.append({'agent': agent, 'transfers': t_count, 'handled': h_count})

candidates.sort(key=lambda x: (x['transfers'], -x['handled']))

print('__RESULT__:')
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-12268255451877300690': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15607863566886824677': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3973721063512414452': [{'count': '39'}], 'var_function-call-15089162678779735596': [{'count': '393'}], 'var_function-call-8139464499209271755': 'file_storage/function-call-8139464499209271755.json', 'var_function-call-6344237457182612528': [{'agent': '005Wt000003NDqFIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEzqIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEGhIAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJ6gIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIVZIA4', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NBcAIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NHsrIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NFr4IAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NINVIA4', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NJhlIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NHpeIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NI2XIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJTFIA4', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJoDIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIc2IAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NBykIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJD9IAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJrRIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NDsUIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIwzIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJ8HIAW', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NFKoIAO', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NIaQIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NDJ1IAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIvNIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NISLIA4', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJEjIAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NGjuIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJ0DIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NInLIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIliIAG', 'transfers': 1, 'handled': 2}], 'var_function-call-12640321273298988117': 'file_storage/function-call-12640321273298988117.json', 'var_function-call-3102371209540513812': [{'agent': '005Wt000003NJ8HIAW', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NFKoIAO', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NHsrIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NINVIA4', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NJhlIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NDqFIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEzqIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEGhIAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJ6gIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIVZIA4', 'transfers': 0, 'handled': 1}], 'var_function-call-3961299641171375166': [{'agent': '005Wt000003NJ8HIAW', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NFKoIAO', 'transfers': 0, 'handled': 3}, {'agent': '005Wt000003NHsrIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NINVIA4', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NJhlIAG', 'transfers': 0, 'handled': 2}, {'agent': '005Wt000003NDqFIAW', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEzqIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NEGhIAO', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NJ6gIAG', 'transfers': 0, 'handled': 1}, {'agent': '005Wt000003NIVZIA4', 'transfers': 0, 'handled': 1}], 'var_function-call-9440393474866294018': [{'Id': '005Wt000003NFKoIAO', 'FirstName': 'Akari', 'LastName': 'Fujiwara', 'Alias': 'fujiwara'}, {'Id': '005Wt000003NJ8HIAW', 'FirstName': 'Sun', 'LastName': 'Park', 'Alias': 'sun.park'}]}

exec(code, env_args)
