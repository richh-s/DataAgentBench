code = """import json
from datetime import datetime
rows = var_call_cKmJLkABNaL2p5ePDjUOPKv1

# Normalize and process
cases = []
for r in rows:
    case_id = r.get('case_id')
    created = r.get('createddate_str')
    closed = r.get('closeddate_str')
    # owner_assignment_count may be string
    try:
        owner_count = int(r.get('owner_assignment_count') or 0)
    except:
        owner_count = 0
    owners_history = r.get('owners_history')
    # Normalize owners_history to list
    if owners_history is None or owners_history == 'None':
        owners = []
    elif isinstance(owners_history, list):
        owners = [oh for oh in owners_history if oh]
    else:
        # try to parse if string representation of list
        s = str(owners_history)
        if s.startswith('[') and s.endswith(']'):
            try:
                owners = json.loads(s)
            except:
                owners = []
        else:
            owners = [s]
    case_owner = r.get('case_ownerid')
    # trim whitespace
    if isinstance(case_owner, str):
        case_owner = case_owner.strip()
    # parse datetimes
    try:
        created_dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f%z") if created else None
    except:
        try:
            created_dt = datetime.fromisoformat(created) if created else None
        except:
            created_dt = None
    try:
        closed_dt = datetime.strptime(closed, "%Y-%m-%dT%H:%M:%S.%f%z") if closed else None
    except:
        try:
            closed_dt = datetime.fromisoformat(closed) if closed else None
        except:
            closed_dt = None
    cases.append({
        'case_id': case_id,
        'created': created_dt,
        'closed': closed_dt,
        'owner_count': owner_count,
        'owners': [o.strip() for o in owners],
        'case_owner': case_owner
    })

# Count serviced cases per agent (includes involvement even if transferred)
from collections import defaultdict
serviced_counts = defaultdict(int)
for c in cases:
    involved = set()
    for o in c['owners']:
        if o:
            involved.add(o.strip())
    if c['case_owner']:
        involved.add(c['case_owner'].strip())
    for a in involved:
        serviced_counts[a] += 1

# Compute handle times (only for cases that were NOT transferred to other agents)
# According to policy, do not compute handle time for cases that have been transferred to other agents.
# Cases transferred have owner_count > 1. We'll include owner_count <= 1.
handle_times = defaultdict(list)
for c in cases:
    if c['owner_count'] > 1:
        continue
    if c['created'] is None or c['closed'] is None:
        continue
    duration = (c['closed'] - c['created']).total_seconds()
    owner = c['case_owner']
    if owner:
        handle_times[owner].append(duration)

# Filter agents who processed more than one case
candidates = {}
for agent, count in serviced_counts.items():
    if count > 1:
        # compute average handle time if agent has any handle times
        times = handle_times.get(agent, [])
        if times:
            avg = sum(times)/len(times)
            candidates[agent] = avg

# Find agent with lowest average handle time
if not candidates:
    result = None
else:
    best_agent = min(candidates.items(), key=lambda x: x[1])[0]
    result = best_agent

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_nvz4SefgTXJtiNT6BS3ngkZA': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_lyenWb5xfxPPHlobZTvJrG1J': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_cKmJLkABNaL2p5ePDjUOPKv1': [{'case_id': '#500Wt00000DDzscIAD', 'createddate_str': '2023-05-02T23:55:00.000+0000', 'closeddate_str': '2023-05-03T00:11:47.000+0000', 'owner_assignment_count': '0', 'owners_history': 'None', 'case_ownerid': '005Wt000003NEtOIAW'}, {'case_id': '#500Wt00000DE02HIAT', 'createddate_str': '2023-06-03T14:45:00.000+0000', 'closeddate_str': '2023-06-03T15:21:34.000+0000', 'owner_assignment_count': '0', 'owners_history': 'None', 'case_ownerid': '005Wt000003NIddIAG'}, {'case_id': '500Wt00000DDepmIAD', 'createddate_str': '2023-07-01T10:30:00.000+0000', 'closeddate_str': '2023-07-01T19:41:08.000+0000', 'owner_assignment_count': '1', 'owners_history': ['005Wt000003NJufIAG'], 'case_ownerid': '005Wt000003NJufIAG'}, {'case_id': '500Wt00000DDyzpIAD', 'createddate_str': '2023-08-15T14:30:00.000+0000', 'closeddate_str': '2023-08-15T14:54:02.000+0000', 'owner_assignment_count': '1', 'owners_history': ['005Wt000003NJGLIA4'], 'case_ownerid': '005Wt000003NJGLIA4'}, {'case_id': '500Wt00000DDzUPIA1', 'createddate_str': '2023-05-10T14:45:00.000+0000', 'closeddate_str': '2023-05-10T14:59:42.000+0000', 'owner_assignment_count': '1', 'owners_history': ['005Wt000003NDqDIAW'], 'case_ownerid': '005Wt000003NDqDIAW'}, {'case_id': '500Wt00000DDzsbIAD', 'createddate_str': '2023-06-30T13:03:00.000+0000', 'closeddate_str': '2023-06-30T19:03:08.000+0000', 'owner_assignment_count': '1', 'owners_history': ['005Wt000003NJD9IAO'], 'case_ownerid': '005Wt000003NJD9IAO'}, {'case_id': '500Wt00000DDzuEIAT', 'createddate_str': '2023-06-02T09:30:00.000+0000', 'closeddate_str': '2023-06-02T13:35:12.000+0000', 'owner_assignment_count': '1', 'owners_history': ['005Wt000003NJJaIAO'], 'case_ownerid': '005Wt000003NJJaIAO'}]}

exec(code, env_args)
