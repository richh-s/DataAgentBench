code = """import json
import os

# Load funding data directly from known file path
try:
    funding_var = globals()['var_functions.query_db:46']
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
    print('Loaded funding data:', len(funding_data))
except:
    funding_data = []
    print('Could not load funding data')

# Load civic data directly from known file path
try:
    civic_var = globals()['var_functions.query_db:5']
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
    print('Loaded civic docs:', len(civic_docs))
except:
    civic_docs = []
    print('Could not load civic docs')

# Now analyze the data
if funding_data and civic_docs:
    # Create funding lookup
    funded_projects = {}
    for rec in funding_data:
        amt = int(rec['Amount'])
        if amt > 50000:
            funded_projects[rec['Project_Name']] = amt
    
    print('High-funded projects:', len(funded_projects))
    
    # Search for capital design projects
    matches = []
    all_text = ''
    for doc in civic_docs:
        all_text += ' ' + doc['text']
    
    text_lower = all_text.lower()
    for project_name in funded_projects:
        if project_name.lower() in text_lower:
            idx = text_lower.find(project_name.lower())
            context = text_lower[max(0, idx-200):idx+400]
            if 'capital' in context and 'design' in context:
                matches.append(project_name)
    
    unique_matches = list(set(matches))
    print('Capital design projects >$50k:', len(unique_matches))
    
    result = {'count': len(unique_matches), 'projects': unique_matches}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    result = {'count': 0, 'projects': [], 'error': 'Missing data'}
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
