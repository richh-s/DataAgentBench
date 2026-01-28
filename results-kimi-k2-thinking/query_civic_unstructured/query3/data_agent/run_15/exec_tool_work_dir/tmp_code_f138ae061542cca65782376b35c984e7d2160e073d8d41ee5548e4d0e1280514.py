code = """import pandas as pd
import json
import re

# Load funding data from the file
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify FEMA/emergency projects from funding data
fema_emergency_funding = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        fema_emergency_funding.append(record)

print(f"\nFEMA/Emergency projects from funding data: {len(fema_emergency_funding)}")
for proj in fema_emergency_funding:
    print(f"- {proj['Project_Name']} | {proj['Funding_Source']} | ${proj['Amount']:,}")

# Extract all project information from civic documents
all_projects = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Find project sections - look for patterns like project names followed by status indicators
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project names (typically bolded or as headers, often followed by status sections)
        if len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
            # Check if next lines contain project indicators
            if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or 'Project Description:' in lines[i+1]):
                project_name = line
                project_info = {
                    'Project_Name': project_name,
                    'filename': filename,
                    'topic': '',
                    'type': '',
                    'status': '',
                    'st': '',
                    'et': '',
                    'fema_related': False
                }
                
                # Look ahead for status and other info
                j = i + 1
                while j < len(lines) and j < i + 20:  # Look ahead up to 20 lines
                    next_line = lines[j].strip()
                    
                    # Check for FEMA/emergency mentions
                    if 'fema' in next_line.lower() or 'emergency' in next_line.lower():
                        project_info['fema_related'] = True
                    
                    # Extract status from Updates section
                    if 'Updates:' in next_line or 'Project is' in next_line:
                        # Look a few more lines for actual status
                        for k in range(j, min(j+5, len(lines))):
                            status_line = lines[k].strip()
                            if 'under construction' in status_line.lower():
                                project_info['status'] = 'construction'
                                project_info['type'] = 'capital'
                                break
                            elif 'design' in status_line.lower() and 'complete' not in status_line.lower():
                                project_info['status'] = 'design'
                                project_info['type'] = 'capital'
                                break
                            elif 'completed' in status_line.lower() or 'construction was completed' in status_line.lower():
                                project_info['status'] = 'completed'
                                project_info['type'] = 'capital'
                                break
                            elif 'not started' in status_line.lower():
                                project_info['status'] = 'not started'
                                project_info['type'] = 'capital'
                                break
                    
                    # Extract project schedule dates
                    if 'Project Schedule:' in next_line or 'Complete Design:' in next_line:
                        # Look for dates
                        for k in range(j, min(j+3, len(lines))):
                            date_line = lines[k].strip()
                            if ':' in date_line and len(date_line) < 50:
                                parts = date_line.split(':', 1)
                                if len(parts) == 2:
                                    key = parts[0].strip()
                                    value = parts[1].strip()
                                    if 'complete' in key.lower() or 'advertise' in key.lower() or 'begin' in key.lower():
                                        if '2023' in value or '2024' in value or '2022' in value:
                                            project_info['st'] = value
                    
                    j += 1
                
                # Infer type from project name
                proj_lower = project_name.lower()
                if 'disaster' in proj_lower or 'fema' in proj_lower or 'fire' in proj_lower:
                    project_info['type'] = 'disaster'
                elif 'storm' in proj_lower or 'drain' in proj_lower or 'road' in proj_lower or 'street' in proj_lower:
                    project_info['type'] = 'capital'
                
                all_projects.append(project_info)
        
        i += 1

print(f"\nTotal projects extracted from documents: {len(all_projects)}")
print(f"Projects marked as FEMA/emergency related: {sum(1 for p in all_projects if p['fema_related'])}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
