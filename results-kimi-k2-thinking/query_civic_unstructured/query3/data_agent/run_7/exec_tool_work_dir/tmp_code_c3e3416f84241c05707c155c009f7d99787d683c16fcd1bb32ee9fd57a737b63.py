code = """import json
import os

# Try to access the variables properly
mongo_var_name = 'var_functions.query_db:2'
funding_var_name = 'var_functions.query_db:6'

# Get the file paths from the variables
mongo_file = locals().get(mongo_var_name) or globals().get(mongo_var_name)
funding_file = locals().get(funding_var_name) or globals().get(funding_var_name)

print("Mongo file path:", mongo_file)
print("Funding file path:", funding_file)

# Check if files exist
if mongo_file and os.path.exists(mongo_file):
    with open(mongo_file, 'r') as f:
        mongo_docs = json.load(f)
    print("MongoDB documents loaded:", len(mongo_docs))
else:
    print("Mongo file not accessible")
    mongo_docs = []

if funding_file and os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_recs = json.load(f)
    print("Funding records loaded:", len(funding_recs))
else:
    print("Funding file not accessible")
    funding_recs = []

print("\nFirst few funding records:")
for i, rec in enumerate(funding_recs[:3]):
    print("  %d. %s" % (i+1, rec.get('Project_Name', '')))

print("\nFirst few project references:")
for i, doc in enumerate(mongo_docs[:1]):
    print("Document %d:" % (i+1))
    text = doc.get('text', '')[:500]
    print(text)
    print("...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
