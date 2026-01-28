code = """import json
import re
import os

# Load the funding data
funding_file_path = str(var_functions.query_db:5)
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs text data
civic_file_path = str(var_functions.query_db:6)
with open(civic_file_path, 'r') as f:
    civic_data = json.load(f)

# Process funding data into a dictionary for easy lookup
funding_dict = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if project_name:
        funding_dict[project_name] = {
            'Funding_ID': record.get('Funding_ID', ''),
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        }

# Function to extract project information from civic doc text
def extract_projects_from_text(text_content):
    projects = []
    if not text_content:
        return projects
    
    lines = text_content.split('\n')
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or len(line) < 5:
            continue
            
        # Skip document headers
        skip_keywords = ['agenda', 'report', 'meeting', 'item', 'to:', 'prepared by:', 'approved by:', 'date:', 'subject:', 'recommended action:', 'discussion:', 'page', 'public works', 'commission']
        if any(keyword in line.lower()[:50] for keyword in skip_keywords):
            continue
        
        # Look for project name (typically a title line)
        if (line and 
            not line.startswith('(') and 
            not line.startswith('-') and
            not any(marker in line for marker in ['cid:', 'Updates:', 'Schedule:'])):
            
            # Check if line looks like a project name
            if (len(line.split()) <= 8 or  # Usually short titles
                'Project' in line or
                'Park' in line or
                line.startswith('20')):  # Year-based names
                
                # Save previous project
                if current_project and 'Project_Name' in project_info:
                    projects.append(project_info)
                
                # Start new project
                current_project = line
                project_info = {'Project_Name': line, 'topic': '', 'status': '', 'st': '', 'et': ''}
        
        # Extract status and dates
        if current_project:
            # Check for completion status with 2022
            if 'completed' in line.lower() or 'completion' in line.lower():
                if '2022' in line:
                    project_info['status'] = 'completed'
                    project_info['et'] = '2022'
            
            # Check for park-related topics
            if 'Park' in line:
                project_info['topic'] = 'park'
    
    # Add last project
    if current_project and 'Project_Name' in project_info:
        projects.append(project_info)
    
    return projects

# Extract all projects from civic documents
all_projects = []
for doc in civic_data:
    text_content = doc.get('text', '')
    if text_content:
        projects = extract_projects_from_text(text_content)
        all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
project_names_added = set()

# First pass: match exact project names
for project in all_projects:
    if 'park' in project['topic'].lower() and project['status'] == 'completed':
        project_name = project['Project_Name']
        
        # Look for matching funding record
        for fund_name, fund_info in funding_dict.items():
            if fund_name.strip().lower() == project_name.strip().lower():
                if fund_name not in project_names_added:
                    park_projects_2022.append({
                        'Project_Name': fund_name,
                        'status': 'completed',
                        'year': '2022',
                        'Funding_Source': fund_info['Funding_Source'],
                        'Amount': fund_info['Amount']
                    })
                    project_names_added.add(fund_name)
                break

# Second pass: check funding table for park projects and verify completion
if len(park_projects_2022) == 0:
    # Check for park projects in funding table
    park_keywords = ['park', 'playground']
    for fund_name, fund_info in funding_dict.items():
        if any(keyword in fund_name.lower() for keyword in park_keywords):
            # Look for this project in civic docs with 2022 completion
            for project in all_projects:
                if (project['status'] == 'completed' and 
                    (fund_name.strip().lower() in project['Project_Name'].strip().lower() or
                     project['Project_Name'].strip().lower() in fund_name.strip().lower())):
                    
                    if fund_name not in project_names_added:
                        park_projects_2022.append({
                            'Project_Name': fund_name,
                            'status': 'completed',
                            'year': '2022',
                            'Funding_Source': fund_info['Funding_Source'],
                            'Amount': fund_info['Amount']
                        })
                        project_names_added.add(fund_name)
                    break

# Calculate total funding
total_funding = sum(project['Amount'] for project in park_projects_2022)

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(park_projects_2022),
    'projects': park_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
