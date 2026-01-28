code = """import json
import os

# Load data from files
mongo_path = '/tmp/tmpb7g0r9mn.json'
funding_path = '/tmp/tmp0o2e0g2u.json'

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
results = []

try:
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
except Exception as e:
    print('Error processing records:', e)
    results = []

results.sort(key=lambda x: x['Amount'], reverse=True)

output = []
for r in results:
    output.append('%s|%s|%d|%s|%s|%s' % (
        r['Project_Name'], r['Funding_Source'], r['Amount'],
        r['Topics'], r['Status'], r['Type']
    ))

result_json = json.dumps(output)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
