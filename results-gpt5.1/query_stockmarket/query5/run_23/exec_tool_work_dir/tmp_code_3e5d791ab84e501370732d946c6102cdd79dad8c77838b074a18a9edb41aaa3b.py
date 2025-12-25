code = """import json, pandas as pd
from math import isfinite

path = var_call_oVQjh9u5mLSbAixKxJMu927W
with open(path) as f:
    s_list = json.load(f)
syms = [r['Symbol'] for r in s_list]

trade_tables_path = var_call_Wv8ti8avHzWM8aB2sDzY4lzK
with open(trade_tables_path) as f:
    all_tables = json.load(f)

syms_trade = sorted(set(syms).intersection(all_tables))

chunks = []
for sym in syms_trade:
    chunks.append(sym)

result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_oVQjh9u5mLSbAixKxJMu927W': 'file_storage/call_oVQjh9u5mLSbAixKxJMu927W.json', 'var_call_Wv8ti8avHzWM8aB2sDzY4lzK': 'file_storage/call_Wv8ti8avHzWM8aB2sDzY4lzK.json'}

exec(code, env_args)
