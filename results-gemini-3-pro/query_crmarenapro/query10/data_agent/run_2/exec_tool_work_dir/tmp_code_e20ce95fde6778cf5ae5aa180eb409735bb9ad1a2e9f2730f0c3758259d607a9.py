code = """import json
from datetime import datetime

# Load cases
cases_key = 'var_function-call-16296263846446172672' # The clean list of IDs? 
# Wait, I want the full case objects (createddate, closeddate, ownerid).
# The full case objects were in 'var_function-call-7634771961496327246'.
# But I need to re-read that because I didn't save the full objects in a handy file in previous step, 
# I only printed clean IDs. 
# However, I can read 'var_function-call-7634771961496327246' again.

cases_raw_key = 'var_function-call-7634771961496327246'
cases_raw = locals()[cases_raw_key]
if isinstance(cases_raw, str):
    with open(cases_raw, 'r') as f:
        cases_list = json.load(f)
else:
    cases_list = cases_raw

# Load history
history_key = 'var_function-call-10689379072275162428'
history_path = locals()[history_key]
with open(history_path, 'r') as f:
    history_list = json.load(f)

# Helper to clean ID
def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
        return i
    return i

# Process History
# Map case_id (clean) -> count of owner assignments
# Map case_id (clean) -> set of agents (clean)
case_assignments = {}
case_agents = {}

for h in history_list:
    if h.get('field__c') == 'Owner Assignment':
        cid = clean_id(h.get('caseid__c'))
        
        # Count assignments
        case_assignments[cid] = case_assignments.get(cid, 0) + 1
        
        # Track agents
        old_val = clean_id(h.get('oldvalue__c'))
        new_val = clean_id(h.get('newvalue__c'))
        
        if cid not in case_agents:
            case_agents[cid] = set()
        
        if old_val and old_val != 'None':
            case_agents[cid].add(old_val)
        if new_val and new_val != 'None':
            case_agents[cid].add(new_val)

# Process Cases
# We only care about the cases in our time window (cases_list)
# Calculate duration and assign to agents
agent_processed_cases = {} # agent_id -> set(case_ids)
agent_single_owner_times = {} # agent_id -> list of durations (seconds)

valid_case_ids = set()

for c in cases_list:
    cid = clean_id(c['id'])
    valid_case_ids.add(cid)
    owner = clean_id(c['ownerid'])
    
    # Calculate duration
    # Format: 2023-07-01T10:30:00.000+0000
    # Python 3.12 might handle ISO with timezone. 
    # If not, I'll strip simple.
    # The format seems to be ISO8601.
    created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    duration = (closed - created).total_seconds()
    
    # Identify if Single Owner
    # Check history count.
    # If case not in history, maybe count is 0? 
    # But if it has an owner, it must have at least 1 assignment?
    # Or maybe the history is incomplete? 
    # The hint says "For cases ... there will be only ONE 'Owner Assignment'".
    # So if it's missing from history, maybe it's 1 (initial)? Or 0?
    # I'll assume if it's in the DB, it should be in history if history tracks "Owner Assignment".
    # Wait, in the preview, every case seemed to have an entry where oldvalue="None".
    # So count should be >= 1.
    
    num_assigns = case_assignments.get(cid, 0)
    
    is_single_owner = (num_assigns == 1)
    
    # Determine agents involved
    # Agents involved are those in history AND the current owner (should be consistent).
    involved_agents = case_agents.get(cid, set())
    # Add current owner just in case
    involved_agents.add(owner)
    
    for agent in involved_agents:
        if agent not in agent_processed_cases:
            agent_processed_cases[agent] = set()
        agent_processed_cases[agent].add(cid)
        
    # If Single Owner, add duration to THAT owner's stats
    if is_single_owner:
        # Who is the single owner? The current owner.
        if owner not in agent_single_owner_times:
            agent_single_owner_times[owner] = []
        agent_single_owner_times[owner].append(duration)

# Filter Agents
results = []
for agent, cases in agent_processed_cases.items():
    if len(cases) > 1:
        # Eligible
        times = agent_single_owner_times.get(agent, [])
        if times:
            avg_time = sum(times) / len(times)
            results.append({'agent': agent, 'avg_time': avg_time, 'case_count': len(cases)})

# Find lowest
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9342110329570298783': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7634771961496327246': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4838252256481333369': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-16296263846446172672': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'var_function-call-10689379072275162428': 'file_storage/function-call-10689379072275162428.json'}

exec(code, env_args)
