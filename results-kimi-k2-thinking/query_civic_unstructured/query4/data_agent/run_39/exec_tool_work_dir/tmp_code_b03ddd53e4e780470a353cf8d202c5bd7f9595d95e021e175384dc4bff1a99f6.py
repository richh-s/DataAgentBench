code = """import json
import re

civic_docs_file = var_functions.query_db:5
funding_file = var_functions.query_db:8

# Load the full data
try:
    # If the variables are file paths
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
except:
    # If the variables are already data
    civic_docs = var_functions.query_db:5

try:
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
except:
    funding_data = var_functions.query_db:8

print(f"Total civic documents: {len(civic_docs)}")
print(f"Total funding records: {len(funding_data)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
