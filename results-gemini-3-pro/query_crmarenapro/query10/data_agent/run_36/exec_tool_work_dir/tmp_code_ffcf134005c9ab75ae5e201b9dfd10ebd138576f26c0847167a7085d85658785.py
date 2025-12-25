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

case_assignments = {}
for h in history_data:
    if h['field__c'] == 'Owner Assignment':
        cid = clean_id(h['caseid__c'])
        if cid:
            if cid not in case_assignments:
                case_assignments[cid] = []
            case_assignments[cid].append(h)

filtered_cases = []
for c in cases_data:
    cid = clean_id(c['id'])
    closed_str = c['closeddate']
    if not closed_str or closed_str == 'None':
        continue
    closed_dt = parse_date(closed_str)
    
    if start_date <= closed_dt <= end_date:
        filtered_cases.append(c)

print("__RESULT__:")
print(json.dumps(filtered_cases))"""

env_args = {'var_function-call-1509840735203086818': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8995979380551569871': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}], 'var_function-call-10766181199186176938': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-4456964055745370618': [{'count': '153'}], 'var_function-call-5219504624406109697': 'file_storage/function-call-5219504624406109697.json', 'var_function-call-2147877274171806371': 'file_storage/function-call-2147877274171806371.json', 'var_function-call-8134304008643660492': [], 'var_function-call-16134038160464543950': {'count_in_range': 7, 'agents_count': 8, 'sample_agent': [['005Wt000003NJufIAG', {'managed': 1, 'ht_sum': 33068.0, 'ht_count': 1}], ['None', {'managed': 7, 'ht_sum': 0.0, 'ht_count': 0}], ['005Wt000003NJGLIA4', {'managed': 1, 'ht_sum': 1442.0, 'ht_count': 1}], ['005Wt000003NDqDIAW', {'managed': 1, 'ht_sum': 882.0, 'ht_count': 1}], ['005Wt000003NJD9IAO', {'managed': 1, 'ht_sum': 21608.0, 'ht_count': 1}]]}}

exec(code, env_args)
