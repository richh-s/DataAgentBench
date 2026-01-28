code = """import json
from collections import defaultdict
import re

# Read civic documents from file
civic_file_path = locals()['var_functions.query_db:12']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data from file
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[proj_name] = amount

# Extract project information from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Identify section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'not started'
            continue
            
        # Look for project names
        if current_section and line and not line.startswith('(') and not line.startswith('2022'):
            # Skip common keywords
            skip_keywords = ['updates:', 'schedule:', 'project description:', 'project updates:', 'revised', 'preliminary design']
            should_skip = any(keyword in line.lower() for keyword in skip_keywords)
            
            if not should_skip and len(line) > 10 and not line.startswith('Page') and 'cid:' not in line:
                # Clean the project name
                project_name = re.sub(r'^[^A-Za-z]*', '', line)
                project_name = re.sub(r'\(cid:\d+\)', '', project_name).strip()
                
                if len(project_name) > 5:
                    # Determine project type
                    project_type = 'capital'
                    if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
                        project_type = 'disaster'
                    
                    # Determine status from section
                    if current_section == 'design':
                        status = 'design'
                    elif current_section == 'construction':
                        status = 'completed'
                    elif current_section == 'not started':
                        status = 'not started'
                    else:
                        status = 'unknown'
                    
                    projects.append({
                        'project_name': project_name,
                        'status': status,
                        'type': project_type
                    })

# Find design projects with funding > $50,000
design_projects_with_funding = []
for proj in projects:
    if proj['status'] == 'design':
        proj_name = proj['project_name']
        # Check exact match
        if proj_name in funding_map:
            design_projects_with_funding.append({
                'project_name': proj_name,
                'funding': funding_map[proj_name]
            })

# Count unique projects
unique_projects = []
seen = set()
for proj in design_projects_with_funding:
    if proj['project_name'] not in seen:
        seen.add(proj['project_name'])
        unique_projects.append(proj)

result = {
    'count': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
