code = """import json
import re

# Load the MongoDB data from the stored file
with open('/tmp/tmpb1b8k8h6.json', 'r') as f:
    civic_docs_data = json.load(f)

print('Number of documents:', len(civic_docs_data))
print('First document keys:', list(civic_docs_data[0].keys()))

# Let's look at the first document's text to understand the format
doc = civic_docs_data[0]
text = doc['text']
print('\nFirst document text preview:')
print(text[:2000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
