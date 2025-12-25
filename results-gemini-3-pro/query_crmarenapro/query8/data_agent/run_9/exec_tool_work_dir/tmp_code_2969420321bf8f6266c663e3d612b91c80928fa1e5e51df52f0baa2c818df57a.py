code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-9224824487569700459'], 'r') as f:
    history = json.load(f)

# Parameters
end_date = datetime(2023, 4, 10)
start_date = datetime(2022, 4, 10)

agent_handled = {}
agent_transferred = {}

for record in history:
    # Parse date
    # Format: 2023-09-07T16:30:00.000+0000
    # Python isoformat might handle it, or strptime
    # +0000 is UTC.
    cdate_str = record['createddate']
    # Simplified parsing: first 19 chars are YYYY-MM-DDTHH:MM:SS
    # Ignore timezone for simplicity or handle it if needed. Assuming UTC or consistent.
    # The prompt implies a date comparison.
    try:
        dt = datetime.strptime(cdate_str[:19], "%Y-%m-%dT%H:%M:%S")
    except:
        continue

    if start_date <= dt <= end_date:
        # Clean IDs
        old_val = record['oldvalue__c']
        new_val = record['newvalue__c']
        
        if old_val:
            old_val = old_val.strip().lstrip('#')
        if new_val:
            new_val = new_val.strip().lstrip('#')
            
        # Count Handled (Received Assignment)
        # newvalue__c is the agent receiving assignment (or initial)
        if new_val and new_val != 'None':
            agent_handled[new_val] = agent_handled.get(new_val, 0) + 1
            
        # Count Transferred (Sent Assignment)
        # oldvalue__c is the agent transferring out
        if old_val and old_val != 'None':
            agent_transferred[old_val] = agent_transferred.get(old_val, 0) + 1

# Filter agents with handled > 0
eligible_agents = []
for agent, count in agent_handled.items():
    if count > 0:
        t_count = agent_transferred.get(agent, 0)
        eligible_agents.append({'id': agent, 'handled': count, 'transferred': t_count})

# Sort by transferred ASC
eligible_agents.sort(key=lambda x: x['transferred'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-14614809315977098220': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1916479405294806639': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4651257634675235691': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005389SIAQ', 'caseid__c': '500Wt00000DDfvXIAT', 'oldvalue__c': '005Wt000003NHg0IAG', 'newvalue__c': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T20:27:15.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538NzIAI', 'caseid__c': '500Wt00000DDz6FIAT', 'oldvalue__c': '005Wt000003NDqFIAW', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T13:07:23.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538m9IAA', 'caseid__c': '500Wt00000DDYpGIAX', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T13:52:45.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000539blIAA', 'caseid__c': '500Wt00000DDTERIA5', 'oldvalue__c': '005Wt000003NJ6fIAG', 'newvalue__c': '005Wt000003NIk5IAG', 'createddate': '2022-03-10T11:37:09.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-8419406847472328550': [{'count': '165'}], 'var_function-call-9224824487569700459': 'file_storage/function-call-9224824487569700459.json'}

exec(code, env_args)
