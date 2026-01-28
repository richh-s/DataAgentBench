code = """# Load the MongoDB query result
import json

# Read the full result from the file path stored in the variable
with open('var_functions.query_db:2', 'r') as f:
    civic_docs_result = json.load(f)

print(f"Found {len(civic_docs_result)} documents containing 'emergency' or 'FEMA'")

# Let's examine the structure of the first document
if civic_docs_result:
    print("\nFirst document preview:")
    print(f"Filename: {civic_docs_result[0]['filename']}")
    print(f"Text preview (first 500 chars):\n{civic_docs_result[0]['text'][:500]}...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
