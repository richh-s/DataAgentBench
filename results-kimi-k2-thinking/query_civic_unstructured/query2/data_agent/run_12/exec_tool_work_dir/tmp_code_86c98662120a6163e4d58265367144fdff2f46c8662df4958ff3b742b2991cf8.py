code = """import json
import pandas as pd
import re

# Load the funding data from the file
with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

# Load the civic docs data from the file  
with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)
print(f"Total funding records: {len(df_funding)}")

# Function to extract completed park projects from text
def extract_completed_park_projects(text):
    projects = []
    
    # Look for patterns indicating completed projects
    # Common format: Project Name followed by Updates section
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names that might be park-related
        # Usually they're on their own line or have specific markers
        is_project_line = False
        if len(line) < 100 and not line.startswith('(') and not line.startswith('-'):
            # Check if next few lines contain status info
            next_lines = ' '.join(lines[i+1:i+4]).lower()
            if 'park' in line.lower() and ('completed' in next_lines or 'construction was completed' in next_lines):
                is_project_line = True
        
        if is_project_line:
            # Check if project was completed in 2022
            next_chunk = ' '.join(lines[i:i+6]).lower()
            if 'completed' in next_chunk and '2022' in next_chunk:
                # Extract date info
                date_match = re.search(r'(\w+\s+2022|2022-\w+|completed[\s,]*\w+[\s,]*2022)', next_chunk, re.IGNORECASE)
                date_str = date_match.group(1) if date_match else '2022'
                
                project_name = line.replace('\u2013', '-').replace('\u201c', '"').replace('\u201d', '"').strip()
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': 'park',
                    'status': 'completed',
                    'et': date_str
                })
    
    return projects

# Extract all completed park projects from 2022
all_park_projects_2022 = []
for doc in civic_docs_data:
    projects = extract_completed_park_projects(doc['text'])
    all_park_projects_2022.extend(projects)

print(f"Found {len(all_park_projects_2022)} park projects completed in 2022")
for proj in all_park_projects_2022:
    print(f"  {proj['Project_Name']}")

# Clean the project names for matching
def clean_project_name(name):
    # Remove common suffixes and clean up
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip()

# Clean funding project names
df_funding['Project_Name_Clean'] = df_funding['Project_Name'].apply(clean_project_name)

# Create list of clean park project names
park_project_names = [clean_project_name(proj['Project_Name']) for proj in all_park_projects_2022]

print(f"\nPark project names to match:")
for name in park_project_names:
    print(f"  '{name}'")

# Find matching projects in funding data
matched_projects = []
total_funding = 0

for park_name in park_project_names:
    # Look for exact or partial matches
    matches = df_funding[df_funding['Project_Name_Clean'].str.contains(park_name, case=False, na=False) |
                        df_funding['Project_Name'].str.contains(park_name, case=False, na=False)]
    
    if not matches.empty:
        for _, match in matches.iterrows():
            amount = int(match['Amount'])
            total_funding += amount
            matched_projects.append({
                'project_name': park_name,
                'funding_record': match['Project_Name'],
                'amount': amount
            })
            print(f"Matched: {park_name} -> {match['Project_Name']} (${amount:,})")

# Also check if any funding records contain park names
funding_project_names = df_funding['Project_Name_Clean'].tolist()

for park_name in park_project_names:
    for fund_name in funding_project_names:
        # Check for substring matches both ways
        if (park_name.lower() in fund_name.lower() or 
            fund_name.lower() in park_name.lower()):
            
            # Check if we already have this match
            already_matched = any(m['project_name'] == park_name and 
                                 clean_project_name(m['funding_record']) == fund_name 
                                 for m in matched_projects)
            
            if not already_matched:
                fund_row = df_funding[df_funding['Project_Name_Clean'] == fund_name]
                if not fund_row.empty:
                    amount = int(fund_row.iloc[0]['Amount'])
                    total_funding += amount
                    matched_projects.append({
                        'project_name': park_name,
                        'funding_record': fund_row.iloc[0]['Project_Name'],
                        'amount': amount
                    })
                    print(f"New match: {park_name} -> {fund_row.iloc[0]['Project_Name']} (${amount:,})")

print(f"\nTotal matched projects: {len(matched_projects)}")
print(f"Total funding for park projects completed in 2022: ${total_funding:,}")

# Format results
result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
