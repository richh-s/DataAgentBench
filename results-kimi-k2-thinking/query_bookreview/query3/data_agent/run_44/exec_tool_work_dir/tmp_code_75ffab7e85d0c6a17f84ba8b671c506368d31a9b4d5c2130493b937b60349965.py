code = """import json
import pandas as pd

# Check what's available in the environment
print('Available variables:')
for key in list(locals().keys()):
    if 'functions.query_db' in key:
        print(f"Found variable: {key}")"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
