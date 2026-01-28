code = """import json
import re

# Load civic documents data
civic_docs_path = var_functions_query_db__2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Number of civic documents loaded:', len(civic_docs))

# Print first document details
first_doc = civic_docs[0]
print('\nFirst document filename:', first_doc.get('filename'))
print('First document text length:', len(first_doc.get('text', '')))

# Show sample of text to understand structure
sample_text = first_doc.get('text', '')[:500]
print('\nSample text:')
print(sample_text)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
