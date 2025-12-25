code = """import json
from datetime import datetime

# Load the case history
file_path = locals()['var_function-call-12358601199876924892']
with open(file_path, 'r') as f:
    history = json.load(f)

# Define date range: 2022-04-01 to 2023-03-31
start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31)

def parse_date(date_str):
    try:
        dt = datetime.strptime(date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        return dt
    except:
        return None

handled_counts = {}
transfer_counts = {}
handled_agents = set()

for row in history:
    d = parse_date(row['createddate'])
    if d and start_date <= d <= end_date:
        # Check Assigned (Handled)
        new_owner = row.get('newvalue__c')
        if new_owner and new_owner != 'None':
            new_owner = new_owner.strip()
            # Only count users
            if new_owner.startswith('005'):
                handled_agents.add(new_owner)
                handled_counts[new_owner] = handled_counts.get(new_owner, 0) + 1
        
        # Check Transferred (From)
        old_owner = row.get('oldvalue__c')
        if old_owner and old_owner != 'None':
            old_owner = old_owner.strip()
            if old_owner.startswith('005'):
                transfer_counts[old_owner] = transfer_counts.get(old_owner, 0) + 1

# Filter: Handled > 0
valid_agents = list(handled_agents)

# Find min transfer count among valid agents
if not valid_agents:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    agent_stats = []
    for agent in valid_agents:
        t_count = transfer_counts.get(agent, 0)
        h_count = handled_counts.get(agent, 0)
        agent_stats.append({'id': agent, 'transfers': t_count, 'handled': h_count})
    
    min_transfers = min(a['transfers'] for a in agent_stats)
    best_agents = [a for a in agent_stats if a['transfers'] == min_transfers]
    
    # Sort by handled count desc as a potential tie breaker or for inspection
    best_agents.sort(key=lambda x: x['handled'], reverse=True)
    
    print("__RESULT__:")
    print(json.dumps(best_agents))"""

env_args = {'var_function-call-2420836909563224927': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5384257016623672216': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-12044959519315846892': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-12358601199876924892': 'file_storage/function-call-12358601199876924892.json', 'var_function-call-10586730684050158883': {'min_transfers': 0, 'candidates': ['005Wt000003NIc2IAG', '005Wt000003NINVIA4', '005Wt000003NI2XIAW', '005Wt000003NDJ1IAO', '005Wt000003NBykIAG', '005Wt000003NIvNIAW', '005Wt000003NJoDIAW', '005Wt000003NISLIA4', '005Wt000003NFr4IAG', '005Wt000003NHsrIAG', '005Wt000003NIVZIA4', '005Wt000003NJD9IAO', '005Wt000003NGjuIAG', '005Wt000003NIaQIAW', '005Wt000003NJ8HIAW', '005Wt000003NBcAIAW', '005Wt000003NEzqIAG', '005Wt000003NJrRIAW', '005Wt000003NHpeIAG', '005Wt000003NJ0DIAW', '005Wt000003NJcvIAG', '005Wt000003NDsUIAW', '005Wt000003NIwzIAG', '005Wt000003NFKoIAO', '005Wt000003NEGhIAO', '005Wt000003NDqFIAW', '005Wt000003NJEjIAO', '005Wt000003NJhlIAG', '005Wt000003NJTFIA4', '005Wt000003NInLIAW', '005Wt000003NJ6gIAG'], 'count_candidates': 31}}

exec(code, env_args)
