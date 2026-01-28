code = """# Access the stored data directly
# First, let's see what variables are available
import json
import pandas as pd
import re

# The data should be in var_functions.query_db_6
print("Checking available variables...")
available_vars = [name for name in dir() if name.startswith('var_')]
print(f"Available variables: {available_vars}")

# Let's access the data
if 'var_functions.query_db_6' in globals():
    pub_data = var_functions.query_db_6
    print(f"Type of data: {type(pub_data)}")
    if isinstance(pub_data, str) and pub_data.endswith('.json'):
        # It's a file path
        with open(pub_data, 'r') as f:
            pub_data = json.load(f)
    print(f"Loaded {len(pub_data)} records")
elif 'var_functions.query_db_5' in globals():
    pub_data = var_functions.query_db_5
    print(f"Using preview data, type: {type(pub_data)}")
else:
    print("No data found in expected variables")
    pub_data = []"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
