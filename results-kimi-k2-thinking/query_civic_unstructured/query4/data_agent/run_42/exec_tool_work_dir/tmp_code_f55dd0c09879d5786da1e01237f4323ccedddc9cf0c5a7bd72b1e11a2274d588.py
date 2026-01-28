code = """import json
import re

# Get data from variables
mongo_docs = var_functions.query_db:14
funding_records = var_functions.query_db:4

print('Types:', type(mongo_docs), type(funding_records))
print('Lengths:', len(mongo_docs), len(funding_records))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
