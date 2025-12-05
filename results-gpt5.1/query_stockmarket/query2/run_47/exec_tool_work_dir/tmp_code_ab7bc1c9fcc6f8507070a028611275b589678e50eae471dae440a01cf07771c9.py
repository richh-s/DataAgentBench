code = """import json, pandas as pd
from pathlib import Path

# Load full NYSE Arca ETF symbol list
file_path = Path(var_call_8KSzzxCHWv2ZIXGSkL4t3J5w)
nyse_arca_symbols = pd.read_json(file_path).Symbol.tolist()

# Intersect with available price tables
tables = var_call_3E9lJPVwJ03G9FQMygMt8JoZ
available = set(tables)
symbols = [s for s in nyse_arca_symbols if s in available]

result = json.dumps(symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_8KSzzxCHWv2ZIXGSkL4t3J5w': 'file_storage/call_8KSzzxCHWv2ZIXGSkL4t3J5w.json', 'var_call_3E9lJPVwJ03G9FQMygMt8JoZ': 'file_storage/call_3E9lJPVwJ03G9FQMygMt8JoZ.json'}

exec(code, env_args)
