code = """import json

# Read the civic documents
civic_file = open('/tmp/tmpq0c3uww8.json')
civic_docs = json.load(civic_file)
civic_file.close()

print('Loaded', len(civic_docs), 'documents')

# Read funding data
funding_file = open('/tmp/tmphv6u7l7_.json')
funding_data = json.load(funding_file)
funding_file.close()

print('Loaded', len(funding_data), 'funding records')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
