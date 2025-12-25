code = """import json
import pandas as pd
from datetime import datetime

# Load case history
with open(locals()['var_function-call-9442101070801900645'], 'r') as f:
    history_data = json.load(f)

# Load case data
case_data = locals()['var_function-call-9442101070801902604']

# Clean IDs function
def clean_id(id_val):
    if not id_val: return None
    return str(id_val).strip().lstrip('#')

# Date parsing
def parse_date(date_str):
    # Format: 2023-09-07T16:30:00.000+0000
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        # Try without microseconds if needed
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")

start_date = datetime.strptime("2022-04-10T00:00:00+0000", "%Y-%m-%dT%H:%M:%S%z")
end_date = datetime.strptime("2023-04-10T23:59:59+0000", "%Y-%m-%dT%H:%M:%S%z")

handled_counts = {} # Agent ID -> Count (Incoming)
transfer_counts = {} # Agent ID -> Count (Outgoing)

# Process History
# Filter for 'Owner Assignment' and date range
# Also handle normalization
# history_data entries: id, caseid__c, oldvalue__c, newvalue__c, createddate, field__c

history_in_period = []
for entry in history_data:
    if entry.get('field__c') not in ['Owner Assignment', 'Owner']:
        continue
    
    d = parse_date(entry['createddate'])
    if start_date <= d <= end_date:
        history_in_period.append(entry)

# Sort history by date just in case
history_in_period.sort(key=lambda x: parse_date(x['createddate']))

processed_cases_initial = set()

for entry in history_in_period:
    old_val = clean_id(entry.get('oldvalue__c'))
    new_val = clean_id(entry.get('newvalue__c'))
    case_id = clean_id(entry.get('caseid__c'))
    
    # Check if old_val is None or string "None"
    if old_val == 'None' or old_val is None:
        # Initial Assignment
        if new_val:
            handled_counts[new_val] = handled_counts.get(new_val, 0) + 1
            processed_cases_initial.add(case_id)
    else:
        # Transfer
        # Outgoing from old_val
        transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
        # Incoming to new_val
        if new_val:
            handled_counts[new_val] = handled_counts.get(new_val, 0) + 1

# Process Case Data for missed Initial Assignments
# case_data entries: id, ownerid, createddate
for entry in case_data:
    case_id = clean_id(entry.get('id'))
    d = parse_date(entry['createddate'])
    
    # Only consider cases created in period for Initial Assignment counting
    if start_date <= d <= end_date:
        if case_id not in processed_cases_initial:
            # Need to determine Initial Owner
            # Check if this case has any transfer in history_in_period (where old != None)
            # If so, the first transfer's old_val is the Initial Owner.
            # But wait, if we iterated through history_in_period, we would have seen it?
            # Yes. But the 'processed_cases_initial' set only tracks explicit 'None'->'User' transitions.
            # If the history lacks 'None'->'User' but has 'UserA'->'UserB', then UserA was initial.
            # However, I need to know IF I already counted UserA.
            # In the loop above:
            # If I saw 'UserA'->'UserB', I incremented handled_counts[UserB] and transfer_counts[UserA].
            # Did I increment handled_counts[UserA] (Initial)? NO.
            # So I need to catch this case here.
            
            # Find first transfer for this case in history (even if not in period? No, if created in period, first transfer must be >= created >= start).
            # I can't easily search `history_in_period` again efficiently without indexing.
            # Let's re-scan or build an index? Or just assume `Case.ownerid` if no None->User history?
            
            # Actually, if there is a transfer A->B, then A was initial.
            # I need to find A.
            # Case table `ownerid` is the CURRENT owner (likely B or C).
            # So I cannot use `Case.ownerid`.
            
            # Solution: Build a map of first_transfer_from for cases.
            pass

# Let's rebuild the logic slightly to be robust.
# 1. Collect all transfers (old!=None) in period by Case ID.
# 2. Collect all initial assignments (old=None) in period by Case ID.
# 3. For each Case created in period:
#    - If in (2): Initial Owner = new_val. Handled(Initial Owner) += 1.
#    - Else If in (1): Initial Owner = old_val of earliest transfer. Handled(Initial Owner) += 1.
#    - Else: Initial Owner = Case.ownerid. Handled(Initial Owner) += 1.
# 4. For all transfers in (1):
#    - Transfer(old_val) += 1.
#    - Handled(new_val) += 1.

# Re-run counters
handled_counts = {}
transfer_counts = {}

# Index history
transfers_by_case = {} # case_id -> list of (date, old, new)
initials_by_case = {} # case_id -> (date, owner)

for entry in history_in_period:
    c_id = clean_id(entry.get('caseid__c'))
    o_val = clean_id(entry.get('oldvalue__c'))
    n_val = clean_id(entry.get('newvalue__c'))
    dt = parse_date(entry['createddate'])
    
    if o_val == 'None' or o_val is None:
        if c_id not in initials_by_case or dt < initials_by_case[c_id][0]:
            initials_by_case[c_id] = (dt, n_val)
    else:
        if c_id not in transfers_by_case:
            transfers_by_case[c_id] = []
        transfers_by_case[c_id].append((dt, o_val, n_val))

# Sort transfers
for c in transfers_by_case:
    transfers_by_case[c].sort(key=lambda x: x[0])

# Process "Handled" from Initial Assignments (Cases created in period)
for entry in case_data:
    c_id = clean_id(entry.get('id'))
    dt = parse_date(entry['createddate'])
    
    if start_date <= dt <= end_date:
        owner = None
        if c_id in initials_by_case:
            owner = initials_by_case[c_id][1]
        elif c_id in transfers_by_case:
            owner = transfers_by_case[c_id][0][1] # old_val of first transfer
        else:
            owner = clean_id(entry.get('ownerid'))
        
        if owner:
            handled_counts[owner] = handled_counts.get(owner, 0) + 1

# Process "Handled" from Incoming Transfers (in period)
# Process "Transfer Count" from Outgoing Transfers (in period)
# This comes from the history list directly (since we filtered by date already)
for entry in history_in_period:
    o_val = clean_id(entry.get('oldvalue__c'))
    n_val = clean_id(entry.get('newvalue__c'))
    
    if o_val != 'None' and o_val is not None:
        # Outgoing
        transfer_counts[o_val] = transfer_counts.get(o_val, 0) + 1
        # Incoming
        if n_val:
            handled_counts[n_val] = handled_counts.get(n_val, 0) + 1

# Find agents with Handled > 0
candidates = [a for a, c in handled_counts.items() if c > 0]

# For candidates, get transfer count (default 0)
results = []
for agent in candidates:
    tc = transfer_counts.get(agent, 0)
    results.append({'id': agent, 'transfer_count': tc})

# Sort by transfer count (asc)
results.sort(key=lambda x: x['transfer_count'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16532689106221558856': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-9442101070801900645': 'file_storage/function-call-9442101070801900645.json', 'var_function-call-9442101070801902604': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-04-15T09:30:00.000+0000'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-09-06T11:15:00.000+0000'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2023-09-04T14:20:00.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO', 'createddate': '2023-09-05T10:15:00.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}]}

exec(code, env_args)
