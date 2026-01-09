code = """import json

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

data = load_maybe_path(var_call_6utPHfBorwslFay1JD1BUoPb)
tickers = data['tickers']

# build VALUES list (safe chars)
values = ','.join(["('{}')".format(t.replace("'","''")) for t in tickers])
query = "WITH etf_symbols(Symbol) AS (VALUES {} ) SELECT Symbol FROM etf_symbols".format(values)

print('__RESULT__:')
print(json.dumps({'query_prefix': query[:500], 'query_len': len(query)}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json', 'var_call_thm6ei54l0e6pFUuac5abObE': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_qC68T4mkWIs1M9TjPg0r2y6E': [{'Symbol': 'ADP'}], 'var_call_sI5KrhXo2vVKANR33gfvsdUq': [], 'var_call_pzzuYZ9TXTlXoCvpfgD3UhkH': [{'Symbol': 'ACWV'}, {'Symbol': 'ACWX'}, {'Symbol': 'AGG'}], 'var_call_5MXoGG88wzEdffakB8LJauK0': [], 'var_call_ztSen5iuFgqp7glZ3tk9gbjb': {'n_tickers': 1435}}

exec(code, env_args)
