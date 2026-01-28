code = """import json
import pandas as pd

# Load the owner assignment data from storage
assignments = locals()['var_functions.query_db:8']

# Create a DataFrame for easier processing
df = pd.DataFrame(assignments)

# Clean up potential corruption in IDs
def clean_id(id_val):
    if id_val is None:
        return None
    id_str = str(id_val)
    # Remove leading # if present
    if id_str.startswith('#'):
        id_str = id_str[1:]
    # Trim whitespace
    return id_str.strip()

# Apply cleanup to relevant columns
for col in ['caseid__c', 'oldvalue__c', 'newvalue__c']:
    df[col] = df[col].apply(clean_id)

# Identify transfers: oldvalue is not None and not 'None' and different from newvalue
df['is_transfer'] = df['oldvalue__c'].notna() & (df['oldvalue__c'] != 'None') & (df['oldvalue__c'] != '')

# Count unique cases per agent (both initial and subsequent)
cases_by_agent = {}

# Initial assignments (oldvalue is None, 'None', or '')
initial_rows = df[(df['oldvalue__c'].isna()) | (df['oldvalue__c'] == 'None') | (df['oldvalue__c'] == '')]
for idx, row in initial_rows.iterrows():
    agent = str(row['newvalue__c'])
    case_id = str(row['caseid__c'])
    if agent and agent != 'None' and agent != '':
        if agent not in cases_by_agent:
            cases_by_agent[agent] = set()
        cases_by_agent[agent].add(case_id)

# Subsequent assignments (transferred to)
transfer_rows = df[df['is_transfer']]
for idx, row in transfer_rows.iterrows():
    agent = str(row['newvalue__c'])
    case_id = str(row['caseid__c'])
    if agent and agent != 'None' and agent != '':
        if agent not in cases_by_agent:
            cases_by_agent[agent] = set()
        cases_by_agent[agent].add(case_id)

# Count per agent
case_count_list = []
for agent, cases in cases_by_agent.items():
    case_count_list.append({'agent_id': agent, 'case_count': len(cases)})

case_count_df = pd.DataFrame(case_count_list)

# Filter agents with more than 0 cases
active_agents = case_count_df[case_count_df['case_count'] > 0]

# Count transfers: when agent is the oldvalue (transferring FROM)
transfer_counts = df[df['is_transfer']]['oldvalue__c'].value_counts().reset_index()
transfer_counts.columns = ['agent_id', 'transfer_count']

# Merge with active agents
result_df = pd.merge(active_agents, transfer_counts, on='agent_id', how='left')

# Fill NaN transfer counts with 0
result_df['transfer_count'] = result_df['transfer_count'].fillna(0)

# Sort by transfer count and get the agent with the fewest transfers
result_df = result_df.sort_values(['transfer_count', 'agent_id'])

if len(result_df) > 0:
    fewest_transfers_agent = result_df.iloc[0]
    result = {
        'agent_id': fewest_transfers_agent['agent_id'],
        'transfer_count': int(fewest_transfers_agent['transfer_count']),
        'cases_handled': int(fewest_transfers_agent['case_count'])
    }
else:
    result = {'error': 'No agents found with more than 0 cases'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:5': [{'id': 'a04Wt00000539LdIAI', 'caseid__c': '500Wt00000DDxSdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539LgIAI', 'caseid__c': '500Wt00000DE0ByIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538FwIAI', 'caseid__c': '500Wt00000DDfYwIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538asIAA', 'caseid__c': '500Wt00000DDzz3IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539DZIAY', 'caseid__c': '500Wt00000DE03tIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539NFIAY', 'caseid__c': '500Wt00000DDgLKIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537TYIAY', 'caseid__c': '500Wt00000DE0BxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000533xrIAA', 'caseid__c': '500Wt00000DDze6IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538O5IAI', 'caseid__c': '500Wt00000DDyuwIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005395ZIAQ', 'caseid__c': '500Wt00000DDnt6IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000536cIIAQ', 'caseid__c': '500Wt00000DDU5iIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000534aYIAQ', 'caseid__c': '500Wt00000DDzW2IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537V7IAI', 'caseid__c': '500Wt00000DDsG2IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539yLIAQ', 'caseid__c': '500Wt00000DDPSZIA5', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537wYIAQ', 'caseid__c': '500Wt00000DDZ27IAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000535ulIAA', 'caseid__c': '500Wt00000DDYUGIA5', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005322UIAQ', 'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053A6RIAU', 'caseid__c': '500Wt00000DDfFcIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537jeIAA', 'caseid__c': '500Wt00000DDzRBIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [{'id': '#a04Wt00000539iDIAQ', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': [{'caseid__c': '500Wt00000DDPIsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDPZ0IAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'caseid__c': '500Wt00000DDQRsIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'caseid__c': '500Wt00000DDYpHIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDZJuIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDZtKIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'caseid__c': '500Wt00000DDfx8IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDg1zIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDg20IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDg8RIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'caseid__c': '500Wt00000DDgLLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDsKuIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'caseid__c': '500Wt00000DDxScIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDxduIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDxkMIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'caseid__c': '500Wt00000DDy8aIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DDyRvIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'caseid__c': '500Wt00000DDyzoIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzB4IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzJ8IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzMLIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzNxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzPZIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'caseid__c': '500Wt00000DDzSoIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'caseid__c': '500Wt00000DDzXeIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzcTIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzqzIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzvqIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzxRIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DE0FDIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0IPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DE0K1IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DE0LdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'caseid__c': '500Wt00000DE0VJIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}], 'var_functions.query_db:10': [{'caseid__c': '500Wt00000DDZtLIAX', 'assignment_count': '2'}]}

exec(code, env_args)
