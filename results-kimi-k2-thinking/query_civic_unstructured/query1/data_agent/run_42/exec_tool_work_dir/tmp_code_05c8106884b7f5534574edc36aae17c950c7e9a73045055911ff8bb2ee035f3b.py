code = """import json
import os

print('Starting data analysis...')

# Find available result files
result_files = []
for f in os.listdir('.'):
    if f.endswith('.json') and 'query_db' in f:
        result_files.append(f)

print('Available result files:', result_files)

# Count projects from funding data > $50k
count_funding_over_50k = 0
with open('var_functions.query_db_110.json', 'r') as f:
    funding_data = json.load(f)
    count_funding_over_50k = len(funding_data)

print(f'Projects with funding > $50,000: {count_funding_over_50k}')

# Extract design projects from mongo data
design_projects = []
with open('var_functions.query_db_104.json', 'r') as f:
    mongo_data = json.load(f)
    
    for doc in mongo_data:
        text = doc.get('text', '')
        lines = text.split('\n')
        in_design_section = False
        
        for line in lines:
            clean = line.strip()
            if 'Capital Improvement Projects (Design)' in clean:
                in_design_section = True
            elif '(Construction)' in clean or '(Not Started)' in clean:
                in_design_section = False
            elif in_design_section and clean and len(clean) > 5:
                # Skip non-project lines
                skip_patterns = ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 
                               'To:', 'Subject:', 'Page', 'Prepared by:', 'RECOMMENDED ACTION', 'DISCUSSION:',
                               'Consultant', 'Staff is', 'Staff will', 'City is', 'Project is', 'Plans are']
                should_skip = any(pattern in clean for pattern in skip_patterns)
                
                if not should_skip and not clean.startswith('(') and not clean.startswith('•'):
                    if not clean.isupper():
                        project_name = clean.strip('•- ')
                        design_projects.append(project_name)

print(f'Projects in design status extracted: {len(design_projects)}')
print(f'First few design projects: {design_projects[:10]}')

# Get funding project names
funding_names = [record['Project_Name'] for record in funding_data]

# Find matches
matches = set()
for design_name in design_projects:
    for funding_name in funding_names:
        if funding_name.lower() in design_name.lower() or design_name.lower() in funding_name.lower():
            matches.add(funding_name)

result = len(matches)
print(f'Final answer: {result}')

__RESULT__:
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
