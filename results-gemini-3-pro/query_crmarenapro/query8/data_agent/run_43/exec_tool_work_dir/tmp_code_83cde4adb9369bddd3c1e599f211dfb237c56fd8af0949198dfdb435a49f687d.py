code = """import json

# Reuse previous logic
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

filtered_history = []
for row in history_data:
    try:
        d_str = row['createddate'][:10]
        if '2022-04-10' <= d_str <= '2023-04-10':
            filtered_history.append(row)
    except:
        pass

handled_agents = set()
for row in case_data:
    oid = clean_id(row['ownerid'])
    if oid: handled_agents.add(oid)
for row in history_data:
    ov = clean_id(row['oldvalue__c'])
    nv = clean_id(row['newvalue__c'])
    if ov: handled_agents.add(ov)
    if nv: handled_agents.add(nv)

transfer_counts = {agent: 0 for agent in handled_agents}
for row in filtered_history:
    ov = clean_id(row['oldvalue__c'])
    if ov and ov in transfer_counts:
        transfer_counts[ov] += 1

# Analyze distribution
counts = list(transfer_counts.values())
print("Min count:", min(counts) if counts else "None")
print("Max count:", max(counts) if counts else "None")
print("Count of 0s:", counts.count(0))

# Check counts > 0
non_zero = {k: v for k, v in transfer_counts.items() if v > 0}
print("Non-zero counts:", non_zero)"""

env_args = {'var_function-call-9772945741413585450': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4198054654733975161': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-5542852444659011097': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-7652902568116026259': [{'count': '165'}], 'var_function-call-1600279952077093655': [{'count': '153'}], 'var_function-call-17378029346723867815': 'file_storage/function-call-17378029346723867815.json', 'var_function-call-524129039605534771': [{'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '#005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NEzqIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NJcwIAG'}, {'ownerid': '005Wt000003NFhOIAW'}, {'ownerid': '005Wt000003NItlIAG'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '#005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NIfFIAW'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NHfyIAG'}, {'ownerid': '#005Wt000003NJoDIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '005Wt000003NJcvIAG'}, {'ownerid': '005Wt000003NJppIAG'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NJrRIAW'}, {'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NEGhIAO'}, {'ownerid': '#005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NDqFIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NEdKIAW'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NJQ1IAO'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NDsUIAW'}, {'ownerid': '005Wt000003NDJ1IAO'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NBykIAG'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '#005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NInJIAW'}, {'ownerid': '#005Wt000003NInLIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NIfHIAW'}, {'ownerid': '#005Wt000003NJUrIAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '005Wt000003NHGAIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIfFIAW'}, {'ownerid': '005Wt000003NIaQIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NINVIA4'}, {'ownerid': '005Wt000003NJ3RIAW'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '#005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '#005Wt000003NJcvIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIc2IAG'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NHfzIAG'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJoDIAW'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NGwpIAG'}, {'ownerid': '005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIliIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '#005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NEGhIAO'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NDXZIA4'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NHGAIA4'}], 'var_function-call-3868234305671370974': ['005Wt000003NBcAIAW', '005Wt000003NBykIAG', '005Wt000003NDJ1IAO', '005Wt000003NDXZIA4', '005Wt000003NDqDIAW', '005Wt000003NDqEIAW', '005Wt000003NDqFIAW', '005Wt000003NDsUIAW', '005Wt000003NDu7IAG', '005Wt000003NEGhIAO', '005Wt000003NEdKIAW', '005Wt000003NEtOIAW', '005Wt000003NEzqIAG', '005Wt000003NF1SIAW', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NFW6IAO', '005Wt000003NFhOIAW', '005Wt000003NFr4IAG', '005Wt000003NGjuIAG', '005Wt000003NGwpIAG', '005Wt000003NH3GIAW', '005Wt000003NHGAIA4', '005Wt000003NHfyIAG', '005Wt000003NHfzIAG', '005Wt000003NHg0IAG', '005Wt000003NHpeIAG', '005Wt000003NHsrIAG', '005Wt000003NHuUIAW', '005Wt000003NI2XIAW', '005Wt000003NI5mIAG', '005Wt000003NI90IAG', '005Wt000003NIAcIAO', '005Wt000003NIDqIAO', '005Wt000003NINVIA4', '005Wt000003NISLIA4', '005Wt000003NIVZIA4', '005Wt000003NIXBIA4', '005Wt000003NIYnIAO', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG', '005Wt000003NIc3IAG', '005Wt000003NIddIAG', '005Wt000003NIfFIAW', '005Wt000003NIfHIAW', '005Wt000003NIk5IAG', '005Wt000003NIk7IAG', '005Wt000003NInJIAW', '005Wt000003NInLIAW', '005Wt000003NItlIAG', '005Wt000003NIvNIAW', '005Wt000003NIwzIAG', '005Wt000003NJ0DIAW', '005Wt000003NJ3RIAW', '005Wt000003NJ6fIAG', '005Wt000003NJ6gIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ9tIAG', '005Wt000003NJD9IAO', '005Wt000003NJEjIAO', '005Wt000003NJGLIA4', '005Wt000003NJJaIAO', '005Wt000003NJLBIA4', '005Wt000003NJQ1IAO', '005Wt000003NJTFIA4', '005Wt000003NJUrIAO', '005Wt000003NJWTIA4', '005Wt000003NJbJIAW', '005Wt000003NJcvIAG', '005Wt000003NJcwIAG', '005Wt000003NJeXIAW', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJppIAG', '005Wt000003NJrRIAW', '005Wt000003NJufIAG', '005Wt000003NJzVIAW']}

exec(code, env_args)
