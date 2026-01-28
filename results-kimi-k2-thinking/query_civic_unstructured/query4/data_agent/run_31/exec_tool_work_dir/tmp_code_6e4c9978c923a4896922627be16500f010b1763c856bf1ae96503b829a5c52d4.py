code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the data
try:
    funding_data = var_functions.query_db_14
    all_projects = var_functions.query_db_2
    projects_2022 = var_functions.query_db_16
    
    print("Data loaded successfully")
    print(f"Funding records: {len(funding_data)}")
    print(f"All project docs: {len(all_projects)}")
    print(f"2022 project docs: {len(projects_2022)}")
    
except Exception as e:
    print(f"Error: {e}")

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Function to extract project info from text
def extract_projects_from_text(text):
    projects = []
    
    # Look for project names and dates in the text
    # Common patterns for projects
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically capitalized, sometimes with year prefix)
        if line and (line.isupper() or line.startswith('2022') or line.startswith('2021')):
            # Skip noise lines
            if 'Page' in line or 'Agenda' in line or line.startswith('('):
                continue
                
            project_name = line
            
            # Look for schedule info in following lines
            start_date = None
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                
                # Look for start/completion dates
                if 'Complete Design:' in next_line or 'Begin Construction:' in next_line or 'Complete Construction:' in next_line:
                    date_match = re.search(r'(Spring|Summer|Fall|Winter)\s+2022', next_line, re.IGNORECASE)
                    if date_match:
                        start_date = date_match.group(0)
                        break
                
                # Also check for year patterns
                if '2022' in next_line and ('Advertise' in next_line or 'Complete Design' in next_line or 'Begin Construction' in next_line):
                    season_match = re.search(r'(Spring|Summer|Fall|Winter)', next_line, re.IGNORECASE)
                    if season_match:
                        start_date = f"2022-{season_match.group(1)}"
                        break
                        
            if start_date:
                projects.append({
                    'Project_Name': project_name,
                    'Start_Date': start_date
                })
    
    return projects

# Extract projects from all documents
all_extracted_projects = []
for doc in projects_2022:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_extracted_projects.extend(projects)

print(f"Extracted {len(all_extracted_projects)} potential projects with dates")

# Filter for Spring 2022 projects
spring_2022_projects = [p for p in all_extracted_projects if '2022' in p['Start_Date'] and 'Spring' in p['Start_Date']]

print(f"Spring 2022 projects found: {len(spring_2022_projects)}")
for p in spring_2022_projects:
    print(f"  - {p['Project_Name']}: {p['Start_Date']}")

# Get funding for these projects (need to match names)
project_names = [p['Project_Name'] for p in spring_2022_projects]
matched_funding = funding_df[funding_df['Project_Name'].isin(project_names)]

total_funding = 0
project_count = len(matched_funding)

if project_count > 0:
    total_funding = matched_funding['Amount'].sum()
    print(f"\nMatched {project_count} projects with funding")
    print(f"Total funding: ${total_funding:,}")
    for _, row in matched_funding.iterrows():
        print(f"  - {row['Project_Name']}: ${row['Amount']:,}")
else:
    # Try fuzzy matching
    print("No exact matches found, checking partial matches...")
    for proj_name in project_names:
        # Look for similar names in funding data
        matches = funding_df[funding_df['Project_Name'].str.contains(proj_name[:30], case=False, na=False)]
        if not matches.empty:
            print(f"Potential match for '{proj_name}':")
            for _, row in matches.iterrows():
                print(f"  - {row['Project_Name']}: ${row['Amount']:,}")
                total_funding += row['Amount']
                project_count += 1

print("__RESULT__:")
result = {
    "project_count": project_count,
    "total_funding": int(total_funding),
    "spring_2022_projects": project_names,
    "matched_projects": len(matched_funding)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}}

exec(code, env_args)
