code = """import pandas as pd
import json
from datetime import datetime

# Load data from previous steps
cases = [
    {"id": "500Wt00000DDepmIAD", "ownerid": "005Wt000003NJufIAG", "createddate": "2023-07-01T10:30:00.000+0000", "closeddate": "2023-07-01T19:41:08.000+0000"},
    {"id": "500Wt00000DDyzpIAD", "ownerid": "005Wt000003NJGLIA4", "createddate": "2023-08-15T14:30:00.000+0000", "closeddate": "2023-08-15T14:54:02.000+0000"},
    {"id": "500Wt00000DDzUPIA1", "ownerid": "005Wt000003NDqDIAW", "createddate": "2023-05-10T14:45:00.000+0000", "closeddate": "2023-05-10T14:59:42.000+0000"},
    {"id": "500Wt00000DDzsbIAD", "ownerid": "005Wt000003NJD9IAO", "createddate": "2023-06-30T13:03:00.000+0000", "closeddate": "2023-06-30T19:03:08.000+0000"},
    {"id": "#500Wt00000DDzscIAD", "ownerid": "005Wt000003NEtOIAW", "createddate": "2023-05-02T23:55:00.000+0000", "closeddate": "2023-05-03T00:11:47.000+0000"},
    {"id": "500Wt00000DDzuEIAT", "ownerid": "005Wt000003NJJaIAO", "createddate": "2023-06-02T09:30:00.000+0000", "closeddate": "2023-06-02T13:35:12.000+0000"},
    {"id": "#500Wt00000DE02HIAT", "ownerid": "005Wt000003NIddIAG", "createddate": "2023-06-03T14:45:00.000+0000", "closeddate": "2023-06-03T15:21:34.000+0000"}
]

history1 = [
    {"id": "#a04Wt00000537LUIAY", "caseid__c": "500Wt00000DDepmIAD", "oldvalue__c": "None", "newvalue__c": "005Wt000003NJufIAG", "createddate": "2023-07-01T10:30:00.000+0000", "field__c": "Owner Assignment"},
    {"id": "a04Wt00000537baIAA", "caseid__c": "500Wt00000DDzUPIA1", "oldvalue__c": "None", "newvalue__c": "005Wt000003NDqDIAW", "createddate": "2023-05-10T14:45:00.000+0000", "field__c": "Owner Assignment"},
    {"id": "a04Wt00000538hMIAQ", "caseid__c": "500Wt00000DDzuEIAT", "oldvalue__c": "None", "newvalue__c": "005Wt000003NJJaIAO", "createddate": "2023-06-02T09:30:00.000+0000", "field__c": "Owner Assignment"},
    {"id": "#a04Wt00000538r0IAA", "caseid__c": "500Wt00000DDyzpIAD", "oldvalue__c": "None", "newvalue__c": "005Wt000003NJGLIA4", "createddate": "2023-08-15T14:30:00.000+0000", "field__c": "Owner Assignment"},
    {"id": "a04Wt00000538scIAA", "caseid__c": "500Wt00000DDzsbIAD", "oldvalue__c": "None", "newvalue__c": "005Wt000003NJD9IAO", "createddate": "2023-06-30T13:03:00.000+0000", "field__c": "Owner Assignment"}
]

history2 = [
    {"id": "a04Wt00000532s4IAA", "caseid__c": "500Wt00000DDzscIAD", "oldvalue__c": "None", "newvalue__c": "005Wt000003NEtOIAW", "createddate": "2023-05-02T23:55:00.000+0000", "field__c": "Owner Assignment"},
    {"id": "a04Wt00000533XzIAI", "caseid__c": "500Wt00000DDzscIAD", "oldvalue__c": "None", "newvalue__c": "None", "createddate": "2023-05-03T00:11:47.000+0000", "field__c": "Case Closed"},
    {"id": "a04Wt00000537msIAA", "caseid__c": "500Wt00000DE02HIAT", "oldvalue__c": "None", "newvalue__c": "None", "createddate": "2023-06-03T14:45:00.000+0000", "field__c": "Case Creation"},
    {"id": "a04Wt00000537zmIAA", "caseid__c": "500Wt00000DE02HIAT", "oldvalue__c": "None", "newvalue__c": "None", "createddate": "2023-06-03T15:21:34.000+0000", "field__c": "Case Closed"},
    {"id": "#a04Wt00000538O0IAI", "caseid__c": "500Wt00000DDzscIAD", "oldvalue__c": "None", "newvalue__c": "None", "createddate": "2023-05-02T23:55:00.000+0000", "field__c": "Case Creation"},
    {"id": "a04Wt00000539BxIAI", "caseid__c": "500Wt00000DE02HIAT", "oldvalue__c": "None", "newvalue__c": "005Wt000003NIddIAG", "createddate": "2023-06-03T14:45:00.000+0000", "field__c": "Owner Assignment"}
]

# Combine history and filter
all_history = history1 + history2
owner_history = [h for h in all_history if h.get("field__c") == "Owner Assignment"]

# Helper to normalize ID
def normalize_id(oid):
    if not oid: return oid
    return oid.replace("#", "")

# Helper to parse date
def parse_date(date_str):
    # Format: 2023-07-01T10:30:00.000+0000
    # Python 3.11+ supports fromisoformat with Z/offset, but +0000 might need handling if not supported in env.
    # The format is consistent, so we can use strptime
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")

# Process cases
case_data = {}

for c in cases:
    cid = normalize_id(c["id"])
    create_dt = parse_date(c["createddate"])
    close_dt = parse_date(c["closeddate"])
    handle_time = (close_dt - create_dt).total_seconds()
    
    case_data[cid] = {
        "handle_time": handle_time,
        "owner_assignments": [],
        "owners": set()
    }

# Map history to cases
for h in owner_history:
    cid = normalize_id(h["caseid__c"])
    if cid in case_data:
        owner = normalize_id(h["newvalue__c"])
        case_data[cid]["owner_assignments"].append(h)
        case_data[cid]["owners"].add(owner)

# Agents processing
agents = {} # agent_id -> {processed_cases: set(), valid_handle_times: []}

for cid, data in case_data.items():
    transfer_count = len(data["owner_assignments"])
    involved_agents = data["owners"]
    
    # If no history found, check Case.ownerid (fallback, though prompt implies history MUST exist for correct calc)
    if transfer_count == 0:
        # Fallback: assume 1 owner from Case table
        # But this might be risky. Let's look at the cases.
        # From previous steps, all 7 cases have at least one 'Owner Assignment' row in the combined history.
        # history1 covered 5 cases. history2 covered 2 cases.
        # So transfer_count should be >= 1 for all.
        pass

    for agent in involved_agents:
        if agent not in agents:
            agents[agent] = {"processed_cases": set(), "valid_handle_times": []}
        
        agents[agent]["processed_cases"].add(cid)
        
        if transfer_count == 1:
            # Case was never transferred. This agent is the sole owner.
            # Add handle time.
            agents[agent]["valid_handle_times"].append(data["handle_time"])

# Calculate results
results = []
for agent_id, info in agents.items():
    processed_count = len(info["processed_cases"])
    if processed_count > 1:
        valid_times = info["valid_handle_times"]
        if valid_times:
            avg_time = sum(valid_times) / len(valid_times)
            results.append({
                "agent_id": agent_id,
                "processed_count": processed_count,
                "avg_handle_time": avg_time
            })
        else:
            # processed > 1 case, but none were valid for handle time (all transferred)
            # The agent has no average handle time.
            pass

# Sort by avg handle time
results.sort(key=lambda x: x["avg_handle_time"])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4169914442679779612': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6185992116014929346': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-6185992116014931461': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-13086923880513892808': [{'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539tVIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539v7IAA', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T16:03:45.000+0000', 'field__c': 'Case Closed'}], 'var_function-call-16717640008608374153': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6896054191619716323': [{'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1060913979323647870': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000533XzIAI', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-03T00:11:47.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000537msIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537zmIAA', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'Case Closed'}, {'id': '#a04Wt00000538O0IAI', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
