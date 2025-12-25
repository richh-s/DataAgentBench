code = """import json
from datetime import datetime

# Load data
with open(locals()['var_function-call-8126399227036074897'], 'r') as f:
    data = json.load(f)

start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31)

def clean_id(val):
    if not val or val == 'None':
        return None
    val = str(val).strip()
    if val.startswith('#'):
        return val[1:]
    return val

handled_agents = set()
transfer_counts = {}
debug_non_ids = set()

filtered_cnt = 0
for r in data:
    if r.get('field__c') != 'Owner Assignment':
        continue
    
    c_date_str = r.get('createddate')
    try:
        dt = datetime.strptime(c_date_str[:10], "%Y-%m-%d")
        if not (start_date <= dt <= end_date):
            continue
    except:
        continue

    filtered_cnt += 1
    
    ov = clean_id(r.get('oldvalue__c'))
    nv = clean_id(r.get('newvalue__c'))

    if ov:
        handled_agents.add(ov)
        if not ov.startswith('005'):
            debug_non_ids.add(ov)
    if nv:
        handled_agents.add(nv)
        if not nv.startswith('005'):
            debug_non_ids.add(nv)
            
    # Count transfers
    if ov:
        transfer_counts[ov] = transfer_counts.get(ov, 0) + 1

# Ensure all handled agents are in transfer_counts
for a in handled_agents:
    if a not in transfer_counts:
        transfer_counts[a] = 0

sorted_agents = sorted(transfer_counts.items(), key=lambda x: (x[1], x[0]))

print("__RESULT__:")
print(json.dumps({
    "total_handled_agents": len(handled_agents),
    "agents_with_0_transfers": len([x for x in transfer_counts.values() if x == 0]),
    "non_005_ids": list(debug_non_ids),
    "top_5_agents": sorted_agents[:5]
}))"""

env_args = {'var_function-call-3552046821111797620': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-16132431978656463409': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-2215454728334574223': [{'count': '393'}], 'var_function-call-8126399227036074897': 'file_storage/function-call-8126399227036074897.json', 'var_function-call-12894595186619539585': [['005Wt000003NBcAIAW', 0], ['005Wt000003NBykIAG', 0], ['005Wt000003NDJ1IAO', 0], ['005Wt000003NDqFIAW', 0], ['005Wt000003NDsUIAW', 0], ['005Wt000003NEGhIAO', 0], ['005Wt000003NEzqIAG', 0], ['005Wt000003NFKoIAO', 0], ['005Wt000003NFr4IAG', 0], ['005Wt000003NGjuIAG', 0], ['005Wt000003NHpeIAG', 0], ['005Wt000003NHsrIAG', 0], ['005Wt000003NI2XIAW', 0], ['005Wt000003NINVIA4', 0], ['005Wt000003NISLIA4', 0], ['005Wt000003NIVZIA4', 0], ['005Wt000003NIaQIAW', 0], ['005Wt000003NIc2IAG', 0], ['005Wt000003NInLIAW', 0], ['005Wt000003NIvNIAW', 0], ['005Wt000003NIwzIAG', 0], ['005Wt000003NJ0DIAW', 0], ['005Wt000003NJ6gIAG', 0], ['005Wt000003NJ8HIAW', 0], ['005Wt000003NJD9IAO', 0], ['005Wt000003NJEjIAO', 0], ['005Wt000003NJTFIA4', 0], ['005Wt000003NJcvIAG', 0], ['005Wt000003NJhlIAG', 0], ['005Wt000003NJoDIAW', 0], ['005Wt000003NJrRIAW', 0], ['005Wt000003NIliIAG', 1]]}

exec(code, env_args)
