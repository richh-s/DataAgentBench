code = """import json
import re
from datetime import datetime

# Load civic documents from file
with open('var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file  
with open('var_functions.query_db:3.json', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# First, let's examine the structure of civic documents
sample_doc = civic_docs[0]
print(f"\nSample civic doc keys: {list(sample_doc.keys())}")
print(f"Sample civic doc filename: {sample_doc.get('filename')}")
print("Sample civic doc text preview: " + sample_doc.get('text')[:500] + "...")

# Let's also examine funding data structure
print(f"\nSample funding record: {funding_data[0]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
