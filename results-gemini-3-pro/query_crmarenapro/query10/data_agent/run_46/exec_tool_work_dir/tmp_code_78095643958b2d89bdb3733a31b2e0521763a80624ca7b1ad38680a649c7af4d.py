code = """import json
import pandas as pd
from dateutil import parser

# Load data
with open(locals()['var_function-call-12752173730338651938'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-5158981950458698748'], 'r') as f:
    history = json.load(f)

# Helper to clean ID
def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

# Process Cases
valid_cases = []
start_date = pd.Timestamp("2023-05-02").replace(tzinfo=pd.Timestamp("2023-05-02T00:00:00+0000").tzinfo) # Approximate UTC handling
end_date = pd.Timestamp("2023-09-02").replace(tzinfo=pd.Timestamp("2023-09-02T00:00:00+0000").tzinfo)

filtered_cases = []
for c in cases:
    c['id'] = clean_id(c['id'])
    c['ownerid'] = clean_id(c['ownerid'])
    
    # Date filtering
    if not c['closeddate'] or c['closeddate'] == 'None':
        continue
    
    try:
        closed = pd.to_datetime(c['closeddate'])
        created = pd.to_datetime(c['createddate'])
    except:
        continue
        
    # Check range (using isoformat string compare or datetime objects)
    # The timestamps in JSON are like "2023-09-30T16:03:45.000+0000"
    # pd.to_datetime handles them.
    
    # We need to ensure tz awareness consistency.
    # The timestamps have offset +0000.
    
    if start_date <= closed <= end_date:
        duration = (closed - created).total_seconds()
        c['duration_seconds'] = duration
        filtered_cases.append(c)

# Process History
case_owners_history = {} # case_id -> list of owner_ids
case_transfer_counts = {} # case_id -> count of 'Owner Assignment'

for h in history:
    h['caseid__c'] = clean_id(h['caseid__c'])
    if h['field__c'] == 'Owner Assignment':
        cid = h['caseid__c']
        case_transfer_counts[cid] = case_transfer_counts.get(cid, 0) + 1
        
        # Collect owners
        # NewValue is the new owner.
        # OldValue might be previous.
        new_own = clean_id(h['newvalue__c'])
        old_own = clean_id(h['oldvalue__c'])
        
        if cid not in case_owners_history:
            case_owners_history[cid] = set()
        
        if new_own and new_own != 'None':
            case_owners_history[cid].add(new_own)
        if old_own and old_own != 'None':
            case_owners_history[cid].add(old_own)

# Agent Stats
agent_stats = {} # agent_id -> {'processed_count': 0, 'handle_times': []}

for c in filtered_cases:
    cid = c['id']
    
    # Determine Owners
    owners = set()
    # Add current owner
    if c['ownerid']:
        owners.add(c['ownerid'])
    # Add history owners
    if cid in case_owners_history:
        owners.update(case_owners_history[cid])
        
    # Determine if Transferred
    # Rule: > 1 'Owner Assignment' entries implies transferred.
    # However, missing history (count=0) -> Not Transferred.
    # count=1 -> Not Transferred.
    transfer_count = case_transfer_counts.get(cid, 0)
    is_transferred = transfer_count > 1
    
    # Update Stats
    for agent in owners:
        if agent not in agent_stats:
            agent_stats[agent] = {'processed_count': 0, 'handle_times': []}
        
        agent_stats[agent]['processed_count'] += 1
        
        if not is_transferred:
            # Only attribute handle time if NOT transferred AND this agent is the owner
            # If not transferred, there should be only 1 owner in the set effectively (or the history matches current).
            # If there's 1 assignment, the owner in history should match current.
            # So if agent is in owners, and is_transferred is False, they get the credit.
            agent_stats[agent]['handle_times'].append(c['duration_seconds'])

# Calculate Averages and Filter
results = []
for agent, stats in agent_stats.items():
    if stats['processed_count'] > 1:
        if len(stats['handle_times']) > 0:
            avg_time = sum(stats['handle_times']) / len(stats['handle_times'])
            results.append({'agent': agent, 'avg_time': avg_time, 'count': stats['processed_count']})

# Sort
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13743909922389763632': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3568898558727432362': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer   '}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'status': 'Closed '}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'status': 'Closed'}], 'var_function-call-6990477605809042509': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10779346049285551617': [{'count': '393'}], 'var_function-call-8348757270633510177': [{'count': '153'}], 'var_function-call-12752173730338651938': 'file_storage/function-call-12752173730338651938.json', 'var_function-call-5158981950458698748': 'file_storage/function-call-5158981950458698748.json'}

exec(code, env_args)
