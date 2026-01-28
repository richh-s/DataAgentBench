code = """import json
import re
from datetime import datetime

# Load the full result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")
print("\nFirst document structure:")
print(f"Keys: {documents[0].keys()}")
print(f"\nFilename: {documents[0]['filename']}")
print(f"\nText preview (first 500 chars):")
print(documents[0]['text'][:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
