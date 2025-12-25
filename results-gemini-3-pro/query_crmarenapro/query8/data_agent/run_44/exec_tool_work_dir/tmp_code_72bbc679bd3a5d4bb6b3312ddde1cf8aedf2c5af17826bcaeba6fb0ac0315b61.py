code = """import json
import pandas as pd

with open(locals()['var_function-call-3927801684446189843'], 'r') as f:
    history_data = json.load(f)

df = pd.DataFrame(history_data)

def clean_id(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.startswith('#'):
        s = s[1:]
    if s == 'None':
        return None
    return s

df['oldvalue'] = df['oldvalue__c'].apply(clean_id)
df['newvalue'] = df['newvalue__c'].apply(clean_id)
df['date'] = pd.to_datetime(df['createddate'])

start_date = pd.Timestamp('2022-04-10', tz='UTC')
end_date = pd.Timestamp('2023-04-10', tz='UTC')

mask = (df['date'] >= start_date) & (df['date'] <= end_date)
window_df = df[mask]

print(f"Total rows in window: {len(window_df)}")

# Handled
handled_counts = window_df['newvalue'].value_counts()
# Transfers
transfer_counts = window_df['oldvalue'].value_counts()

# All agents active (handled > 0)
active_agents = handled_counts[handled_counts > 0].index.tolist()
print(f"Number of agents handled > 0: {len(active_agents)}")

results = []
for agent_id in active_agents:
    if not agent_id: continue
    t_count = transfer_counts.get(agent_id, 0)
    h_count = handled_counts[agent_id]
    results.append({'AgentId': agent_id, 'TransferCount': t_count, 'HandledCount': h_count})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by=['TransferCount', 'HandledCount'], ascending=[True, False])

print("Top 10 Candidates (Min Transfers, Max Handled):")
print(results_df.head(10).to_json(orient='records'))

print("Distribution of Transfer Counts:")
print(results_df['TransferCount'].value_counts().to_json())"""

env_args = {'var_function-call-7815841651268430622': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1911759767125460883': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3927801684446189843': 'file_storage/function-call-3927801684446189843.json', 'var_function-call-3544899369714927464': [{'AgentId': '005Wt000003NJ8HIAW', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NJhlIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NHsrIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NINVIA4', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIVZIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJ6gIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NHpeIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NI2XIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDqFIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NEzqIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJoDIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJTFIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIc2IAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NBykIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJrRIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJD9IAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIwzIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDsUIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIaQIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDJ1IAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIvNIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NISLIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJEjIAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NGjuIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJ0DIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NInLIAW', 'TransferCount': 0, 'HandledCount': 1}], 'var_function-call-15158139698347831638': [{'count': '153'}]}

exec(code, env_args)
