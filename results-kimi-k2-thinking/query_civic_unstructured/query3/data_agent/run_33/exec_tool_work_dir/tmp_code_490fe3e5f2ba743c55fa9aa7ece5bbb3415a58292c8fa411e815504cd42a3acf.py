code = """import json
import re

civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

result_projects = []
seen = set()

for f in funding_data:
    if 'fema' in f['Project_Name'].lower():
        result_projects.append({
            'Project_Name': f['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Status not in civic docs'
        })
        seen.add(f['Project_Name'].lower())

doc_texts = [doc['text'] for doc in civic_docs]
all_text = ' '.join(doc_texts)

check_words = ['emergency', 'fema']
matched_names = []

for text in doc_texts:
    lines = text.split('\n')
    for line in lines:
        low = line.lower()
        if any(word in low for word in check_words):
            clean = line.strip()
            if len(clean) > 8 and not clean.startswith('('):
                if clean.lower() not in seen:
                    matched_names.append(clean)
                    seen.add(clean.lower())

for name in matched_names:
    found_funding = None
    for f in funding_data:
        if name in f['Project_Name'] or f['Project_Name'] in name:
            found_funding = f
            break
    
    if found_funding:
        amount = int(found_funding['Amount'])
        source = found_funding['Funding_Source']
    else:
        amount = 0
        source = 'No funding data'
    
    result_projects.append({
        'Project_Name': name,
        'Funding_Source': source,
        'Amount': amount,
        'Status': 'Mentioned in documents'
    })

result_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(result_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
