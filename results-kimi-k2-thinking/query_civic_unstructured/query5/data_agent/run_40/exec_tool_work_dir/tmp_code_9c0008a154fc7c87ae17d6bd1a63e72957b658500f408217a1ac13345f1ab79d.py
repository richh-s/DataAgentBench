code = """import json
import re
from collections import defaultdict

# Load the civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:3']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Preview first civic document
if civic_docs:
    print("\nFirst civic doc preview:")
    print(f"Filename: {civic_docs[0].get('filename')}")
    print(f"Text snippet: {civic_docs[0].get('text')[:500]}...")

# Preview first few funding records
print("\nFirst few funding records:")
for i, rec in enumerate(funding_data[:5]):
    print(f"  {rec}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
