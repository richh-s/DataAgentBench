code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-14150000516763647607'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['createddate'] = pd.to_datetime(df['createddate'])

# Range: 2022-04-01 to 2023-03-31 (Last 4 completed quarters)
start_date = pd.Timestamp("2022-04-01", tz="UTC")
end_date = pd.Timestamp("2023-03-31 23:59:59", tz="UTC")

mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
df_period = df[mask].copy()

def clean_id(val):
    if val is None:
        return None
    val = str(val).strip()
    if val.startswith('#'):
        return val[1:]
    if val == 'None':
        return None
    return val

df_period['newvalue__c'] = df_period['newvalue__c'].apply(clean_id)
df_period['oldvalue__c'] = df_period['oldvalue__c'].apply(clean_id)

handled_counts = df_period['newvalue__c'].value_counts()
transfer_counts = df_period['oldvalue__c'].value_counts()

handled_agents = handled_counts.index.tolist()

results = []
for agent in handled_agents:
    t_count = transfer_counts.get(agent, 0)
    h_count = handled_counts.get(agent, 0)
    results.append({'agent_id': agent, 'transfer_count': t_count, 'handled_count': h_count})

results_df = pd.DataFrame(results)

if not results_df.empty:
    min_count = results_df['transfer_count'].min()
    candidates = results_df[results_df['transfer_count'] == min_count]
    candidates_sorted = candidates.sort_values(by='handled_count', ascending=False)
    print("__RESULT__:")
    print(candidates_sorted.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-11088062025914686682': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6082533964182735930': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-3320703554039932973': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14150000516763647607': 'file_storage/function-call-14150000516763647607.json', 'var_function-call-9196562452500107220': ['005Wt000003NDqFIAW', '005Wt000003NEzqIAG', '005Wt000003NEGhIAO', '005Wt000003NJ6gIAG', '005Wt000003NIVZIA4', '005Wt000003NBcAIAW', '005Wt000003NHsrIAG', '005Wt000003NFr4IAG', '005Wt000003NINVIA4', '005Wt000003NJhlIAG', '005Wt000003NHpeIAG', '005Wt000003NI2XIAW', '005Wt000003NJTFIA4', '005Wt000003NJoDIAW', '005Wt000003NIc2IAG', '005Wt000003NBykIAG', '005Wt000003NJD9IAO', '005Wt000003NJrRIAW', '005Wt000003NDsUIAW', '005Wt000003NIwzIAG', '005Wt000003NJ8HIAW', '005Wt000003NFKoIAO', '005Wt000003NIaQIAW', '005Wt000003NDJ1IAO', '005Wt000003NIvNIAW', '005Wt000003NISLIA4', '005Wt000003NJEjIAO', '005Wt000003NGjuIAG', '005Wt000003NJ0DIAW', '005Wt000003NInLIAW'], 'var_function-call-3710934653442004953': [{'agent_id': '005Wt000003NJ8HIAW', 'transfer_count': 0, 'handled_count': 3}, {'agent_id': '005Wt000003NFKoIAO', 'transfer_count': 0, 'handled_count': 3}, {'agent_id': '005Wt000003NJhlIAG', 'transfer_count': 0, 'handled_count': 2}, {'agent_id': '005Wt000003NHsrIAG', 'transfer_count': 0, 'handled_count': 2}, {'agent_id': '005Wt000003NINVIA4', 'transfer_count': 0, 'handled_count': 2}, {'agent_id': '005Wt000003NEGhIAO', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NBcAIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NIVZIA4', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJ6gIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NFr4IAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NHpeIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NI2XIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NDqFIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NEzqIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJoDIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJTFIA4', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NIc2IAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NBykIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJrRIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJD9IAO', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NIwzIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NDsUIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NIaQIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NDJ1IAO', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NIvNIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NISLIA4', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJEjIAO', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NGjuIAG', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NJ0DIAW', 'transfer_count': 0, 'handled_count': 1}, {'agent_id': '005Wt000003NInLIAW', 'transfer_count': 0, 'handled_count': 1}], 'var_function-call-3969817233931907028': [{'Id': '005Wt000003NFKoIAO', 'FirstName': 'Akari', 'LastName': 'Fujiwara', 'Alias': 'fujiwara'}, {'Id': '005Wt000003NJ8HIAW', 'FirstName': 'Sun', 'LastName': 'Park', 'Alias': 'sun.park'}]}

exec(code, env_args)
