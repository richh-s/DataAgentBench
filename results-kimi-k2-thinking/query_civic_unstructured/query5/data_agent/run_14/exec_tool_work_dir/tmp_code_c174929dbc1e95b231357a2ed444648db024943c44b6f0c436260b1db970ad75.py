code = """import json
import re

result_path = locals()['var_functions.query_db:2']

with open(result_path, 'r') as f:
    civic_docs = json.load(f)

print('Number of documents:', len(civic_docs))
if civic_docs:
    print('Keys:', list(civic_docs[0].keys()))
    print('Sample text:', civic_docs[0]['text'][:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
