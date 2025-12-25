code = """import json

with open(locals()['var_function-call-9049256654640604985'], 'r') as f:
    companies = json.load(f)

symbols = [c['Symbol'] for c in companies]
print(f"__RESULT__:\n{len(symbols)}")"""

env_args = {'var_function-call-9049256654640604985': 'file_storage/function-call-9049256654640604985.json'}

exec(code, env_args)
