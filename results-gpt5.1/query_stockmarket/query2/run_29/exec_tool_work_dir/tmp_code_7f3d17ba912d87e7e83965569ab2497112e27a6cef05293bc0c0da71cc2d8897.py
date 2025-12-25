code = """import json, pandas as pd
from itertools import islice

# load symbols from file
path = var_call_O38QeKCZQTiRHAagblNAEKSb
with open(path, 'r') as f:
    data = json.load(f)

symbols = [row['Symbol'] for row in data]
# intersect with available stocktrade tables
trade_tables = set(var_call_MTmAQk2GLCCYWluTFhS8CHaJ)
available = [s for s in symbols if s in trade_tables]

result = json.dumps(available)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_O38QeKCZQTiRHAagblNAEKSb': 'file_storage/call_O38QeKCZQTiRHAagblNAEKSb.json', 'var_call_MTmAQk2GLCCYWluTFhS8CHaJ': 'file_storage/call_MTmAQk2GLCCYWluTFhS8CHaJ.json'}

exec(code, env_args)
