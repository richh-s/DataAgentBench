code = """import json
import pandas as pd
symbols = pd.DataFrame(var_call_ijijKyCktWtYyKwR7LP4oUla)['Symbol'].tolist()
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]
queries = []
for chunk in chunks:
    in_list = ','.join(["'"+s+"'" for s in chunk])
    q = f"SELECT table_name FROM information_schema.tables WHERE table_name IN ({in_list});"
    queries.append(q)
result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_AqPskMD0dgVJd6XNjMNdelSc': 'file_storage/call_AqPskMD0dgVJd6XNjMNdelSc.json', 'var_call_ijijKyCktWtYyKwR7LP4oUla': 'file_storage/call_ijijKyCktWtYyKwR7LP4oUla.json'}

exec(code, env_args)
