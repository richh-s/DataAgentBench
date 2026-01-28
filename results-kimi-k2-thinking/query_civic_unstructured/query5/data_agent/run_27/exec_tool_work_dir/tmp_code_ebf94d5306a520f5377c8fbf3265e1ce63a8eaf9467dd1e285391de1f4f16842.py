code = """import json

# Get the file paths from storage 
funding_file_var = 'var_functions.query_db:5'
civic_file_var = 'var_functions.query_db:6'

funding_file = locals()[funding_file_var]
civic_file = locals()[civic_file_var]

print("Funding file path:", funding_file)
print("Civic file path:", civic_file)

# Read funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print("\nFunding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Show a few sample funding records
print("\nSample funding records:")
for i, record in enumerate(funding_data[:3]):
    print("  ", record)

# Show a sample civic doc
print("\nSample civic doc:")
print("  Filename:", civic_docs[0]['filename'])
print("  Text length:", len(civic_docs[0]['text']), "characters")
print("  Text preview:", civic_docs[0]['text'][:300], "...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
