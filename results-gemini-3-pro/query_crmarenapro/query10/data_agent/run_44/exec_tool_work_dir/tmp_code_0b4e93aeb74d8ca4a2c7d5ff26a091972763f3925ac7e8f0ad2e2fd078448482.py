code = """import json
from collections import defaultdict, Counter
from datetime import datetime

# Load data
cases_in_window = locals()['var_function-call-9379197308370690660']
all_cases = locals()['var_function-call-4883546314682679349']
history_path = locals()['var_function-call-6841357651747039383']
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(id_str):
    if not id_str: return None
    if id_str.startswith('#'): return id_str[1:]
    return id_str

# Index history by caseid
history_by_case = defaultdict(list)
for h in history:
    cid = clean_id(h.get('caseid__c'))
    if cid: history_by_case[cid].append(h)

# 1. Compute Global Processed Counts
processed_counts = Counter()

# We need to process ALL cases to get the counts
for c in all_cases:
    cid = clean_id(c['id'])
    h_list = history_by_case.get(cid, [])
    owner_assignments = [h for h in h_list if h.get('field__c') == 'Owner Assignment']
    
    # Agents involved
    agents = set()
    for oa in owner_assignments:
        old = clean_id(oa.get('oldvalue__c'))
        new = clean_id(oa.get('newvalue__c'))
        if old and old != 'None': agents.add(old)
        if new and new != 'None': agents.add(new)
    
    final_owner = clean_id(c['ownerid'])
    if final_owner:
        agents.add(final_owner)
    
    # Check if history is missing (sample showed 0 assignments for window cases).
    # If 0 assignments, assume just final owner.
    # Note: If no history, we assume initial = final.
    
    for a in agents:
        processed_counts[a] += 1

# 2. Compute Handle Time for Cases Closed In Window
# And filter candidates
candidates = []

# Map window cases by id
window_case_ids = set()
for c in cases_in_window:
    window_case_ids.add(clean_id(c['id']))

# Calculate durations for window cases
agent_durations = defaultdict(list)

for c in cases_in_window:
    cid = clean_id(c['id'])
    # Re-calculate agents involved in this specific case to assign handle time correctly
    # Only assign to Final Owner if not transferred.
    
    h_list = history_by_case.get(cid, [])
    owner_assignments = [h for h in h_list if h.get('field__c') == 'Owner Assignment']
    
    num_assignments = len(owner_assignments)
    final_owner = clean_id(c['ownerid'])
    
    # Parse dates
    fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
    try:
        created = datetime.strptime(c['createddate'], fmt)
        closed = datetime.strptime(c['closeddate'], fmt)
        dur = (closed - created).total_seconds()
    except:
        continue

    # Logic: "For cases that have NOT been transferred to an other agent, there will be only ONE 'Owner Assignment', and for those that have been transferred, there will be MORE THAN ONE 'Owner Assignment'."
    # "When computing handle time, we do not compute handle time for cases that have been transferred to other agents."
    
    # If num_assignments <= 1: Not transferred. Assign to Final Owner.
    # If num_assignments > 1: Transferred. Ignore.
    
    if num_assignments <= 1:
        if final_owner:
            agent_durations[final_owner].append(dur)

# 3. Combine
results = []
for agent, count in processed_counts.items():
    if count > 1:
        # Eligible
        # Check if they have handle time stats in the window
        if agent in agent_durations and len(agent_durations[agent]) > 0:
            avg_ht = sum(agent_durations[agent]) / len(agent_durations[agent])
            results.append({
                "agent_id": agent,
                "global_processed_count": count,
                "avg_handle_time": avg_ht
            })

# Sort
sorted_results = sorted(results, key=lambda x: x['avg_handle_time'])

print("__RESULT__:")
print(json.dumps(sorted_results))"""

