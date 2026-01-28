code = """import json, os, re

# Load funding data
funding_file = "/tmp/tmp4n6h1h4h.json"
funding_data = []
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

# Load civic docs data  
civic_file = "/tmp/tmp4p5a1c3b.json"
if os.path.exists(civic_file):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    # Try alternative filename
    civic_file = "/tmp/tmp4p5a1c3b.json" 
    civic_docs = []

# If file loading failed, try to use the variable directly
civic_docs_var = locals().get('var_functions.query_db:44', [])
if not civic_docs and civic_docs_var:
    if isinstance(civic_docs_var, list):
        civic_docs = civic_docs_var
    else:
        print('Civic docs is not a list')

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Extract Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    for i,line in enumerate(lines):
        line = line.strip()
        if len(line) < 5: continue
        
        # Skip headers
        skip_words = ['Page', 'RECOMMENDED', 'DISCUSSION', 'Prepared', 'Approved', 'Subject:', 'To:', 'Meeting date']
        if any(w in line for w in skip_words): continue
        if line.startswith('(') or line.startswith('cid:'): continue
        
        if '2022' in line:
            # Check surrounding context for Spring
            context = ' '.join(lines[max(0,i-5):min(len(lines),i+5)])
            is_spring = ('Spring' in line) or ('spring' in context) or ('Spring' in context)
            
            # Check filename
            if any(m in filename for m in ['032022','042022','052022']):
                is_spring = True
                
            if is_spring:
                spring_projects.append({'name':line,'file':filename})

print('Spring 2022 projects:', len(spring_projects))

# Match with funding
project_names = [p['name'] for p in spring_projects]
matched = []

for fund in funding_data:
    fund_name = fund.get('Project_Name','').lower()
    fund_amount = int(fund.get('Amount',0))
    
    # Try string matching
    for proj in project_names:
        proj_lower = proj.lower()
        if fund_name in proj_lower or proj_lower in fund_name:
            if len(fund_name) > 10 or len(proj_lower) > 10:
                matched.append({'project':proj,'fund_name':fund.get('Project_Name'),'amount':fund_amount})
                break

# Deduplicate
unique_matches = {}
for m in matched:
    key = m['project'] + '|' + str(m['amount'])
    unique_matches[key] = m

final_matches = list(unique_matches.values())
total_funding = sum(m['amount'] for m in final_matches)

# Deduplicate projects
unique_projects = set(project_names)

result = {
    'spring_2022_projects_count': len(unique_projects),
    'matched_funding_count': len(final_matches),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'status': 'checked'}, 'var_functions.execute_python:36': {'checked': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'count': '500', 'total_funding': '28094000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
