code = """import pandas as pd

transfer_counts = locals()['var_function-call-17042086654673477825']
cases_handled = locals()['var_function-call-3936922946144775777']

df_transfers = pd.DataFrame(transfer_counts)
df_cases = pd.DataFrame(cases_handled)

df_transfers['agent_id'] = df_transfers['agent_id'].str.replace('#', '').str.strip()
df_cases['agent_id'] = df_cases['agent_id'].str.replace('#', '').str.strip()

df_transfers['transfer_count'] = df_transfers['transfer_count'].astype(int)

all_agents = pd.merge(
    df_cases.drop_duplicates(subset=['agent_id']),
    df_transfers,
    on='agent_id',
    how='left'
)

all_agents['transfer_count'] = all_agents['transfer_count'].fillna(0).astype(int)

filtered_agents = all_agents[all_agents['agent_id'] != 'None']

min_transfer_agent = filtered_agents.loc[filtered_agents['transfer_count'].idxmin()]

print("__RESULT__:")
print(min_transfer_agent['agent_id'].to_json())"""

env_args = {'var_function-call-17431991377331302986': [], 'var_function-call-17020032533369458087': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15053433829327906504': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-17042086654673477825': [{'agent_id': 'None', 'transfer_count': '38'}, {'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}], 'var_function-call-3936922946144775777': [{'agent_id': '005Wt000003NJrRIAW'}, {'agent_id': '005Wt000003NBykIAG'}, {'agent_id': '005Wt000003NIVZIA4'}, {'agent_id': '#005Wt000003NEzqIAG'}, {'agent_id': '005Wt000003NHpeIAG'}, {'agent_id': '005Wt000003NI2XIAW'}, {'agent_id': '005Wt000003NJD9IAO'}, {'agent_id': '005Wt000003NIc2IAG'}, {'agent_id': '005Wt000003NHsrIAG'}, {'agent_id': '005Wt000003NJhlIAG'}, {'agent_id': '005Wt000003NJTFIA4'}, {'agent_id': '#005Wt000003NJEjIAO'}, {'agent_id': '005Wt000003NJ0DIAW'}, {'agent_id': '#005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NJ8HIAW'}, {'agent_id': '#005Wt000003NBcAIAW'}, {'agent_id': '#005Wt000003NInLIAW'}, {'agent_id': '#005Wt000003NGjuIAG'}, {'agent_id': '005Wt000003NDJ1IAO'}, {'agent_id': '005Wt000003NDsUIAW'}, {'agent_id': '005Wt000003NINVIA4'}, {'agent_id': '005Wt000003NJ6gIAG'}, {'agent_id': '005Wt000003NIwzIAG'}, {'agent_id': '005Wt000003NDqFIAW'}, {'agent_id': '#005Wt000003NJoDIAW'}, {'agent_id': '005Wt000003NISLIA4'}, {'agent_id': '005Wt000003NFKoIAO'}, {'agent_id': '005Wt000003NEGhIAO'}, {'agent_id': '005Wt000003NIvNIAW'}, {'agent_id': '005Wt000003NIliIAG'}, {'agent_id': '#005Wt000003NFr4IAG'}, {'agent_id': '005Wt000003NIaQIAW'}]}

exec(code, env_args)
