code = """import json
import pandas as pd
from datetime import datetime

# Load data
closed_cases_raw = locals()['var_function-call-13083223580502144905']
history_path = locals()['var_function-call-10307824699368594110']

with open(history_path, 'r') as f:
    history_raw = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if not i: return i
    return i.replace('#', '')

# Parse dates
def parse_date(d):
    # Format: 2023-07-01T10:30:00.000+0000
    try:
        return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        return datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z") # Fallback

# Define Window
window_start = parse_date("2023-05-02T00:00:00.000+0000")
window_end = parse_date("2023-09-02T23:59:59.999+0000")

# Process Closed Cases
closed_cases = []
for c in closed_cases_raw:
    cid = clean_id(c['id'])
    oid = clean_id(c['ownerid'])
    created = parse_date(c['createddate'])
    closed = parse_date(c['closeddate'])
    
    # Calculate Handle Time (seconds or minutes?)
    # "duration taken to close a case"
    # Let's use seconds for precision, then avg.
    duration = (closed - created).total_seconds()
    
    closed_cases.append({
        'id': cid,
        'owner_id': oid,
        'handle_time': duration,
        'closed_date': closed
    })

# Process Managed Cases (Agents processing cases in window)
# We track which cases each agent "processed" in the window.
# Processing = Assigned (in window) OR Closing (in window).
# Actually, if assigned before and closed after, they processed it in window.
# But we only have assignment date and close date.
# We will count a case for an agent if:
# 1. Agent was assigned the case IN the window.
# 2. Agent closed the case IN the window.
# 3. Agent was the owner during the window? (If assigned before and not closed or closed in window).
# Given the data, we can look at history assignments in window.

agent_managed_cases = {} # agent_id -> set of case_ids

# 1. From History (Assignments in window)
for h in history_raw:
    h_date = parse_date(h['createddate'])
    if window_start <= h_date <= window_end:
        # Agent assigned (new value)
        new_agent = clean_id(h['newvalue__c'])
        cid = clean_id(h['caseid__c'])
        if new_agent and new_agent != 'None':
            if new_agent not in agent_managed_cases: agent_managed_cases[new_agent] = set()
            agent_managed_cases[new_agent].add(cid)
        
        # Agent transferred from (old value) - did they process it in window?
        # Yes, they handed it off.
        old_agent = clean_id(h['oldvalue__c'])
        if old_agent and old_agent != 'None':
            if old_agent not in agent_managed_cases: agent_managed_cases[old_agent] = set()
            agent_managed_cases[old_agent].add(cid)

# 2. From Closed Cases (Closing in window)
for c in closed_cases:
    agent = c['owner_id']
    cid = c['id']
    if agent not in agent_managed_cases: agent_managed_cases[agent] = set()
    agent_managed_cases[agent].add(cid)

# Calculate Stats
agent_stats = []

for agent, cases in agent_managed_cases.items():
    managed_count = len(cases)
    
    # Calculate Avg Handle Time for cases CLOSED by this agent in the window
    # Filter closed_cases for this agent
    agent_closed = [x for x in closed_cases if x['owner_id'] == agent]
    
    if agent_closed:
        avg_ht = sum(x['handle_time'] for x in agent_closed) / len(agent_closed)
        agent_stats.append({
            'agent_id': agent,
            'managed_count': managed_count,
            'avg_handle_time': avg_ht,
            'closed_count': len(agent_closed)
        })

# Filter and Find Min
filtered_stats = [x for x in agent_stats if x['managed_count'] > 1]
filtered_stats.sort(key=lambda x: x['avg_handle_time'])

print("__RESULT__:")
print(json.dumps(filtered_stats))"""

env_args = {'var_function-call-16719493468663396395': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13083223580502144905': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-16547132494700792091': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5431925037286751549': [{'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}], 'var_function-call-10709049619401092256': [{'count': '165'}], 'var_function-call-10307824699368594110': 'file_storage/function-call-10307824699368594110.json'}

exec(code, env_args)
