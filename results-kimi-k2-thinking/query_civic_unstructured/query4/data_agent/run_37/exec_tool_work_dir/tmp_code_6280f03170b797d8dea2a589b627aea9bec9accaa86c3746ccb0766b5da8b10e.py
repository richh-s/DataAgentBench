code = """import json

# Access civic documents
docs = locals().get('var_functions.query_db:2')

if not docs:
    result = {'error': 'no_docs'}
else:
    projects_2022 = []
    for doc in docs:
        text = doc.get('text', '')
        fn = doc.get('filename', '')
        
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and '2022' in line:
                skip_words = ['Page', 'RECOMMENDED', 'DISCUSSION', 'Prepared', 'Approved', 'Subject', 'Meeting']
                should_skip = any(w in line for w in skip_words)
                if not should_skip and not line.startswith('(') and not line.startswith('cid:'):
                    projects_2022.append({'name': line[:100], 'file': fn})
    
    spring_projects = [p for p in projects_2022 if 'Spring' in p['name'] or 'Spring' in p['file']]
    
    result = {
        'total_2022': len(projects_2022),
        'spring_2022': len(spring_projects),
        'samples': projects_2022[:5]
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
