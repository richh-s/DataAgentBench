code = """import json
import re
from collections import defaultdict

# Read the civic documents data
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data  
with open('var_functions.query_db:1', 'r') as f:
    funding_data = json.load(f)

# Process civic documents to extract project information
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    # Pattern to match project names and their details
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically bold or title case lines)
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
            # Check if this looks like a project name
            # Usually followed by status indicators
            next_lines = '\n'.join(lines[i:i+5])
            
            # Check for capital projects with design status
            if 'Capital Improvement Projects (Design)' in text or 'Capital Improvement Projects' in text:
                # Look for individual projects in design section
                if line and not line.endswith(':'):
                    potential_project = line
                    
                    # Look for brackets that might indicate status
                    if '(Design)' in text or 'Design' in next_lines:
                        status = 'design'
                        type_found = 'capital'
                        
                        # Extract project name more cleanly
                        project_name = potential_project.strip()
                        
                        # Skip section headers
                        if ('Capital Improvement Projects' in project_name or 
                            'Disaster Recovery Projects' in project_name or
                            'Public Works' in project_name or
                            'Commission' in project_name or
                            'Subject:' in project_name or
                            'RECOMMENDED ACTION' in project_name or
                            'DISCUSSION:' in project_name or
                            'Page ' in project_name):
                            continue
                            
                        # Clean up project names
                        if project_name.endswith(':'):
                            project_name = project_name[:-1].strip()
                        if 'Updates:' in project_name:
                            continue
                        if 'Project Schedule:' in project_name:
                            continue
                        if 'Project Description:' in project_name:
                            continue
                        if 'To:' in project_name or 'From:' in project_name:
                            continue
                        if 'Date' in project_name and ':' in project_name:
                            continue
                        if 'Prepared by' in project_name:
                            continue
                        if 'Approved by' in project_name:
                            continue
                        if project_name.isupper() and len(project_name) < 50:
                            continue  # Skip headers
                        if len(project_name) > 200:
                            continue  # Skip too long
                            
                        if project_name:
                            projects.append({
                                'Project_Name': project_name,
                                'status': 'design',
                                'type': 'capital',
                                'topic': '',  # Will extract topics later
                                'st': '',
                                'et': ''
                            })

# Create a more robust extraction by looking for patterns
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find design section
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)', 
                                    text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names (lines that are likely project titles)
        section_lines = design_section.split('\n')
        
        for line in section_lines:
            line = line.strip()
            
            # Skip empty lines, bullets, and obvious non-project lines
            if (not line or 
                line.startswith('•') or 
                line.startswith('(') or
                line.startswith('Page') or
                'cid:' in line or
                'Updates:' in line or
                'Schedule:' in line or
                'Project Schedule:' in line or
                len(line) < 10 or
                line.isupper() and len(line) < 50 or
                'Capital Improvement Projects' in line):
                continue
                
            # Clean up the line to get project name
            project_name = line.strip()
            
            # Remove trailing colons and common suffixes to clean
            if project_name.endswith(':'):
                project_name = project_name[:-1].strip()
                
            # Skip if it's just "Updates" or similar
            if project_name.lower() in ['updates', 'project schedule', 'estimated schedule', 
                                       'recommended action', 'project description']:
                continue
                
            # Add if it's a reasonable length and looks like a project name
            if 10 < len(project_name) < 150 and project_name[0].isalnum():
                projects.append({
                    'Project_Name': project_name,
                    'status': 'design',
                    'type': 'capital',
                    'topic': '',
                    'st': '',
                    'et': ''
                })

# Remove duplicates based on project name
seen = set()
unique_projects = []
for p in projects:
    name = p['Project_Name']
    if name not in seen:
        seen.add(name)
        unique_projects.append(p)

projects = unique_projects

# Convert funding data to dict for lookup
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Find projects with funding > $50,000 that are capital design projects
capital_design_projects = []
for project in projects:
    proj_name = project['Project_Name']
    
    # Check if this project has funding > 50000
    if proj_name in funding_dict and funding_dict[proj_name] > 50000:
        capital_design_projects.append({
            'Project_Name': proj_name,
            'Funding': funding_dict[proj_name],
            'Status': project['status'],
            'Type': project['type']
        })

# Count the results
count = len(capital_design_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'projects': capital_design_projects[:10]  # First 10 for debugging
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
