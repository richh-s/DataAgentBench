code = """import json
import pandas as pd

# Load Users
users_file = locals()['var_function-call-8651648157017643766']
with open(users_file, 'r') as f:
    users_data = json.load(f)

# Extract and clean User IDs
# Remove leading # and trailing whitespace
valid_user_ids = set()
for u in users_data:
    raw_id = u.get('Id', '')
    if raw_id:
        clean_id = raw_id.strip().lstrip('#')
        valid_user_ids.add(clean_id)

# Load Case History
history_file = locals()['var_function-call-483118190896669373']
with open(history_file, 'r') as f:
    history_data = json.load(f)

# Define time window
start_date = '2022-04-10'
end_date = '2023-04-10'

handled_agents = set()
transfer_counts = {}

# We need to process history
# First pass: Identify all agents who handled cases (Handled Set)
# Second pass: Count transfers in window

for entry in history_data:
    # Clean IDs
    old_val = entry.get('oldvalue__c')
    new_val = entry.get('newvalue__c')
    
    # Check if None string or None type
    # Based on preview, it might be string "None" or null.
    # We treat anything not a valid user ID as None/System
    
    old_clean = None
    if old_val and isinstance(old_val, str):
        c = old_val.strip().lstrip('#')
        if c in valid_user_ids:
            old_clean = c
    
    new_clean = None
    if new_val and isinstance(new_val, str):
        c = new_val.strip().lstrip('#')
        if c in valid_user_ids:
            new_clean = c
            
    # Add to Handled Set
    if old_clean:
        handled_agents.add(old_clean)
    if new_clean:
        handled_agents.add(new_clean)

    # Check Date for Transfer Count
    created_date = entry.get('createddate', '')
    # Simple string comparison for ISO format works? 
    # createddate format: "2023-09-07T16:30:00.000+0000"
    # We can compare strings if format is consistent ISO.
    # "2022-04-10" vs "2023-09-..."
    # Let's use string comparison of first 10 chars (YYYY-MM-DD)
    
    if created_date:
        date_str = created_date[:10]
        if start_date <= date_str <= end_date:
            # It's in the window
            # If it's a transfer FROM an agent, increment count
            if old_clean:
                transfer_counts[old_clean] = transfer_counts.get(old_clean, 0) + 1

# Now we have Handled Set and Transfer Counts
# For agents in Handled Set but not in transfer_counts, count is 0.

results = []
for agent_id in handled_agents:
    count = transfer_counts.get(agent_id, 0)
    results.append({'Id': agent_id, 'count': count})

# Find Min
if not results:
    print("__RESULT__:")
    print(json.dumps("No agents handled cases"))
else:
    min_count = min(r['count'] for r in results)
    min_agents = [r['Id'] for r in results if r['count'] == min_count]
    
    # Sort for deterministic output if multiple
    min_agents.sort()
    
    print("__RESULT__:")
    print(json.dumps(min_agents))"""

env_args = {'var_function-call-10212791459466561092': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-8651648157017643766': 'file_storage/function-call-8651648157017643766.json', 'var_function-call-895613744430847647': [{'count': '165'}], 'var_function-call-483118190896669373': 'file_storage/function-call-483118190896669373.json'}

exec(code, env_args)
