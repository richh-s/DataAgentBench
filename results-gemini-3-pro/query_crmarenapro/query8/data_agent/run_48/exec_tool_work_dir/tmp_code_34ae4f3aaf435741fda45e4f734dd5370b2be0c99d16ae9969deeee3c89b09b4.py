code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-14770685575047062042'], 'r') as f:
    history_data = json.load(f)
with open(locals()['var_function-call-11360643150858883900'], 'r') as f:
    case_data = json.load(f)

# Dates
start_date = "2022-04-01"
end_date = "2023-03-31"

# Helper to parse date string (ISO format) and compare
# Dates in data: "2023-09-07T16:30:00.000+0000"
# We can use string comparison for YYYY-MM-DD if ISO format matches, but let's be robust
def in_range(date_str):
    if not date_str: return False
    # Use string slicing for YYYY-MM-DD
    d = date_str[:10]
    return start_date <= d <= end_date

# Filter history
history_filtered = [r for r in history_data if in_range(r.get('createddate'))]

# Filter cases
cases_filtered = [r for r in case_data if in_range(r.get('createddate'))]

# Clean ID function
def clean_id(i):
    if not i: return None
    if i == 'None': return None
    return i.lstrip('#')

# Identify agents who handled cases in the period
handled_agents = set()

# From History
for r in history_filtered:
    old = clean_id(r.get('oldvalue__c'))
    new = clean_id(r.get('newvalue__c'))
    if old: handled_agents.add(old)
    if new: handled_agents.add(new)

# From Cases (Initial assignment / Current owner of new cases)
for r in cases_filtered:
    owner = clean_id(r.get('ownerid'))
    if owner: handled_agents.add(owner)

# Calculate transfer counts (how many times agent is oldvalue__c)
transfer_counts = {agent: 0 for agent in handled_agents}

for r in history_filtered:
    old = clean_id(r.get('oldvalue__c'))
    if old and old in transfer_counts:
        transfer_counts[old] += 1

# Find min transfers
if not transfer_counts:
    result = "No agents found"
else:
    min_transfers = min(transfer_counts.values())
    candidates = [a for a, c in transfer_counts.items() if c == min_transfers]
    result = {"min_transfers": min_transfers, "candidates": candidates}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8945435299677273893': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4371058042737837782': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-3765472477778977412': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10721788631355263215': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14770685575047062042': 'file_storage/function-call-14770685575047062042.json', 'var_function-call-11360643150858883900': 'file_storage/function-call-11360643150858883900.json'}

exec(code, env_args)
