code = """import json

# Access the stored variables more carefully
civic_docs_var = locals()['var_functions.query_db:4']
funding_var = locals()['var_functions.query_db:5']

print("Type of civic_docs_var:", type(civic_docs_var))
print("Type of funding_var:", type(funding_var))

# If they're strings (file paths), load them
if isinstance(civic_docs_var, str):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

if isinstance(funding_var, str):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Show sample data
if civic_docs:
    print("Sample civic doc keys:", list(civic_docs[0].keys()))
if funding_data:
    print("Sample funding record:", funding_data[0])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
