code = """import json
import pandas as pd

# The storage variable contains a file path
file_path = var_functions.query_db:2

# Read the package data from the file
with open(file_path, 'r') as f:
    package_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'num_records': len(package_data),
    'first_record': package_data[0] if package_data else None,
    'columns': list(package_data[0].keys()) if package_data else []
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
