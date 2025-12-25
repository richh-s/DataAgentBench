code = """import json
# transfer counts are empty (no owner changes), so every agent has 0 transfers
# we just need the agent(s) with fewest transfers (>0 cases already enforced by case_count query)
case_counts = var_call_uAL13fcCnlemvkiaTO2Ndju3
# all have 0 transfers, so pick any one deterministically, e.g., the first after sorting agent_id
agent_ids = sorted([r['agent_id'] for r in case_counts])
result = agent_ids[0] if agent_ids else None
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_4ZU4imWKsRIyOMHPtpospgmR': [], 'var_call_uAL13fcCnlemvkiaTO2Ndju3': [{'agent_id': '005Wt000003NJrRIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NBykIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'case_count': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'case_count': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'case_count': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'case_count': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'case_count': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'case_count': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NINVIA4', 'case_count': '2'}, {'agent_id': '005Wt000003NIddIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'case_count': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'case_count': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NISLIA4', 'case_count': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'case_count': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'case_count': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'case_count': '1'}, {'agent_id': '005Wt000003NIliIAG', 'case_count': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'case_count': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'case_count': '1'}]}

exec(code, env_args)
