code = """import json
import re
from collections import defaultdict

# Load funding data from the stored variable
funding_data = locals()['var_functions.query_db:2']

# Load civic documents from the stored variable
civic_docs = locals()['var_functions.query_db:24']

print("Loaded data successfully")
print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Sample funding record
if funding_data:
    print(f"Sample funding: {funding_data[0]}")

# Sample civic doc
if civic_docs:
    print(f"Sample civic doc: {civic_docs[0].keys()}")

print('__RESULT__:')
print(json.dumps({"status": "loaded", "funding_count": len(funding_data), "civic_count": len(civic_docs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
