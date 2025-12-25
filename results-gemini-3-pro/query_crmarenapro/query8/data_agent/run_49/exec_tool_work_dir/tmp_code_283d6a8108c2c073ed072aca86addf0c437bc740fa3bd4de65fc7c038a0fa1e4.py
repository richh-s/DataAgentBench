code = """import json
import pandas as pd

# Load data
case_data = json.load(open(locals()['var_function-call-6169736016805257938'], 'r'))
case_history = json.load(open(locals()['var_function-call-9711040516199644191'], 'r'))

def clean_id(val):
    if not val or str(val) == 'None':
        return None
    val = str(val).strip()
    if val.startswith('#'):
        val = val[1:]
    return val

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        return None

start_date = pd.Timestamp("2022-04-10").tz_localize('UTC')
end_date = pd.Timestamp("2023-04-10").tz_localize('UTC')

# Track cases handled per agent
agent_cases = {} # agent_id -> set of case_ids
transfer_counts = {} # agent_id -> count

# Process Case table
for row in case_data:
    c_date = parse_date(row.get('createddate'))
    cl_date = parse_date(row.get('closeddate'))
    if str(row.get('closeddate')) == 'None':
        cl_date = None
        
    is_active = False
    if c_date and c_date <= end_date:
        if cl_date:
            if cl_date >= start_date:
                is_active = True
        else:
            is_active = True
            
    if is_active:
        oid = clean_id(row.get('ownerid'))
        cid = clean_id(row.get('id'))
        if oid and cid:
            if oid not in agent_cases:
                agent_cases[oid] = set()
            agent_cases[oid].add(cid)

# Process History
for row in case_history:
    d = parse_date(row.get('createddate'))
    if d and start_date <= d <= end_date:
        old_v = clean_id(row.get('oldvalue__c'))
        new_v = clean_id(row.get('newvalue__c'))
        cid = clean_id(row.get('caseid__c'))
        
        if old_v:
            # Transfer from old_v
            transfer_counts[old_v] = transfer_counts.get(old_v, 0) + 1
            if cid:
                if old_v not in agent_cases:
                    agent_cases[old_v] = set()
                agent_cases[old_v].add(cid)
        
        if new_v and cid:
            if new_v not in agent_cases:
                agent_cases[new_v] = set()
            agent_cases[new_v].add(cid)

# Filter: Handled > 0
valid_agents = [a for a in agent_cases if len(agent_cases[a]) > 0]

# Find min transfers
if not valid_agents:
    print("__RESULT__:")
    print(json.dumps({"min_transfers": "No agents found", "candidates": []}))
else:
    min_transfers = float('inf')
    for a in valid_agents:
        count = transfer_counts.get(a, 0)
        if count < min_transfers:
            min_transfers = count

    # Candidates
    candidates = []
    for a in valid_agents:
        if transfer_counts.get(a, 0) == min_transfers:
            candidates.append({
                'id': a,
                'cases_handled': len(agent_cases[a])
            })

    # Sort by cases_handled descending
    candidates.sort(key=lambda x: x['cases_handled'], reverse=True)

    print("__RESULT__:")
    print(json.dumps({"min_transfers": min_transfers, "candidates": candidates[:10]}))"""

