code = """import json
import os
import pandas as pd

# Load funding data
funding_file = "/tmp/tmp4g9x7lxn.json"
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        content = f.read().strip()
        funding_data = json.loads(content) if content.startswith('[') else []
else:
    funding_data = []

print(f"Loaded {len(funding_data)} funding records")

if funding_data:
    df = pd.DataFrame(funding_data)
    print("Columns:", df.columns.tolist())
    print("First few rows:")
    print(df.head())
else:
    print("No funding data found")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
