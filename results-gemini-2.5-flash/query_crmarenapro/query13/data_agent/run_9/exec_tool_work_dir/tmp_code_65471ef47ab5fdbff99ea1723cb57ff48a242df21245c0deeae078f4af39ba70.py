code = """import json
result = locals()['var_function-call-6893356296509075333'][0]['AgentId']
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6893356296509075333': [{'AgentId': '005Wt000003NIXCIA4', 'TotalSales': '46919.149999999994'}]}

exec(code, env_args)
