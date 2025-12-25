code = """import json
from datetime import datetime

# Load data
with open(locals()['var_function-call-8425610515159770077'], 'r') as f:
    all_cases = json.load(f)
with open(locals()['var_function-call-2331162336508267354'], 'r') as f:
    all_history = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

def parse_date(d):
    if not d or d == 'None':
        return None
    try:
        return datetime.strptime(d.split('+')[0], "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        try:
             return datetime.strptime(d.split('+')[0], "%Y-%m-%dT%H:%M:%S")
        except:
             return None

# Build history map
case_history = {}
for h in all_history:
    cid = clean_id(h['caseid__c'])
    if cid not in case_history:
        case_history[cid] = []
    case_history[cid].append(h)

# 1. Global Processed Count
agent_processed_global = {}

for c in all_cases:
    cid = clean_id(c['id'])
    owners = set()
    owners.add(clean_id(c['ownerid'])) # Case owner is always an owner
    
    # Add history owners
    if cid in case_history:
        for h in case_history[cid]:
            owners.add(clean_id(h['newvalue__c']))
            
    for ag in owners:
        if ag not in agent_processed_global:
            agent_processed_global[ag] = set()
        agent_processed_global[ag].add(cid)

eligible_agents = set()
for ag, cases in agent_processed_global.items():
    if len(cases) > 1:
        eligible_agents.add(ag)

# 2. Handle Time in Window
start_date = datetime(2023, 5, 2)
end_date = datetime(2023, 9, 2, 23, 59, 59)

agent_stats = {} # agent -> {total_time, count}

for c in all_cases:
    # Filter by closed date
    c_date = parse_date(c['closeddate'])
    if c_date and start_date <= c_date <= end_date:
        cid = clean_id(c['id'])
        
        # Check transfer status
        # Rule: Not transferred if <= 1 'Owner Assignment' records
        hist_entries = case_history.get(cid, [])
        is_transferred = len(hist_entries) > 1
        
        if not is_transferred:
            # Single owner
            owner = clean_id(c['ownerid'])
            # Verify owner is in eligible_agents
            if owner in eligible_agents:
                create_dt = parse_date(c['createddate'])
                if create_dt:
                    duration = (c_date - create_dt).total_seconds()
                    
                    if owner not in agent_stats:
                        agent_stats[owner] = {'total': 0.0, 'count': 0}
                    agent_stats[owner]['total'] += duration
                    agent_stats[owner]['count'] += 1

# 3. Find Lowest Average
min_avg = float('inf')
best_agent = None

debug_results = []

for ag, stats in agent_stats.items():
    if stats['count'] > 0:
        avg = stats['total'] / stats['count']
        debug_results.append({'agent': ag, 'avg': avg, 'count': stats['count']})
        if avg < min_avg:
            min_avg = avg
            best_agent = ag

print("__RESULT__:")
if best_agent:
    print(json.dumps(best_agent))
else:
    # Fallback to check if we can print debug info
    print(json.dumps({"error": "No agent found", "eligible_count": len(eligible_agents), "stats": debug_results}))"""

env_args = {'var_function-call-12736873582406850600': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-500048813479003814': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-15256579350552778872': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-17553053307972667841': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-2331162336508267354': 'file_storage/function-call-2331162336508267354.json', 'var_function-call-6612947768807540813': None, 'var_function-call-12044503619572217299': 'DEBUG', 'var_function-call-1676887979453229637': {'total_cases': 7, 'cases_with_history': 7, 'agents_processed_gt_1': [], 'agents_with_single_owner': ['005Wt000003NJufIAG', '005Wt000003NJGLIA4', '005Wt000003NDqDIAW', '005Wt000003NJD9IAO', '005Wt000003NEtOIAW', '005Wt000003NJJaIAO', '005Wt000003NIddIAG'], 'valid_agents': [], 'sample_case_id': '500Wt00000DDzscIAD', 'sample_hist_id': '500Wt00000DDzMLIA1'}, 'var_function-call-11916735775624741978': [{'count': '153'}], 'var_function-call-8425610515159770077': 'file_storage/function-call-8425610515159770077.json'}

exec(code, env_args)
