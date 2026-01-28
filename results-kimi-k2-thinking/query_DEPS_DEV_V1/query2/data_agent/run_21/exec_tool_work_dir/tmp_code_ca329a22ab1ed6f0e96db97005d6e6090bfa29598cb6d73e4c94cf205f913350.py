code = """import json
import pandas as pd

packages_data = locals()['var_functions.query_db:0']
ppv_data = locals()['var_functions.query_db:2']

debug_output = "Packages count: " + str(len(packages_data[:100])) + "\n"
debug_output += "Project package version count: " + str(len(ppv_data))

print('__RESULT__:')
print(debug_output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
