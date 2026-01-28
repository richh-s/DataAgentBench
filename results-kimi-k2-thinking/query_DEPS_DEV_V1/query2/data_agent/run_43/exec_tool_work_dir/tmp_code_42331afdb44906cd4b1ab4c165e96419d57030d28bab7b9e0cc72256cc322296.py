code = """import json
import pandas as pd

# Load the package data from the file
with open('var_functions.query_db:5', 'r') as f:
    package_data = json.load(f)

print(f"Total packages loaded: {len(package_data)}")
print("\nFirst few records:")
for i, record in enumerate(package_data[:5]):
    print(f"\nRecord {i+1}:")
    print(json.dumps(record, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
