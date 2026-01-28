code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the file paths
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

# Load the data from files
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create a DataFrame for funding records
funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by project names or headings - look for common project patterns
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project names that are capitalized or have specific patterns
        if line and (line.isupper() or 'Project' in line or any(keyword in line for keyword in ['Resurfacing', 'Improvements', 'Repairs', 'Drainage', 'Replacement'])):
            # This might be a project name
            if len(line) > 10 and len(line) < 200:  # Reasonable length
                current_project = line
        
        # Extract status information
        if current_project:
            status = None
            if 'completed' in line.lower() or 'construction was completed' in line.lower():
                status = 'completed'
            elif 'design' in line.lower() or 'working with consultant' in line.lower():
                status = 'design'
            elif 'not started' in line.lower():
                status = 'not started'
            
            # Extract dates
            et = None
            if 'Complete' in line or 'completion' in line.lower():
                # Look for year patterns
                year_match = re.search(r'(20\d{2})', line)
                if year_match:
                    et = year_match.group(1)
            
            # Extract topics (check if park-related)
            topic = ''
            if 'park' in current_project.lower() or 'park' in line.lower():
                topic = 'park'
            
            if status or et or topic:
                extracted_projects.append({
                    'Project_Name': current_project,
                    'status': status,
                    'et': et,
                    'topic': topic,
                    'source_file': filename
                })

# Create DataFrame from extracted projects
projects_df = pd.DataFrame(extracted_projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = projects_df[
    (projects_df['topic'] == 'park') & 
    (projects_df['status'] == 'completed') & 
    (projects_df['et'] == '2022')
]

# Get unique project names
park_project_names = park_projects_2022['Project_Name'].unique()

# Map common variations in project names between civic docs and funding table
name_mapping = {
    'Bluffs Park Shade Structure': ['Bluffs Park Shade Structure'],
    'Malibu Bluffs Park South Walkway Repairs': ['Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs'],
    'Trancas Canyon Park Playground': ['Trancas Canyon Park Playground'],
    'Trancas Canyon Park Upper and Lower Slopes Repair': ['Trancas Canyon Park Upper and Lower Slopes Repair']
}

# Find matching projects in funding data
matching_projects = []
total_funding = 0

for project_name in park_project_names:
    # Look for exact match first
    matching_funding = funding_df[funding_df['Project_Name'].str.contains(project_name, case=False, na=False)]
    
    if not matching_funding.empty:
        matching_projects.append({
            'project_name': project_name,
            'funding_records': matching_funding.to_dict('records')
        })
        total_funding += matching_funding['Amount'].sum()
    else:
        # Try partial matching
        for funding_name in funding_df['Project_Name']:
            if (project_name.lower() in funding_name.lower() or 
                funding_name.lower() in project_name.lower()):
                matching_funding = funding_df[funding_df['Project_Name'] == funding_name]
                matching_projects.append({
                    'project_name': project_name,
                    'funding_records': matching_funding.to_dict('records')
                })
                total_funding += matching_funding['Amount'].sum()
                break

result_dict = {
    'total_funding': int(total_funding),
    'matching_projects_count': len(matching_projects),
    'matching_projects': matching_projects
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
