code = """import json

# Read the full result from the file
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents: ' + str(len(civic_docs)))

# Let's examine the structure of the first document to understand how to parse it
first_doc = civic_docs[0]
print('First document keys: ' + str(first_doc.keys()))
text_preview = first_doc['text'][:500]
print('First document text preview: ' + text_preview)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
