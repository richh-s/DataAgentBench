code = """import json
import re

# Load the documents from the previous query
documents_path = locals()['var_functions.query_db:0']
with open(documents_path, 'r') as f:
    documents = json.load(f)

print('__RESULT__:')
result_msg = f'Found {len(documents)} documents'

# Let's examine the first document structure
if documents:
    first_keys = list(documents[0].keys())
    text_sample = documents[0]['text'][:500]
    
    # Count occurrences of emergency/FEMA in the documents
    emergency_count = sum(1 for doc in documents if 'emergency' in doc['text'].lower())
    fema_count = sum(1 for doc in documents if 'fema' in doc['text'].lower())
    
    result_dict = {
        'message': result_msg,
        'first_doc_keys': first_keys,
        'text_sample_preview': text_sample,
        'emergency_count': emergency_count,
        'fema_count': fema_count,
        'total_docs': len(documents)
    }
    print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
