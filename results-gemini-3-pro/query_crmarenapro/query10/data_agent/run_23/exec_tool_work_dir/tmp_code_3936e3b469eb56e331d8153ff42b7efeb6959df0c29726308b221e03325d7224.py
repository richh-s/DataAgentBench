code = """import json
import datetime

# Load data
cases = locals()['var_function-call-3413395133262997031']
# History is in a file
with open(locals()['var_function-call-11478678007413607521'], 'r') as f:
    history = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if i and isinstance(i, str) and i.startswith('#'):
        return i[1:]
    return i

# Helper to parse date
def parse_date(d_str):
    if not d_str or d_str == 'None':
        return None
    try:
        dt = datetime.datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        return dt
    except ValueError:
        try:
             dt = datetime.datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z")
             return dt
        except:
             return None

# Build History Map
history_map = {}
for h in history:
    cid = clean_id(h.get('caseid__c'))
    if cid:
        if cid not in history_map:
            history_map[cid] = []
        history_map[cid].append(h)

# Agent Stats
agent_stats = {} # {agent_id: {'processed_count': 0, 'handle_times': []}}

for c in cases:
    cid = clean_id(c.get('id'))
    owner_id = clean_id(c.get('ownerid'))
    created_date = parse_date(c.get('createddate'))
    closed_date = parse_date(c.get('closeddate'))
    
    if not created_date or not closed_date:
        continue
    
    duration = (closed_date - created_date).total_seconds()
    
    h_entries = history_map.get(cid, [])
    
    # Processors
    processors = set()
    # If no history, assume owner_id is the only one (Initial)
    if not h_entries:
        processors.add(owner_id)
        assignment_count = 1 # Assuming implicit assignment
        # Wait, if no history, assignment_count = 0 in terms of RECORDS.
        # But logic says "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
        # If the DB tracks "Owner Assignment" properly, there should be one record.
        # If there are NO records, maybe it's corrupted or logic differs.
        # Let's assume if NO history, it's Single Owner (the current owner).
        assignment_count = 1
    else:
        # Check newvalue__c for processors
        for h in h_entries:
            p = clean_id(h.get('newvalue__c'))
            if p:
                processors.add(p)
        # Ensure final owner is in processors
        processors.add(owner_id)
        assignment_count = len(h_entries)

    # Update processed count
    for p in processors:
        if p not in agent_stats:
            agent_stats[p] = {'processed_count': 0, 'handle_times': []}
        agent_stats[p]['processed_count'] += 1
        
    # Handle Time Logic
    # If assignment_count == 1 (Single Owner)
    if assignment_count == 1:
         agent_stats[owner_id]['handle_times'].append(duration)

# Analyze
results = []
for aid, stats in agent_stats.items():
    if stats['processed_count'] > 1:
        if len(stats['handle_times']) > 0:
            avg_ht = sum(stats['handle_times']) / len(stats['handle_times'])
            results.append({'agent_id': aid, 'avg_ht': avg_ht, 'count': stats['processed_count']})
        else:
            # Processed > 1 but no handle times (all transferred?)
            pass

# Sort by avg_ht
results.sort(key=lambda x: x['avg_ht'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2266883777880752231': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1179932955608252203': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-14487514633330753000': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1153138630470492623': [{'count': '7'}], 'var_function-call-14162274668640195149': [{'count': '393'}], 'var_function-call-3413395133262997031': [{'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'priority': 'High', 'subject': 'Tailoring Problem', 'description': 'The AI Cirku-Tech tool is not flexible enough for specific customizations required by our unique projects.', 'status': 'Closed', 'contactid': '#003Wt00000Jqt79IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHViZIAX', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'priority': 'Medium', 'subject': 'AI Features Unreliable', 'description': 'The AI functionalities of the CollabCircuit Hub are not consistently working, leading to decreased productivity and dissatisfaction among our team members.', 'status': 'Closed', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '001Wt00000PHVfJIAX', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'priority': 'High', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'status': 'Closed', 'contactid': '003Wt00000JqviSIAR', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '#001Wt00000PGovMIAT', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'priority': 'High', 'subject': 'Scaling Issues with OptiPower', 'description': 'I face challenges in scaling the OptiPower Manager to accommodate increasing demands for our projects.', 'status': 'Closed', 'contactid': '#003Wt00000JqxfNIAR', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'orderitemid__c': '802Wt00000796qDIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PFsmcIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'priority': 'High', 'subject': 'Installation Issues', 'description': 'I am experiencing persistent errors during installation that prevent me from setting up the PulseSim Pro software.', 'status': 'Closed', 'contactid': '003Wt00000JqqEAIAZ', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'priority': 'Medium', 'subject': 'Setup Error', 'description': 'The initial installation process for PulseSim Pro constantly fails, which is blocking my workflow.', 'status': 'Closed', 'contactid': '#003Wt00000JqqEAIAZ', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-11478678007413607521': 'file_storage/function-call-11478678007413607521.json'}

exec(code, env_args)
