code = """import json
import pandas as pd
import re

civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

print('Loaded', len(civic_docs_data), 'documents from civic_docs_database')
if civic_docs_data:
    print('Sample document keys:', list(civic_docs_data[0].keys()))

print('Loaded', len(funding_data), 'funding records from funding_database')
if funding_data:
    print('Sample funding record:', funding_data[0])

if civic_docs_data:
    doc1 = civic_docs_data[0]
    print('First document filename:', doc1.get('filename'))
    print('Text preview (first 500 chars):', doc1.get('text', '')[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
