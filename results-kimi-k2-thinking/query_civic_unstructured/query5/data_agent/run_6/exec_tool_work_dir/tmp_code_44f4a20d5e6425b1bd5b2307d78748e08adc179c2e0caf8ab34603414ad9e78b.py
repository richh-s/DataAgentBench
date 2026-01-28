code = """import json
import pandas as pd
import re

# Load the civic documents data
with open('/tmp/tmp2v7m_6l3.json', 'r') as f:
    civic_docs = json.load(f)

# Load the funding data  
with open('/tmp/tmpf4d6q2f3.json', 'r') as f:
    funding_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)

# Process civic documents to extract project information
all_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for project names and details
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 5:
            # Check if this appears to be a project name (title case, reasonable length)
            if line == line.title() and not line.startswith('(') and not line.isupper() and len(line.split()) >= 2:
                project = {'name': line}
                
                # Look for type indicators (FEMA, CalOES, disaster, etc.)
                next_lines = ' '.join(lines[i:i+15])
                
                # Determine type
                has_disaster_indicators = any(indicator in next_lines.lower() for indicator in ['fema', 'caloes', 'disaster', 'fire recovery', 'emergency'])
                has_disaster_suffix = any(suffix in next_lines for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)'])
                
                if has_disaster_indicators or has_disaster_suffix:
                    project['type'] = 'disaster'
                else:
                    project['type'] = 'capital'
                
                # Extract start date (look for '2022' in schedule)
                if '2022' in next_lines:
                    project['start_year'] = '2022'
                elif any(season in next_lines for season in ['Spring 2022', 'Fall 2022', 'Summer 2022', 'Winter 2022']):
                    project['start_year'] = '2022'
                else:
                    project['start_year'] = None
                
                all_projects.append(project)

# Create DataFrame of projects
projects_df = pd.DataFrame(all_projects)

# Filter for disaster projects that started in 2022
disaster_2022_projects = projects_df[
    (projects_df['type'] == 'disaster') & 
    (projects_df['start_year'] == '2022')
]

print(f"Found {len(disaster_2022_projects)} disaster projects starting in 2022 in civic docs")

# Match these with funding data
matched_projects = []
total_funding = 0

for _, proj in disaster_2022_projects.iterrows():
    proj_name = proj['name']
    
    # Try exact match first
    match = funding_df[funding_df['Project_Name'].str.lower() == proj_name.lower()]
    
    if len(match) == 0:
        # Try partial match
        match = funding_df[funding_df['Project_Name'].str.lower().str.contains(proj_name.lower(), na=False)]
    
    if len(match) == 0 and ' ' in proj_name:
        # Try matching on key words
        key_words = [word for word in proj_name.split() if len(word) > 4]
        for word in key_words:
            match = funding_df[funding_df['Project_Name'].str.lower().str.contains(word.lower(), na=False)]
            if len(match) > 0:
                break
    
    if len(match) > 0:
        for _, fund in match.iterrows():
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project_name': proj_name,
                'funding_project': fund['Project_Name'],
                'amount': amount
            })

# Also check for disaster projects with 2022 in their names from funding data
disaster_2022_funding = funding_df[
    funding_df['Project_Name'].str.contains(r'2022.*(?:FEMA|CalOES|CalJPIA)|(?:FEMA|CalOES|CalJPIA).*2022', case=False, na=False)
]

print(f"Found {len(disaster_2022_funding)} disaster projects with 2022 in name from funding data")

for _, proj in disaster_2022_funding.iterrows():
    amount = int(proj['Amount'])
    total_funding += amount
    matched_projects.append({
        'project_name': proj['Project_Name'],
        'funding_project': proj['Project_Name'],
        'amount': amount
    })

# Remove duplicates
unique_projects = []
seen = set()
for proj in matched_projects:
    key = (proj['funding_project'], proj['amount'])
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

total_funding = sum(proj['amount'] for proj in unique_projects)

print(f"Total unique disaster projects for 2022: {len(unique_projects)}")
print(f"Total funding: ${total_funding:,}")
print("\nDetailed projects:")
for proj in unique_projects:
    print(f"  - {proj['funding_project']}: ${proj['amount']:,}")

result = {
    'total_funding': total_funding,
    'num_projects': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
