code = """import json
from datetime import datetime

# Load data
cases_raw_key = 'var_function-call-7634771961496327246' # The 7 relevant cases
all_cases_key = 'var_function-call-11056044257391785904' # All cases
history_key = 'var_function-call-10689379072275162428' # History

# Load 7 cases
cases_raw = locals()[cases_raw_key]
if isinstance(cases_raw, str):
    with open(cases_raw, 'r') as f:
        target_cases = json.load(f)
else:
    target_cases = cases_raw

# Load all cases
all_cases_raw = locals()[all_cases_key]
if isinstance(all_cases_raw, str):
    with open(all_cases_raw, 'r') as f:
        all_cases = json.load(f)
else:
    all_cases = all_cases_raw

# Load history
history_path = locals()[history_key]
with open(history_path, 'r') as f:
    history_list = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
    return i

# 1. Calculate Total Processed Cases per Agent (Global)
agent_total_cases = {} # agent_id -> set(case_ids)

# From All Cases (Current Owners)
for c in all_cases:
    cid = clean_id(c['id'])
    owner = clean_id(c['ownerid'])
    if owner:
        if owner not in agent_total_cases:
            agent_total_cases[owner] = set()
        agent_total_cases[owner].add(cid)

# From History
case_assignments_count = {} # clean_cid -> int
for h in history_list:
    if h.get('field__c') == 'Owner Assignment':
        cid = clean_id(h.get('caseid__c'))
        
        # Count for single-owner check later
        case_assignments_count[cid] = case_assignments_count.get(cid, 0) + 1
        
        old_val = clean_id(h.get('oldvalue__c'))
        new_val = clean_id(h.get('newvalue__c'))
        
        if old_val and old_val != 'None':
            if old_val not in agent_total_cases:
                agent_total_cases[old_val] = set()
            agent_total_cases[old_val].add(cid)
            
        if new_val and new_val != 'None':
            if new_val not in agent_total_cases:
                agent_total_cases[new_val] = set()
            agent_total_cases[new_val].add(cid)

# Identify Eligible Agents (> 1 processed case)
eligible_agents = set()
for agent, cases in agent_total_cases.items():
    if len(cases) > 1:
        eligible_agents.add(agent)

# 2. Calculate Handle Time for Target Cases (4-month window)
# Only for Single Owner cases.
agent_durations = {} # agent_id -> list of durations

for c in target_cases:
    cid = clean_id(c['id'])
    owner = clean_id(c['ownerid'])
    
    # Check Single Owner
    # If case has 1 assignment in history -> Single Owner.
    # Note: I'm using the global history scan for counts.
    # All 7 target cases should be in history if they are closed.
    # We verified earlier they had num_assigns = 1.
    num_assigns = case_assignments_count.get(cid, 0)
    
    # If num_assigns is 0, it might be an issue, but we saw 1 earlier.
    # If num_assigns == 1, it is Single Owner.
    if num_assigns == 1:
        # Calculate duration
        created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        duration = (closed - created).total_seconds()
        
        if owner:
            if owner not in agent_durations:
                agent_durations[owner] = []
            agent_durations[owner].append(duration)

# 3. Compute Averages for Eligible Agents
final_results = []
for agent in agent_durations:
    if agent in eligible_agents:
        times = agent_durations[agent]
        if times:
            avg = sum(times) / len(times)
            final_results.append({'agent': agent, 'avg': avg})

final_results.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-9342110329570298783': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7634771961496327246': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4838252256481333369': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-16296263846446172672': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'var_function-call-10689379072275162428': 'file_storage/function-call-10689379072275162428.json', 'var_function-call-4960120652764271519': [], 'var_function-call-4830366056139126687': [{'case_id': '500Wt00000DDepmIAD', 'num_assigns': 1, 'owner': '005Wt000003NJufIAG', 'history_agents': ['005Wt000003NJufIAG']}, {'case_id': '500Wt00000DDyzpIAD', 'num_assigns': 1, 'owner': '005Wt000003NJGLIA4', 'history_agents': ['005Wt000003NJGLIA4']}, {'case_id': '500Wt00000DDzUPIA1', 'num_assigns': 1, 'owner': '005Wt000003NDqDIAW', 'history_agents': ['005Wt000003NDqDIAW']}, {'case_id': '500Wt00000DDzsbIAD', 'num_assigns': 1, 'owner': '005Wt000003NJD9IAO', 'history_agents': ['005Wt000003NJD9IAO']}, {'case_id': '500Wt00000DDzscIAD', 'num_assigns': 1, 'owner': '005Wt000003NEtOIAW', 'history_agents': ['005Wt000003NEtOIAW']}, {'case_id': '500Wt00000DDzuEIAT', 'num_assigns': 1, 'owner': '005Wt000003NJJaIAO', 'history_agents': ['005Wt000003NJJaIAO']}, {'case_id': '500Wt00000DE02HIAT', 'num_assigns': 1, 'owner': '005Wt000003NIddIAG', 'history_agents': ['005Wt000003NIddIAG']}], 'var_function-call-11056044257391785904': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW'}, {'id': '500Wt00000DDRVzIAP', 'ownerid': '005Wt000003NItlIAG'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDTERIA5', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDYdwIAH', 'ownerid': '#005Wt000003NJbJIAW'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW'}, {'id': '#500Wt00000DDZmsIAH', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '#500Wt00000DDet1IAD', 'ownerid': '005Wt000003NH3GIAW'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDg1yIAD', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW'}, {'id': '#500Wt00000DDg8QIAT', 'ownerid': '#005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDxVqIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDxZ4IAL', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO'}, {'id': '#500Wt00000DDxnbIAD', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '500Wt00000DDy8bIAD', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDymuIAD', 'ownerid': '005Wt000003NIDqIAO'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDz6GIAT', 'ownerid': '#005Wt000003NJhlIAG'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW'}, {'id': '#500Wt00000DDzKjIAL', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDzSnIAL', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '#500Wt00000DDzZFIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzarIAD', 'ownerid': '005Wt000003NHGAIA4'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzfhIAD', 'ownerid': '005Wt000003NIfFIAW'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW'}, {'id': '500Wt00000DDzmAIAT', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDzuDIAT', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '#500Wt00000DE077IAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE08jIAD', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0AMIA1', 'ownerid': '005Wt000003NJeXIAW'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG'}, {'id': '500Wt00000DE0DZIA1', 'ownerid': '#005Wt000003NIvNIAW'}, {'id': '#500Wt00000DE0FCIA1', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0NFIA1', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0QTIA1', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DE0S5IAL', 'ownerid': '#005Wt000003NEGhIAO'}, {'id': '#500Wt00000DE0ThIAL', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DE0WwIAL', 'ownerid': '005Wt000003NDXZIA4'}, {'id': '500Wt00000DE0YXIA1', 'ownerid': '005Wt000003NJ6fIAG'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4'}]}

exec(code, env_args)
