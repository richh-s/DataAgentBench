code = """import json
from datetime import datetime

file_path = locals()['var_function-call-16423644886177447864']

with open(file_path, 'r') as f:
    history = json.load(f)

start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10)

def parse_date(d_str):
    try:
        dt = datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        return dt.replace(tzinfo=None)
    except ValueError:
        try:
             dt = datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z")
             return dt.replace(tzinfo=None)
        except:
             return None

def clean_id(i):
    if not i or i == 'None':
        return None
    s = i.strip()
    if s.startswith('#'):
        s = s[1:]
    return s

transfer_counts = {}
handled_counts = {}
handled_agents = set()

for record in history:
    d_str = record.get('createddate')
    if not d_str:
        continue
    
    dt = parse_date(d_str)
    if not dt:
        continue
    
    # Filter date range
    if start_date <= dt <= end_date:
        old_val = clean_id(record.get('oldvalue__c'))
        new_val = clean_id(record.get('newvalue__c'))
        
        # Count transfers (sender)
        if old_val:
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
            
        # Track handled agents (receiver)
        if new_val:
            handled_agents.add(new_val)
            handled_counts[new_val] = handled_counts.get(new_val, 0) + 1

results = []
for agent in handled_agents:
    t_count = transfer_counts.get(agent, 0)
    h_count = handled_counts.get(agent, 0)
    results.append({
        'id': agent,
        'transfers': t_count,
        'handled': h_count
    })

# Sort: transfers ASC, handled DESC, id ASC
results.sort(key=lambda x: (x['transfers'], -x['handled'], x['id']))

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-13839168121012937296': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15665864907560440775': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-17818763881546237246': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-17156830544783936492': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-18158446380111994279': [{'count': '165'}], 'var_function-call-16423644886177447864': 'file_storage/function-call-16423644886177447864.json', 'var_function-call-18305135798892170151': ['005Wt000003NBcAIAW', '005Wt000003NBykIAG', '005Wt000003NDJ1IAO', '005Wt000003NDqFIAW', '005Wt000003NDsUIAW', '005Wt000003NEGhIAO', '005Wt000003NEzqIAG', '005Wt000003NFKoIAO', '005Wt000003NFr4IAG', '005Wt000003NGjuIAG', '005Wt000003NHpeIAG', '005Wt000003NHsrIAG', '005Wt000003NI2XIAW', '005Wt000003NINVIA4', '005Wt000003NISLIA4', '005Wt000003NIVZIA4', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG', '005Wt000003NInLIAW', '005Wt000003NIvNIAW', '005Wt000003NIwzIAG', '005Wt000003NJ0DIAW', '005Wt000003NJ6gIAG', '005Wt000003NJ8HIAW', '005Wt000003NJD9IAO', '005Wt000003NJEjIAO', '005Wt000003NJTFIA4', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJrRIAW']}

exec(code, env_args)
