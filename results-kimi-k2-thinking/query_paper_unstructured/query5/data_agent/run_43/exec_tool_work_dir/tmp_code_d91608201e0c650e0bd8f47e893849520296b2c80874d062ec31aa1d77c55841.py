code = """# Let's check what variables we have access to
import json
import os

# List JSON files in current directory to see what was created
files = [f for f in os.listdir('.') if f.endswith('.json')]
print('JSON files:', files)

# Try different variable access patterns
storage_keys = [k for k in globals().keys() if 'functions.query_db' in k]
print('Query DB keys:', storage_keys)

# If nothing else works, let's try to load the data by querying the sources directly
print('Attempting direct data loading...')"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
