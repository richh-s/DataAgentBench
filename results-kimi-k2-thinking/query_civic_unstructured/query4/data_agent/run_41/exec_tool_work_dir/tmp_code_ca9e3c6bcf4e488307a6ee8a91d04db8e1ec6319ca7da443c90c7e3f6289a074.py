code = """import json
import re

# Load the full result from the file
with open('/tmp/tmp_d5q7p7j.json', 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")
print("Sample document structure:")
if documents:
    print(json.dumps(documents[0].keys(), indent=2))
    print(f"\nFirst document text preview (first 500 chars):")
    print(documents[0]['text'][:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
