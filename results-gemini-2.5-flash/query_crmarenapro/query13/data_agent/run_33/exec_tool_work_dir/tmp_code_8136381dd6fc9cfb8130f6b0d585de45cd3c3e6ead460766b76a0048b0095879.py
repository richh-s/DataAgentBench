code = """result = locals()['var_function-call-1601944853390447986'][0]['AgentId']
print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-1601944853390447986': [{'AgentId': '005Wt000003NHzJIAW', 'TotalSales': '297493.625'}]}

exec(code, env_args)
