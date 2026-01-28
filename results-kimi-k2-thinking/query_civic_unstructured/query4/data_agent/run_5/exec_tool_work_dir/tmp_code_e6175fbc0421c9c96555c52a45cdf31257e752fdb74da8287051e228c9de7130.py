code = """import json

# Read the file paths from storage
civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

print("Civic docs file:", civic_docs_file)
print("Funding file:", funding_file)

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Show first few records of each
print("\nFirst civic doc keys:", list(civic_docs[0].keys()) if civic_docs else "No docs")
print("\nFirst funding record:", funding_data[0] if funding_data else "No funding")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
