code = """import json
import pandas as pd

# Check what the variable contains
print(f"Type of var_functions.query_db:2: {type(var_functions.query_db:2)}")
print(f"Value of var_functions.query_db:2: {var_functions.query_db:2}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
