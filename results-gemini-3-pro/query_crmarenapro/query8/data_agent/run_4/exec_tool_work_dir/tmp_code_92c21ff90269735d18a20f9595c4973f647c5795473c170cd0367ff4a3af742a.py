code = """import json
from datetime import datetime

with open(locals()['var_function-call-12020941486477026334'], 'r') as f:
    history = json.load(f)

start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10)

transfer_counts = {}
handled_counts = {}
population = set()

for entry in history:
    dt_str = entry['createddate']
    clean_dt_str = dt_str.split('+')[0].split('.')[0]
    dt = datetime.strptime(clean_dt_str, "%Y-%m-%dT%H:%M:%S")
    
    nv = entry.get('newvalue__c')
    ov = entry.get('oldvalue__c')
    
    # Check window
    in_window = start_date <= dt <= end_date
    
    # To be in population "handled > 0 cases", they must have handled a case.
    # The question implies general handling or window handling?
    # Let's count handled events in the window to distinguish active agents.
    if in_window:
        if nv and nv != 'None':
            handled_counts[nv] = handled_counts.get(nv, 0) + 1
            population.add(nv)
        if ov and ov != 'None':
            handled_counts[ov] = handled_counts.get(ov, 0) + 1
            population.add(ov)
            # Transfer count
            transfer_counts[ov] = transfer_counts.get(ov, 0) + 1

# Min transfer count
results = []
for agent_id in population:
    t_count = transfer_counts.get(agent_id, 0)
    h_count = handled_counts.get(agent_id, 0)
    results.append({'id': agent_id, 't_count': t_count, 'h_count': h_count})

if results:
    min_t = min(r['t_count'] for r in results)
    candidates = [r for r in results if r['t_count'] == min_t]
    # Sort by handled count descending
    candidates.sort(key=lambda x: x['h_count'], reverse=True)
    out = {'min_transfer': min_t, 'top_candidates': candidates[:5]}
else:
    out = {'result': 'No agents found'}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_function-call-10037541303498214618': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10863993742589604424': [{'field__c': 'Case Creation', 'cnt': '153'}, {'field__c': 'Case Closed', 'cnt': '75'}, {'field__c': 'Owner Assignment', 'cnt': '165'}], 'var_function-call-14618880228806568354': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12020941486477026334': 'file_storage/function-call-12020941486477026334.json', 'var_function-call-9454345416466752804': {'min_val': 0, 'min_agents': ['005Wt000003NJrRIAW', '005Wt000003NIc2IAG', '005Wt000003NJzVIAW', '005Wt000003NHfzIAG', '005Wt000003NJTFIA4', '005Wt000003NInLIAW', '005Wt000003NHg0IAG', '005Wt000003NJcvIAG', '005Wt000003NI90IAG', '005Wt000003NFKpIAO', '005Wt000003NJQ1IAO', '005Wt000003NJcwIAG', '005Wt000003NBcAIAW', '005Wt000003NEdKIAW', '005Wt000003NFhOIAW', '005Wt000003NIddIAG', '005Wt000003NJ8HIAW', '005Wt000003NEzqIAG', '005Wt000003NHpeIAG', '005Wt000003NBykIAG', '005Wt000003NJhlIAG', '005Wt000003NDqFIAW', '005Wt000003NISLIA4', '005Wt000003NDXZIA4', '005Wt000003NHuUIAW', '005Wt000003NFW6IAO', '005Wt000003NJEjIAO', '005Wt000003NIAcIAO', '005Wt000003NJ6gIAG', '005Wt000003NDqEIAW', '005Wt000003NHsrIAG', '005Wt000003NFr4IAG', '005Wt000003NIaQIAW', '005Wt000003NEGhIAO', '005Wt000003NIk7IAG', '005Wt000003NJ9tIAG', '005Wt000003NJeXIAW', '005Wt000003NJJaIAO', '005Wt000003NI2XIAW', '005Wt000003NIc3IAG', '005Wt000003NJppIAG', '005Wt000003NItlIAG', '005Wt000003NIVZIA4', '005Wt000003NIwzIAG', '005Wt000003NDu7IAG', '005Wt000003NINVIA4', '005Wt000003NIfFIAW', '005Wt000003NGwpIAG', '005Wt000003NJWTIA4', '005Wt000003NIk5IAG', '005Wt000003NJLBIA4', '005Wt000003NDqDIAW', '005Wt000003NHGAIA4', '005Wt000003NJ0DIAW', '005Wt000003NH3GIAW', '005Wt000003NEtOIAW', '005Wt000003NJ6fIAG', '005Wt000003NIfHIAW', '005Wt000003NHfyIAG', '005Wt000003NJufIAG', '005Wt000003NJoDIAW', '005Wt000003NInJIAW', '005Wt000003NIDqIAO', '005Wt000003NIvNIAW', '005Wt000003NIYnIAO', '005Wt000003NJD9IAO', '005Wt000003NI5mIAG', '005Wt000003NJGLIA4', '005Wt000003NDJ1IAO', '005Wt000003NFKoIAO', '005Wt000003NDsUIAW', '005Wt000003NJUrIAO', '005Wt000003NGjuIAG', '005Wt000003NJ3RIAW', '005Wt000003NF1SIAW', '005Wt000003NJbJIAW', '005Wt000003NIXBIA4'], 'total_pop': 78}, 'var_function-call-13653562278988197262': {'min_val': 0, 'min_agents': ['005Wt000003NJoDIAW', '005Wt000003NGjuIAG', '005Wt000003NHsrIAG', '005Wt000003NJEjIAO', '005Wt000003NInLIAW', '005Wt000003NINVIA4', '005Wt000003NDsUIAW', '005Wt000003NIvNIAW', '005Wt000003NHpeIAG', '005Wt000003NJ6gIAG', '005Wt000003NJD9IAO', '005Wt000003NJhlIAG', '005Wt000003NIwzIAG', '005Wt000003NJrRIAW', '005Wt000003NISLIA4', '005Wt000003NFr4IAG', '005Wt000003NJ0DIAW', '005Wt000003NDqFIAW', '005Wt000003NIVZIA4', '005Wt000003NBykIAG', '005Wt000003NEGhIAO', '005Wt000003NIc2IAG', '005Wt000003NFKoIAO', '005Wt000003NJTFIA4', '005Wt000003NBcAIAW', '005Wt000003NDJ1IAO', '005Wt000003NEzqIAG', '005Wt000003NI2XIAW', '005Wt000003NJ8HIAW', '005Wt000003NIaQIAW'], 'pop_size': 31}}

exec(code, env_args)
