code = """import json
case_counts = var_call_APYRRk4gFJlJaKY3jhV2smQI
# Agents with >0 cases are all in this list; transfer counts default to 0 since no transfers found
# Find the minimum transfer count (0) and any agent with that; but all have 0, so we can pick the one with fewest cases as tie-breaker
min_cases = min(int(r['case_count']) for r in case_counts)
# Among agents with min_cases, just pick the first agent_id
candidate_agents = [r['agent_id'] for r in case_counts if int(r['case_count']) == min_cases]
agent_id = candidate_agents[0] if candidate_agents else None
result = json.dumps(agent_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_qjRFZ89sUYVlYenYyKfoOeDY': [], 'var_call_APYRRk4gFJlJaKY3jhV2smQI': [{'agent_id': '#005Wt000003NBcAIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'case_count': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'case_count': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'case_count': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'case_count': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'case_count': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NBykIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NEGhIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'case_count': '2'}, {'agent_id': '005Wt000003NHpeIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NI2XIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NINVIA4', 'case_count': '2'}, {'agent_id': '005Wt000003NISLIA4', 'case_count': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'case_count': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIddIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIliIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'case_count': '3'}, {'agent_id': '005Wt000003NJD9IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NJTFIA4', 'case_count': '1'}, {'agent_id': '005Wt000003NJhlIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NJrRIAW', 'case_count': '1'}]}

exec(code, env_args)
