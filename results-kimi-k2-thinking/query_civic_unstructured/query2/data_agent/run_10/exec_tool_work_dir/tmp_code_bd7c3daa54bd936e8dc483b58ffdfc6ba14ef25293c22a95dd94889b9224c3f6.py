code = """import json
import re

# Get the civic documents data from the variable
# The key is 'var_functions.query_db:2'
civic_docs_data = locals().get('var_functions.query_db:2')

if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    # It's a file path
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    # It's already the data
    civic_docs = civic_docs_data

print('__RESULT__:')
print(json.dumps({
    "num_documents": len(civic_docs) if civic_docs else 0,
    "type": str(type(civic_docs)),
    "data_preview": str(civic_docs)[:500] if civic_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
