code = """import json

# Load civic documents from file
with open('var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file  
with open('var_functions.query_db:3.json', 'r') as f:
    funding_data = json.load(f)

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Examine civic document structure
sample_doc = civic_docs[0]
print('\nSample civic doc keys: ' + str(list(sample_doc.keys())))
print('Sample civic doc filename: ' + str(sample_doc.get('filename')))
print('Sample civic doc text preview: ' + sample_doc.get('text')[:500] + '...')

# Examine funding data structure
print('\nSample funding record: ' + str(funding_data[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
