code = """import json
import re

# Debug: Check what data we have
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:16']

# Print counts to verify data loaded
print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'sample_civic_doc': civic_docs[0] if civic_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:30': []}

exec(code, env_args)
