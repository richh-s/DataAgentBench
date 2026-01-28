code = """import json
path = var_call_0iR8WlQ5ARF8bgujNkAIgkQb
if isinstance(path, str) and path.endswith('.json'):
    with open(path,'r') as f:
        payload = json.load(f)
else:
    payload = path
symbols = payload['symbols']

# chunk size small to avoid very long SQL
chunks = [symbols[i:i+25] for i in range(0, len(symbols), 25)]

def esc_table(s):
    return s.replace('"','""')

def one_select(sym):
    t = esc_table(sym)
    return "SELECT '"+sym+"' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \""+t+"\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'"

queries = []
for ch in chunks:
    q = "WITH mx AS (" + " UNION ALL ".join(one_select(sym) for sym in ch) + ") SELECT * FROM mx WHERE max_adj_close > 200"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_chunks': len(queries)}))"""

env_args = {'var_call_y7ZF0nkKnhjCsARv9z2cAVOg': 'file_storage/call_y7ZF0nkKnhjCsARv9z2cAVOg.json', 'var_call_meoUs7y7uUlDfzjL99xuAS8N': 'file_storage/call_meoUs7y7uUlDfzjL99xuAS8N.json', 'var_call_0iR8WlQ5ARF8bgujNkAIgkQb': 'file_storage/call_0iR8WlQ5ARF8bgujNkAIgkQb.json', 'var_call_pmuJ496qX2Xskx1sT9uaHcys': {'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'n': 1435}, 'var_call_ppiUjSebFcAH0yAp2UzQxqOM': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_mYqAwa1yYSEq4NUaTNLuI1Qf': {'ok': True}, 'var_call_2gwx1W2snpv73yd4RQ79XXP2': {'sym': 'AAAU'}, 'var_call_jRqsG9MyViaa3J6IaW87yMNh': [{'max_adj_close': 'nan'}], 'var_call_6XRVivX7JGalRr0epsLUf8tE': [{'max_adj_close': '193.3121490478516'}], 'var_call_gv9IkXCZhqxW9fXzn6tUAf3u': [{'Symbol': 'SPY', 'max_adj_close': '193.3121490478516'}, {'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}]}

exec(code, env_args)
