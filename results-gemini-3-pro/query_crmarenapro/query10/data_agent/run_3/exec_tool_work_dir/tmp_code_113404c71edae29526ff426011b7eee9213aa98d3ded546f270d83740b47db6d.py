code = """import json
import pandas as pd

# Load cases
cases = locals()['var_function-call-6829958192257380587']

# Load history
with open(locals()['var_function-call-5472046148514724816']) as f:
    history = json.load(f)

def clean_id(i):
    if not i: return i
    i = str(i).strip()
    if i.startswith('#'): i = i[1:]
    return i

# Map history
history_map = {}
for h in history:
    if h.get('field__c') != 'Owner Assignment': continue
    cid = clean_id(h['caseid__c'])
    agent = clean_id(h['newvalue__c'])
    if cid not in history_map: history_map[cid] = []
    history_map[cid].append(agent)

agent_processed_count = {}
agent_handle_times = {}

for c in cases:
    cid = clean_id(c['id'])
    owners = history_map.get(cid, [])
    
    # If no history, assume current owner is the only one
    if not owners:
        owners = [clean_id(c['ownerid'])]
        
    # Update processed counts
    # Use set to count unique cases per agent? 
    # "processing more than one case" - usually counts distinct cases.
    unique_owners = set(owners)
    for agent in unique_owners:
        agent_processed_count[agent] = agent_processed_count.get(agent, 0) + 1
        
    # Check transfer status
    # "For cases that have NOT been transferred ... there will be only ONE Owner Assignment"
    # So if len(owners) == 1 -> Not transferred.
    if len(owners) == 1:
        agent = owners[0]
        created = pd.to_datetime(c['createddate'])
        closed = pd.to_datetime(c['closeddate'])
        duration = (closed - created).total_seconds()
        
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(duration)

# Find agent
min_avg = float('inf')
best_agent = None

candidates = []

for agent, count in agent_processed_count.items():
    if count > 1:
        if agent in agent_handle_times and agent_handle_times[agent]:
            avg = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            candidates.append({'agent': agent, 'avg': avg, 'count': count})
            if avg < min_avg:
                min_avg = avg
                best_agent = agent

print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_function-call-5625231465480023439': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6829958192257380587': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6186000776147679419': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4820904134128037488': [{'count': '7'}], 'var_function-call-6089381638363886069': [{'count': '165'}], 'var_function-call-5472046148514724816': 'file_storage/function-call-5472046148514724816.json'}

exec(code, env_args)
