code = """import json
from datetime import datetime

# Load data
cases_data = locals()['var_function-call-14138959272631473858']
history_path = locals()['var_function-call-532126828366941617']
with open(history_path, 'r') as f:
    history_data = json.load(f)

# Helper to clean ID
def clean_id(i):
    if i and i.startswith('#'):
        return i[1:]
    return i

# Process Cases
# Map case_id (clean) -> info
cases_info = {}
start_date = datetime(2023, 5, 2)
end_date = datetime(2023, 9, 2, 23, 59, 59)

for c in cases_data:
    cid = clean_id(c['id'])
    oid = clean_id(c['ownerid'])
    
    # Parse dates
    created_str = c['createddate'] 
    closed_str = c['closeddate']
    
    # Format: 2023-07-01T10:30:00.000+0000 -> 2023-07-01T10:30:00
    created_dt = datetime.strptime(created_str[:19], "%Y-%m-%dT%H:%M:%S")
    
    closed_dt = None
    if closed_str and closed_str != "None":
        closed_dt = datetime.strptime(closed_str[:19], "%Y-%m-%dT%H:%M:%S")
    
    cases_info[cid] = {
        'owner': oid,
        'created': created_dt,
        'closed': closed_dt,
        'history_owners': set(),
        'history_count': 0
    }

# Process History
for h in history_data:
    cid = clean_id(h['caseid__c'])
    new_agent = clean_id(h['newvalue__c'])
    
    if cid in cases_info:
        cases_info[cid]['history_owners'].add(new_agent)
        cases_info[cid]['history_count'] += 1

# Calculate Managed Count per Agent
agent_managed = {} # AgentID -> Set(CaseID)

for cid, info in cases_info.items():
    # Owner from Case table
    agent = info['owner']
    if agent not in agent_managed: agent_managed[agent] = set()
    agent_managed[agent].add(cid)
    
    # Owners from History
    for h_agent in info['history_owners']:
        if h_agent not in agent_managed: agent_managed[h_agent] = set()
        agent_managed[h_agent].add(cid)

# Calculate Handle Time per Agent
agent_handle_times = {} # AgentID -> List(seconds)

for cid, info in cases_info.items():
    # Only consider cases CLOSED in the past 4 months
    if info['closed'] and start_date <= info['closed'] <= end_date:
        
        # Check transfer status: 
        # "For cases that have NOT been transferred ..., there will be only ONE 'Owner Assignment'"
        if info['history_count'] != 1:
            continue # Transferred or invalid history
            
        duration = (info['closed'] - info['created']).total_seconds()
        
        # Assign to the single owner (info['owner'])
        owner = info['owner']
        if owner not in agent_handle_times: agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Filter and Find Min
min_avg = float('inf')
best_agent = None

for agent, cases_set in agent_managed.items():
    if len(cases_set) > 1:
        # Qualifies filter
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            if avg_time < min_avg:
                min_avg = avg_time
                best_agent = agent

print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_function-call-10608182050768682697': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9535056746092939698': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-11946221018510917316': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1341771895883435587': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-8461189765829300694': [{'caseid__c': '500Wt00000DDepmIAD', 'newvalue__c': '005Wt000003NJufIAG', 'oldvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'newvalue__c': '005Wt000003NDqDIAW', 'oldvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'newvalue__c': '005Wt000003NJJaIAO', 'oldvalue__c': 'None'}, {'caseid__c': '500Wt00000DDyzpIAD', 'newvalue__c': '005Wt000003NJGLIA4', 'oldvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzsbIAD', 'newvalue__c': '005Wt000003NJD9IAO', 'oldvalue__c': 'None'}], 'var_function-call-16786810427201852755': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000533XzIAI', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-03T00:11:47.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000537msIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537zmIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'Case Closed'}, {'id': '#a04Wt00000538O0IAI', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14138959272631473858': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW', 'createddate': '2021-01-10T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2021-06-03T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG', 'createddate': '2022-03-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW', 'createddate': '2021-10-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2022-03-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T11:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG', 'createddate': '2021-11-11T12:13:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO', 'createddate': '2020-07-01T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T18:04:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2020-11-05T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO', 'createddate': '2021-08-24T13:25:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG', 'createddate': '2021-11-01T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2021-02-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-05-24T04:08:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW', 'createddate': '2021-06-02T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW', 'createddate': '2022-03-04T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW', 'createddate': '2021-11-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2021-10-22T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO', 'createddate': '2022-01-28T02:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-09-10T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-01-10T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW', 'createddate': '2021-11-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2021-01-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW', 'createddate': '2021-07-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2021-11-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2021-09-17T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2021-07-07T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4', 'createddate': '2021-06-16T08:30:00.000+0000', 'closeddate': 'None'}], 'var_function-call-5540403844820444898': [{'count': '165'}], 'var_function-call-532126828366941617': 'file_storage/function-call-532126828366941617.json'}

exec(code, env_args)
