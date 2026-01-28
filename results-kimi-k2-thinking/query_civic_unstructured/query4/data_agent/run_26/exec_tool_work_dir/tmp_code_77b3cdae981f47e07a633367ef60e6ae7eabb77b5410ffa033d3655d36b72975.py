code = """# Load and examine the data
import json

# Load the civic documents data
civic_docs_file = var_functions.query_db:0
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")
print("\nFirst civic document preview:")
print(json.dumps(civic_docs[0], indent=2)[:1000])
print("\nFirst funding record:")
print(json.dumps(funding_data[0], indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
