code = """import json

history_path = locals()['var_function-call-17378029346723867815']
with open(history_path, 'r') as f:
    history_data = json.load(f)

case_data = locals()['var_function-call-524129039605534771']

def clean_id(val):
    if not val or val == 'None':
        return None
    val = str(val).strip()
    if val.startswith('#'):
        val = val[1:]
    return val

# Filter History for last 4 quarters (2022-04-10 to 2023-04-10)
filtered_history = []
for row in history_data:
    try:
        # Date string: "2023-09-07T16:30:00.000+0000"
        # Take YYYY-MM-DD
        d_str = row['createddate'][:10]
        if '2022-04-10' <= d_str <= '2023-04-10':
            filtered_history.append(row)
    except:
        pass

# Identify Handled Agents (Universe)
handled_agents = set()

# From Case (Current Owners)
for row in case_data:
    oid = clean_id(row['ownerid'])
    if oid:
        handled_agents.add(oid)

# From History (Old and New Owners in the period)
# Also, strictly speaking, we should perhaps check history outside the period too?
# But we only have filtered history (or full history in `history_data`).
# I will check `history_data` (full) to populate `handled_agents` more robustly?
# "Among those who handled more than 0 cases" -> Generally handled cases.
for row in history_data:
    ov = clean_id(row['oldvalue__c'])
    nv = clean_id(row['newvalue__c'])
    if ov: handled_agents.add(ov)
    if nv: handled_agents.add(nv)

# Calculate Transfer Counts (in the last 4 quarters)
transfer_counts = {agent: 0 for agent in handled_agents}

for row in filtered_history:
    ov = clean_id(row['oldvalue__c'])
    # Only count if ov is a valid agent (not None)
    if ov:
        if ov in transfer_counts:
            transfer_counts[ov] += 1
        else:
            # Should be in handled_agents, but just in case
            transfer_counts[ov] = 1

# Find min
if not transfer_counts:
    result = []
else:
    min_val = min(transfer_counts.values())
    candidates = [k for k, v in transfer_counts.items() if v == min_val]
    # If multiple, maybe return the one with most cases handled? Or just sorted list.
    candidates.sort()
    result = candidates

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9772945741413585450': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4198054654733975161': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-5542852444659011097': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-7652902568116026259': [{'count': '165'}], 'var_function-call-1600279952077093655': [{'count': '153'}], 'var_function-call-17378029346723867815': 'file_storage/function-call-17378029346723867815.json', 'var_function-call-524129039605534771': [{'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '#005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NEzqIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NJcwIAG'}, {'ownerid': '005Wt000003NFhOIAW'}, {'ownerid': '005Wt000003NItlIAG'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '#005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NIfFIAW'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NHfyIAG'}, {'ownerid': '#005Wt000003NJoDIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '005Wt000003NJcvIAG'}, {'ownerid': '005Wt000003NJppIAG'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NJrRIAW'}, {'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NEGhIAO'}, {'ownerid': '#005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NDqFIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NEdKIAW'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NJQ1IAO'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NDsUIAW'}, {'ownerid': '005Wt000003NDJ1IAO'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NBykIAG'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '#005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NInJIAW'}, {'ownerid': '#005Wt000003NInLIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NIfHIAW'}, {'ownerid': '#005Wt000003NJUrIAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '005Wt000003NHGAIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIfFIAW'}, {'ownerid': '005Wt000003NIaQIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NINVIA4'}, {'ownerid': '005Wt000003NJ3RIAW'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '#005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '#005Wt000003NJcvIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIc2IAG'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NHfzIAG'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJoDIAW'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NGwpIAG'}, {'ownerid': '005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIliIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '#005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NEGhIAO'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NDXZIA4'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NHGAIA4'}]}

exec(code, env_args)
