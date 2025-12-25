code = """import json

symbols_info = var_call_VpDgoA7fXkQOcSnmZFJBToDI

# load full list of trade tables
import pandas as pd
from pathlib import Path

# read list_db result file
trade_tables_path = var_call_z0vUN3AiZB3aOsmYx8b60Vnr
with open(trade_tables_path, 'r') as f:
    trade_tables = json.load(f)

nasdaq_cap_symbols = {row['Symbol']: row['Company Description'] for row in symbols_info}

common_symbols = [s for s in trade_tables if s in nasdaq_cap_symbols]

result = json.dumps({'symbols': common_symbols[:50]})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_z0vUN3AiZB3aOsmYx8b60Vnr': 'file_storage/call_z0vUN3AiZB3aOsmYx8b60Vnr.json', 'var_call_VpDgoA7fXkQOcSnmZFJBToDI': 'file_storage/call_VpDgoA7fXkQOcSnmZFJBToDI.json'}

exec(code, env_args)
