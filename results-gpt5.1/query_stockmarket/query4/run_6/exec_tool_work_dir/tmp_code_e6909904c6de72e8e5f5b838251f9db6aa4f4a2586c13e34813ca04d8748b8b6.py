code = """import json, pandas as pd
from pathlib import Path

# load full symbol list from stocktrade_database list_db
symbols_file = Path(var_call_j1hBv3V3ZZWOpa4mStXWTXtX)
symbols = json.loads(symbols_file.read_text())

# load NYSE non-ETF symbols
nyse_file = Path(var_call_WRHKc34y7FBeKhsb9Vlccuk3)
nyse_records = json.loads(nyse_file.read_text())
nyse_symbols = {r['Symbol']: r['Company'] for r in nyse_records}

# intersect
common = [s for s in symbols if s in nyse_symbols]

result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_j1hBv3V3ZZWOpa4mStXWTXtX': 'file_storage/call_j1hBv3V3ZZWOpa4mStXWTXtX.json', 'var_call_WRHKc34y7FBeKhsb9Vlccuk3': 'file_storage/call_WRHKc34y7FBeKhsb9Vlccuk3.json'}

exec(code, env_args)
