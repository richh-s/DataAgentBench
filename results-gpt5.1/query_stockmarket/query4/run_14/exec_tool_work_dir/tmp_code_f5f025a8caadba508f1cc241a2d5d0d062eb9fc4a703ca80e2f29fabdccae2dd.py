code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_ztbaJgeCz9oZX2eUsKrA5Vda)
with symbols_path.open() as f:
    symbols_data = json.load(f)

symbols = [row['Symbol'] for row in symbols_data]

# limit to those that have price tables
trade_tables_path = Path(var_call_IAIAXD5wrlL3zcJ2yOOOF8NI)
with trade_tables_path.open() as f:
    trade_tables = set(json.load(f))

symbols = [s for s in symbols if s in trade_tables]

# take a manageable subset to query in one go
subset = symbols[:200]

result = json.dumps(subset)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_IAIAXD5wrlL3zcJ2yOOOF8NI': 'file_storage/call_IAIAXD5wrlL3zcJ2yOOOF8NI.json', 'var_call_ztbaJgeCz9oZX2eUsKrA5Vda': 'file_storage/call_ztbaJgeCz9oZX2eUsKrA5Vda.json'}

exec(code, env_args)