env_args = {'var_function-call-16935417607994828587': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11268043920336260726': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-9379197308370690660': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6841357651747039383': 'file_storage/function-call-6841357651747039383.json', 'var_function-call-10712201643136478981': [], 'var_function-call-11650599874123248297': {'debug_cases': [{'case_id': '500Wt00000DDepmIAD', 'num_assignments': 0, 'agents': ['005Wt000003NJufIAG'], 'measured': True, 'duration': 33068.0, 'final_owner': '005Wt000003NJufIAG'}, {'case_id': '500Wt00000DDyzpIAD', 'num_assignments': 0, 'agents': ['005Wt000003NJGLIA4'], 'measured': True, 'duration': 1442.0, 'final_owner': '005Wt000003NJGLIA4'}, {'case_id': '500Wt00000DDzUPIA1', 'num_assignments': 0, 'agents': ['005Wt000003NDqDIAW'], 'measured': True, 'duration': 882.0, 'final_owner': '005Wt000003NDqDIAW'}, {'case_id': '500Wt00000DDzsbIAD', 'num_assignments': 0, 'agents': ['005Wt000003NJD9IAO'], 'measured': True, 'duration': 21608.0, 'final_owner': '005Wt000003NJD9IAO'}, {'case_id': '500Wt00000DDzscIAD', 'num_assignments': 0, 'agents': ['005Wt000003NEtOIAW'], 'measured': True, 'duration': 1007.0, 'final_owner': '005Wt000003NEtOIAW'}, {'case_id': '500Wt00000DDzuEIAT', 'num_assignments': 0, 'agents': ['005Wt000003NJJaIAO'], 'measured': True, 'duration': 14712.0, 'final_owner': '005Wt000003NJJaIAO'}, {'case_id': '500Wt00000DE02HIAT', 'num_assignments': 0, 'agents': ['005Wt000003NIddIAG'], 'measured': True, 'duration': 2194.0, 'final_owner': '005Wt000003NIddIAG'}], 'counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'durations_keys': ['005Wt000003NJufIAG', '005Wt000003NJGLIA4', '005Wt000003NDqDIAW', '005Wt000003NJD9IAO', '005Wt000003NEtOIAW', '005Wt000003NJJaIAO', '005Wt000003NIddIAG']}, 'var_function-call-4883546314682679349': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW'}, {'id': '500Wt00000DDRVzIAP', 'ownerid': '005Wt000003NItlIAG'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDTERIA5', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDYdwIAH', 'ownerid': '#005Wt000003NJbJIAW'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW'}, {'id': '#500Wt00000DDZmsIAH', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '#500Wt00000DDet1IAD', 'ownerid': '005Wt000003NH3GIAW'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDg1yIAD', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW'}, {'id': '#500Wt00000DDg8QIAT', 'ownerid': '#005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDxVqIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDxZ4IAL', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO'}, {'id': '#500Wt00000DDxnbIAD', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '500Wt00000DDy8bIAD', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDymuIAD', 'ownerid': '005Wt000003NIDqIAO'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDz6GIAT', 'ownerid': '#005Wt000003NJhlIAG'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW'}, {'id': '#500Wt00000DDzKjIAL', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDzSnIAL', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '#500Wt00000DDzZFIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzarIAD', 'ownerid': '005Wt000003NHGAIA4'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzfhIAD', 'ownerid': '005Wt000003NIfFIAW'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW'}, {'id': '500Wt00000DDzmAIAT', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDzuDIAT', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '#500Wt00000DE077IAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE08jIAD', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0AMIA1', 'ownerid': '005Wt000003NJeXIAW'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG'}, {'id': '500Wt00000DE0DZIA1', 'ownerid': '#005Wt000003NIvNIAW'}, {'id': '#500Wt00000DE0FCIA1', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0NFIA1', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0QTIA1', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DE0S5IAL', 'ownerid': '#005Wt000003NEGhIAO'}, {'id': '#500Wt00000DE0ThIAL', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DE0WwIAL', 'ownerid': '005Wt000003NDXZIA4'}, {'id': '500Wt00000DE0YXIA1', 'ownerid': '005Wt000003NJ6fIAG'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4'}]}

exec(code, env_args)
