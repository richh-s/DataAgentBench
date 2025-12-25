code = """import json
from datetime import datetime

# Load data
with open(locals()['var_function-call-12639703507394349142'], 'r') as f:
    history_data = json.load(f)

current_owners_data = locals()['var_function-call-552801240223168671']

# Config
start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10)

def clean_id(id_str):
    if not id_str: return None
    if id_str.startswith('#'):
        return id_str[1:]
    return id_str

def parse_date(date_str):
    # Format: "2023-09-07T16:30:00.000+0000"
    # Python 3.11+ fromisoformat handles 'Z' and offsets, but simpler to slice if fixed format
    # Or use strptime. %z handles +0000
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        # Try without microseconds if they are missing or different
        try:
             dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        except:
             # Fallback: ignore timezone for comparison if needed, but better to keep it
             # Let's strip timezone if strptime fails or use dateutil if available (not available)
             # Manual parse: 2023-09-07T16:30:00
             dt = datetime.fromisoformat(date_str.replace('+0000', '+00:00'))
    
    # Convert to offset-naive for comparison with start_date/end_date (which are naive)
    # Or make start/end aware. Better to make start/end aware (UTC)
    return dt

# Make start/end aware (UTC)
from datetime import timezone
start_date = start_date.replace(tzinfo=timezone.utc)
end_date = end_date.replace(tzinfo=timezone.utc)

agent_transfers = {} # Default 0
agent_handled = set()

# Process history
# Group by Case
cases = {}
for rec in history_data:
    case_id = clean_id(rec['caseid__c'])
    if not case_id: continue
    if case_id not in cases:
        cases[case_id] = []
    cases[case_id].append(rec)

for case_id, recs in cases.items():
    # Sort by date
    # Parse dates first to sort correctly
    parsed_recs = []
    for r in recs:
        d = parse_date(r['createddate'])
        parsed_recs.append((d, r))
    
    parsed_recs.sort(key=lambda x: x[0])
    
    # Iterate
    # Sequence of owners
    for i in range(len(parsed_recs)):
        current_rec = parsed_recs[i][1]
        current_agent = clean_id(current_rec['newvalue__c'])
        current_date = parsed_recs[i][0]
        
        if not current_agent: continue
        
        agent_handled.add(current_agent)
        
        # Check for transfer
        if i < len(parsed_recs) - 1:
            next_date = parsed_recs[i+1][0]
            # Transfer from current_agent happens at next_date
            if start_date <= next_date <= end_date:
                agent_transfers[current_agent] = agent_transfers.get(current_agent, 0) + 1

# Process current owners to ensure all handled agents are included
for rec in current_owners_data:
    agent = clean_id(rec['ownerid'])
    if agent:
        agent_handled.add(agent)

# Find min transfers
min_transfers = float('inf')
min_agents = []

for agent in agent_handled:
    count = agent_transfers.get(agent, 0)
    if count < min_transfers:
        min_transfers = count
        min_agents = [agent]
    elif count == min_transfers:
        min_agents.append(agent)

print("__RESULT__:")
print(json.dumps(min_agents))"""

env_args = {'var_function-call-12750645328546507404': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17379795203378931937': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-2758909594085963491': [{'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-12639703507394349142': 'file_storage/function-call-12639703507394349142.json', 'var_function-call-552801240223168671': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW'}, {'id': '500Wt00000DDRVzIAP', 'ownerid': '005Wt000003NItlIAG'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDTERIA5', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDYdwIAH', 'ownerid': '#005Wt000003NJbJIAW'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW'}, {'id': '#500Wt00000DDZmsIAH', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '#500Wt00000DDet1IAD', 'ownerid': '005Wt000003NH3GIAW'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDg1yIAD', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW'}, {'id': '#500Wt00000DDg8QIAT', 'ownerid': '#005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDxVqIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDxZ4IAL', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO'}, {'id': '#500Wt00000DDxnbIAD', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '500Wt00000DDy8bIAD', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDymuIAD', 'ownerid': '005Wt000003NIDqIAO'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDz6GIAT', 'ownerid': '#005Wt000003NJhlIAG'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW'}, {'id': '#500Wt00000DDzKjIAL', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDzSnIAL', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '#500Wt00000DDzZFIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzarIAD', 'ownerid': '005Wt000003NHGAIA4'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzfhIAD', 'ownerid': '005Wt000003NIfFIAW'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW'}, {'id': '500Wt00000DDzmAIAT', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDzuDIAT', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '#500Wt00000DE077IAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE08jIAD', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0AMIA1', 'ownerid': '005Wt000003NJeXIAW'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG'}, {'id': '500Wt00000DE0DZIA1', 'ownerid': '#005Wt000003NIvNIAW'}, {'id': '#500Wt00000DE0FCIA1', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0NFIA1', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0QTIA1', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DE0S5IAL', 'ownerid': '#005Wt000003NEGhIAO'}, {'id': '#500Wt00000DE0ThIAL', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DE0WwIAL', 'ownerid': '005Wt000003NDXZIA4'}, {'id': '500Wt00000DE0YXIA1', 'ownerid': '005Wt000003NJ6fIAG'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4'}]}

exec(code, env_args)
