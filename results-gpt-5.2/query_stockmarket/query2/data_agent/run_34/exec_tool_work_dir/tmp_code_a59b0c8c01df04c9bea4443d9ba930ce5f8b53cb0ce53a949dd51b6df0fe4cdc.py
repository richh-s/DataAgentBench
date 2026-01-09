code = """import json, pandas as pd

# Load NYSE Arca ETFs
path = var_call_y7ZF0nkKnhjCsARv9z2cAVOg
with open(path, 'r') as f:
    etfs = json.load(f)

# Load list of trade tables
trade_path = var_call_meoUs7y7uUlDfzjL99xuAS8N
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

etf_symbols = [r['Symbol'] for r in etfs]
# Only those with price tables
symbols = [s for s in etf_symbols if s in trade_tables]

# Prepare output for querying in chunks
print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_y7ZF0nkKnhjCsARv9z2cAVOg': 'file_storage/call_y7ZF0nkKnhjCsARv9z2cAVOg.json', 'var_call_meoUs7y7uUlDfzjL99xuAS8N': 'file_storage/call_meoUs7y7uUlDfzjL99xuAS8N.json'}

exec(code, env_args)
