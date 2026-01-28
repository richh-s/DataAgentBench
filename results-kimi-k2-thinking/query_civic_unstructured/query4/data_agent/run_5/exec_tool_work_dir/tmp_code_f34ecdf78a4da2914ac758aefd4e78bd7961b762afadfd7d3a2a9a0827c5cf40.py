code = """# Direct approach - get the data from storage
import json

# Get the file paths stored from the query_db calls (2 and 3)
civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

print("Loading from files...")
print(f"Civic docs file: {civic_docs_file}")
print(f"Funding file: {funding_file}")

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Let's check the structure
if civic_docs:
    print(f"First civic doc has keys: {list(civic_docs[0].keys())}")
if funding_data:
    print(f"First funding record: {funding_data[0]}")
    print(f"Amount type: {type(funding_data[0]['Amount'])}")
    print(f"Funding_ID type: {type(funding_data[0]['Funding_ID'])}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
