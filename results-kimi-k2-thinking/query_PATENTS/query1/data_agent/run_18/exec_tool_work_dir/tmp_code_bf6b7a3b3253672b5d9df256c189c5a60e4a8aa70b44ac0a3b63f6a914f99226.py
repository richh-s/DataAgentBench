code = """import json
import os

# Let's see what variables we have
all_vars = list(locals().keys())
print('All local variables:')
for var in sorted(all_vars):
    if 'query_db' in str(var):
        print(f'  {var}')

# Check if we can access them directly
if 'var_functions.query_db:10' in locals():
    pub_file = locals()['var_functions.query_db:10']
    print(f'Publication file: {pub_file}')
    
if 'var_functions.query_db:12' in locals():
    cpc_file = locals()['var_functions.query_db:12']
    print(f'CPC file: {cpc_file}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
