code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

etfs = load_maybe_path(var_call_8RGLkP0mxzDDo92o9BkQ9JLL)
trade_tables = set(load_maybe_path(var_call_m60gBb32NxffOTEy9S0C09DP))

tickers = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in trade_tables})

print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'n': len(tickers)}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json'}

exec(code, env_args)
