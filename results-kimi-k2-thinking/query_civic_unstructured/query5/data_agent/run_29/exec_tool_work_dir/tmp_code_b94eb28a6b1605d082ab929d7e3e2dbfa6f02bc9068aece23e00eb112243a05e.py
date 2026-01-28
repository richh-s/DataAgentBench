code = """# First, let's examine what we actually have in storage
import json

civic_docs = var_functions.query_db:2
funding_records = var_functions.query_db:5

print('Civic docs type:', type(civic_docs))
print('Number of civic docs:', len(civic_docs))
print('First civic doc keys:', list(civic_docs[0].keys()) if civic_docs else 'No docs')

print('Funding records type:', type(funding_records))
print('Number of funding records:', len(funding_records))
print('First funding record:', funding_records[0] if funding_records else 'No records')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
