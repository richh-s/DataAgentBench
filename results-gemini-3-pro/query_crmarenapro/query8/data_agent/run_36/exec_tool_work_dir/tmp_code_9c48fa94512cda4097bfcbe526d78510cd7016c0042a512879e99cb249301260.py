code = """import json
import datetime

cases = json.load(open(locals()['var_function-call-13480936882204567300']))
history = json.load(open(locals()['var_function-call-3991008059814266160']))

def clean_id(i):
    if i and i.startswith('#'):
        return i[1:]
    return i

def parse_dt(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")

p_start = datetime.datetime(2022, 4, 1, tzinfo=datetime.timezone.utc)
p_end = datetime.datetime(2023, 3, 31, 23, 59, 59, tzinfo=datetime.timezone.utc)

case_transfers = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    old_v = clean_id(h['oldvalue__c'])
    new_v = clean_id(h['newvalue__c'])
    if old_v == 'None': old_v = None
    if new_v == 'None': new_v = None
    dt = parse_dt(h['createddate'])
    if cid not in case_transfers:
        case_transfers[cid] = []
    case_transfers[cid].append({'old': old_v, 'new': new_v, 'date': dt})

for cid in case_transfers:
    case_transfers[cid].sort(key=lambda x: x['date'])

agent_assignments_p = {} # Agent -> count
agent_transfer_counts_p = {} # Agent -> count

for c in cases:
    cid = clean_id(c['id'])
    created_dt = parse_dt(c['createddate'])
    transfers = case_transfers.get(cid, [])
    
    timeline = []
    current_agent = None
    current_start = created_dt
    
    if transfers and transfers[0]['old'] is None:
        current_agent = transfers[0]['new']
        current_start = transfers[0]['date']
        start_idx = 1
    elif transfers:
        current_agent = transfers[0]['old']
        current_start = created_dt
        start_idx = 0
    else:
        current_agent = clean_id(c['ownerid'])
        current_start = created_dt
        start_idx = 0
        
    for i in range(start_idx, len(transfers)):
        t = transfers[i]
        timeline.append((current_agent, current_start, t['date']))
        current_agent = t['new']
        current_start = t['date']
        
    closed_dt = None
    if c['closeddate'] and c['closeddate'] != 'None':
        closed_dt = parse_dt(c['closeddate'])
    final_end = closed_dt if closed_dt else datetime.datetime.now(datetime.timezone.utc)
    timeline.append((current_agent, current_start, final_end))
    
    # Check assignments in P
    for agent, start, end in timeline:
        if not agent: continue
        # Assignment occurred at 'start'.
        if p_start <= start <= p_end:
            agent_assignments_p[agent] = agent_assignments_p.get(agent, 0) + 1
            
    # Check transfers in P
    for t in transfers:
        if t['old'] is not None:
            if p_start <= t['date'] <= p_end:
                aid = t['old']
                agent_transfer_counts_p[aid] = agent_transfer_counts_p.get(aid, 0) + 1

candidates = []
for agent, count in agent_assignments_p.items():
    if count > 0:
        tc = agent_transfer_counts_p.get(agent, 0)
        candidates.append({'id': agent, 'transfer_count': tc, 'assignment_count': count})

candidates.sort(key=lambda x: (x['transfer_count'], -x['assignment_count']))

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-10596123665962995333': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4624164474270102215': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15624615594297472901': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-15061620003663225348': [{'count': '153'}], 'var_function-call-13480936882204567300': 'file_storage/function-call-13480936882204567300.json', 'var_function-call-3991008059814266160': 'file_storage/function-call-3991008059814266160.json', 'var_function-call-942573968385245110': [{'id': '005Wt000003NJ0DIAW', 'count': 0}, {'id': '005Wt000003NDu7IAG', 'count': 0}, {'id': '005Wt000003NJhlIAG', 'count': 0}, {'id': '005Wt000003NGjuIAG', 'count': 0}, {'id': '005Wt000003NJWTIA4', 'count': 0}, {'id': '005Wt000003NIvNIAW', 'count': 0}, {'id': '005Wt000003NIVZIA4', 'count': 0}, {'id': '005Wt000003NFhOIAW', 'count': 0}, {'id': '005Wt000003NJoDIAW', 'count': 0}, {'id': '005Wt000003NIYnIAO', 'count': 0}, {'id': '005Wt000003NJ6gIAG', 'count': 0}, {'id': '005Wt000003NJeXIAW', 'count': 0}, {'id': '005Wt000003NIfHIAW', 'count': 0}, {'id': '005Wt000003NEdKIAW', 'count': 0}, {'id': '005Wt000003NHpeIAG', 'count': 0}, {'id': '005Wt000003NFKoIAO', 'count': 0}, {'id': '005Wt000003NEtOIAW', 'count': 0}, {'id': '005Wt000003NJTFIA4', 'count': 0}, {'id': '005Wt000003NIDqIAO', 'count': 0}, {'id': '005Wt000003NJLBIA4', 'count': 0}, {'id': '005Wt000003NDJ1IAO', 'count': 0}, {'id': '005Wt000003NHuUIAW', 'count': 0}, {'id': '005Wt000003NInLIAW', 'count': 0}, {'id': '005Wt000003NJQ1IAO', 'count': 0}, {'id': '005Wt000003NFKpIAO', 'count': 0}, {'id': '005Wt000003NJD9IAO', 'count': 0}, {'id': '005Wt000003NJ9tIAG', 'count': 0}, {'id': '005Wt000003NJ3RIAW', 'count': 0}, {'id': '005Wt000003NDsUIAW', 'count': 0}, {'id': '005Wt000003NFW6IAO', 'count': 0}, {'id': '005Wt000003NISLIA4', 'count': 0}, {'id': '005Wt000003NIk7IAG', 'count': 0}, {'id': '005Wt000003NJcwIAG', 'count': 0}, {'id': '005Wt000003NINVIA4', 'count': 0}, {'id': '005Wt000003NIc2IAG', 'count': 0}, {'id': '005Wt000003NHGAIA4', 'count': 0}, {'id': '005Wt000003NHsrIAG', 'count': 0}, {'id': '005Wt000003NIXBIA4', 'count': 0}, {'id': '005Wt000003NJrRIAW', 'count': 0}, {'id': '005Wt000003NJ8HIAW', 'count': 0}, {'id': '005Wt000003NIaQIAW', 'count': 0}, {'id': '005Wt000003NBykIAG', 'count': 0}, {'id': '005Wt000003NJEjIAO', 'count': 0}, {'id': '005Wt000003NDqFIAW', 'count': 0}, {'id': '005Wt000003NJufIAG', 'count': 0}, {'id': '005Wt000003NJJaIAO', 'count': 0}, {'id': '005Wt000003NBcAIAW', 'count': 0}, {'id': '005Wt000003NHfyIAG', 'count': 0}, {'id': '005Wt000003NEGhIAO', 'count': 0}, {'id': '005Wt000003NInJIAW', 'count': 0}, {'id': '005Wt000003NI2XIAW', 'count': 0}, {'id': '005Wt000003NEzqIAG', 'count': 0}, {'id': '005Wt000003NH3GIAW', 'count': 0}, {'id': '005Wt000003NIwzIAG', 'count': 0}, {'id': '005Wt000003NJcvIAG', 'count': 0}, {'id': '005Wt000003NFr4IAG', 'count': 0}, {'id': '005Wt000003NIliIAG', 'count': 1}], 'var_function-call-12917926841178267448': [{'id': '005Wt000003NIk7IAG', 'transfer_count': 0, 'handled_count': 3}, {'id': '005Wt000003NFKoIAO', 'transfer_count': 0, 'handled_count': 3}, {'id': '005Wt000003NJWTIA4', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJLBIA4', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJ6gIAG', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJoDIAW', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NINVIA4', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NIXBIA4', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJhlIAG', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJ8HIAW', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NHsrIAG', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NI2XIAW', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NBcAIAW', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NHpeIAG', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJEjIAO', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NJ0DIAW', 'transfer_count': 0, 'handled_count': 2}, {'id': '005Wt000003NEzqIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJD9IAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJcwIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NFhOIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NFKpIAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJ9tIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJeXIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NHuUIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NEtOIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NHfyIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NGjuIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIYnIAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJcvIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NFW6IAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJrRIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIvNIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NEGhIAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NDqFIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NEdKIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJQ1IAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NDu7IAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJufIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJTFIA4', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NDsUIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NDJ1IAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NISLIA4', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NBykIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NInJIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NInLIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NH3GIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIfHIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIwzIAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIaQIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJ3RIAW', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIDqIAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NFr4IAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIc2IAG', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIVZIA4', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NJJaIAO', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NHGAIA4', 'transfer_count': 0, 'handled_count': 1}, {'id': '005Wt000003NIliIAG', 'transfer_count': 1, 'handled_count': 2}], 'var_function-call-9030124968750351251': [{'Id': '005Wt000003NFKoIAO', 'FirstName': 'Akari', 'LastName': 'Fujiwara', 'Username': '1745179504.lam3c.akari.fujiwara@techagents.com'}, {'Id': '005Wt000003NIk7IAG', 'FirstName': 'Ibrahim ', 'LastName': 'Mohamed   ', 'Username': '1745179504.9vmfq.ibrahim.mohamed@techagents.com'}], 'var_function-call-15127485163775613856': {'005Wt000003NIk7IAG': [{'case_id': '500Wt00000DDPsOIAX', 'start': '2021-07-06T14:30:00+00:00', 'end': '2025-12-12T06:20:26.297769+00:00', 'overlap': True}, {'case_id': '500Wt00000DDsG4IAL', 'start': '2020-11-05T11:00:00+00:00', 'end': '2025-12-12T06:20:26.298766+00:00', 'overlap': True}, {'case_id': '500Wt00000DDydCIAT', 'start': '2021-05-24T04:08:00+00:00', 'end': '2025-12-12T06:20:26.299066+00:00', 'overlap': True}], '005Wt000003NFKoIAO': [{'case_id': '500Wt00000DDQRsIAP', 'start': '2023-03-08T06:49:00+00:00', 'end': '2023-03-08T07:07:30+00:00', 'overlap': True}, {'case_id': '500Wt00000DDzB4IAL', 'start': '2023-03-05T09:30:00+00:00', 'end': '2025-12-12T06:20:26.299250+00:00', 'overlap': True}, {'case_id': '500Wt00000DE0FDIA1', 'start': '2023-03-22T14:30:00+00:00', 'end': '2023-03-23T08:12:40+00:00', 'overlap': True}]}}

exec(code, env_args)
