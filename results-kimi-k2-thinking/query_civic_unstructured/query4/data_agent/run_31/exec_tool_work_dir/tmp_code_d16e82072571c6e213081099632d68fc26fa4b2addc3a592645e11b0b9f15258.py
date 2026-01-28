code = """import json
import pandas as pd

# Access the result from the storage using the key name
results = locals().get('var_functions.query_db:2', [])

print(f"Number of documents: {len(results)}")
if results:
    print(f"First document keys: {results[0].keys()}")
    print("Sample document:")
    print(json.dumps(results[0], indent=2))
else:
    print("No data found")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
