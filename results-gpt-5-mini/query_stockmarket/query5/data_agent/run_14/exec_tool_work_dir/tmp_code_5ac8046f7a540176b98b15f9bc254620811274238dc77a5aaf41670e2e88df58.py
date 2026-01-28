code = """import json
import os
# Load previous tool results
with open(var_call_HGyGjC7o6mlyzGcV9YqRot21, 'r') as f:
    data_stockinfo = json.load(f)
with open(var_call_EEujyNWciR62lhYczKx9JiG1, 'r') as f:
    data_stocktrade_tables = json.load(f)

symbols_info = {item['Symbol']: item.get('Company Description','') for item in data_stockinfo}

tables = set(data_stocktrade_tables)
common_symbols = [s for s in symbols_info.keys() if s in tables]

result = {'symbols': common_symbols, 'companies': {s: symbols_info[s] for s in common_symbols}}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EEujyNWciR62lhYczKx9JiG1': 'file_storage/call_EEujyNWciR62lhYczKx9JiG1.json', 'var_call_HGyGjC7o6mlyzGcV9YqRot21': 'file_storage/call_HGyGjC7o6mlyzGcV9YqRot21.json'}

exec(code, env_args)
