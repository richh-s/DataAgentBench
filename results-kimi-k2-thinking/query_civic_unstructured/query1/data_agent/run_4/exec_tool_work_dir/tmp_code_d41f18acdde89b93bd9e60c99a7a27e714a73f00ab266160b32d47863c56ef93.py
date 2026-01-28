code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a dictionary of funding projects with amount > 50000
funding_dict = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        project_name = item['Project_Name'].strip()
        funding_dict[project_name] = {
            'amount': amount,
            'source': item['Funding_Source']
        }

# Extract capital projects with design status
print('Searching for capital projects with design status...')

# We'll parse the text more carefully
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections about design projects
    # Look for "Capital Improvement Projects" followed by "(Design)"
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        if 'Capital Improvement Projects' in section and 'Design' in section:
            # This is a design section, extract project names
            lines = section.split('\n')
            capture_projects = False
            
            for line in lines:
                line = line.strip()
                
                # Start capturing after we see the Design header
                if 'Design' in line and 'Capital' in line:
                    capture_projects = True
                    continue
                
                # Stop at the next major section
                if capture_projects and line.startswith('Capital') and 'Construction' in line:
                    break
                if capture_projects and line.startswith('Capital') and 'Not Started' in line:
                    break
                if capture_projects and line.startswith('DISASTER'):
                    break
                    
                # Skip non-project lines
                if not capture_projects:
                    continue
                    
                if not line:
                    continue
                if line.startswith('(') or 'cid:' in line:
                    continue
                if any(keyword in line for keyword in ['Updates:', 'Schedule:', 'Staff', 'City', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda', 'Item']):
                    continue
                if any(phase in line for phase in ['Spring', 'Summer', 'Fall', 'Winter', 'Q1', 'Q2', 'Q3', 'Q4']):
                    continue
                if any(year in line for year in ['2022', '2023', '2024']):
                    # Only skip if it's just a year/phase line
                    if re.match(r'^(Complete|Advertise|Begin)?\s*\w*\s*\d{4}$', line):
                        continue
                if 'Complete Design' in line or 'Advertise' in line or 'Begin Construction' in line:
                    continue
                if line.startswith('-') or line.startswith('•'):
                    continue
                    
                # If we get here, this might be a project name
                if len(line) > 5 and len(line) < 150:
                    # Clean up the name
                    clean_name = re.sub(r'\s+', ' ', line).strip()
                    if clean_name and not clean_name.endswith(':'):
                        # Remove parenthetical suffixes for matching
                        base_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
                        all_design_projects.append(base_name.strip())

# Remove duplicates
unique_design_projects = list(set(all_design_projects))

print(f'Found {len(unique_design_projects)} potential design projects')
for p in sorted(unique_design_projects)[:10]:
    print(f'  - {p}')

# Match with funding data
capital_design_funding = []

for project_name in unique_design_projects:
    # Check for matches in funding data
    for fund_name in funding_dict.keys():
        # Direct match or project name is prefix of funding name
        if project_name == fund_name or fund_name.startswith(project_name + ' ') or fund_name.startswith(project_name + '('):
            capital_design_funding.append({
                'project': project_name,
                'amount': funding_dict[fund_name]['amount'],
                'source': funding_dict[fund_name]['source']
            })
            break

# Count results
count = len(capital_design_funding)

print(f'__RESULT__: {count}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
