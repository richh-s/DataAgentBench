code = """import json, pandas as pd
from pathlib import Path

symbols_info = json.load(open(var_call_u4SH0vKvfciBdGBHsw3KzBbC))
nyse_df = pd.DataFrame(symbols_info)
nyse_symbols = nyse_df['Symbol'].tolist()

trade_tables = json.load(open(var_call_f82991HMIo7ulXwY7WyhH3PY))
common = sorted(set(nyse_symbols).intersection(trade_tables))
result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_f82991HMIo7ulXwY7WyhH3PY': 'file_storage/call_f82991HMIo7ulXwY7WyhH3PY.json', 'var_call_u4SH0vKvfciBdGBHsw3KzBbC': 'file_storage/call_u4SH0vKvfciBdGBHsw3KzBbC.json'}

exec(code, env_args)
