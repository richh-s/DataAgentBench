code = """import json, pandas as pd
import os
with open(var_call_cg7OABKXDhrcOUTOmpYyeuXT) as f:
    symbols_info = pd.DataFrame(json.load(f))
with open(var_call_k4caEoQj7lXVlNyqgQlt51Us) as f:
    trade_tables = json.load(f)
valid_symbols = [s for s in symbols_info['Symbol'] if s in trade_tables]
result = json.dumps(valid_symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_k4caEoQj7lXVlNyqgQlt51Us': 'file_storage/call_k4caEoQj7lXVlNyqgQlt51Us.json', 'var_call_cg7OABKXDhrcOUTOmpYyeuXT': 'file_storage/call_cg7OABKXDhrcOUTOmpYyeuXT.json'}

exec(code, env_args)
