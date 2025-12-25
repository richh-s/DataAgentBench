code = """import json
import pandas as pd
symbols_file = var_call_yAwZzrWyQVMkKPkWYf9G6yca
with open(symbols_file, 'r') as f:
    all_symbols = json.load(f)
info_file = var_call_wjDF1reXZ8tTsle6jzEeVTds
with open(info_file, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
cap_syms = set(info_df['Symbol'])
valid_syms = [s for s in all_symbols if s in cap_syms]
result = json.dumps(valid_syms)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yAwZzrWyQVMkKPkWYf9G6yca': 'file_storage/call_yAwZzrWyQVMkKPkWYf9G6yca.json', 'var_call_wjDF1reXZ8tTsle6jzEeVTds': 'file_storage/call_wjDF1reXZ8tTsle6jzEeVTds.json'}

exec(code, env_args)
