code = """import json
import os

# Load MongoDB documents
mongo_path = var_functions.query_db:2
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Load Funding records
funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Filter for FEMA/emergency projects
keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
results = []

for rec in funding_recs:
    proj_name = rec.get('Project_Name', '').lower()
    if any(kw in proj_name for kw in keywords):
        topics = [kw for kw in keywords if kw in proj_name]
        results.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Topics': ','.join(topics),
            'Status': 'design',
            'Type': 'disaster'
        })

# Sort by amount descending
results.sort(key=lambda x: x['Amount'], reverse=True)

# Convert to JSON string
output_json = json.dumps(results, indent=2)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
