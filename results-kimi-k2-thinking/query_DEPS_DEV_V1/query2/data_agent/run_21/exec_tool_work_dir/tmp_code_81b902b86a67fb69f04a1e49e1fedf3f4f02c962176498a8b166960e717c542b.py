code = """import json
import pandas as pd

# Access the stored data directly
debug_output = ""
packages_data = locals()['var_functions.query_db:0']
ppv_data = locals()['var_functions.query_db:2']

debug_output += f"Packages count: {len(packages_data)}\n"
debug_output += f"Project package version count: {len(ppv_data)}\n"

print('__RESULT__:')
print(debug_output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
