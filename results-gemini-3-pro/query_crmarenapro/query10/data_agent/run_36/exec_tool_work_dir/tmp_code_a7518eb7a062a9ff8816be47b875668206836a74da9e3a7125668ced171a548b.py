code = """import json
from datetime import datetime, timezone

with open(locals()['var_function-call-5219504624406109697'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-2147877274171806371'], 'r') as f:
    history_data = json.load(f)

def clean_id(i):
    if not i: return None
    i = i.strip()
    if i == "None": return None
    if i.startswith('#'): i = i[1:]
    return i

def parse_date(d_str):
    if not d_str or d_str == 'None': return None
    return datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")

start_date = datetime(2023, 5, 2, tzinfo=timezone.utc)
end_date = datetime(2023, 9, 2, 23, 59, 59, tzinfo=timezone.utc)

# 1. Map assignments
case_assignments = {}
for h in history_data:
    if h['field__c'] == 'Owner Assignment':
        cid = clean_id(h['caseid__c'])
        if cid:
            if cid not in case_assignments:
                case_assignments[cid] = []
            case_assignments[cid].append(h)

agents = {}
def get_agent(aid):
    if aid not in agents:
        agents[aid] = {'active_managed': 0, 'lifetime_managed': 0, 'ht_sum': 0.0, 'ht_count': 0}
    return agents[aid]

# 2. Process all cases
for c in cases_data:
    cid = clean_id(c['id'])
    closed_str = c['closeddate']
    created_str = c['createddate']
    
    closed_dt = parse_date(closed_str)
    created_dt = parse_date(created_str)
    
    # Identify managed agents
    assignments = case_assignments.get(cid, [])
    managed_agents = set()
    final_owner = clean_id(c['ownerid'])
    if final_owner: managed_agents.add(final_owner)
    for a in assignments:
        ov = clean_id(a['oldvalue__c'])
        nv = clean_id(a['newvalue__c'])
        if ov: managed_agents.add(ov)
        if nv: managed_agents.add(nv)
    
    # Lifetime count
    for ag in managed_agents:
        get_agent(ag)['lifetime_managed'] += 1
        
    # Active in window count
    # Case is active in window if Created <= End AND (Closed >= Start OR Closed is None)
    is_active = False
    if created_dt and created_dt <= end_date:
        if closed_dt:
            if closed_dt >= start_date:
                is_active = True
        else:
            is_active = True # Still open
            
    if is_active:
        for ag in managed_agents:
            get_agent(ag)['active_managed'] += 1

    # HT Calculation (Closed in window)
    if closed_dt and (start_date <= closed_dt <= end_date):
        # Only if not transferred (assignments <= 1)
        if len(assignments) <= 1:
            duration = (closed_dt - created_dt).total_seconds()
            if final_owner:
                # HT only counts for the final owner if not transferred
                # Wait. If assignments <= 1, managed_agents has 1 person (final_owner).
                # Unless history is missing initial. 
                # Just add to final_owner.
                get_agent(final_owner)['ht_sum'] += duration
                get_agent(final_owner)['ht_count'] += 1

# 3. Evaluate results
results = []
for ag_id, stats in agents.items():
    if stats['ht_count'] > 0:
        avg_ht = stats['ht_sum'] / stats['ht_count']
        results.append({
            'id': ag_id,
            'avg_ht': avg_ht,
            'active_managed': stats['active_managed'],
            'lifetime_managed': stats['lifetime_managed'],
            'ht_count': stats['ht_count']
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1509840735203086818': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8995979380551569871': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}], 'var_function-call-10766181199186176938': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-4456964055745370618': [{'count': '153'}], 'var_function-call-5219504624406109697': 'file_storage/function-call-5219504624406109697.json', 'var_function-call-2147877274171806371': 'file_storage/function-call-2147877274171806371.json', 'var_function-call-8134304008643660492': [], 'var_function-call-16134038160464543950': {'count_in_range': 7, 'agents_count': 8, 'sample_agent': [['005Wt000003NJufIAG', {'managed': 1, 'ht_sum': 33068.0, 'ht_count': 1}], ['None', {'managed': 7, 'ht_sum': 0.0, 'ht_count': 0}], ['005Wt000003NJGLIA4', {'managed': 1, 'ht_sum': 1442.0, 'ht_count': 1}], ['005Wt000003NDqDIAW', {'managed': 1, 'ht_sum': 882.0, 'ht_count': 1}], ['005Wt000003NJD9IAO', {'managed': 1, 'ht_sum': 21608.0, 'ht_count': 1}]]}, 'var_function-call-14493276817926375130': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
