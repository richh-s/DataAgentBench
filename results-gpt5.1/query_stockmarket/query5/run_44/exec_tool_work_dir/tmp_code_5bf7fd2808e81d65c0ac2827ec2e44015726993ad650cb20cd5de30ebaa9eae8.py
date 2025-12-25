code = """import json, pandas as pd
from pathlib import Path

symbols_df = pd.DataFrame(json.load(open(var_call_OzYXi60EVSzw50t6Z2WyhpgF)))

trade_tables = json.load(open(var_call_GqOs4ILaEK4BJsk36L0lZmS7))

valid_symbols = sorted(set(symbols_df['Symbol']).intersection(trade_tables))

batch = valid_symbols

result = json.dumps(batch)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_GqOs4ILaEK4BJsk36L0lZmS7': 'file_storage/call_GqOs4ILaEK4BJsk36L0lZmS7.json', 'var_call_OzYXi60EVSzw50t6Z2WyhpgF': 'file_storage/call_OzYXi60EVSzw50t6Z2WyhpgF.json'}

exec(code, env_args)
