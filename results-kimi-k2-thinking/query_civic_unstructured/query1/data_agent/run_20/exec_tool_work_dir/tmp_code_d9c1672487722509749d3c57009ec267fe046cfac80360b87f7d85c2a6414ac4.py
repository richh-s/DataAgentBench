code = """import json, os
# Load funding data
key0 = 'var_functions.query_db:0'
with open(locals()[key0], 'r') as f:
    funding_data = json.load(f)
print('Funding records count:', len(funding_data))
print('Sample funding record:', funding_data[:3])
# Load civic docs data
key2 = 'var_functions.query_db:2'
with open(locals()[key2], 'r') as f:
    civic_docs = json.load(f)
print('Civic docs count:', len(civic_docs))
print('Sample civic doc structure:', dict(civic_docs[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
