code = """import json
from datetime import datetime

with open(locals()['var_function-call-12020941486477026334'], 'r') as f:
    history = json.load(f)

start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10)

transfer_counts = {}
population = set()

for entry in history:
    # Date parsing
    dt_str = entry['createddate']
    # "2023-09-07T16:30:00.000+0000"
    # Take part before +, then part before . (if exists) or just first 19 chars
    clean_dt_str = dt_str.split('+')[0].split('.')[0]
    dt = datetime.strptime(clean_dt_str, "%Y-%m-%dT%H:%M:%S")
    
    # Population
    nv = entry.get('newvalue__c')
    ov = entry.get('oldvalue__c')
    
    if nv and nv != 'None':
        population.add(nv)
    if ov and ov != 'None':
        population.add(ov)
        
    # Check window
    if start_date <= dt <= end_date:
        if ov and ov != 'None':
            transfer_counts[ov] = transfer_counts.get(ov, 0) + 1

results = []
for agent_id in population:
    count = transfer_counts.get(agent_id, 0)
    results.append({'id': agent_id, 'count': count})

if not results:
    out = {'min_val': 0, 'min_agents': [], 'total_pop': 0}
else:
    min_val = min(r['count'] for r in results)
    min_agents = [r['id'] for r in results if r['count'] == min_val]
    out = {'min_val': min_val, 'min_agents': min_agents, 'total_pop': len(population)}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_function-call-10037541303498214618': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10863993742589604424': [{'field__c': 'Case Creation', 'cnt': '153'}, {'field__c': 'Case Closed', 'cnt': '75'}, {'field__c': 'Owner Assignment', 'cnt': '165'}], 'var_function-call-14618880228806568354': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12020941486477026334': 'file_storage/function-call-12020941486477026334.json'}

exec(code, env_args)
