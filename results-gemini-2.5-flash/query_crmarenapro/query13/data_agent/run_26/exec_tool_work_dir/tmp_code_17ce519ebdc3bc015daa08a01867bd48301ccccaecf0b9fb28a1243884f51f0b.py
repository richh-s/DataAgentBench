code = """import json
result = locals()['var_function-call-988744738905481241']
agent_id = result[0]['AgentId']
print('__RESULT__:')
print(json.dumps(agent_id))"""

env_args = {'var_function-call-13839769025991590438': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-988744738905481241': [{'AgentId': '005Wt000003NIXCIA4', 'TotalSales': '46919.149999999994'}]}

exec(code, env_args)
