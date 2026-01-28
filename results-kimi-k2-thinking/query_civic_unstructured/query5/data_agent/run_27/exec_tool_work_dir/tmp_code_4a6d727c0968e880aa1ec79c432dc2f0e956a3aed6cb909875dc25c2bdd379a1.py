code = """import json
import re
from datetime import datetime

# Read funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Show a few sample funding records
print("\nSample funding records:")
for i, record in enumerate(funding_data[:5]):
    print(f"  {record}")

# Show a sample civic doc
print(f"\nSample civic doc:")
print(f"  Filename: {civic_docs[0]['filename']}")
print(f"  Text preview: {civic_docs[0]['text'][:500]}...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
