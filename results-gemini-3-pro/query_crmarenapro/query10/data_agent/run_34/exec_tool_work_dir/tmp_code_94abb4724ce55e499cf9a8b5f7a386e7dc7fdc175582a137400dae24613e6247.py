code = """import json
import pandas as pd
from datetime import datetime

# Load previous results
cases = locals()['var_function-call-10030256816200420512']
history_file = locals()['var_function-call-5672048893223626647']

with open(history_file, 'r') as f:
    history = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

# Filter dates
start_date = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_date = pd.Timestamp('2023-09-02').tz_localize('UTC') # End of day? usually inclusive. 
# Prompt says "Today's date: 2023-09-02". Usually means until now.
# I'll include the whole day of 2023-09-02 if needed, but timestamps in result have time.
# I'll assume strictly <= 2023-09-02 23:59:59 or just compare dates.
# Let's use strict timestamp comparison if available.
# Actually, if I just compare dates, it's safer.

# Process Cases
valid_cases = []
for c in cases:
    # Clean ID
    c['id'] = clean_id(c['id'])
    c['ownerid'] = clean_id(c['ownerid'])
    
    # Parse dates
    # Format: "2023-09-30T11:30:00.000+0000"
    # pd.to_datetime handles ISO mixed formats well
    closed_dt = pd.to_datetime(c['closeddate'])
    created_dt = pd.to_datetime(c['createddate'])
    
    # Check window
    # Window: past 4 months from 2023-09-02.
    # Start: 2023-05-02. End: 2023-09-02.
    if start_date <= closed_dt <= end_date + pd.Timedelta(days=1): # Include 9-02
        # Actually end_date is 2023-09-02 00:00:00 UTC.
        # If I want to include events on 2023-09-02, I should go up to 2023-09-03 00:00:00 (exclusive)
        # or use date() comparison.
        if start_date.date() <= closed_dt.date() <= end_date.date():
            c['closed_dt'] = closed_dt
            c['created_dt'] = created_dt
            c['duration'] = (closed_dt - created_dt).total_seconds()
            valid_cases.append(c)

# Build History Map
# Map case_id -> list of owners
case_owners_map = {}
# Filter history for "Owner Assignment" is already done in query
for h in history:
    cid = clean_id(h['caseid__c'])
    new_owner = clean_id(h['newvalue__c'])
    if cid not in case_owners_map:
        case_owners_map[cid] = []
    case_owners_map[cid].append(new_owner)

# Agent Stats
agent_stats = {} # { agent_id: { 'processed_count': 0, 'handle_times': [] } }

for c in valid_cases:
    cid = c['id']
    
    # Determine owners from history
    # If no history, assume Case.ownerid
    history_owners = case_owners_map.get(cid, [])
    
    if not history_owners:
        # No history found. Assume single owner = current owner
        owners = [c['ownerid']]
        is_transferred = False
    else:
        # Have history.
        # "For cases that have NOT been transferred ... only ONE 'Owner Assignment'"
        # Check count of history entries
        # My history list contains *entries*.
        # Count entries
        count_assignments = len(history_owners)
        owners = list(set(history_owners)) # Unique owners
        if count_assignments > 1:
            is_transferred = True
        else:
            is_transferred = False
            
    # Update Agent Stats
    for agent in owners:
        if agent not in agent_stats:
            agent_stats[agent] = {'processed_count': 0, 'handle_times': []}
        
        agent_stats[agent]['processed_count'] += 1
        
        if not is_transferred:
            # Only single owner gets handle time
            # And only if this agent is that owner (should be true if not transferred)
            # Just to be safe:
            # If not transferred, owners list has 1 element.
            agent_stats[agent]['handle_times'].append(c['duration'])

# Calculate Results
results = []
for agent, stats in agent_stats.items():
    if stats['processed_count'] > 1:
        # Avg Handle Time
        # Only consider valid handle times (non-transferred cases)
        # If no non-transferred cases, avg is undefined.
        # "lowest average handle time". Undefined is not a number.
        # Maybe exclude?
        if len(stats['handle_times']) > 0:
            avg_time = sum(stats['handle_times']) / len(stats['handle_times'])
            results.append({
                'agent_id': agent,
                'avg_time': avg_time,
                'processed_count': stats['processed_count'],
                'valid_time_count': len(stats['handle_times'])
            })

# Sort by avg_time
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3625916449941540232': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10030256816200420512': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-16441387585647630656': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-5672048893223626647': 'file_storage/function-call-5672048893223626647.json'}

exec(code, env_args)
