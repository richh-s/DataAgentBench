code = """import json
import pandas as pd

# Load data
closed_cases = locals()['var_function-call-6235709102432108974']
open_cases = locals()['var_function-call-16482798849681777187']
history_path = locals()['var_function-call-5446965614530322862']

with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(x):
    if not x: return x
    return str(x).replace('#', '').strip()

# Maps
processed_map = {} # agent -> set(case_ids)
handle_time_map = {} # agent -> list(durations)

# Helper to process owners
def get_owners(cid, current_owner, history_records):
    owners = set()
    owners.add(clean_id(current_owner))
    
    # Filter history for this case
    # Optimized: Pre-group history by caseid?
    # Given history size, maybe better to loop once or dict.
    # We will build a dict of history first.
    return owners

# Build History Dict
history_dict = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    if cid not in history_dict:
        history_dict[cid] = []
    history_dict[cid].append(h)

# Process All Cases for "Processed Count"
# Combine lists
all_cases = []
for c in closed_cases:
    c['is_closed_in_window'] = True
    all_cases.append(c)
for c in open_cases:
    c['is_closed_in_window'] = False
    all_cases.append(c)

for c in all_cases:
    cid = clean_id(c['id'])
    owner = clean_id(c['ownerid'])
    
    case_owners = set()
    case_owners.add(owner)
    
    # History
    recs = history_dict.get(cid, [])
    history_count = len(recs)
    
    for h in recs:
        if h['newvalue__c']: case_owners.add(clean_id(h['newvalue__c']))
        if h['oldvalue__c'] and h['oldvalue__c'] != 'None': case_owners.add(clean_id(h['oldvalue__c']))
    
    # Add to processed_map
    for agent in case_owners:
        if agent not in processed_map:
            processed_map[agent] = set()
        processed_map[agent].add(cid)

    # Handle Time (Only for Closed in Window and Single Owner)
    if c.get('is_closed_in_window'):
        if history_count <= 1: # Single owner (Assuming 0 or 1 record implies no transfer away/to)
            # Actually, if history_count > 1, it's transferred.
            # If history_count == 1: Initial assignment.
            # If history_count == 0: No history? (Unlikely but assume single owner).
            
            # Duration
            try:
                created = pd.to_datetime(c['createddate'])
                closed = pd.to_datetime(c['closeddate'])
                duration = (closed - created).total_seconds()
            except:
                duration = 0
            
            # Add to owner's handle time
            # Owner is c['ownerid']
            if owner not in handle_time_map:
                handle_time_map[owner] = []
            handle_time_map[owner].append(duration)

# Analyze
results = []
for agent, p_cases in processed_map.items():
    if len(p_cases) > 1:
        # Check handle time
        if agent in handle_time_map and len(handle_time_map[agent]) > 0:
            avg_time = sum(handle_time_map[agent]) / len(handle_time_map[agent])
            results.append({
                'agent': agent,
                'avg_time': avg_time,
                'processed_count': len(p_cases)
            })

# Sort
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-25694081247760875': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12242375876057293113': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-4426529604873226006': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-10682198703271803977': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14247413615305265901': [{'count': '7'}], 'var_function-call-6235709102432108974': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-5446965614530322862': 'file_storage/function-call-5446965614530322862.json', 'var_function-call-10458650047739438891': [], 'var_function-call-2960978588983402610': {'500Wt00000DDepmIAD': {'history_count': 1, 'owners': ['005Wt000003NJufIAG'], 'duration_hours': 9.185555555555556}, '500Wt00000DDyzpIAD': {'history_count': 1, 'owners': ['005Wt000003NJGLIA4'], 'duration_hours': 0.40055555555555555}, '500Wt00000DDzUPIA1': {'history_count': 1, 'owners': ['005Wt000003NDqDIAW'], 'duration_hours': 0.245}, '500Wt00000DDzsbIAD': {'history_count': 1, 'owners': ['005Wt000003NJD9IAO'], 'duration_hours': 6.002222222222223}, '500Wt00000DDzscIAD': {'history_count': 1, 'owners': ['005Wt000003NEtOIAW'], 'duration_hours': 0.2797222222222222}, '500Wt00000DDzuEIAT': {'history_count': 1, 'owners': ['005Wt000003NJJaIAO'], 'duration_hours': 4.086666666666667}, '500Wt00000DE02HIAT': {'history_count': 1, 'owners': ['005Wt000003NIddIAG'], 'duration_hours': 0.6094444444444445}}, 'var_function-call-10223285237212817615': [], 'var_function-call-16482798849681777187': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-07-06T14:30:00.000+0000'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2021-06-03T14:30:00.000+0000'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG', 'createddate': '2022-03-02T10:15:00.000+0000'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW', 'createddate': '2021-10-05T14:45:00.000+0000'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:30:00.000+0000'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2022-03-15T11:00:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG', 'createddate': '2021-11-11T12:13:00.000+0000'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T10:30:00.000+0000'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO', 'createddate': '2021-08-24T13:25:00.000+0000'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG', 'createddate': '2021-11-01T10:15:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-05-24T04:08:00.000+0000'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW', 'createddate': '2021-06-02T10:00:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW', 'createddate': '2022-03-04T11:30:00.000+0000'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW', 'createddate': '2021-11-02T11:00:00.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-09-06T11:15:00.000+0000'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2021-10-22T10:15:00.000+0000'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO', 'createddate': '2022-01-28T02:41:00.000+0000'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-09-10T14:45:00.000+0000'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2023-09-04T14:20:00.000+0000'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-01-10T11:15:00.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO', 'createddate': '2023-09-05T10:15:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW', 'createddate': '2021-11-15T14:45:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW', 'createddate': '2021-07-05T10:15:00.000+0000'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2021-11-02T09:00:00.000+0000'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2021-09-17T09:45:00.000+0000'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2021-07-07T09:45:00.000+0000'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4', 'createddate': '2021-06-16T08:30:00.000+0000'}]}

exec(code, env_args)
