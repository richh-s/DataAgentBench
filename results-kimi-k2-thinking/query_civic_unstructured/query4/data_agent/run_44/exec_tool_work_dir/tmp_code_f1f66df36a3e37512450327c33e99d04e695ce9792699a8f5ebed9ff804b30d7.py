code = """import json
import re

# Read the full result from the file
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

# Let's examine the structure of the first document to understand how to parse it
first_doc = civic_docs[0]
print('\nFirst document keys: ' + str(first_doc.keys()))
print('First document text preview: ' + first_doc['text'][:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
