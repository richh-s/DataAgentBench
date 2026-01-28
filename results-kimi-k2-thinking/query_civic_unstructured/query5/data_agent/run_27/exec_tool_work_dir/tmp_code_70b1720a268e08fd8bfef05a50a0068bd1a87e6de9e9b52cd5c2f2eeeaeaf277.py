code = """import json
import re

# Read the JSON files
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Show sample data
print("\nSample funding record:", funding_data[0])
print("\nSample civic doc keys:", list(civic_docs[0].keys()))
print("Sample civic doc filename:", civic_docs[0]['filename'])
print("Sample civic doc text preview:", civic_docs[0]['text'][:300], "...")

result = {"funding_count": len(funding_data), "civic_count": len(civic_docs)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}}

exec(code, env_args)
