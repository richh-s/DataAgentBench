code = """import json
import pandas as pd
from datetime import datetime, timezone

# Load data
with open(locals()['var_function-call-5219504624406109697'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-2147877274171806371'], 'r') as f:
    history_data = json.load(f)

# Helper to clean ID
def clean_id(i):
    if not i: return None
    i = i.strip()
    if i.startswith('#'): i = i[1:]
    return i

# Helper to parse date
def parse_date(d_str):
    if not d_str or d_str == 'None': return None
    # Format example: "2023-07-02T11:00:00.000+0000"
    # Python 3.11+ handles +0000.
    return datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")

# Date range
start_date = datetime(2023, 5, 2, tzinfo=timezone.utc)
end_date = datetime(2023, 9, 2, 23, 59, 59, tzinfo=timezone.utc)

# Process History
# Group owner assignments by case
case_assignments = {} # case_id -> list of records
for h in history_data:
    if h['field__c'] == 'Owner Assignment':
        cid = clean_id(h['caseid__c'])
        if cid:
            if cid not in case_assignments:
                case_assignments[cid] = []
            case_assignments[cid].append(h)

# Agent stats
# agent_id -> {'managed': 0, 'ht_sum': 0.0, 'ht_count': 0}
agents = {}

def get_agent(aid):
    if aid not in agents:
        agents[aid] = {'managed': 0, 'ht_sum': 0.0, 'ht_count': 0}
    return agents[aid]

# Process Cases
count_analyzed = 0
for c in cases_data:
    cid = clean_id(c['id'])
    closed_str = c['closeddate']
    if not closed_str or closed_str == 'None':
        continue
    
    closed_dt = parse_date(closed_str)
    created_dt = parse_date(c['createddate'])
    
    # Filter by date range (Closed Date)
    if not (start_date <= closed_dt <= end_date):
        continue

    count_analyzed += 1
    
    # Check assignments
    assignments = case_assignments.get(cid, [])
    num_assignments = len(assignments)
    
    # Identify managed agents
    managed_agents = set()
    
    # Add final owner
    final_owner = clean_id(c['ownerid'])
    if final_owner: managed_agents.add(final_owner)
    
    # Add from history
    for a in assignments:
        ov = clean_id(a['oldvalue__c'])
        nv = clean_id(a['newvalue__c'])
        if ov: managed_agents.add(ov)
        if nv: managed_agents.add(nv)
        
    # Update managed count
    for ag in managed_agents:
        get_agent(ag)['managed'] += 1
        
    # Handle Time Logic
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # If num_assignments > 1 -> Transferred. Skip HT.
    # If num_assignments == 1 -> Not Transferred. Calc HT.
    # If num_assignments == 0 -> Assume Not Transferred (Initial only). Calc HT.
    
    if num_assignments <= 1:
        # Calculate HT
        # duration in seconds
        duration = (closed_dt - created_dt).total_seconds()
        
        # Assign to the owner. Who is the owner?
        # If not transferred, final_owner should be the only owner.
        if final_owner:
            ag_stats = get_agent(final_owner)
            ag_stats['ht_sum'] += duration
            ag_stats['ht_count'] += 1

# Calculate averages and find winner
results = []
for ag_id, stats in agents.items():
    if stats['managed'] > 1:
        if stats['ht_count'] > 0:
            avg_ht = stats['ht_sum'] / stats['ht_count']
            results.append({
                'id': ag_id,
                'avg_ht': avg_ht,
                'managed': stats['managed'],
                'ht_count': stats['ht_count']
            })

# Sort by lowest avg_ht
results.sort(key=lambda x: x['avg_ht'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1509840735203086818': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8995979380551569871': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}], 'var_function-call-10766181199186176938': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-4456964055745370618': [{'count': '153'}], 'var_function-call-5219504624406109697': 'file_storage/function-call-5219504624406109697.json', 'var_function-call-2147877274171806371': 'file_storage/function-call-2147877274171806371.json'}

exec(code, env_args)
