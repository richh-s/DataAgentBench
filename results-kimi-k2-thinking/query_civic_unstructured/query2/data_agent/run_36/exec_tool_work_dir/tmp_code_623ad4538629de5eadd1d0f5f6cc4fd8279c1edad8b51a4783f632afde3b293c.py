code = """import json
import pandas as pd
import os

# Load data from files
print("Loading data from files...")

# Load park documents (completed in 2022 with park topic)
park_file = "/tmp/tmprv7m5z8x.json"
if os.path.exists(park_file):
    with open(park_file, 'r') as f:
        park_docs = json.load(f)
    print(f"Loaded {len(park_docs)} park-related documents")
else:
    park_docs = []
    print("Park file not found")

# Load funding data
funding_file = "/tmp/tmp4g9x7lxn.json"
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            funding_data = json.loads(content)
        else:
            funding_data = []
    print(f"Loaded {len(funding_data)} funding records")
else:
    funding_data = []
    print("Funding file not found")

# Prepare data
if funding_data:
    funding_df = pd.DataFrame(funding_data)
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')
    print("Funding data prepared")
else:
    print("No funding data")

print("Data loading complete")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
