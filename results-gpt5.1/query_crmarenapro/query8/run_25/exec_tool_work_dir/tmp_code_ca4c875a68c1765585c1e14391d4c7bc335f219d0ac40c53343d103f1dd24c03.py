code = """import json
handled = var_call_y1j4EoE32BtTRbYEoX0KQJdg
nonzero_agents = {row['agent_id'] for row in handled if int(row['handled_cases']) > 0}
transfers = var_call_42Oeh4mVswTx8U1HOW3hSYmY
transfer_map = {row['agent_id']: int(row['transfer_count']) for row in transfers if row.get('agent_id') is not None}
result_agent = None
min_transfers = None
for agent in nonzero_agents:
    tc = transfer_map.get(agent, 0)
    if (min_transfers is None) or (tc < min_transfers):
        min_transfers = tc
        result_agent = agent
out = json.dumps({'agent_id': result_agent, 'transfer_count': min_transfers})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_42Oeh4mVswTx8U1HOW3hSYmY': [], 'var_call_y1j4EoE32BtTRbYEoX0KQJdg': [{'agent_id': '#005Wt000003NBcAIAW', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'handled_cases': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NBykIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'handled_cases': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NEGhIAO', 'handled_cases': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'handled_cases': '2'}, {'agent_id': '005Wt000003NHpeIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'handled_cases': '2'}, {'agent_id': '005Wt000003NI2XIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NINVIA4', 'handled_cases': '2'}, {'agent_id': '005Wt000003NISLIA4', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIddIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIliIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'handled_cases': '1'}, {'agent_id': '005Wt000003NJ6gIAG', 'handled_cases': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'handled_cases': '3'}, {'agent_id': '005Wt000003NJD9IAO', 'handled_cases': '1'}, {'agent_id': '005Wt000003NJTFIA4', 'handled_cases': '1'}, {'agent_id': '005Wt000003NJhlIAG', 'handled_cases': '2'}, {'agent_id': '005Wt000003NJrRIAW', 'handled_cases': '1'}]}

exec(code, env_args)
