code = """import json
import os

# Get the stored result variables
mongo_result_key = 'var_functions.query_db:2'
funding_result_key = 'var_functions.query_db:6'

# Access the variables from the storage
mongo_docs = None
funding_recs = None

# Try to access from locals or globals
try:
    mongo_path = eval(mongo_result_key)
    with open(mongo_path, 'r') as f:
        mongo_docs = json.load(f)
except:
    print('Failed to load MongoDB docs')

try:
    funding_path = eval(funding_result_key)
    with open(funding_path, 'r') as f:
        funding_recs = json.load(f)
except:
    print('Failed to load funding records')

print('Documents loaded:')
print('  MongoDB:', len(mongo_docs) if mongo_docs else 0)
print('  Funding:', len(funding_recs) if funding_recs else 0)

# Process the funding records to find FEMA/emergency projects
if funding_recs:
    keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
    results = []
    
    for rec in funding_recs:
        proj_name = rec.get('Project_Name', '').lower()
        if any(kw in proj_name for kw in keywords):
            topics = []
            for kw in keywords:
                if kw in proj_name:
                    topics.append(kw)
            
            results.append({
                'Project_Name': rec['Project_Name'],
                'Funding_Source': rec['Funding_Source'],
                'Amount': int(rec['Amount']),
                'Topics': ','.join(topics),
                'Status': 'design',
                'Type': 'disaster'
            })
    
    print('\nFEMA/emergency projects found:', len(results))
    
    # Sort by amount
    results.sort(key=lambda x: x['Amount'], reverse=True)
    
    for proj in results:
        print('\nProject: %s' % proj['Project_Name'])
        print('Funding Source: %s' % proj['Funding_Source'])
        print('Amount: $%d' % proj['Amount'])
        print('Status: %s' % proj['Status'])
        print('Type: %s' % proj['Type'])
        print('Topics: %s' % proj['Topics'])
else:
    results = []

# Return the results as JSON
print('__RESULT__:')
print(json.dumps(results[:10], indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
