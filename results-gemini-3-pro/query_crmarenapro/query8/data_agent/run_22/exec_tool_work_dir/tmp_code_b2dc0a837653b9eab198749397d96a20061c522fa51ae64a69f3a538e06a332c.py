code = """import json
import pandas as pd
from datetime import datetime
from collections import defaultdict

with open(locals()['var_function-call-4374425599450765811'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-4374425599450764582'], 'r') as f:
    history = json.load(f)

def parse_date(d_str):
    if not d_str or d_str == 'None':
        return None
    try:
        return datetime.strptime(d_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    except:
        return None

def clean_id(i):
    if not i or i == 'None':
        return None
    i = i.strip()
    if i.startswith('#'):
        i = i[1:]
    return i

start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31, 23, 59, 59)

agent_cases = defaultdict(set)
agent_transfers = defaultdict(int)

# Process History
for h in history:
    d = parse_date(h.get('createddate'))
    if d and start_date <= d <= end_date:
        if h.get('field__c') in ['Owner Assignment', 'Owner']:
            old_v = clean_id(h.get('oldvalue__c'))
            new_v = clean_id(h.get('newvalue__c'))
            case_id = h.get('caseid__c')
            
            if old_v:
                agent_transfers[old_v] += 1
                agent_cases[old_v].add(case_id)
            
            if new_v:
                agent_cases[new_v].add(case_id)

# Process Cases (Initial ownership for cases created in range)
for c in cases:
    d = parse_date(c.get('createddate'))
    if d and start_date <= d <= end_date:
        owner = clean_id(c.get('ownerid'))
        if owner:
            agent_cases[owner].add(c.get('id'))

# Candidates: handled > 0 cases
candidates = []
for agent, cases_set in agent_cases.items():
    if len(cases_set) > 0:
        candidates.append({
            'id': agent,
            'transfers': agent_transfers.get(agent, 0),
            'handled_count': len(cases_set)
        })

# Analyze
if candidates:
    min_transfers = min(c['transfers'] for c in candidates)
    best = [c for c in candidates if c['transfers'] == min_transfers]
    # Sort by handled_count descending just to see
    best.sort(key=lambda x: x['handled_count'], reverse=True)
else:
    min_transfers = -1
    best = []

print("__RESULT__:")
print(json.dumps({'min_transfers': min_transfers, 'count': len(best), 'top_5': best[:5]}))"""

env_args = {'var_function-call-14423261937625395862': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14423261937625396313': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14423261937625396764': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-15972725945770119135': [{'count': '153'}], 'var_function-call-15972725945770117872': [{'count': '393'}], 'var_function-call-4374425599450765811': 'file_storage/function-call-4374425599450765811.json', 'var_function-call-4374425599450764582': 'file_storage/function-call-4374425599450764582.json', 'var_function-call-18326942288218182339': ['005Wt000003NIc2IAG', '005Wt000003NJrRIAW', '005Wt000003NFKoIAO', '005Wt000003NBcAIAW', '005Wt000003NJcvIAG', '005Wt000003NINVIA4', '005Wt000003NIwzIAG', '005Wt000003NHsrIAG', '005Wt000003NISLIA4', '005Wt000003NJ6gIAG', '005Wt000003NEzqIAG', '005Wt000003NJEjIAO', '005Wt000003NBykIAG', '005Wt000003NInLIAW', '005Wt000003NDJ1IAO', '005Wt000003NJTFIA4', '005Wt000003NIVZIA4', '005Wt000003NDqFIAW', '005Wt000003NGjuIAG', '005Wt000003NEGhIAO', '005Wt000003NI2XIAW', '005Wt000003NJ0DIAW', '005Wt000003NDsUIAW', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJ8HIAW', '005Wt000003NHpeIAG', '005Wt000003NFr4IAG', '005Wt000003NJD9IAO', '005Wt000003NIvNIAW', '005Wt000003NIaQIAW']}

exec(code, env_args)
