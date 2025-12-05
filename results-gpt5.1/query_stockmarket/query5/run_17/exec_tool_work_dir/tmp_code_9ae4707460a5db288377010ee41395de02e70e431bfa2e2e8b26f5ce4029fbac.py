code = """import json, pandas as pd
from pathlib import Path

symbols_info = pd.read_json(Path(var_call_FUfQ4JCVFBKmuGoimQaDHVNz))
trade_tables = pd.read_json(Path(var_call_TgARrzPML3y7pBMFl9SL0jhh))

nasdaq_cap_syms = set(symbols_info['Symbol'].astype(str))
trade_syms = set(trade_tables.astype(str))
common_syms = sorted(nasdaq_cap_syms & trade_syms)

result = json.dumps(common_syms)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_TgARrzPML3y7pBMFl9SL0jhh': 'file_storage/call_TgARrzPML3y7pBMFl9SL0jhh.json', 'var_call_FUfQ4JCVFBKmuGoimQaDHVNz': 'file_storage/call_FUfQ4JCVFBKmuGoimQaDHVNz.json'}

exec(code, env_args)
