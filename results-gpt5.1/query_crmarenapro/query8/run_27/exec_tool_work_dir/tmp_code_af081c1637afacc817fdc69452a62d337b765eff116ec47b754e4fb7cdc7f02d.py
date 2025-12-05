code = """import json
import pandas as pd

transfers = pd.DataFrame(var_call_Qdjfugy6qfrQlNe2fdmpR9fd)
cases = pd.DataFrame(var_call_05VstGIzPwKY41JL8zULrVTQ)

# Normalize IDs by stripping leading '#'
for df in (transfers, cases):
    df['agent_id_norm'] = df['agent_id'].str.lstrip('#')

# Convert counts to int
transfers['transfer_count'] = transfers['transfer_count'].astype(int)
cases['case_count'] = cases['case_count'].astype(int)

# Filter agents with >0 cases is already true by construction, but ensure join only on those
merged = pd.merge(cases, transfers, left_on='agent_id_norm', right_on='agent_id_norm', how='left')

# Agents who handled >0 cases but may have 0 transfers (NaN -> 0)
merged['transfer_count'] = merged['transfer_count'].fillna(0).astype(int)

# Identify minimum transfer count among these agents
min_transfer = merged['transfer_count'].min()
min_agents = merged[merged['transfer_count'] == min_transfer]

# If multiple agents tie, return all their normalized Ids
result_ids = min_agents['agent_id_norm'].unique().tolist()

result = json.dumps(result_ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Qdjfugy6qfrQlNe2fdmpR9fd': [{'agent_id': '005Wt000003NJrRIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NBykIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJoDIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'transfer_count': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'transfer_count': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NInLIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NFr4IAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'transfer_count': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'transfer_count': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'transfer_count': '1'}, {'agent_id': '005Wt000003NEzqIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'transfer_count': '3'}, {'agent_id': '005Wt000003NGjuIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'transfer_count': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NINVIA4', 'transfer_count': '2'}, {'agent_id': '005Wt000003NIddIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'transfer_count': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NJEjIAO', 'transfer_count': '1'}, {'agent_id': '005Wt000003NISLIA4', 'transfer_count': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'transfer_count': '3'}, {'agent_id': '005Wt000003NEGhIAO', 'transfer_count': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NIliIAG', 'transfer_count': '2'}, {'agent_id': '005Wt000003NIaQIAW', 'transfer_count': '1'}, {'agent_id': '005Wt000003NBcAIAW', 'transfer_count': '1'}], 'var_call_05VstGIzPwKY41JL8zULrVTQ': [{'agent_id': '005Wt000003NJrRIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NBykIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'case_count': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'case_count': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'case_count': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'case_count': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NINVIA4', 'case_count': '2'}, {'agent_id': '005Wt000003NIddIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NISLIA4', 'case_count': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'case_count': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NIliIAG', 'case_count': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'case_count': '1'}]}

exec(code, env_args)
