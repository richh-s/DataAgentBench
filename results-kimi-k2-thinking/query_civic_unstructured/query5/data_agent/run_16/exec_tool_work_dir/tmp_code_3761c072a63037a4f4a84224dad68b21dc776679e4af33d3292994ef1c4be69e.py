code = """import json
import re
import os

# Load funding data
funding_file = var_functions.query_db:30
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:31
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Identify disaster-related projects from funding data
disaster_project_names = set()

for item in funding_data:
    project_name = item.get('Project_Name', '')
    if project_name:
        # Check for disaster-related keywords
        name_upper = project_name.upper()
        if any(keyword in name_upper for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'FIRE', 'EMERGENCY']):
            disaster_project_names.add(project_name)

# Step 2: Analyze civic documents to find projects that started in 2022
projects_started_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Method 1: Project names starting with 2022
        if line.startswith('2022') and 'Project' in line:
            # Check if it's disaster-related
            if any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'FIRE', 'EMERGENCY']):
                projects_started_2022.add(line.strip())
        
        # Method 2: Look for project context mentioning 2022
        if '2022' in line:
            # Look for project names in surrounding lines
            for j in range(max(0, i-3), min(len(lines), i+4)):
                proj_line = lines[j].strip()
                if proj_line.endswith('Project') or 'FEMA Project' in proj_line or 'CalOES Project' in proj_line:
                    # Check if disaster-related
                    if any(keyword in proj_line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'FIRE', 'EMERGENCY']):
                        # Extract clean project name
                        proj_name = proj_line.strip()
                        # Remove suffix if present to match funding data
                        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', proj_name)
                        if clean_name:
                            projects_started_2022.add(clean_name)

# Method 3: Look for (FEMA/CalOES Project) patterns with 2022 context
for doc in civic_docs:
    text = doc.get('text', '')
    # Find all projects with disaster suffixes
    pattern = r'([A-Z][^\n(]*?)\s*\(([^)]*(?:FEMA|CalOES|CalJPIA)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name = match[0].strip()
        if proj_name and len(proj_name) > 5:
            # Check if 2022 is mentioned anywhere in the document
            if '2022' in text:
                projects_started_2022.add(proj_name)
            else:
                # Check context around the project mention
                try:
                    pos = text.index(match[0])
                    context = text[max(0, pos-150):min(len(text), pos+150)]
                    if '2022' in context:
                        projects_started_2022.add(proj_name)
                except:
                    pass

# Method 4: Look for projects with exact 2022 in their name
for item in funding_data:
    project_name = item.get('Project_Name', '')
    if project_name and '2022' in project_name:
        # Check if disaster-related
        if any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'FIRE', 'EMERGENCY']):
            disaster_project_names.add(project_name)

# Step 3: Find projects that are both disaster-related AND started in 2022
disaster_projects_2022 = disaster_project_names & projects_started_2022

# Also add projects that have 2022 in their name and are disaster-related
for item in funding_data:
    project_name = item.get('Project_Name', '')
    if project_name and '2022' in project_name:
        if any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'FIRE', 'EMERGENCY']):
            disaster_projects_2022.add(project_name)

# Step 4: Calculate total funding
total_funding = 0
funded_projects = []

for item in funding_data:
    project_name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    
    # Check if this project is in our disaster projects that started in 2022
    if project_name in disaster_projects_2022:
        total_funding += amount
        funded_projects.append({
            'project_name': project_name,
            'amount': amount
        })
    else:
        # Check for suffix variations
        for disaster_proj in disaster_projects_2022:
            if project_name.startswith(disaster_proj) or disaster_proj.startswith(project_name):
                total_funding += amount
                funded_projects.append({
                    'project_name': project_name,
                    'amount': amount
                })
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(funded_projects),
    'projects': funded_projects
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
