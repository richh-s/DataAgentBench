code = """import json, os

mongo_path = '/tmp/mongodb_results_f1d6ea71.json'
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

funding_path = '/tmp/sqlite_results_83b2c1a4.json'
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

print('MongoDB docs:', len(mongo_docs))
print('Funding records:', len(funding_recs))

fema_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
results = []

for rec in funding_recs:
    proj_name = rec.get('Project_Name', '').lower()
    if any(kw in proj_name for kw in fema_keywords):
        result = {
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'topics': ', '.join([k for k in fema_keywords if k in proj_name]),
            'status': 'design',
            'type': 'disaster'
        }
        results.append(result)

print('Projects found:', len(results))

results.sort(key=lambda x: x['Amount'], reverse=True)

print('\nTop 10 projects:')
for proj in results[:10]:
    print('Name:', proj['Project_Name'])
    print('Amount:', proj['Amount'])
    print('Source:', proj['Funding_Source'])
    print('Topics:', proj['topics'])
    print('Status:', proj['status'])
    print('Type:', proj['type'])
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
