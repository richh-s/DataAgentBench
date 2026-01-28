code = """import json
import os

# Check what files exist in the current directory
files = os.listdir('.')
print("Files in current directory:")
for f in files:
    if 'query_db' in f:
        print(f)

# Check if we can access the stored variables directly
civic_key = 'var_functions.query_db:5'
funding_key = 'var_functions.query_db:2'

if civic_key in locals():
    print(f"Civic docs type: {type(locals()[civic_key])}")
if funding_key in locals():
    print(f"Funding type: {type(locals()[funding_key])}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
