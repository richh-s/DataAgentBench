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
        elif 'Disaster Recovery Projects' in line:
            current_section = 'disaster'
            continue
            
        # Look for project names
        if current_section and line:
            # Skip bullet points and patterns that aren't project names
            if line.startswith('(') or line.startswith('•') or line.startswith('▪'):
                continue
            
            # Skip common keywords
            lower_line = line.lower()
            if any(word in lower_line for word in ['updates', 'schedule', 'project description', 'revised', 'preliminary design']):
                continue
            
            # Skip page numbers
            if line.startswith('Page'):
                continue
            
            # Clean the project name
            project_name = re.sub(r'^[^A-Za-z]*', '', line)
            project_name = re.sub(r'\(cid:\d+\)', '', project_name).strip()
            
            if len(project_name) > 10:  # Reasonable length for a project name
                # Determine project type
                project_type = 'capital'
                if 'FEMA' in project_name or 'CalOES' in project_name or 'CalJPIA' in project_name:
                    project_type = 'disaster'
                
                # Determine status from section
                status = current_section
                
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
