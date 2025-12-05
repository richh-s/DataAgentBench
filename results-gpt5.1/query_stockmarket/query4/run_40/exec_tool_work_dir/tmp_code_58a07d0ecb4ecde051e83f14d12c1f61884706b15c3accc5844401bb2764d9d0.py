code = """import json, pandas as pd
from collections import defaultdict

# load full list of symbols from stocktrade_database
path = var_call_4b3M17SmieQImgcLpqQUSat2
with open(path, 'r') as f:
    trade_symbols = json.load(f)

# load NYSE non-ETF symbols
path2 = var_call_M7KbQESCFS3cHmQYPs3PNfB0
with open(path2, 'r') as f:
    nyse_meta = json.load(f)

nyse_df = pd.DataFrame(nyse_meta)
nyse_symbols = set(nyse_df['Symbol'])

# intersection
common = sorted(symbol for symbol in trade_symbols if symbol in nyse_symbols)

result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4b3M17SmieQImgcLpqQUSat2': 'file_storage/call_4b3M17SmieQImgcLpqQUSat2.json', 'var_call_M7KbQESCFS3cHmQYPs3PNfB0': 'file_storage/call_M7KbQESCFS3cHmQYPs3PNfB0.json'}

exec(code, env_args)
