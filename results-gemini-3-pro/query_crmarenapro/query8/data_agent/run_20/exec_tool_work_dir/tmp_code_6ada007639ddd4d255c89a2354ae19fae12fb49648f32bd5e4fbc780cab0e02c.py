code = """import json

# Load Users
users_file = locals()['var_function-call-8651648157017643766']
with open(users_file, 'r') as f:
    users_data = json.load(f)

valid_user_ids = set()
for u in users_data:
    raw_id = u.get('Id', '')
    if raw_id:
        clean_id = raw_id.strip().lstrip('#')
        valid_user_ids.add(clean_id)

# Load History
history_file = locals()['var_function-call-483118190896669373']
with open(history_file, 'r') as f:
    history_data = json.load(f)

start_date = '2022-04-10'
end_date = '2023-04-10'

handled_in_period = set()
transfer_counts = {}

for entry in history_data:
    created_date = entry.get('createddate', '')[:10]
    
    # Check if entry is in period
    in_period = (start_date <= created_date <= end_date)
    
    old_val = entry.get('oldvalue__c')
    new_val = entry.get('newvalue__c')
    
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
    
    # If in period, add to handled set
    if in_period:
        if old_clean:
            handled_in_period.add(old_clean)
        if new_clean:
            handled_in_period.add(new_clean)
            
        # Count transfers
        if old_clean:
            transfer_counts[old_clean] = transfer_counts.get(old_clean, 0) + 1

# Calculate counts for handled agents
results = []
for agent_id in handled_in_period:
    count = transfer_counts.get(agent_id, 0)
    results.append({'Id': agent_id, 'count': count})

if not results:
    print("__RESULT__:")
    print(json.dumps("No agents handled cases in period"))
else:
    min_count = min(r['count'] for r in results)
    min_agents = [r['Id'] for r in results if r['count'] == min_count]
    min_agents.sort()
    
    print("__RESULT__:")
    print(json.dumps(min_agents))"""

env_args = {'var_function-call-10212791459466561092': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-8651648157017643766': 'file_storage/function-call-8651648157017643766.json', 'var_function-call-895613744430847647': [{'count': '165'}], 'var_function-call-483118190896669373': 'file_storage/function-call-483118190896669373.json', 'var_function-call-16800653331733781090': ['005Wt000003NBcAIAW', '005Wt000003NBykIAG', '005Wt000003NDJ1IAO', '005Wt000003NDXZIA4', '005Wt000003NDqDIAW', '005Wt000003NDqEIAW', '005Wt000003NDqFIAW', '005Wt000003NDsUIAW', '005Wt000003NDu7IAG', '005Wt000003NEGhIAO', '005Wt000003NEdKIAW', '005Wt000003NEtOIAW', '005Wt000003NEzqIAG', '005Wt000003NF1SIAW', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NFW6IAO', '005Wt000003NFhOIAW', '005Wt000003NFr4IAG', '005Wt000003NGjuIAG', '005Wt000003NGwpIAG', '005Wt000003NH3GIAW', '005Wt000003NHGAIA4', '005Wt000003NHfyIAG', '005Wt000003NHfzIAG', '005Wt000003NHg0IAG', '005Wt000003NHpeIAG', '005Wt000003NHsrIAG', '005Wt000003NHuUIAW', '005Wt000003NI2XIAW', '005Wt000003NI5mIAG', '005Wt000003NI90IAG', '005Wt000003NIAcIAO', '005Wt000003NIDqIAO', '005Wt000003NINVIA4', '005Wt000003NISLIA4', '005Wt000003NIVZIA4', '005Wt000003NIXBIA4', '005Wt000003NIYnIAO', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG', '005Wt000003NIc3IAG', '005Wt000003NIddIAG', '005Wt000003NIfFIAW', '005Wt000003NIfHIAW', '005Wt000003NIk5IAG', '005Wt000003NIk7IAG', '005Wt000003NInJIAW', '005Wt000003NInLIAW', '005Wt000003NItlIAG', '005Wt000003NIvNIAW', '005Wt000003NIwzIAG', '005Wt000003NJ0DIAW', '005Wt000003NJ3RIAW', '005Wt000003NJ6fIAG', '005Wt000003NJ6gIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ9tIAG', '005Wt000003NJD9IAO', '005Wt000003NJEjIAO', '005Wt000003NJGLIA4', '005Wt000003NJJaIAO', '005Wt000003NJLBIA4', '005Wt000003NJQ1IAO', '005Wt000003NJTFIA4', '005Wt000003NJUrIAO', '005Wt000003NJWTIA4', '005Wt000003NJbJIAW', '005Wt000003NJcvIAG', '005Wt000003NJcwIAG', '005Wt000003NJeXIAW', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJppIAG', '005Wt000003NJrRIAW', '005Wt000003NJufIAG', '005Wt000003NJzVIAW']}

exec(code, env_args)
