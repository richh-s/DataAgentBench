code = """import json
import datetime

# Load data
cases_path = locals()['var_function-call-12694135486162102069'] # File path
with open(cases_path, 'r') as f:
    cases = json.load(f)

history_path = locals()['var_function-call-17758410668140452546'] # File path
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

today = datetime.datetime(2023, 9, 2, tzinfo=datetime.timezone.utc)
start_date = datetime.datetime(2023, 5, 2, tzinfo=datetime.timezone.utc)

def parse_date(d_str):
    if not d_str or d_str == 'None': return None
    try:
        dt = datetime.datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        return dt
    except ValueError:
        try:
             dt = datetime.datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z")
             return dt
        except:
             return None

all_cases_map = {}
for c in cases:
    c_id = clean_id(c['id'])
    closed = parse_date(c['closeddate'])
    created = parse_date(c['createddate'])
    owner = clean_id(c['ownerid'])
    
    all_cases_map[c_id] = {
        'id': c_id,
        'created': created,
        'closed': closed,
        'final_owner': owner,
        'owners': {owner} if owner else set()
    }

for h in history:
    if h.get('field__c') == 'Owner Assignment':
        c_id = clean_id(h['caseid__c'])
        if c_id in all_cases_map:
            new_owner = clean_id(h['newvalue__c'])
            old_owner = clean_id(h['oldvalue__c'])
            
            if new_owner and new_owner != 'None':
                all_cases_map[c_id]['owners'].add(new_owner)
            if old_owner and old_owner != 'None':
                all_cases_map[c_id]['owners'].add(old_owner)

agent_stats = {}

# Initialize
for info in all_cases_map.values():
    for o in info['owners']:
        if o not in agent_stats:
            agent_stats[o] = {'managed_total': 0, 'aht_sum': 0, 'aht_count': 0}

# Count Managed
for info in all_cases_map.values():
    for o in info['owners']:
        agent_stats[o]['managed_total'] += 1

# Compute AHT
for info in all_cases_map.values():
    closed = info['closed']
    created = info['created']
    owners = info['owners']
    
    if closed and created and start_date <= closed <= today:
        if len(owners) == 1:
            owner = list(owners)[0]
            duration = (closed - created).total_seconds()
            if owner in agent_stats:
                agent_stats[owner]['aht_sum'] += duration
                agent_stats[owner]['aht_count'] += 1

eligible_agents = []
for agent, stats in agent_stats.items():
    if stats['managed_total'] > 1:
        if stats['aht_count'] > 0:
            avg_time = stats['aht_sum'] / stats['aht_count']
            eligible_agents.append({
                'id': agent,
                'avg_time': avg_time,
                'managed_total': stats['managed_total']
            })

eligible_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-11983403154172027239': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7858578306868479509': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-17758410668140452546': 'file_storage/function-call-17758410668140452546.json', 'var_function-call-16680084720488788894': [], 'var_function-call-3535784194785594371': {'num_filtered_cases': 7, 'agent_stats': {'005Wt000003NJufIAG': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NJGLIA4': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NDqDIAW': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NJD9IAO': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NEtOIAW': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NJJaIAO': {'managed_count': 1, 'handled_count': 1}, '005Wt000003NIddIAG': {'managed_count': 1, 'handled_count': 1}}}, 'var_function-call-12694135486162102069': 'file_storage/function-call-12694135486162102069.json'}

exec(code, env_args)
