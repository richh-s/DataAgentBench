code = """import json
from datetime import datetime

with open(locals()['var_function-call-12036530776075449149'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-14588621972763640650'], 'r') as f:
    history = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        return i.strip().lstrip('#')
    return i

def parse_date(d):
    if not d or d == 'None': return None
    try:
        return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        try:
             return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z")
        except:
             return None

end_date = datetime.strptime("2023-09-02T23:59:59+0000", "%Y-%m-%dT%H:%M:%S%z")
start_date = datetime.strptime("2023-05-02T00:00:00+0000", "%Y-%m-%dT%H:%M:%S%z")

case_assignments = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    owner = clean_id(h['newvalue__c'])
    if not cid or not owner: continue
    if cid not in case_assignments:
        case_assignments[cid] = []
    case_assignments[cid].append(owner)

agent_processed_count = {}
agent_handle_times = {}

active_count_debug = 0
closed_in_period_debug = 0

for c in cases:
    cid = clean_id(c['id'])
    closed = parse_date(c['closeddate'])
    created = parse_date(c['createddate'])
    
    # Active Check
    # Created <= End
    # Closed >= Start or None
    is_active = False
    if created and created <= end_date:
        if not closed or closed >= start_date:
            is_active = True
            
    is_closed_in_period = False
    if closed and start_date <= closed <= end_date:
        is_closed_in_period = True
        
    if is_active: active_count_debug += 1
    if is_closed_in_period: closed_in_period_debug += 1
    
    # Get Processors
    assignments = case_assignments.get(cid, [])
    current_owner = clean_id(c['ownerid'])
    processors = set(assignments)
    if not assignments: processors.add(current_owner)
    
    # Update Counts (Active)
    if is_active:
        for p in processors:
            agent_processed_count[p] = agent_processed_count.get(p, 0) + 1
            
    # Update Handle Times (Closed in Period, Not Transferred)
    is_transferred = len(assignments) > 1
    if is_closed_in_period and not is_transferred:
        if not created: continue
        ht = (closed - created).total_seconds()
        owner = assignments[0] if assignments else current_owner
        
        if owner not in agent_handle_times: agent_handle_times[owner] = []
        agent_handle_times[owner].append(ht)

# Find Best Agent
best_agent = None
min_avg = float('inf')

candidates = []

for agent, count in agent_processed_count.items():
    if count > 1:
        if agent in agent_handle_times and agent_handle_times[agent]:
            avg = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            candidates.append((agent, avg, count))
            if avg < min_avg:
                min_avg = avg
                best_agent = agent

print("__RESULT__:")
print(json.dumps({
    "active_cases": active_count_debug,
    "closed_cases": closed_in_period_debug,
    "candidates": candidates,
    "best_agent": best_agent
}))"""

env_args = {'var_function-call-7401295907139314145': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11292736271626414979': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-7648281904145735316': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12036530776075449149': 'file_storage/function-call-12036530776075449149.json', 'var_function-call-14588621972763640650': 'file_storage/function-call-14588621972763640650.json', 'var_function-call-12384156789691024942': None, 'var_function-call-7707040309768070143': {'target_cases': 7, 'transferred': 0, 'non_transferred': 7, 'sample_processed_counts': [['005Wt000003NJufIAG', 1], ['005Wt000003NJGLIA4', 1], ['005Wt000003NDqDIAW', 1], ['005Wt000003NJD9IAO', 1], ['005Wt000003NEtOIAW', 1]]}, 'var_function-call-602365689252274697': {'total_cases': 75, 'total_history_entries_unique_cases': 153, 'matches': 75, 'potential_transfers_global': 4}}

exec(code, env_args)
