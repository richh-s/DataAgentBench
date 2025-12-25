code = """import json
import pandas as pd
from datetime import datetime, timezone

# Load data
with open(locals()['var_function-call-3119883133918778239'], 'r') as f:
    cases_data = json.load(f)

with open(locals()['var_function-call-18131444671333490707'], 'r') as f:
    history_data = json.load(f)

def clean_id(i):
    if i and i.startswith('#'):
        return i[1:]
    return i

def parse_date(d):
    if not d or d == 'None':
        return None
    try:
        return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        try:
            return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z")
        except:
            return None

# Process History
case_history = {}
for h in history_data:
    cid = clean_id(h.get('caseid__c'))
    oid = clean_id(h.get('newvalue__c'))
    cdate = parse_date(h.get('createddate'))
    if cid and oid and cdate:
        if cid not in case_history:
            case_history[cid] = []
        case_history[cid].append({'date': cdate, 'owner': oid})

for cid in case_history:
    case_history[cid].sort(key=lambda x: x['date'])

start_date = datetime(2023, 5, 2, tzinfo=timezone.utc)
end_date = datetime(2023, 9, 2, 23, 59, 59, tzinfo=timezone.utc)

agent_total_processed_count = {} # Agent -> set of case_ids (all time)
agent_window_handle_times = {} # Agent -> list of durations (in window)

for c in cases_data:
    cid = clean_id(c.get('id'))
    closed_date = parse_date(c.get('closeddate'))
    created_date = parse_date(c.get('createddate'))
    
    # Determine owners (all time)
    owners = []
    if cid in case_history:
        owners = [x['owner'] for x in case_history[cid]]
    else:
        curr_owner = clean_id(c.get('ownerid'))
        if curr_owner:
            owners = [curr_owner]
            
    # Update total processed count
    for o in set(owners):
        if o not in agent_total_processed_count:
            agent_total_processed_count[o] = set()
        agent_total_processed_count[o].add(cid)
        
    # Check window for handle time
    if closed_date and start_date <= closed_date <= end_date:
        # Calculate handle time for FINAL owner
        duration = (closed_date - created_date).total_seconds()
        final_owner = owners[-1]
        
        if final_owner not in agent_window_handle_times:
            agent_window_handle_times[final_owner] = []
        agent_window_handle_times[final_owner].append(duration)

# Filter and Calculate
results = []
for agent in agent_total_processed_count:
    total_count = len(agent_total_processed_count[agent])
    if total_count > 1:
        # Must have handle time in window
        if agent in agent_window_handle_times:
            times = agent_window_handle_times[agent]
            avg_time = sum(times) / len(times)
            results.append({'agent': agent, 'avg_time': avg_time, 'count': total_count})

results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9942462505138529069': [{'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'priority': 'High', 'subject': 'Tailoring Problem', 'description': 'The AI Cirku-Tech tool is not flexible enough for specific customizations required by our unique projects.', 'status': 'Closed', 'contactid': '#003Wt00000Jqt79IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHViZIAX', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'priority': 'Medium', 'subject': 'AI Features Unreliable', 'description': 'The AI functionalities of the CollabCircuit Hub are not consistently working, leading to decreased productivity and dissatisfaction among our team members.', 'status': 'Closed', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '001Wt00000PHVfJIAX', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'priority': 'High', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'status': 'Closed', 'contactid': '003Wt00000JqviSIAR', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '#001Wt00000PGovMIAT', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'priority': 'High', 'subject': 'Scaling Issues with OptiPower', 'description': 'I face challenges in scaling the OptiPower Manager to accommodate increasing demands for our projects.', 'status': 'Closed', 'contactid': '#003Wt00000JqxfNIAR', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'orderitemid__c': '802Wt00000796qDIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PFsmcIAD', 'ownerid': '005Wt000003NEtOIAW'}], 'var_function-call-16399685360638173134': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-1831095406268104650': [{'count': '7'}], 'var_function-call-10695664970778867569': [{'count': '33'}], 'var_function-call-3419309582017879422': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'newvalue__c': '005Wt000003NJufIAG', 'assignment_date': '2023-07-01T10:30:00.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'newvalue__c': '005Wt000003NDqDIAW', 'assignment_date': '2023-05-10T14:45:00.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'newvalue__c': '005Wt000003NJJaIAO', 'assignment_date': '2023-06-02T09:30:00.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'newvalue__c': '005Wt000003NJGLIA4', 'assignment_date': '2023-08-15T14:30:00.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'newvalue__c': '005Wt000003NJD9IAO', 'assignment_date': '2023-06-30T13:03:00.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'newvalue__c': 'None', 'assignment_date': 'None'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'newvalue__c': 'None', 'assignment_date': 'None'}], 'var_function-call-12446716404083854311': [{'id': 'a04Wt00000537msIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537zmIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11214778995977530316': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14666509999231107248': [{'caseid__c': '500Wt00000DDz6FIAT', 'cnt': '2'}, {'caseid__c': '500Wt00000DDflsIAD', 'cnt': '2'}, {'caseid__c': '500Wt00000DDDfwIAH', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzW3IAL', 'cnt': '2'}, {'caseid__c': '500Wt00000DDfvXIAT', 'cnt': '2'}, {'caseid__c': '500Wt00000DDYpGIAX', 'cnt': '2'}, {'caseid__c': '500Wt00000DE0YXIA1', 'cnt': '2'}, {'caseid__c': '500Wt00000DDZtLIAX', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzRCIA1', 'cnt': '2'}, {'caseid__c': '500Wt00000DDnt7IAD', 'cnt': '2'}, {'caseid__c': '500Wt00000DDzSnIAL', 'cnt': '2'}, {'caseid__c': '500Wt00000DDTERIA5', 'cnt': '2'}], 'var_function-call-7995095031378652022': [{'count': '153'}], 'var_function-call-3119883133918778239': 'file_storage/function-call-3119883133918778239.json', 'var_function-call-18131444671333490707': 'file_storage/function-call-18131444671333490707.json', 'var_function-call-5642097747574217868': []}

exec(code, env_args)