env_args = {'var_function-call-9690860097743401831': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14933305045033697401': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4251482298526234565': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-9208389653081350638': [{'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '#005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NEzqIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NJcwIAG'}, {'ownerid': '005Wt000003NFhOIAW'}, {'ownerid': '005Wt000003NItlIAG'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '#005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NIfFIAW'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NHfyIAG'}, {'ownerid': '#005Wt000003NJoDIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '005Wt000003NJcvIAG'}, {'ownerid': '005Wt000003NJppIAG'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NJrRIAW'}, {'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NEGhIAO'}, {'ownerid': '#005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NDqFIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NEdKIAW'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NJQ1IAO'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NDsUIAW'}, {'ownerid': '005Wt000003NDJ1IAO'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NBykIAG'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '#005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NInJIAW'}, {'ownerid': '#005Wt000003NInLIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NIfHIAW'}, {'ownerid': '#005Wt000003NJUrIAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '005Wt000003NHGAIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIfFIAW'}, {'ownerid': '005Wt000003NIaQIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NINVIA4'}, {'ownerid': '005Wt000003NJ3RIAW'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '#005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '#005Wt000003NJcvIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIc2IAG'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NHfzIAG'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJoDIAW'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NGwpIAG'}, {'ownerid': '005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIliIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '#005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NEGhIAO'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NDXZIA4'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NHGAIA4'}], 'var_function-call-11047613532111607836': [{'count': '165'}], 'var_function-call-9711040516199644191': 'file_storage/function-call-9711040516199644191.json', 'var_function-call-6405842398321689761': {'min_transfers': 0, 'candidates': ['005Wt000003NJcwIAG', '005Wt000003NDsUIAW', '005Wt000003NDqFIAW', '005Wt000003NF1SIAW', '005Wt000003NJcvIAG', '005Wt000003NDXZIA4', '005Wt000003NJ6gIAG', '005Wt000003NIXBIA4', '005Wt000003NEdKIAW', '005Wt000003NJhlIAG', '005Wt000003NHsrIAG', '005Wt000003NJTFIA4', '005Wt000003NI90IAG', '005Wt000003NGjuIAG', '005Wt000003NJrRIAW', '005Wt000003NHpeIAG', '005Wt000003NJppIAG', '005Wt000003NHGAIA4', '005Wt000003NIddIAG', '005Wt000003NJeXIAW', '005Wt000003NFKoIAO', '005Wt000003NHuUIAW', '005Wt000003NIVZIA4', '005Wt000003NJ6fIAG', '005Wt000003NEzqIAG', '005Wt000003NIwzIAG', '005Wt000003NHfyIAG', '005Wt000003NI2XIAW', '005Wt000003NBykIAG', '005Wt000003NISLIA4', '005Wt000003NJufIAG', '005Wt000003NIAcIAO', '005Wt000003NIvNIAW', '005Wt000003NI5mIAG', '005Wt000003NJQ1IAO', '005Wt000003NFhOIAW', '005Wt000003NJbJIAW', '005Wt000003NIaQIAW', '005Wt000003NInLIAW', '005Wt000003NJWTIA4', '005Wt000003NJLBIA4', '005Wt000003NIYnIAO', '005Wt000003NDu7IAG', '005Wt000003NDqDIAW', '005Wt000003NItlIAG', '005Wt000003NFW6IAO', '005Wt000003NIk5IAG', '005Wt000003NH3GIAW', '005Wt000003NGwpIAG', '005Wt000003NHg0IAG', '005Wt000003NIk7IAG', '005Wt000003NBcAIAW', '005Wt000003NJGLIA4', '005Wt000003NJ8HIAW', '005Wt000003NJUrIAO', '005Wt000003NIDqIAO', '005Wt000003NJJaIAO', '005Wt000003NIc3IAG', '005Wt000003NIc2IAG', '005Wt000003NJ3RIAW', '005Wt000003NIfFIAW', '005Wt000003NINVIA4', '005Wt000003NFKpIAO', '005Wt000003NEGhIAO', '005Wt000003NFr4IAG', '005Wt000003NHfzIAG', '005Wt000003NDJ1IAO', '005Wt000003NJEjIAO', '005Wt000003NDqEIAW', '005Wt000003NJ9tIAG', '005Wt000003NJoDIAW', '005Wt000003NJ0DIAW', '005Wt000003NEtOIAW', '005Wt000003NJD9IAO', '005Wt000003NJzVIAW', '005Wt000003NInJIAW', '005Wt000003NIfHIAW'], 'count_candidates': 77}, 'var_function-call-5980305958030265987': 'file_storage/function-call-5980305958030265987.json', 'var_function-call-16722632085605291917': {'min_transfers': 0, 'candidates': ['005Wt000003NJJaIAO', '005Wt000003NFKoIAO', '005Wt000003NDJ1IAO', '005Wt000003NJD9IAO', '005Wt000003NHfyIAG', '005Wt000003NJ0DIAW', '005Wt000003NIfHIAW', '005Wt000003NEtOIAW', '005Wt000003NJ3RIAW', '005Wt000003NJcwIAG', '005Wt000003NEdKIAW', '005Wt000003NH3GIAW', '005Wt000003NJLBIA4', '005Wt000003NIk7IAG', '005Wt000003NJhlIAG', '005Wt000003NJQ1IAO', '005Wt000003NIwzIAG', '005Wt000003NDsUIAW', '005Wt000003NBcAIAW', '005Wt000003NIc2IAG', '005Wt000003NHsrIAG', '005Wt000003NIYnIAO', '005Wt000003NHuUIAW', '005Wt000003NBykIAG', '005Wt000003NHGAIA4', '005Wt000003NInLIAW', '005Wt000003NIvNIAW', '005Wt000003NFKpIAO', '005Wt000003NJeXIAW', '005Wt000003NIDqIAO', '005Wt000003NJ6gIAG', '005Wt000003NEzqIAG', '005Wt000003NINVIA4', '005Wt000003NEGhIAO', '005Wt000003NJTFIA4', '005Wt000003NFW6IAO', '005Wt000003NJrRIAW', '005Wt000003NDu7IAG', '005Wt000003NI2XIAW', '005Wt000003NJufIAG', '005Wt000003NHpeIAG', '005Wt000003NIaQIAW', '005Wt000003NJWTIA4', '005Wt000003NIXBIA4', '005Wt000003NFr4IAG', '005Wt000003NIVZIA4', '005Wt000003NISLIA4', '005Wt000003NInJIAW', '005Wt000003NDqFIAW', '005Wt000003NJ8HIAW', '005Wt000003NJcvIAG', '005Wt000003NJ9tIAG', '005Wt000003NJoDIAW', '005Wt000003NGjuIAG', '005Wt000003NJEjIAO', '005Wt000003NFhOIAW'], 'count_candidates': 56}, 'var_function-call-7837149810432888262': {'min_transfers': inf, 'candidates': []}, 'var_function-call-6169736016805257938': 'file_storage/function-call-6169736016805257938.json'}

exec(code, env_args)
