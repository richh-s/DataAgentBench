code = """import json
import pandas as pd

# Load new cases list
cases_list = locals()['var_function-call-9709612173670337225']
# Load history
with open(locals()['var_function-call-11308014558138915622'], 'r') as f:
    history_list = json.load(f)

def clean_id(x):
    if not isinstance(x, str): return x
    x = x.strip()
    if x.startswith('#'): return x[1:]
    return x

# Prepare History Map
case_owners = {}
for h in history_list:
    cid = clean_id(h.get('caseid__c'))
    oid = clean_id(h.get('newvalue__c'))
    if cid and oid:
        if cid not in case_owners: case_owners[cid] = []
        case_owners[cid].append(oid)

agent_volume = {} # agent -> count of active cases managed
agent_handle_data = {} # agent -> list of durations

start_date = pd.to_datetime('2023-05-02').tz_localize('UTC')
end_date = pd.to_datetime('2023-09-02').tz_localize('UTC')

for c in cases_list:
    cid = clean_id(c.get('id'))
    if not cid: continue
    
    # Get owners
    hist_owners = case_owners.get(cid, [])
    if not hist_owners:
        # Fallback
        oid = clean_id(c.get('ownerid'))
        owners = [oid] if oid else []
    else:
        owners = hist_owners
    
    unique_owners = set(owners)
    
    # Volume Count (Active Cases)
    # The query already filtered for active cases.
    # So we count this case for all its owners.
    for agent in unique_owners:
        agent_volume[agent] = agent_volume.get(agent, 0) + 1
        
    # Handle Time (Closed in Window)
    closed_str = c.get('closeddate')
    created_str = c.get('createddate')
    
    if closed_str and closed_str != 'None':
        try:
            closed_dt = pd.to_datetime(closed_str)
            created_dt = pd.to_datetime(created_str)
            
            # Check if closed in window
            if closed_dt >= start_date and closed_dt <= end_date:
                # Check if Single Owner
                if len(unique_owners) == 1:
                    duration = (closed_dt - created_dt).total_seconds()
                    agent = list(unique_owners)[0] # The single owner
                    
                    if agent not in agent_handle_data:
                        agent_handle_data[agent] = []
                    agent_handle_data[agent].append(duration)
                    
        except Exception as e:
            pass

# Calculate Avg and Filter
final_results = []
for agent, vol in agent_volume.items():
    if vol > 1:
        times = agent_handle_data.get(agent, [])
        if len(times) > 0:
            avg_time = sum(times) / len(times)
            final_results.append({
                'agent_id': agent,
                'avg_time': avg_time,
                'volume': vol,
                'handle_count': len(times)
            })

final_results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-9305866664193886812': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5909842420318969754': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10922903359105958166': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11308014558138915622': 'file_storage/function-call-11308014558138915622.json', 'var_function-call-16183834308635989304': [], 'var_function-call-4744346774618992494': {'Total Cases': 7, 'Total History Entries': 165, 'Cases with History': 153, 'Matched Cases': 7, 'Single Owner Cases': 7, 'Multi Owner Cases': 0, 'No History Cases': 0, 'Sample Case IDs': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD'], 'Sample History IDs': ['500Wt00000DDzpNIAT', '500Wt00000DDfHCIA1', '500Wt00000DDZ0VIAX', '500Wt00000DDQoUIAX', '500Wt00000DDzm9IAD']}, 'var_function-call-10314689673863851144': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'var_function-call-9709612173670337225': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW', 'createddate': '2021-01-10T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2021-06-03T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG', 'createddate': '2022-03-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW', 'createddate': '2021-10-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2022-03-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T11:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG', 'createddate': '2021-11-11T12:13:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO', 'createddate': '2020-07-01T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T18:04:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2020-11-05T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO', 'createddate': '2021-08-24T13:25:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG', 'createddate': '2021-11-01T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2021-02-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-05-24T04:08:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW', 'createddate': '2021-06-02T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW', 'createddate': '2022-03-04T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW', 'createddate': '2021-11-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2021-10-22T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO', 'createddate': '2022-01-28T02:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-09-10T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-01-10T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW', 'createddate': '2021-11-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2021-01-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW', 'createddate': '2021-07-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2021-11-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2021-09-17T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2021-07-07T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4', 'createddate': '2021-06-16T08:30:00.000+0000', 'closeddate': 'None'}]}

exec(code, env_args)
