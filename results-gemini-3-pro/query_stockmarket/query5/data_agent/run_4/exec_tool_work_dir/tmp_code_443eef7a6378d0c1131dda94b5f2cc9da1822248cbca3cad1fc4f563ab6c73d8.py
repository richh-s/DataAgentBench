code = """import json

# Load previous result
with open(locals()['var_function-call-12539182368529526610'], 'r') as f:
    data = json.load(f)

symbols = data['symbols']

# Construct SQL query
queries = []
for sym in symbols:
    # Use double quotes for table name as it's a symbol which might be reserved or case sensitive
    q = f"""SELECT '{sym}' as Symbol, COUNT(*) as Days FROM "{sym}" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"""
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-14828481588465670158': 'file_storage/function-call-14828481588465670158.json', 'var_function-call-6181491610374641516': 'file_storage/function-call-6181491610374641516.json', 'var_function-call-12539182368529526610': 'file_storage/function-call-12539182368529526610.json'}

exec(code, env_args)
