code = """import json, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

etfs_arca = pd.DataFrame(load_records(var_call_6ctMLF9BUUuRXIeIs1vcu4lt))
all_tables = load_records(var_call_jWYwT4eMqUmqOtH5L0tt2agF)
trade_set = set(all_tables)

tickers = [s for s in etfs_arca['Symbol'].tolist() if s in trade_set]

tickers_json = json.dumps(tickers)
print('__RESULT__:')
print(tickers_json)"""

env_args = {'var_call_6ctMLF9BUUuRXIeIs1vcu4lt': 'file_storage/call_6ctMLF9BUUuRXIeIs1vcu4lt.json', 'var_call_jWYwT4eMqUmqOtH5L0tt2agF': 'file_storage/call_jWYwT4eMqUmqOtH5L0tt2agF.json'}

exec(code, env_args)
