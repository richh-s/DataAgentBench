code = """import json
fpath = locals()['var_function-call-10604229133623975260']
with open(fpath, 'r') as f:
    symbols = json.load(f)

chunk = symbols[0:100]
sq = chr(39)
dq = chr(34)
queries = []
for sym in chunk:
    # Shorten the query: Date check can be string comparison
    # SELECT 'SYM' s, MAX("Adj Close") m FROM "SYM" WHERE Date LIKE '2015%' HAVING m>200
    q = f"SELECT {sq}{sym}{sq} s, MAX({dq}Adj Close{dq}) m FROM {dq}{sym}{dq} WHERE Date LIKE {sq}2015%{sq} HAVING MAX({dq}Adj Close{dq}) > 200"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5162594856234074983': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12055750503848787858': 'file_storage/function-call-12055750503848787858.json', 'var_function-call-1195933028834543906': 'file_storage/function-call-1195933028834543906.json', 'var_function-call-4479522260417322904': 'file_storage/function-call-4479522260417322904.json', 'var_function-call-10604229133623975260': 'file_storage/function-call-10604229133623975260.json', 'var_function-call-6238139469492482643': 1435, 'var_function-call-13873116716835971214': 'Hello', 'var_function-call-12734436292721667169': 1435, 'var_function-call-3594353986603810590': 'file_storage/function-call-3594353986603810590.json', 'var_function-call-6357528156472082360': 'file_storage/function-call-6357528156472082360.json'}

exec(code, env_args)
