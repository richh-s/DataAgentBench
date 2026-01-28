code = """import json
import os

# Load MongoDB documents
mongo_path = '/tmp/mongodb_results_f1d6ea71.json'
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Load Funding records
funding_path = '/tmp/sqlite_results_83b2c1a4.json'
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

print('Documents found:')
print('  MongoDB:', len(mongo_docs))
print('  Funding:', len(funding_recs))

# Filter for FEMA/emergency projects
fema_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
results = []

for rec in funding_recs:
    proj_name = rec.get('Project_Name', '').lower()
    if any(keyword in proj_name for keyword in fema_keywords):
        result = {
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'topics': ', '.join([k for k in fema_keywords if k in proj_name]),
            'status': 'design',
            'type': 'disaster'
        }
        results.append(result)

print('\nFEMA/Emergency projects found:', len(results))

# Sort by amount
def get_amount(proj):
    return proj['Amount']
results.sort(key=get_amount, reverse=True)

print('\nTop projects:')
for proj in results[:5]:
    print('  %s' % proj['Project_Name'])
    print('    Amount: $%d' % proj['Amount'])
    print('    Source: %s' % proj['Funding_Source'])
    print('    Topics: %s' % proj['topics'])
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
