code = """import json
import pandas as pd
from pathlib import Path

# Read the full result from the file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    documents = json.load(f)

print('__RESULT__:')
print(json.dumps({'document_count': len(documents), 'sample_documents': documents[:2]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
