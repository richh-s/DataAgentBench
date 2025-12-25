code = """import json

filename = locals()['var_function-call-18079362525503296285']
with open(filename, 'r') as f:
    valid_tables = json.load(f)

batch = valid_tables[:100]
queries = []
q_quote = chr(34) # double quote
s_quote = chr(39) # single quote

for sym in batch:
    # SELECT 'SYM' as Symbol, MAX("Adj Close") as MaxPrice FROM "SYM" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' HAVING MaxPrice > 200
    q = "SELECT " + s_quote + sym + s_quote + " as Symbol, MAX(" + q_quote + "Adj Close" + q_quote + ") as MaxPrice FROM " + q_quote + sym + q_quote + " WHERE Date BETWEEN " + s_quote + "2015-01-01" + s_quote + " AND " + s_quote + "2015-12-31" + s_quote + " HAVING MaxPrice > 200"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-13365528125237992877': [{'Symbol': 'AAAU', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AADR', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'ABEQ', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'ACSG', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'ACWF', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AFK', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AFLG', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AFMC', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AFSM', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AFTY', 'ETF': 'Y', 'Listing Exchange': 'P'}], 'var_function-call-17592671511465676620': 'file_storage/function-call-17592671511465676620.json', 'var_function-call-16788755398465361199': 1435, 'var_function-call-12317635941678307066': 'file_storage/function-call-12317635941678307066.json', 'var_function-call-18079362525503296285': 'file_storage/function-call-18079362525503296285.json', 'var_function-call-2073230096008525227': 1435, 'var_function-call-9322841224094409968': 'test', 'var_function-call-8897849210935094560': 1435, 'var_function-call-15238515856999659918': 'AAAU', 'var_function-call-17204330064088995749': 'done', 'var_function-call-7119557689639915839': "SELECT 'AAAU'"}

exec(code, env_args)
