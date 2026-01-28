code = """import json
import sys

# Load funding data
funding_path = var_functions.query_db_6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load mongo data
mongo_path = var_functions.query_db_2
with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Mongo docs: {len(mongo_data)}")

# Count funding > 50k
count_50k = sum(1 for f in funding_data if int(f['Amount']) > 50000)
print(f"Funding > 50k: {count_50k}")

# Sample
for f in funding_data[:5]:
    print(f"  {f['Project_Name']}: ${f['Amount']}")

# Extract design projects
projects = []
for doc in mongo_data:
    if 'Capital Improvement Projects (Design)' in doc.get('text', ''):
        projects.append(doc['_id'])

print(f"\nDocs with Design section: {len(projects)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
