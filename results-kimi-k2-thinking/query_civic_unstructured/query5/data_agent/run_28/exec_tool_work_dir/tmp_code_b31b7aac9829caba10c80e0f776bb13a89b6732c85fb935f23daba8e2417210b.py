code = """import json
import re

# Read civic documents - access via locals() since variable name contains colon
civic_docs_key = 'var_functions.query_db:2'
with open(locals()[civic_docs_key], 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_key = 'var_functions.query_db:6'
with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'sample_doc_keys': list(civic_docs[0].keys()),
    'sample_text_preview': civic_docs[0]['text'][:500]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
