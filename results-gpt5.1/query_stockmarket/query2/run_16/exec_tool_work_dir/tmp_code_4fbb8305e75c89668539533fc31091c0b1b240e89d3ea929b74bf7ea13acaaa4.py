code = """import json
symbols = [rec['Symbol'] for rec in var_call_ijijKyCktWtYyKwR7LP4oUla]
chunks = [symbols[i:i+50] for i in range(0, len(symbols), 50)]
result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_AqPskMD0dgVJd6XNjMNdelSc': 'file_storage/call_AqPskMD0dgVJd6XNjMNdelSc.json', 'var_call_ijijKyCktWtYyKwR7LP4oUla': 'file_storage/call_ijijKyCktWtYyKwR7LP4oUla.json'}

exec(code, env_args)
