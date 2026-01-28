code = """import json

def load_path(p):
    with open(p,'r') as f:
        return json.load(f)

data = load_path(var_call_6utPHfBorwslFay1JD1BUoPb)

tickers = data['tickers']

chunks = [tickers[i:i+300] for i in range(0, len(tickers), 300)]
sqls = []
for ch in chunks:
    selects = []
    for t in ch:
        selects.append('SELECT \'%s\' AS Symbol FROM "%s" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1' % (t, t))
    sqls.append(' UNION ALL '.join(selects))

print('__RESULT__:')
print(json.dumps({'sqls': sqls, 'n_chunks': len(sqls), 'n_tickers': len(tickers)}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json'}

exec(code, env_args)
