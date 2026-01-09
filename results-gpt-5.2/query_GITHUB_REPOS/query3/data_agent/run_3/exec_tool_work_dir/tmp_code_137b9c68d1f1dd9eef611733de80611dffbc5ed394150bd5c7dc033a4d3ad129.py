code = """import json

path = var_call_d85rKzZDmWtyopRAbZXKnWjx
with open(path,'r') as f:
    data = json.load(f)
queries = data['queries']

out = json.dumps({"n_queries": len(queries), "first_query": queries[0], "last_query": queries[-1]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_yBgoLI7vx8huym8DOYHbmPcx': 'file_storage/call_yBgoLI7vx8huym8DOYHbmPcx.json', 'var_call_d85rKzZDmWtyopRAbZXKnWjx': 'file_storage/call_d85rKzZDmWtyopRAbZXKnWjx.json'}

exec(code, env_args)
