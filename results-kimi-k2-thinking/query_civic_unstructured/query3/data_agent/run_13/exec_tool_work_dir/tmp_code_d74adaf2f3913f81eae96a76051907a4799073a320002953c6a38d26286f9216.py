code = """import json

# Access MongoDB results
mongo_file_path = locals()['var_functions.query_db:2']
print("MongoDB file path:", mongo_file_path)

# Read the JSON file
with open(mongo_file_path, 'r') as f:
    civic_docs = json.load(f)

print("Loaded documents:", len(civic_docs))
print("First document keys:", list(civic_docs[0].keys()))

# Access Funding results  
funding_file_path = locals()['var_functions.query_db:5']
print("\nFunding file path:", funding_file_path)

# Read the JSON file
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

print("Loaded funding records:", len(funding_data))
print("First funding record:", funding_data[0])

# Now let's extract project information from civic_docs
# We'll search for projects with 'emergency' or 'FEMA' in the text

emergency_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'emergency' in text or 'fema' in text:
        # Extract project names and details from this text
        # For now, let's just collect the document
        emergency_projects.append(doc)

print("\nDocuments containing emergency/FEMA:", len(emergency_projects))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
