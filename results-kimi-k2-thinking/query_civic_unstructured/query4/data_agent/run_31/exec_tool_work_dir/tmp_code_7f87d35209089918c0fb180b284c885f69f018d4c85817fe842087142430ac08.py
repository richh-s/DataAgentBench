code = """import json
import pandas as pd
import re

# Load the data from the variables
funding_data = var_functions.query_db_14
all_projects = var_functions.query_db_2
projects_2022 = var_functions.query_db_16

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"Funding records: {len(funding_df)}")
print(f"All project docs: {len(all_projects)}")
print(f"2022 project docs: {len(projects_2022)}")

# Function to extract spring 2022 projects from text
def extract_spring_2022_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and noise
        if not line or line in ['Page', 'Agenda', 'Item'] or 'Page' in line:
            continue
            
        # Look for project names (typically not all caps, descriptive)
        if (len(line) > 10 and len(line) < 150 and 
            not line.startswith('(') and 
            not line.startswith('cid:')):
            
            # Check spring 2022 in nearby lines
            spring_2022_found = False
            for j in range(max(0, i-5), min(len(lines), i+10)):
                context_line = lines[j]
                if 'Spring' in context_line and '2022' in context_line:
                    spring_2022_found = True
                    break
            
            if spring_2022_found:
                # Clean up the project name
                clean_name = line.replace('\u2019', "'").replace('\u2013', '-').strip()
                projects.append(clean_name)
    
    return projects

# Extract all spring 2022 projects
spring_2022_projects = []
for doc in projects_2022:
    text = doc.get('text', '')
    projects = extract_spring_2022_projects(text)
    spring_2022_projects.extend(projects)

print(f"\nAll potential spring 2022 projects found: {len(spring_2022_projects)}")
for i, p in enumerate(spring_2022_projects[:20]):
    print(f"  {i+1}. {p}")

# Match with funding data
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    # Look for exact match first
    match = funding_df[funding_df['Project_Name'] == project]
    
    if not match.empty:
        for _, row in match.iterrows():
            matched_projects.append({
                'Project_Name': project,
                'Amount': row['Amount']
            })
            total_funding += row['Amount']
    else:
        # Try partial matching (first 40 chars)
        partial_matches = funding_df[
            funding_df['Project_Name'].str.contains(re.escape(project[:40]), case=False, na=False)
        ]
        if not partial_matches.empty:
            for _, row in partial_matches.iterrows():
                matched_projects.append({
                    'Project_Name': row['Project_Name'],  # Use actual name from funding
                    'Amount': row['Amount']
                })
                total_funding += row['Amount']

# Remove duplicates based on Project_Name
unique_matched = []
seen_names = set()
for proj in matched_projects:
    if proj['Project_Name'] not in seen_names:
        unique_matched.append(proj)
        seen_names.add(proj['Project_Name'])

result = {
    "project_count": len(unique_matched),
    "total_funding": int(total_funding),
    "projects": unique_matched
}

print(f"\nFinal Result:")
print(f"Projects with Spring 2022 start found: {len(unique_matched)}")
print(f"Total funding: ${total_funding:,}")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}}

exec(code, env_args)
