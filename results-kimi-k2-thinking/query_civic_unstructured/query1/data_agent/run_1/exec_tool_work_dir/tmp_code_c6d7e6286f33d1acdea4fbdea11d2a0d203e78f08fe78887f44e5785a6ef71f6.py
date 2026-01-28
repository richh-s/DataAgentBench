code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a mapping of project names to funding amounts
project_funding = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        project_funding[project_name] = amount

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for project sections with status indicators
    # Pattern: Project name followed by status indicators
    
    # Find all potential project names in the text
    # Look for lines that are likely project names (title case, not too long)
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines or very short lines
        if len(line) < 10 or len(line) > 150:
            continue
            
        # Look for title case lines that could be project names
        if line[0].isupper() and any(c.islower() for c in line):
            # Check if this line appears to be a project name
            # Heuristic: contains words like 'Project', 'Improvements', 'Repair', etc.
            project_indicators = ['Project', 'Improvements', 'Repair', 'Replacement', 'Construction', 
                                'Resurfacing', 'Drainage', 'Road', 'Park', 'Bridge', 'Culvert']
            
            if any(indicator in line for indicator in project_indicators):
                # Check if this project has funding
                if line in project_funding:
                    # Look backwards/forwards for status
                    status = 'unknown'
                    context = ' '.join(lines[max(0, i-5):min(len(lines), i+10)])
                    
                    if 'design' in context.lower():
                        status = 'design'
                    elif 'complete' in context.lower() or 'construction was completed' in context.lower():
                        status = 'completed'
                    elif 'not started' in context.lower():
                        status = 'not started'
                    
                    if status == 'design':
                        extracted_projects.append({
                            'project_name': line,
                            'status': status,
                            'funding': project_funding[line]
                        })
                else:
                    # Check for variations with suffixes
                    for funded_name in project_funding:
                        if funded_name.startswith(line) or line.startswith(funded_name):
                            context = ' '.join(lines[max(0, i-5):min(len(lines), i+10)])
                            
                            status = 'unknown'
                            if 'design' in context.lower():
                                status = 'design'
                            elif 'complete' in context.lower() or 'construction was completed' in context.lower():
                                status = 'completed'
                            elif 'not started' in context.lower():
                                status = 'not started'
                            
                            if status == 'design':
                                extracted_projects.append({
                                    'project_name': funded_name,
                                    'status': status,
                                    'funding': project_funding[funded_name]
                                })

# Remove duplicates
design_projects = []
seen_names = set()
for p in extracted_projects:
    if p['project_name'] not in seen_names:
        design_projects.append(p)
        seen_names.add(p['project_name'])

print('__RESULT__:')
print(json.dumps({
    'design_status_capital_projects_over_50k': len(design_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
