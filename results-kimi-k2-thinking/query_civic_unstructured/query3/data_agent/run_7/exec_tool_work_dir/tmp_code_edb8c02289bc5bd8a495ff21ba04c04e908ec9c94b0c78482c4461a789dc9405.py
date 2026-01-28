code = """import json, os

# Load MongoDB documents
mongo_path = '/tmp/mongodb_results_f1d6ea71.json'
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Load Funding records  
funding_path = '/tmp/sqlite_results_83b2c1a4.json'
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

print('MongoDB docs:', len(mongo_docs))
print('Funding records:', len(funding_recs))

# Filter funding for emergency/FEMA projects
emergency_projects = []
fema_keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']

for rec in funding_recs:
    name = rec.get('Project_Name', '').lower()
    if any(kw in name for kw in fema_keywords):
        rec['topics'] = ','.join([kw for kw in fema_keywords if kw in name])
        rec['type'] = 'disaster'
        rec['status'] = 'design' 
        emergency_projects.append(rec)

print('\nEmergency/FEMA funding records:', len(emergency_projects))
for proj in emergency_projects[:10]:
    print('  %s: %s ($%s)' % (proj['Project_Name'], proj['Funding_Source'], proj['Amount']))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
