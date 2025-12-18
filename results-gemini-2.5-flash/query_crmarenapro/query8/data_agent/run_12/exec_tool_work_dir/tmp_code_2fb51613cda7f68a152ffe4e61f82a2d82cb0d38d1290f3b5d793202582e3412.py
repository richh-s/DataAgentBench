code = """import pandas as pd

transfer_counts_data = locals()['var_function-call-11512560316045410905']
handled_cases_agents_data = locals()['var_function-call-11832476474268001196']

# Process transfer counts
df_transfers = pd.DataFrame(transfer_counts_data)
df_transfers['agent_id'] = df_transfers['agent_id'].astype(str).str.replace('#', '').str.strip()
df_transfers = df_transfers[df_transfers['agent_id'] != 'None']
df_transfers['transfer_count'] = df_transfers['transfer_count'].astype(int)

# Process agents who handled cases
df_handled_agents = pd.DataFrame(handled_cases_agents_data)
df_handled_agents['agent_id'] = df_handled_agents['agent_id'].astype(str).str.replace('#', '').str.strip()
unique_handled_agents = df_handled_agents['agent_id'].unique()

# Create a DataFrame for all agents who handled cases, with initial transfer count as 0
df_all_agents = pd.DataFrame(unique_handled_agents, columns=['agent_id'])
df_all_agents = df_all_agents.merge(df_transfers, on='agent_id', how='left')
df_all_agents['transfer_count'] = df_all_agents['transfer_count'].fillna(0).astype(int)

# Filter for agents who handled more than 0 cases (which is already implicitly done by getting unique_handled_agents)
# Find the agent with the fewest transfer counts
min_transfers_agent = df_all_agents.loc[df_all_agents['transfer_count'].idxmin()]

print('__RESULT__:')
print(min_transfers_agent['agent_id'])"""

env_args = {'var_function-call-14931441098924925574': [], 'var_function-call-2622036328262926729': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-13435240381694856132': [{'agent_id': 'None', 'transfer_count': '38'}, {'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}], 'var_function-call-11512560316045410905': [{'agent_id': 'None', 'transfer_count': '38'}, {'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}], 'var_function-call-11832476474268001196': [{'agent_id': '#005Wt000003NEzqIAG'}, {'agent_id': '005Wt000003NJD9IAO'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '#005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NJ6gIAG'}, {'agent_id': '#005Wt000003NJoDIAW'}, {'agent_id': '005Wt000003NINVIA4'}, {'agent_id': '#005Wt000003NGjuIAG'}, {'agent_id': '005Wt000003NJhlIAG'}, {'agent_id': '005Wt000003NJrRIAW'}, {'agent_id': '005Wt000003NIvNIAW'}, {'agent_id': '005Wt000003NEGhIAO'}, {'agent_id': '005Wt000003NDqFIAW'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '005Wt000003NJTFIA4'}, {'agent_id': '005Wt000003NDsUIAW'}, {'agent_id': '005Wt000003NDJ1IAO'}, {'agent_id': '005Wt000003NHsrIAG'}, {'agent_id': '005Wt000003NISLIA4'}, {'agent_id': '005Wt000003NHsrIAG'}, {'agent_id': '005Wt000003NBykIAG'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '#005Wt000003NInLIAW'}, {'agent_id': '005Wt000003NINVIA4'}, {'agent_id': '005Wt000003NI2XIAW'}, {'agent_id': '#005Wt000003NBcAIAW'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '005Wt000003NJhlIAG'}, {'agent_id': '005Wt000003NIwzIAG'}, {'agent_id': '005Wt000003NIaQIAW'}, {'agent_id': '#005Wt000003NFr4IAG'}, {'agent_id': '005Wt000003NIc2IAG'}, {'agent_id': '005Wt000003NIVZIA4'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NIliIAG'}, {'agent_id': '#005Wt000003NJEjIAO'}, {'agent_id': '005Wt000003NHpeIAG'}, {'agent_id': '005Wt000003NJ0DIAW'}, {'agent_id': '005Wt000003NIliIAG'}, {'agent_id': '005Wt000003NDqFIAW'}, {'agent_id': '005Wt000003NEzqIAG'}, {'agent_id': '005Wt000003NEGhIAO'}, {'agent_id': '005Wt000003NJ6gIAG'}, {'agent_id': '005Wt000003NIVZIA4'}, {'agent_id': '005Wt000003NBcAIAW'}, {'agent_id': '005Wt000003NHsrIAG'}, {'agent_id': '005Wt000003NFr4IAG'}, {'agent_id': '005Wt000003NINVIA4'}, {'agent_id': '005Wt000003NJhlIAG'}, {'agent_id': '005Wt000003NHpeIAG'}, {'agent_id': '005Wt000003NI2XIAW'}, {'agent_id': '005Wt000003NJTFIA4'}, {'agent_id': '005Wt000003NJoDIAW'}, {'agent_id': '005Wt000003NIc2IAG'}, {'agent_id': '005Wt000003NBykIAG'}, {'agent_id': '005Wt000003NJD9IAO'}, {'agent_id': '005Wt000003NJrRIAW'}, {'agent_id': '005Wt000003NDsUIAW'}, {'agent_id': '005Wt000003NIliIAG'}, {'agent_id': '005Wt000003NIwzIAG'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '005Wt000003NJhlIAG'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NIaQIAW'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NINVIA4'}, {'agent_id': '005Wt000003NHsrIAG'}, {'agent_id': '005Wt000003NDJ1IAO'}, {'agent_id': '005Wt000003NIvNIAW'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '005Wt000003NISLIA4'}, {'agent_id': '005Wt000003NJEjIAO'}, {'agent_id': '005Wt000003NGjuIAG'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NJ0DIAW'}, {'agent_id': '005Wt000003NInLIAW'}]}

exec(code, env_args)
