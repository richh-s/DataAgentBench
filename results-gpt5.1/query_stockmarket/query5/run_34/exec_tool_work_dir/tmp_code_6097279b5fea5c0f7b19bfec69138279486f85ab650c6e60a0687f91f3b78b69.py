code = """import json, pandas as pd
symbols_info_path = var_call_aqFejGVlsniDcjfv1ws7Py2w
with open(symbols_info_path, 'r') as f:
    symbols_info = json.load(f)
syms = [r['Symbol'] for r in symbols_info]
all_tables_path = var_call_Y6VKBWpuBLO5UEMFYEGRu28y
with open(all_tables_path, 'r') as f:
    all_tables = json.load(f)
available = sorted(set(syms) & set(all_tables))
result = json.dumps(available)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Y6VKBWpuBLO5UEMFYEGRu28y': 'file_storage/call_Y6VKBWpuBLO5UEMFYEGRu28y.json', 'var_call_aqFejGVlsniDcjfv1ws7Py2w': 'file_storage/call_aqFejGVlsniDcjfv1ws7Py2w.json'}

exec(code, env_args)
