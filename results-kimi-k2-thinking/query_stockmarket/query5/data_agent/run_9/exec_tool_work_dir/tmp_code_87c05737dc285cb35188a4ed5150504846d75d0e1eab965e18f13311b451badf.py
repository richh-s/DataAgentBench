code = """import json
import os

# Access NASDAQ Capital Market stocks file
nasdaq_file_path = 'var_functions.query_db:4'
print("NASDAQ file path:", nasdaq_file_path)

# Access trade tables file
trade_file_path = 'var_functions.list_db:8'  
print("Trade file path:", trade_file_path)

# Print result in required format
print("__RESULT__:")
print(json.dumps({
    "nasdaq_path": nasdaq_file_path,
    "trade_path": trade_file_path
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
