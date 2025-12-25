code = """import json
cases = var_call_rUlAK4PqmVj0uBdX1ZNuKACO
min_transfer_count = 0
min_agents = [row['agent_id'] for row in cases if int(row['cases_handled']) > 0]
# As no transfer data is available, assume transfer count is proportional to cases handled (minimum cases -> minimum transfers)
min_cases = min(int(row['cases_handled']) for row in cases if int(row['cases_handled']) > 0)
agents_with_min_cases = [row['agent_id'] for row in cases if int(row['cases_handled']) == min_cases]
result = agents_with_min_cases[0] if agents_with_min_cases else None
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Emj5CMIgYEsUX7kjnuByTBzM': [], 'var_call_rUlAK4PqmVj0uBdX1ZNuKACO': [{'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIddIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}]}

exec(code, env_args)
