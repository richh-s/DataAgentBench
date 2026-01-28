code = """import json

# Get the file paths from storage
civic_docs_path = locals()['var_functions.query_db:0']
funding_data_path = locals()['var_functions.query_db:2']

print("Civic docs path:", civic_docs_path)
print("Funding data path:", funding_data_path)

# Check if the first one is already loaded data or a file path
if isinstance(civic_docs_path, list):
    civic_docs = civic_docs_path
    print("Civic docs data is already loaded as a list")
else:
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
    print("Civic docs data loaded from file")

if isinstance(funding_data_path, list):
    funding_data = funding_data_path
    print("Funding data is already loaded as a list")
else:
    with open(funding_data_path, 'r') as f:
        funding_data = json.load(f)
    print("Funding data loaded from file")

print("\nTotal records loaded:")
print("- Civic documents:", len(civic_docs))
print("- Funding records:", len(funding_data))

if civic_docs:
    print("\nFirst civic doc keys:", list(civic_docs[0].keys()))
    print("First civic doc filename:", civic_docs[0].get('filename'))

if funding_data:
    print("\nFirst funding record:")
    for key, value in funding_data[0].items():
        print(f"- {key}: {value}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
