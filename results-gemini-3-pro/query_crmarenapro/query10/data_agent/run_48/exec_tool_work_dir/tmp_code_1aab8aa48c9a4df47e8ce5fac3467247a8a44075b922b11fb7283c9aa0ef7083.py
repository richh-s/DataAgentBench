code = """import json
from datetime import datetime, timezone

# Load data
cases = json.load(open('var_function-call-17402588654256926358'))
history = json.load(open('var_function-call-4653464397948645656'))

# Helpers
def parse_date(d_str):
    if not d_str or d_str == 'None': return None
    try:
        return datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        try:
            return datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z")
        except:
            return None

def clean_id(i):
    if i and i.startswith('#'): return i[1:]
    return i

# Stats container
agent_stats = {} 
# structure: {agent_id: {'processed_cases': set(), 'handle_times': []}}
# Using set for processed_cases to ensure unique count per agent

start_date = datetime(2023, 5, 2, tzinfo=timezone.utc)
end_date = datetime(2023, 9, 2, 23, 59, 59, tzinfo=timezone.utc)

# Precompute history info
history_map = {} # case_id -> set of owners
history_counts = {} # case_id -> count of rows
for h in history:
    cid = clean_id(h['caseid__c'])
    
    # Count rows
    history_counts[cid] = history_counts.get(cid, 0) + 1
    
    # Map owners
    if cid not in history_map: history_map[cid] = set()
    nval = clean_id(h['newvalue__c'])
    if nval: history_map[cid].add(nval)
    # also oldvalue if needed? usually oldvalue is None or prev owner.
    oval = clean_id(h['oldvalue__c'])
    if oval and oval != 'None': history_map[cid].add(oval)

# Process cases
for c in cases:
    cid = clean_id(c['id'])
    
    created = parse_date(c['createddate'])
    closed = parse_date(c['closeddate'])
    
    curr_owner = clean_id(c['ownerid'])
    
    # Identify all owners (Agents processing this case)
    owners = set()
    owners.add(curr_owner)
    if cid in history_map:
        owners.update(history_map[cid])
        
    # Check if active in window
    is_active = False
    if created and created <= end_date:
        if closed is None or closed >= start_date:
            is_active = True
            
    # Update Processing Counts
    if is_active:
        for agent in owners:
            if agent not in agent_stats: agent_stats[agent] = {'processed_cases': set(), 'handle_times': []}
            agent_stats[agent]['processed_cases'].add(cid)
            
    # Check Handle Time Eligibility
    # Closed in Window AND Not Transferred
    if closed and closed >= start_date and closed <= end_date:
        # Transfer check
        # If count > 1, it's transferred.
        # If count == 0? If no history, assume single owner (the current one).
        is_transferred = False
        h_count = history_counts.get(cid, 0)
        if h_count > 1:
            is_transferred = True
            
        if not is_transferred:
            duration = (closed - created).total_seconds()
            if curr_owner not in agent_stats: 
                agent_stats[curr_owner] = {'processed_cases': set(), 'handle_times': []}
                # If it wasn't active (impossible if closed in window), we add it now.
                # But it must be active if closed in window.
            agent_stats[curr_owner]['handle_times'].append(duration)

# Calculate averages and find min
eligible_agents = []
for agent, stats in agent_stats.items():
    p_count = len(stats['processed_cases'])
    if p_count > 1 and len(stats['handle_times']) > 0:
        avg_ht = sum(stats['handle_times']) / len(stats['handle_times'])
        eligible_agents.append({'id': agent, 'avg_ht': avg_ht, 'count': p_count})

eligible_agents.sort(key=lambda x: x['avg_ht'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-16291421377177832744': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5542780849517608270': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-18306744028826655999': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-90174517768170883': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15475035359981937942': [{'count': '7'}], 'var_function-call-2266246057672968968': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-11254939790593365322': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG'}], 'var_function-call-2664414492636598296': [{'count': '153'}], 'var_function-call-17402588654256926358': 'file_storage/function-call-17402588654256926358.json', 'var_function-call-4653464397948645656': 'file_storage/function-call-4653464397948645656.json'}

exec(code, env_args)
