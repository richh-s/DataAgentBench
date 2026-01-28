code = """import json
# Read the full stock info results
with open('var_functions.list_db:0', 'r') as f:
    stock_info_result = json.load(f)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
