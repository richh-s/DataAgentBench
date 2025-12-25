code = """import json
import pandas as pd

# Load data
cases_file = locals()['var_function-call-15614097303451671276']
history_file = locals()['var_function-call-5672048893223626647']

with open(cases_file, 'r') as f:
    all_cases = json.load(f)

with open(history_file, 'r') as f:
    history = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

# Build History Map (Case -> List of Owners)
case_owners_map = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    new_owner = clean_id(h['newvalue__c'])
    if cid not in case_owners_map:
        case_owners_map[cid] = []
    case_owners_map[cid].append(new_owner)

# Global Processed Counts
agent_global_counts = {}

for c in all_cases:
    cid = clean_id(c['id'])
    
    # Owners
    history_owners = case_owners_map.get(cid, [])
    if not history_owners:
        owners = [clean_id(c['ownerid'])]
    else:
        owners = list(set(history_owners))
        
    for agent in owners:
        agent_global_counts[agent] = agent_global_counts.get(agent, 0) + 1

# Window Analysis
start_date = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_date = pd.Timestamp('2023-09-02').tz_localize('UTC')

agent_window_times = {} # { agent: [times] }

valid_cases_count = 0

for c in all_cases:
    if not c['closeddate'] or c['closeddate'] == 'None':
        continue
        
    closed_dt = pd.to_datetime(c['closeddate'])
    
    # Check window
    if start_date.date() <= closed_dt.date() <= end_date.date():
        valid_cases_count += 1
        cid = clean_id(c['id'])
        created_dt = pd.to_datetime(c['createddate'])
        duration = (closed_dt - created_dt).total_seconds()
        
        # Check Transfer Status
        history_owners = case_owners_map.get(cid, [])
        # Transferred if > 1 history assignment
        # Or if history exists and count > 1?
        # Use previous logic: len(history_owners) > 1 -> Transferred.
        # If len == 1 -> Not Transferred.
        # If len == 0 -> Not Transferred.
        
        is_transferred = False
        if len(history_owners) > 1:
            is_transferred = True
            
        if not is_transferred:
            # Single owner. Identify owner.
            if history_owners:
                owner = history_owners[0]
            else:
                owner = clean_id(c['ownerid'])
            
            # Add time
            if owner not in agent_window_times:
                agent_window_times[owner] = []
            agent_window_times[owner].append(duration)

# Filter and Calculate
results = []
for agent, times in agent_window_times.items():
    global_count = agent_global_counts.get(agent, 0)
    
    # Condition: processing more than one case (Global count > 1)
    if global_count > 1:
        avg_time = sum(times) / len(times)
        results.append({
            'agent_id': agent,
            'avg_time': avg_time,
            'global_count': global_count,
            'window_count': len(times)
        })

results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3625916449941540232': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10030256816200420512': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-16441387585647630656': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-5672048893223626647': 'file_storage/function-call-5672048893223626647.json', 'var_function-call-7921439147809233110': [], 'var_function-call-15421145515916435414': {'valid_cases_count': 7, 'agent_stats_keys': ['005Wt000003NJufIAG', '005Wt000003NJGLIA4', '005Wt000003NDqDIAW', '005Wt000003NJD9IAO', '005Wt000003NEtOIAW', '005Wt000003NJJaIAO', '005Wt000003NIddIAG'], 'sample_stats': [{'processed_count': 1, 'handle_times': [33068.0]}, {'processed_count': 1, 'handle_times': [1442.0]}, {'processed_count': 1, 'handle_times': [882.0]}], 'debug_cases': [{'id': '500Wt00000DDepmIAD', 'owners': ['005Wt000003NJufIAG'], 'is_transferred': False, 'owners_source': 'History'}, {'id': '500Wt00000DDyzpIAD', 'owners': ['005Wt000003NJGLIA4'], 'is_transferred': False, 'owners_source': 'History'}, {'id': '500Wt00000DDzUPIA1', 'owners': ['005Wt000003NDqDIAW'], 'is_transferred': False, 'owners_source': 'History'}, {'id': '500Wt00000DDzsbIAD', 'owners': ['005Wt000003NJD9IAO'], 'is_transferred': False, 'owners_source': 'History'}, {'id': '500Wt00000DDzscIAD', 'owners': ['005Wt000003NEtOIAW'], 'is_transferred': False, 'owners_source': 'History'}]}, 'var_function-call-15614097303451671276': 'file_storage/function-call-15614097303451671276.json'}

exec(code, env_args)
