code = """import json

def load_path(p):
    with open(p,'r') as f:
        return json.load(f)

data = load_path(var_call_6utPHfBorwslFay1JD1BUoPb)

tickers = data['tickers']

chunks = [tickers[i:i+400] for i in range(0,len(tickers),400)]

sqls = []
for ch in chunks:
    parts = []
    for t in ch:
        parts.append(f"SELECT '{t}' AS Symbol FROM \"{t}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1")
    sqls.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'sqls': sqls, 'n_chunks': len(sqls), 'n_tickers': len(tickers)}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json'}

exec(code, env_args)
