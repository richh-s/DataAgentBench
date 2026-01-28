code = """import pandas as pd
import json
import re

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Look at sample civic document
print("\nSample civic document:")
print(civic_docs[0]['filename'])
print(civic_docs[0]['text'][:500])

# Identify FEMA/emergency projects from funding data
emergency_projects = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_projects.append(record['Project_Name'])

print(f"\nFEMA/Emergency projects from funding data: {len(emergency_projects)}")
for proj in emergency_projects[:10]:
    print(f"- {proj}")

# Process civic documents to extract projects
projects_from_docs = []

for doc in civic_docs[:3]:  # Process first 3 documents as sample
    text = doc['text']
    filename = doc['filename']
    
    # Find project sections
    lines = text.split('\n')
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically bolded or as headers)
        if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
            # Heuristic: project names are often followed by status indicators
            if 'Updates:' in line or 'Project Schedule:' in line or line.endswith('Project'):
                if current_project:
                    projects_from_docs.append(project_info)
                
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'filename': filename,
                    'topic': '',
                    'type': '',
                    'status': '',
                    'st': '',
                    'et': ''
                }
        
        # Extract status information
        if current_project:
            if 'Updates:' in line or 'Project is' in line:
                if 'under construction' in line.lower() or 'construction' in line.lower():
                    project_info['status'] = 'construction'
                    project_info['type'] = 'capital'
                elif 'design' in line.lower():
                    project_info['status'] = 'design'
                    project_info['type'] = 'capital'
                elif 'completed' in line.lower():
                    project_info['status'] = 'completed'
                    project_info['type'] = 'capital'
    
    if current_project and project_info:
        projects_from_docs.append(project_info)

print(f"\nProjects extracted from documents: {len(projects_from_docs)}")
for proj in projects_from_docs[:5]:
    print(f"- {proj['Project_Name'][:50]}... Status: {proj['status']}, Type: {proj['type']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
