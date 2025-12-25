code = """import json
from datetime import datetime, timezone

# Load history (updated with oldvalue)
history_path = locals()['var_function-call-11783088464238331233']
with open(history_path, 'r') as f:
    history_data = json.load(f)

# Load cases
case_path = locals()['var_function-call-1184811431951596709']
with open(case_path, 'r') as f:
    case_data = json.load(f)

start_date = datetime(2022, 4, 10, tzinfo=timezone.utc)
end_date = datetime(2023, 4, 10, tzinfo=timezone.utc)

def clean_id(id_str):
    if not id_str: return None
    if id_str == 'None': return None
    if id_str.startswith('#'):
        return id_str[1:]
    return id_str

def parse_date(date_str):
    if not date_str or date_str == 'None': return None
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        try:
             dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        except:
             dt = datetime.fromisoformat(date_str.replace('+0000', '+00:00'))
    return dt

agent_transfers = {} 
agent_active = set() 

cases_hist = {}
for rec in history_data:
    case_id = clean_id(rec['caseid__c'])
    if not case_id: continue
    if case_id not in cases_hist:
        cases_hist[case_id] = []
    cases_hist[case_id].append(rec)

def check_overlap(s1, e1, s2, e2):
    if e1 is None:
        return s1 <= e2
    else:
        return max(s1, s2) <= min(e1, e2)

cases_map = {clean_id(c['id']): c for c in case_data}
all_case_ids = set(cases_map.keys()) | set(cases_hist.keys())

for case_id in all_case_ids:
    c_info = cases_map.get(case_id)
    hist = cases_hist.get(case_id, [])
    
    parsed_hist = []
    for r in hist:
        d = parse_date(r['createddate'])
        parsed_hist.append((d, r))
    parsed_hist.sort(key=lambda x: x[0])
    
    if not parsed_hist:
        if c_info:
            owner = clean_id(c_info['ownerid'])
            created = parse_date(c_info['createddate'])
            closed = parse_date(c_info['closeddate'])
            if owner and created:
                 if check_overlap(created, closed, start_date, end_date):
                     agent_active.add(owner)
    else:
        # Check first record for transfer FROM oldvalue
        first_rec = parsed_hist[0][1]
        first_date = parsed_hist[0][0]
        first_old = clean_id(first_rec['oldvalue__c'])
        
        # If first_date is in window, and first_old exists, it's a transfer!
        if start_date <= first_date <= end_date:
            if first_old:
                agent_transfers[first_old] = agent_transfers.get(first_old, 0) + 1
                agent_active.add(first_old) # They were active at transfer
        
        # Also, first_old was active before first_date.
        # Check overlap [Created, first_date] with window.
        if first_old:
            if c_info:
                created = parse_date(c_info['createddate'])
                if created and created < first_date:
                    if check_overlap(created, first_date, start_date, end_date):
                        agent_active.add(first_old)
        
        for i in range(len(parsed_hist)):
            curr_rec = parsed_hist[i][1]
            curr_date = parsed_hist[i][0]
            curr_agent = clean_id(curr_rec['newvalue__c'])
            
            if i < len(parsed_hist) - 1:
                end_ownership = parsed_hist[i+1][0]
                # Transfer from curr_agent at end_ownership
                if start_date <= end_ownership <= end_date:
                    if curr_agent:
                        agent_transfers[curr_agent] = agent_transfers.get(curr_agent, 0) + 1
            else:
                end_ownership = None
                if c_info:
                    end_ownership = parse_date(c_info['closeddate'])
            
            if curr_agent:
                 if check_overlap(curr_date, end_ownership, start_date, end_date):
                     agent_active.add(curr_agent)

# Filter active agents
filtered_agents = [a for a in agent_active]
min_val = float('inf')
if filtered_agents:
    min_val = min([agent_transfers.get(a, 0) for a in filtered_agents])

min_agents = [a for a in filtered_agents if agent_transfers.get(a, 0) == min_val]
min_agents.sort()

print("__RESULT__:")
print(json.dumps({
    "min_transfers": min_val,
    "count": len(min_agents),
    "sample": min_agents[:5],
    "active_agents_count": len(agent_active),
    "agents_with_transfers_count": len(agent_transfers)
}))"""

