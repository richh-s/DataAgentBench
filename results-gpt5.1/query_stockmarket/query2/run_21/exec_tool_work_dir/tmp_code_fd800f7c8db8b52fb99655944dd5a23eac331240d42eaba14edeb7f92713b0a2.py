code = """import json, pandas as pd

# Load full ETF symbol list from file path in var_call_hIL8Xy8C1hmn7bVZNvodAPez
with open(var_call_hIL8Xy8C1hmn7bVZNvodAPez, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# We only care about symbols that also exist as tables in stocktrade_database, which we have in var_call_YK1NgylmpGBizcdp2FJuJkJI
with open(var_call_YK1NgylmpGBizcdp2FJuJkJI, 'r') as f:
    trade_tables = set(json.load(f))

symbols = sorted(list(set(etf_symbols) & trade_tables))

# Chunk symbols for later querying
chunk_size = 50
chunks = [symbols[i:i+chunk_size] for i in range(0, len(symbols), chunk_size)]

result = {'chunks': chunks}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hIL8Xy8C1hmn7bVZNvodAPez': 'file_storage/call_hIL8Xy8C1hmn7bVZNvodAPez.json', 'var_call_YK1NgylmpGBizcdp2FJuJkJI': 'file_storage/call_YK1NgylmpGBizcdp2FJuJkJI.json'}

exec(code, env_args)
