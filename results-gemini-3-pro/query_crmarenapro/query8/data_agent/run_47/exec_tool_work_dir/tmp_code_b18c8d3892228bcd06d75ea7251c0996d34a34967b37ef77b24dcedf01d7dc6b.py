code = """import json
import pandas as pd
from datetime import datetime

# Load data
case_owners = locals()['var_function-call-10914459523618645131']
history_file = locals()['var_function-call-7382386176510000887']

with open(history_file, 'r') as f:
    history_data = json.load(f)

# Helper to clean IDs
def clean_id(id_val):
    if not id_val or id_val == 'None':
        return None
    s = str(id_val).strip()
    if s.startswith('#'):
        s = s[1:]
    return s if len(s) >= 15 else None # Salesforce IDs are 15 or 18 chars

# Collect all agents who handled > 0 cases
# Handled means: was ever an owner (current or past)
handled_agents = set()

# From current case owners
for rec in case_owners:
    aid = clean_id(rec.get('ownerid'))
    if aid and aid.startswith('005'):
        handled_agents.add(aid)

# From history
# We need to process history for both 'handled' set and 'transfer counts'
# Let's verify valid IDs first.

processed_history = []
for row in history_data:
    old = clean_id(row.get('oldvalue__c'))
    new = clean_id(row.get('newvalue__c'))
    created = row.get('createddate')
    
    # Add to handled set
    if old and old.startswith('005'):
        handled_agents.add(old)
    if new and new.startswith('005'):
        handled_agents.add(new)
        
    processed_history.append({
        'old': old,
        'new': new,
        'date': created
    })

# Define time range
start_date = pd.Timestamp("2022-04-10").tz_localize('UTC')
end_date = pd.Timestamp("2023-04-10").tz_localize('UTC')

# Count transfers
transfer_counts = {agent: 0 for agent in handled_agents}

for item in processed_history:
    # Check date
    # Format: "2023-09-07T16:30:00.000+0000"
    # pd.to_datetime handles this
    try:
        dt = pd.to_datetime(item['date'])
        # Ensure UTC
        if dt.tz is None:
            dt = dt.tz_localize('UTC')
        else:
            dt = dt.tz_convert('UTC')
            
        if start_date <= dt <= end_date:
            # Check if it is a transfer FROM an agent
            # "Each transfer from agent A to agent B adds to the transfer count for agent A."
            # So old must be an agent.
            old_agent = item['old']
            if old_agent and old_agent.startswith('005'):
                # Also, is it a transfer? Yes, field is Owner Assignment.
                # Does it matter who new is? "transfer ... to another".
                # If new is None, it's not a transfer to another. But Owner Assignment usually has a new owner.
                # If new is not an agent (e.g. queue), does it count?
                # "from one agent to another". This usually implies Agent to Agent.
                # However, "In the queries that specify... applies to both...".
                # Standard definition: Transfer is change of ownership.
                # "From agent A to agent B". This strictly means both must be agents.
                # If A transfers to Queue, is it a transfer count for A?
                # The prompt says: "Each transfer from agent A to agent B adds to the transfer count for agent A."
                # This suggests strict Agent-to-Agent.
                # Let's check if new is agent.
                new_agent = item['new']
                if new_agent and new_agent.startswith('005'):
                    if old_agent in transfer_counts:
                        transfer_counts[old_agent] += 1
    except Exception as e:
        pass

# Find min
min_count = float('inf')
min_agents = []

if not handled_agents:
    result = None
else:
    for agent, count in transfer_counts.items():
        if count < min_count:
            min_count = count
            min_agents = [agent]
        elif count == min_count:
            min_agents.append(agent)
            
    # If multiple, sort and pick first
    min_agents.sort()
    result = min_agents[0] if min_agents else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16460359147305820836': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10675659689436740879': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-10914459523618645131': [{'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '#005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NEzqIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NJcwIAG'}, {'ownerid': '005Wt000003NFhOIAW'}, {'ownerid': '005Wt000003NItlIAG'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '#005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NIfFIAW'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NHfyIAG'}, {'ownerid': '#005Wt000003NJoDIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '005Wt000003NJcvIAG'}, {'ownerid': '005Wt000003NJppIAG'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NJrRIAW'}, {'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NEGhIAO'}, {'ownerid': '#005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NDqFIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NEdKIAW'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NJQ1IAO'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NDsUIAW'}, {'ownerid': '005Wt000003NDJ1IAO'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NBykIAG'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '#005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NInJIAW'}, {'ownerid': '#005Wt000003NInLIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NIfHIAW'}, {'ownerid': '#005Wt000003NJUrIAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '005Wt000003NHGAIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIfFIAW'}, {'ownerid': '005Wt000003NIaQIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NINVIA4'}, {'ownerid': '005Wt000003NJ3RIAW'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '#005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '#005Wt000003NJcvIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIc2IAG'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NHfzIAG'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJoDIAW'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NGwpIAG'}, {'ownerid': '005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIliIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '#005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NEGhIAO'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NDXZIA4'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NHGAIA4'}], 'var_function-call-7382386176510000887': 'file_storage/function-call-7382386176510000887.json'}

exec(code, env_args)
