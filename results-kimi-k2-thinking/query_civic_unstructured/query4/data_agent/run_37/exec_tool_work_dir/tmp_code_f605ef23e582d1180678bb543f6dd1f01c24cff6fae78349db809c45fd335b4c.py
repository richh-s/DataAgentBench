code = """import json
import re

# Load funding data from file
import os
funding_file = "/tmp/tmp4n6h1h4h.json" if os.path.exists("/tmp/tmp4n6h1h4h.json") else None
print('Funding file exists:', os.path.exists("/tmp/tmp4n6h1h4h.json"))

funding_data = []
if funding_file and os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

# Load civic docs data from the string variable
civic_docs = locals().get('var_functions.query_db:44')
if not civic_docs:
    civic_docs = locals().get('var_functions.query_db:42')

print('Civic docs type:', type(civic_docs))
print('Civic docs has data:', bool(civic_docs))

if isinstance(civic_docs, list):
    print('Number of civic documents:', len(civic_docs))
    
# Extract projects from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Parse text to find projects with 2022 dates
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5:
            continue
            
        # Skip non-project lines
        if any(skip in line for skip in ['Page', 'RECOMMENDED', 'DISCUSSION', 'Prepared', 'Approved', 'Subject:', 'To:', 'Meeting date', 'Capital Improvement Projects', 'Project Schedule', 'Updates:', 'Project Description']):
            continue
        if line.startswith('(') or line.startswith('cid:') or line.startswith('.'):
            continue
            
        # Look for 2022 in line
        if '2022' in line:
            # This is likely a project name
            project_name = line.strip()[:200]  # Limit length
            
            # Check if it's spring (look in surrounding text for Spring or March/April/May)
            spring_context = text[max(0, i-50):min(len(text), i+200)]
            is_spring = 'Spring' in spring_context or 'spring' in spring_context
            
            # Also check filename for date
            if '032022' in filename or '042022' or '052022' in filename:
                is_spring = True
            
            if is_spring:
                projects.append({
                    'name': project_name,
                    'filename': filename,
                    'context': spring_context[:200]
                })

print('Found spring 2022 projects:', len(projects))
for p in projects[:5]:
    print('-', p['name'][:80])

# Load funding data
print('Funding records:', len(funding_data))

# Match project names with funding
project_names = [p['name'] for p in projects]
matched_funding = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    for proj in projects:
        proj_name = proj['name'].lower()
        # Check for substring matches
        if (fund_name in proj_name or proj_name in fund_name or 
            any(part in fund_name for part in proj_name.split() if len(part) > 5)):
            matched_funding.append({
                'project': proj['name'],
                'fund_name': fund.get('Project_Name'),
                'amount': int(fund.get('Amount', 0))
            })
            break

print('Matched funding records:', len(matched_funding))
total_funding = sum(f['amount'] for f in matched_funding)
print('Total funding:', total_funding)

result = {
    'spring_2022_projects_count': len(projects),
    'matched_funding_count': len(matched_funding),
    'total_funding': total_funding,
    'projects': project_names[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'status': 'checked'}, 'var_functions.execute_python:36': {'checked': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'count': '500', 'total_funding': '28094000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
