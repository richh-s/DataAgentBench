code = """import json, pandas as pd
symbols_info = pd.read_json(var_call_32XrmsBmoMXkSCSQ7hwoVIGX)
# limit symbols to those also present in stocktrade_database list
all_tables = pd.read_json(var_call_WbpWpWrT3v20W6oT6Am1q5lA)
tradable = symbols_info[symbols_info['Symbol'].isin(all_tables[0])]['Symbol'].tolist()
result = json.dumps(tradable)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_WbpWpWrT3v20W6oT6Am1q5lA': 'file_storage/call_WbpWpWrT3v20W6oT6Am1q5lA.json', 'var_call_32XrmsBmoMXkSCSQ7hwoVIGX': 'file_storage/call_32XrmsBmoMXkSCSQ7hwoVIGX.json'}

exec(code, env_args)
