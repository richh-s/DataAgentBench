code = """import json
import re
import pandas as pd
from collections import defaultdict

# Load civic docs and funding data
civic_docs_file = globals()['var_functions.query_db:5']
funding_file = globals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Convert funding data to DataFrame for easier lookup
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Initialize list to store extracted project information
extracted_projects = []

# Process each civic document
for doc_idx, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    lines = text.splitlines()
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            continue
            
        # Check if this line looks like a project name (contains 'Park' and is reasonably long but not too long)
        if (re.search(r'park', line_stripped, re.IGNORECASE) and 
            len(line_stripped) > 10 and len(line_stripped) < 150 and
            not line_stripped.startswith('(') and # Not a bullet
            not line_stripped.endswith(':')): # Not a section header
            
            # Save previous project if exists
            if current_project and project_info:
                project_info['project_name'] = current_project
                extracted_projects.append(project_info)
            
            # Start new project
            current_project = line_stripped
            project_info = {
                'doc_id': doc_idx,
                'status': None,
                'et': None,
                'topic': 'park'  # Since we found 'park' in the name
            }
        
        # If we have a current project, look for status and dates
        elif current_project:
            # Look for completion status
            if re.search(r'completed', line_stripped, re.IGNORECASE):
                project_info['status'] = 'completed'
            
            # Look for 2022 in date context (et = end time)
            if re.search(r'2022', line_stripped):
                project_info['et'] = '2022'
            
            # Also check for "Construction was completed" patterns with 2022
            if re.search(r'completed.*2022|2022.*completed', line_stripped, re.IGNORECASE):
                project_info['status'] = 'completed'
                project_info['et'] = '2022'
        
    # Add last project if exists
    if current_project and project_info:
        project_info['project_name'] = current_project
        extracted_projects.append(project_info)

print(f"Extracted {len(extracted_projects)} potential park projects")

# Filter projects that are park-related, completed, and in 2022
completed_2022_park = []
for proj in extracted_projects:
    if (proj.get('status') == 'completed' and 
        proj.get('et') == '2022' and
        proj.get('topic') == 'park'):
        completed_2022_park.append(proj)

print(f"Found {len(completed_2022_park)} park projects completed in 2022")

# Extract project names
project_names = [proj['project_name'] for proj in completed_2022_park]
print("Project names:", project_names)

# Match with funding data
# First, normalize project names for matching
def normalize_name(name):
    return re.sub(r'[^a-zA-Z0-9\s]', '', name.lower()).strip()

matched_funding = []
for name in project_names:
    # Direct match first
    matches = funding_df[funding_df['Project_Name'].str.lower() == name.lower()]
    if not matches.empty:
        for _, row in matches.iterrows():
            matched_funding.append({
                'project_name': name,
                'funding_project_name': row['Project_Name'],
                'amount': row['Amount']
            })
    else:
        # Try partial matching with normalized names
        norm_name = normalize_name(name)
        for _, row in funding_df.iterrows():
            norm_funding = normalize_name(row['Project_Name'])
            if norm_name in norm_funding or norm_funding in norm_name:
                matched_funding.append({
                    'project_name': name,
                    'funding_project_name': row['Project_Name'],
                    'amount': row['Amount']
                })

# Remove duplicates based on funding project name
unique_funding = {}
for item in matched_funding:
    key = item['funding_project_name']
    if key not in unique_funding:
        unique_funding[key] = item

final_funding = list(unique_funding.values())

# Calculate total funding
total_funding = sum(item['amount'] for item in final_funding)

print(f"Matched {len(final_funding)} funding records")
print("Funding details:", final_funding)
print("Total funding:", total_funding)

result = {
    'park_projects_2022': project_names,
    'funding_records': final_funding,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'status': 'data loaded'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_count': 500}}

exec(code, env_args)
