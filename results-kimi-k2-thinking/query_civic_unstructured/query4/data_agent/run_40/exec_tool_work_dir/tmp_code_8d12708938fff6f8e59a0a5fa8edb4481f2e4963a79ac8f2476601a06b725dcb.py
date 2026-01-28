code = """import json
import re

# Access the data from variables (they should be lists already)
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:2']

print("Data loaded successfully")
print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Show first few records to understand structure
if funding_data:
    print("\nFirst funding record:", json.dumps(funding_data[0], indent=2))
    
if civic_docs:
    print("\nFirst civic doc keys:", list(civic_docs[0].keys()))
    print("\nFirst civic doc text snippet:", civic_docs[0]['text'][:1000])

print("Done with debug")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
