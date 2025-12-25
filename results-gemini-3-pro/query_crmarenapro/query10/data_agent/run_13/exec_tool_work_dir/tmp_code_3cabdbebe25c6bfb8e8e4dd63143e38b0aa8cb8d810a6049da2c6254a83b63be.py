code = """import json
import pandas as pd

# Load previous data
cases_file = locals()['var_function-call-682345438020800525']
history_file = locals()['var_function-call-4362075390909810117']

with open(cases_file, 'r') as f:
    cases_data = json.load(f)
with open(history_file, 'r') as f:
    history_data = json.load(f)

agent_id = "005Wt000003NJGLIA4"
# Also check similar IDs just in case of corruption
agent_id_clean = agent_id.strip()

print(f"Checking agent: {agent_id_clean}")

# Find cases owned by agent
owned_cases = []
for c in cases_data:
    if str(c.get('ownerid')).strip().lstrip('#') == agent_id_clean:
        owned_cases.append(c)

print(f"Owned cases: {len(owned_cases)}")
for c in owned_cases:
    print(f"  {c['id']} - Created: {c['createddate']}, Closed: {c['closeddate']}")

# Find history involving agent
involved_history = []
for h in history_data:
    if str(h.get('newvalue__c')).strip().lstrip('#') == agent_id_clean or \
       str(h.get('oldvalue__c')).strip().lstrip('#') == agent_id_clean:
        involved_history.append(h)

print(f"History entries: {len(involved_history)}")
for h in involved_history:
    print(f"  Case: {h['caseid__c']}, Old: {h['oldvalue__c']}, New: {h['newvalue__c']}")

# Check if history cases are active in window
# Window: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp("2023-05-02", tz="UTC")
end_date = pd.Timestamp("2023-09-02", tz="UTC")

processed_active_cases = set()

def is_active(c):
    # Parse dates
    try:
        created = pd.to_datetime(c['createddate'])
        if created.tzinfo is None: created = created.tz_localize('UTC')
        
        closed = c['closeddate']
        if closed and str(closed).lower() != 'none':
            closed = pd.to_datetime(closed)
            if closed.tzinfo is None: closed = closed.tz_localize('UTC')
        else:
            closed = None
    except:
        return False
        
    if created > end_date: return False
    if closed is None: return True
    if closed >= start_date: return True
    return False

# Build map of all cases to check activity
case_map = {str(c['id']).strip().lstrip('#'): c for c in cases_data}

# Check owned cases
for c in owned_cases:
    cid = str(c['id']).strip().lstrip('#')
    if is_active(c):
        print(f"  Owned Case {cid} is ACTIVE")
        processed_active_cases.add(cid)
    else:
        print(f"  Owned Case {cid} is NOT ACTIVE")

# Check history cases
for h in involved_history:
    cid = str(h['caseid__c']).strip().lstrip('#')
    if cid in case_map:
        if is_active(case_map[cid]):
             print(f"  History Case {cid} is ACTIVE")
             processed_active_cases.add(cid)
        else:
             print(f"  History Case {cid} is NOT ACTIVE")
    else:
        print(f"  History Case {cid} NOT FOUND in cases")

print(f"Total processed active cases: {len(processed_active_cases)}")
print("__RESULT__:")
print(json.dumps(list(processed_active_cases)))"""

env_args = {'var_function-call-13889925607589652212': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-4362075390909812662': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4362075390909810117': 'file_storage/function-call-4362075390909810117.json', 'var_function-call-11505706217797150176': [], 'var_function-call-5544576152632122422': [{'count': '153'}], 'var_function-call-682345438020800525': 'file_storage/function-call-682345438020800525.json', 'var_function-call-14672251454872513663': [{'agent': '005Wt000003NDqDIAW', 'avg_time': 882.0, 'processed': 3, 'closed': 1}, {'agent': '005Wt000003NEtOIAW', 'avg_time': 1007.0, 'processed': 2, 'closed': 1}, {'agent': '005Wt000003NIddIAG', 'avg_time': 2194.0, 'processed': 2, 'closed': 1}, {'agent': '005Wt000003NJJaIAO', 'avg_time': 14712.0, 'processed': 2, 'closed': 1}, {'agent': '005Wt000003NJD9IAO', 'avg_time': 21608.0, 'processed': 2, 'closed': 1}, {'agent': '005Wt000003NJufIAG', 'avg_time': 33068.0, 'processed': 2, 'closed': 1}]}

exec(code, env_args)
