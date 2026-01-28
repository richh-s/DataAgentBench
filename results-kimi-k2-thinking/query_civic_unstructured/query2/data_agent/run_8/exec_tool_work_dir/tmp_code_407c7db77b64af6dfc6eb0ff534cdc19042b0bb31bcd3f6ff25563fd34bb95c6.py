code = """import json
import pandas as pd
import re

all_vars = list(locals().keys())
print('Available variables count:', len(all_vars))

for var in all_vars:
    if 'query_db' in var:
        print('Found variable:', var)
        value = locals()[var]
        print('Type:', type(value))
        if isinstance(value, str):
            print('Length:', len(value))
            print('Preview:', value[:200])
        else:
            print('Length:', len(value) if hasattr(value, '__len__') else 'N/A')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
