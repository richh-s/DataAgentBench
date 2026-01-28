code = """import json
import datetime

# Get the file path from the variable with colon in name
file_path = globals().get('var_functions.query_db:14')
print('File path:', file_path)

with open(file_path, 'r') as f:
    casehistory = json.load(f)

print('Total casehistory records:', len(casehistory))

# Date range: last 4 quarters from 2023-04-10
start_date = datetime.datetime(2022, 4, 10)
end_date = datetime.datetime(2023, 4, 10)

filtered_records = []
for record in casehistory:
    try:
        created_date = datetime.datetime.fromisoformat(record['createddate'].replace('Z', '+00:00'))
        if start_date <= created_date <= end_date:
            filtered_records.append(record)
    except:
        continue

print('Records in date range:', len(filtered_records))

transfer_counts = {}
case_counts = {}

for record in filtered_records:
    case_id = record['caseid__c']
    old_owner = record['oldvalue__c']
    new_owner = record['newvalue__c']
    
    if new_owner and new_owner != 'None':
        case_counts[new_owner] = case_counts.get(new_owner, 0) + 1
    
    if old_owner and old_owner != 'None' and old_owner != 'None':
        transfer_counts[old_owner] = transfer_counts.get(old_owner, 0) + 1

print('Unique agents with transfers:', len(transfer_counts))
print('Unique agents who handled cases:', len(case_counts))

eligible_agents = {}
for agent in case_counts:
    if case_counts[agent] > 0:
        eligible_agents[agent] = {
            'transfers': transfer_counts.get(agent, 0),
            'cases': case_counts[agent]
        }

print('Eligible agents (>0 cases):', len(eligible_agents))

result = {}
if eligible_agents:
    sorted_agents = sorted(eligible_agents.items(), key=lambda x: x[1]['transfers'])
    best_agent = sorted_agents[0]
    result = {
        'agent_id': best_agent[0],
        'transfers': best_agent[1]['transfers'],
        'cases': best_agent[1]['cases']
    }
else:
    result = {'error': 'No eligible agents found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'field__c': 'Case Creation', 'cnt': '153'}, {'field__c': 'Case Closed', 'cnt': '75'}, {'field__c': 'Owner Assignment', 'cnt': '165'}], 'var_functions.query_db:5': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}], 'var_functions.execute_python:12': {'status': 'data_loaded', 'casehistory_len': 5, 'cases_len': 3}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
