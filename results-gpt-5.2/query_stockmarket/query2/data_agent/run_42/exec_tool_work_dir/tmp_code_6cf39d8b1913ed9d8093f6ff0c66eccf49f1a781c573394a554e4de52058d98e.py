code = """import json

with open(var_call_Gx0fPAIHRtr9SkCxfjDwil6o,'r') as f:
    symbols=[r['symbol'] for r in json.load(f)]
with open(var_call_x46B2WTQq6zbsoWLQaJw9Uiv,'r') as f:
    tables=set(json.load(f))

symbols_in_trade=[s for s in symbols if s in tables]
parts=[]
for s in symbols_in_trade:
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

final_query=None
if parts:
    union_query='\nUNION ALL\n'.join(parts)
    final_query='SELECT symbol, max_adj_close FROM ('+union_query+') t WHERE max_adj_close > 200 ORDER BY symbol'

out={"final_query":final_query,"n_symbols":len(symbols_in_trade)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Gx0fPAIHRtr9SkCxfjDwil6o': 'file_storage/call_Gx0fPAIHRtr9SkCxfjDwil6o.json', 'var_call_x46B2WTQq6zbsoWLQaJw9Uiv': 'file_storage/call_x46B2WTQq6zbsoWLQaJw9Uiv.json'}

exec(code, env_args)
