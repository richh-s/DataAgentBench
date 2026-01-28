code = """import json

def load_path(p):
    with open(p,'r') as f:
        return json.load(f)

data = load_path(var_call_6utPHfBorwslFay1JD1BUoPb)

tickers = data['tickers']
subset = tickers[:3]
selects = []
for t in subset:
    q = "SELECT '{}' AS Symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(t,t)
    selects.append(q)

print('__RESULT__:')
print(json.dumps({'q0': selects[0], 'q1': selects[1], 'q2': selects[2], 'subset': subset}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json', 'var_call_thm6ei54l0e6pFUuac5abObE': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_qC68T4mkWIs1M9TjPg0r2y6E': [{'Symbol': 'ADP'}], 'var_call_sI5KrhXo2vVKANR33gfvsdUq': []}

exec(code, env_args)
