code = """import json
import pandas as pd

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

etfs_arca = pd.DataFrame(load_maybe_path(var_call_jMt97FSyhoanOw2XfsV5xNc8))
trade_tables = set(load_maybe_path(var_call_nXA3YSD1lrPQqkZBI4V8Tkvb))

tickers = sorted(set(etfs_arca['Symbol']).intersection(trade_tables))
print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'n': len(tickers)}))"""

env_args = {'var_call_jMt97FSyhoanOw2XfsV5xNc8': 'file_storage/call_jMt97FSyhoanOw2XfsV5xNc8.json', 'var_call_nXA3YSD1lrPQqkZBI4V8Tkvb': 'file_storage/call_nXA3YSD1lrPQqkZBI4V8Tkvb.json'}

exec(code, env_args)
