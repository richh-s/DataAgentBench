code = """import json
import re
from datetime import datetime

# Load the civic documents data
civic_docs_file = var_functions.query_db:2

# Read the full data from the file
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

print(f"Number of documents: {len(civic_docs_data)}")
print(f"First document keys: {list(civic_docs_data[0].keys())}")
print(f"Sample document:\n{json.dumps(civic_docs_data[0], indent=2)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
