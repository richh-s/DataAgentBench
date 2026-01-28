code = """import json
import re
from datetime import datetime

# Read the civic documents data
civic_docs_path = var_functions.query_db_2  # This should be the file path to the JSON file
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_path = var_functions.query_db_9  # This should be the file path to the JSON file
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents and {len(funding_data)} funding records")

# Preview the data structure
if civic_docs_data:
    print(f"First civic doc: {list(civic_docs_data[0].keys())}")
    print(f"First doc text snippet: {civic_docs_data[0]['text'][:200]}")

if funding_data:
    print(f"First funding record: {funding_data[0]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