env_args = {'var_function-call-12750645328546507404': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17379795203378931937': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-2758909594085963491': [{'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-12639703507394349142': 'file_storage/function-call-12639703507394349142.json', 'var_function-call-552801240223168671': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW'}, {'id': '500Wt00000DDRVzIAP', 'ownerid': '005Wt000003NItlIAG'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDTERIA5', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDYdwIAH', 'ownerid': '#005Wt000003NJbJIAW'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4'}, {'id': '#500Wt00000DDYpHIAX', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW'}, {'id': '#500Wt00000DDZmsIAH', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDZtKIAX', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '#500Wt00000DDet1IAD', 'ownerid': '005Wt000003NH3GIAW'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DDfx8IAD', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDg1yIAD', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '500Wt00000DDg1zIAD', 'ownerid': '005Wt000003NJrRIAW'}, {'id': '500Wt00000DDg20IAD', 'ownerid': '005Wt000003NIvNIAW'}, {'id': '#500Wt00000DDg8QIAT', 'ownerid': '#005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDg8RIAT', 'ownerid': '005Wt000003NEGhIAO'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW'}, {'id': '500Wt00000DDgLLIA1', 'ownerid': '005Wt000003NDqFIAW'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO'}, {'id': '500Wt00000DDsKuIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DDxVqIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDxZ4IAL', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO'}, {'id': '#500Wt00000DDxnbIAD', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDy8aIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '500Wt00000DDy8bIAD', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDymuIAD', 'ownerid': '005Wt000003NIDqIAO'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG'}, {'id': '#500Wt00000DDyzoIAD', 'ownerid': '005Wt000003NBykIAG'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDz6GIAT', 'ownerid': '#005Wt000003NJhlIAG'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW'}, {'id': '#500Wt00000DDzKjIAL', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDzNxIAL', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDzSnIAL', 'ownerid': '005Wt000003NJ9tIAG'}, {'id': '#500Wt00000DDzSoIAL', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '#500Wt00000DDzZFIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzarIAD', 'ownerid': '005Wt000003NHGAIA4'}, {'id': '500Wt00000DDzcTIAT', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzfhIAD', 'ownerid': '005Wt000003NIfFIAW'}, {'id': '500Wt00000DDzhJIAT', 'ownerid': '005Wt000003NIaQIAW'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW'}, {'id': '500Wt00000DDzmAIAT', 'ownerid': '005Wt000003NJbJIAW'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '#500Wt00000DDzuDIAT', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW'}, {'id': '#500Wt00000DE077IAD', 'ownerid': '#005Wt000003NFr4IAG'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE08jIAD', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0AMIA1', 'ownerid': '005Wt000003NJeXIAW'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG'}, {'id': '500Wt00000DE0DZIA1', 'ownerid': '#005Wt000003NIvNIAW'}, {'id': '#500Wt00000DE0FCIA1', 'ownerid': '#005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW'}, {'id': '500Wt00000DE0IPIA1', 'ownerid': '005Wt000003NIliIAG'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO'}, {'id': '500Wt00000DE0LdIAL', 'ownerid': '005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0NFIA1', 'ownerid': '005Wt000003NDu7IAG'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG'}, {'id': '500Wt00000DE0QTIA1', 'ownerid': '005Wt000003NIYnIAO'}, {'id': '500Wt00000DE0S5IAL', 'ownerid': '#005Wt000003NEGhIAO'}, {'id': '#500Wt00000DE0ThIAL', 'ownerid': '005Wt000003NIVZIA4'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DE0WwIAL', 'ownerid': '005Wt000003NDXZIA4'}, {'id': '500Wt00000DE0YXIA1', 'ownerid': '005Wt000003NJ6fIAG'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4'}], 'var_function-call-10345074320805043128': ['005Wt000003NFKpIAO', '005Wt000003NJ8HIAW', '005Wt000003NFW6IAO', '005Wt000003NDqFIAW', '005Wt000003NJUrIAO', '005Wt000003NGjuIAG', '005Wt000003NFKoIAO', '005Wt000003NJufIAG', '005Wt000003NJbJIAW', '005Wt000003NJLBIA4', '005Wt000003NIDqIAO', '005Wt000003NJppIAG', '005Wt000003NI5mIAG', '005Wt000003NIYnIAO', '005Wt000003NI90IAG', '005Wt000003NH3GIAW', '005Wt000003NEdKIAW', '005Wt000003NJJaIAO', '005Wt000003NJGLIA4', '005Wt000003NItlIAG', '005Wt000003NEzqIAG', '005Wt000003NHGAIA4', '005Wt000003NDqDIAW', '005Wt000003NIfFIAW', '005Wt000003NJTFIA4', '005Wt000003NJ0DIAW', '005Wt000003NBcAIAW', '005Wt000003NISLIA4', '005Wt000003NJ6gIAG', '005Wt000003NIvNIAW', '005Wt000003NIc2IAG', '005Wt000003NJ3RIAW', '005Wt000003NDu7IAG', '005Wt000003NIk5IAG', '005Wt000003NJhlIAG', '005Wt000003NJWTIA4', '005Wt000003NJ6fIAG', '005Wt000003NHfyIAG', '005Wt000003NBykIAG', '005Wt000003NInJIAW', '005Wt000003NIc3IAG', '005Wt000003NEtOIAW', '005Wt000003NIAcIAO', '005Wt000003NI2XIAW', '005Wt000003NHg0IAG', '005Wt000003NHuUIAW', '005Wt000003NIk7IAG', '005Wt000003NJD9IAO', '005Wt000003NJcvIAG', '005Wt000003NDXZIA4', '005Wt000003NIddIAG', '005Wt000003NHsrIAG', '005Wt000003NIVZIA4', '005Wt000003NIfHIAW', '005Wt000003NF1SIAW', '005Wt000003NDqEIAW', '005Wt000003NIaQIAW', '005Wt000003NJcwIAG', '005Wt000003NJrRIAW', '005Wt000003NINVIA4', '005Wt000003NJQ1IAO', '005Wt000003NFr4IAG', '005Wt000003NEGhIAO', '005Wt000003NDJ1IAO', '005Wt000003NJeXIAW', '005Wt000003NJoDIAW', '005Wt000003NJzVIAW', '005Wt000003NGwpIAG', '005Wt000003NIXBIA4', '005Wt000003NHpeIAG', '005Wt000003NJEjIAO', '005Wt000003NHfzIAG', '005Wt000003NFhOIAW', '005Wt000003NInLIAW', '005Wt000003NDsUIAW', '005Wt000003NIwzIAG', '005Wt000003NJ9tIAG'], 'var_function-call-15277019579250210006': {'min_transfers': 0, 'count_min_agents': 77, 'sample_min_agents': ['005Wt000003NIc3IAG', '005Wt000003NDqFIAW', '005Wt000003NHGAIA4', '005Wt000003NF1SIAW', '005Wt000003NJLBIA4'], 'all_agents_count': 78, 'agents_with_transfers_count': 1}, 'var_function-call-14638199907959479942': 'file_storage/function-call-14638199907959479942.json', 'var_function-call-1184811431951596709': 'file_storage/function-call-1184811431951596709.json', 'var_function-call-11783088464238331233': 'file_storage/function-call-11783088464238331233.json'}

exec(code, env_args)
