code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-4761739676269309166'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-4045250952106322466'], 'r') as f:
    history = json.load(f)

# Date range
start_date = pd.Timestamp("2022-04-01", tz="UTC")
end_date = pd.Timestamp("2023-03-31", tz="UTC")

# Helper to clean ID
def clean_id(i):
    if i is None or i == "None":
        return None
    s = str(i).strip()
    if not s:
        return None
    return s

# Identify Active Agents (Handled > 0 cases)
active_agents = set()

# 1. From Case table (current owners of cases active in period)
for c in cases:
    # Parse dates
    try:
        c_create = pd.Timestamp(c['createddate'])
    except:
        continue
    
    c_close = None
    if c['closeddate'] and c['closeddate'] != "None":
        try:
            c_close = pd.Timestamp(c['closeddate'])
        except:
            pass
            
    # Check overlap
    # Case interval: [c_create, c_close or infinite]
    # Period: [start_date, end_date]
    
    # Logic: Overlap if not (End < Start OR Start > End)
    # Case ends before period starts?
    if c_close is not None and c_close < start_date:
        continue
    # Case starts after period ends?
    if c_create > end_date:
        continue
        
    # Overlap exists
    # The current owner handled it (at least currently or recently).
    # If the case has history, the current owner might have received it later.
    # But if they are the current owner of an active case, they are "handling" it.
    oid = clean_id(c['ownerid'])
    if oid:
        active_agents.add(oid)

# 2. From History (agents involved in transfers in period)
transfer_counts = {}

for h in history:
    try:
        h_date = pd.Timestamp(h['createddate'])
    except:
        continue
        
    # Check if in period
    if start_date <= h_date <= end_date:
        if h['field__c'] in ["Owner Assignment", "Owner"]:
            old_v = clean_id(h['oldvalue__c'])
            new_v = clean_id(h['newvalue__c'])
            
            # If in period, both handled the case
            if old_v:
                active_agents.add(old_v)
            if new_v:
                active_agents.add(new_v)
                
            # Count Transfer for OLD value
            if old_v:
                transfer_counts[old_v] = transfer_counts.get(old_v, 0) + 1

# Filter active_agents to exclude None
active_agents = {a for a in active_agents if a is not None}

# Calculate min transfers
min_transfers = float('inf')
candidates = []

for agent in active_agents:
    count = transfer_counts.get(agent, 0)
    if count < min_transfers:
        min_transfers = count
        candidates = [agent]
    elif count == min_transfers:
        candidates.append(agent)

# Sort candidates to be deterministic
candidates.sort()

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-6749587193675572085': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-181915633783256925': 'file_storage/function-call-181915633783256925.json', 'var_function-call-4045250952106322466': 'file_storage/function-call-4045250952106322466.json', 'var_function-call-4761739676269309166': 'file_storage/function-call-4761739676269309166.json'}

exec(code, env_args)
