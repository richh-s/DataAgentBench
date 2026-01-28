code = """import json
import os

# Load the MongoDB and Funding data from the files
mongo_path = '/tmp/mongodb_results_f1d6ea71.json'
funding_path = '/tmp/sqlite_results_83b2c1a4.json'

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

print('Loaded', len(mongo_docs), 'MongoDB documents and', len(funding_recs), 'funding records')

# Find FEMA/emergency projects in funding data
keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
projects = []

for rec in funding_recs:
    name = rec.get('Project_Name', '').lower()
    if any(kw in name for kw in keywords):
        topics = [kw for kw in keywords if kw in name]
        projects.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Topics': ', '.join(topics),
            'Status': 'design',
            'Type': 'disaster'
        })

print('Found', len(projects), 'FEMA/emergency projects')

# Sort by amount descending
projects.sort(key=lambda x: x['Amount'], reverse=True)

print('\nAll projects:')
for proj in projects:
    print('Project:', proj['Project_Name'])
    print('Funding Source:', proj['Funding_Source'])
    print('Amount: $', proj['Amount'], sep='')
    print('Status:', proj['Status'])
    print('Type:', proj['Type'])
    print('Topics:', proj['Topics'])
    print('---')

result = json.dumps(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
