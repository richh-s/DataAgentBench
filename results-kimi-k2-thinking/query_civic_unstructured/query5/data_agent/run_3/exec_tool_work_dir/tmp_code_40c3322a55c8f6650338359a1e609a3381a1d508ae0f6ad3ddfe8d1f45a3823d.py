code = """import json
import pandas as pd
import re

# Access the civic documents data from storage
civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

print(f"Loaded {len(civic_docs_data)} documents from civic_docs_database")
print("Sample document keys:", list(civic_docs_data[0].keys()) if civic_docs_data else "No data")

print(f"Loaded {len(funding_data)} funding records from funding_database")
print("Sample funding record:", funding_data[0] if funding_data else "No data")

# Check the first few documents to understand the structure
if civic_docs_data:
    doc1 = civic_docs_data[0]
    print("\nFirst document filename:", doc1.get('filename'))
    print("Text preview (first 500 chars):", doc1.get('text', '')[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
