code = """import json
import os

# Load funding data to inspect structure
funding_file_path = '/tmp/tmp4g9x7lxn.json'

with open(funding_file_path, 'r') as f:
    content = f.read(5000)  # Read first 5000 chars
    print("File content preview:")
    print(content[:1000])
    print("\nFile length:", len(content))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
