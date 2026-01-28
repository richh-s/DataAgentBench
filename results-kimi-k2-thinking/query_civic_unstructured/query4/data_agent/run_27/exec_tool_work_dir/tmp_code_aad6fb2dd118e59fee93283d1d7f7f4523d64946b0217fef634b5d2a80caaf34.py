code = """import json
import re

# Access the variables from storage using string keys
mongo_var = 'var_functions.query_db:5'
funding_var = 'var_functions.query_db:20'

mongo_path = globals()[mongo_var]
funding_path = globals()[funding_var]

# Load the data
with open(mongo_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded data successfully')
print('Civic docs count:', len(civic_docs))
print('Funding records count:', len(funding_records))

# Process documents
doc_with_2022 = []
for i, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    if '2022' in text:
        doc_with_2022.append((i, doc.get('filename', '')))

print('Documents containing 2022:', len(doc_with_2022))

# Check first document structure
if civic_docs:
    first_doc = civic_docs[0]
    print('First doc keys:', list(first_doc.keys()))
    print('First doc filename:', first_doc.get('filename'))
    print('First doc text sample:', first_doc.get('text', '')[:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
