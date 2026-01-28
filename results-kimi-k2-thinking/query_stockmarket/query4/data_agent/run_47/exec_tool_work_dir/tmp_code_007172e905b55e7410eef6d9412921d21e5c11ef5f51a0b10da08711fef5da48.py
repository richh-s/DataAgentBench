code = """import json
import glob
import os

# Check what temp files exist
tmp_files = glob.glob('/tmp/*.json')
print(f"Temp files found: {tmp_files}")

# Also check if there's a variable in locals
if 'var_functions.query_db:0' in locals():
    print("var_functions.query_db:0 found in locals")
    print(f"Type: {type(locals()['var_functions.query_db:0'])}")
    if isinstance(locals()['var_functions.query_db:0'], str):
        print(f"It's a string (file path): {locals()['var_functions.query_db:0']}")
    else:
        print(f"It's data, not a file path")
        # Try to use it directly
        nyse_stocks = locals()['var_functions.query_db:0']
        symbols = [stock['Symbol'] for stock in nyse_stocks]
        print(f"Symbols extracted: {len(symbols)}")
        print(f"First 10: {symbols[:10]}")
        result = {"file_path": None, "symbols": symbols, "count": len(symbols)}
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
