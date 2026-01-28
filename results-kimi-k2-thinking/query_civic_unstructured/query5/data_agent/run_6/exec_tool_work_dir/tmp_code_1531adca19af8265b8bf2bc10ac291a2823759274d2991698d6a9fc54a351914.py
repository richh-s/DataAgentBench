code = """import json
import pandas as pd
import re

# Load funding data
funding_data = var_functions.query_db_36
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"Loaded {len(funding_df)} funding records")
print(f"Sample funding data: {funding_df[['Project_Name', 'Amount']].head()}")

# Identify disaster projects
# Disaster projects have FEMA, CalOES, or CalJPIA in their names
pattern = r'\(FEMA|FEMA\b|\(CalOES|\(CalJPIA'
disaster_mask = funding_df['Project_Name'].str.contains(pattern, case=False, na=False)
disaster_projects = funding_df[disaster_mask]

print(f"Found {len(disaster_projects)} disaster projects")
print(f"Sample disaster projects: {disaster_projects[['Project_Name', 'Amount']].head()}")

# Load civic documents data
civic_docs = var_functions.query_db_48

print(f"Loaded {len(civic_docs)} civic documents")

# Extract project information from civic documents
projects_from_docs = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 10:
            # Check if this looks like a project name
            if line == line.title() and not line.startswith('(') and not line.isupper() and len(line.split()) >= 2:
                # This could be a project name
                if current_project:
                    projects_from_docs.append(current_project)
                
                current_project = {'name': line, 'text': line + '\n'}
            elif current_project and (line.startswith('(') or 'Updates:' in line or 'Project Schedule:' in line or 'cid:' in line):
                if len(line) < 200:  # Skip very long lines
                    current_project['text'] += line + '\n'
    
    if current_project:
        projects_from_docs.append(current_project)

# Parse projects
parsed_projects = []
for proj in projects_from_docs:
    parsed = {'Project_Name': proj['name']}
    text = proj['text']
    
    # Determine type
    has_disaster_indicators = any(indicator in text.lower() for indicator in ['fema', 'caloes', 'caljpia', 'disaster'])
    has_disaster_suffix = any(suffix in text for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)'])
    
    if has_disaster_indicators or has_disaster_suffix:
        parsed['type'] = 'disaster'
    else:
        parsed['type'] = 'capital'
    
    # Extract start date
    if re.search(r'2022[\s\-](Spring|Fall|Summer|Winter|Q[1-4])', text) or '2022-' in text:
        parsed['start_year'] = '2022'
    elif re.search(r'(Spring|Fall|Summer|Winter)[\s\-]2022', text):
        parsed['start_year'] = '2022'
    else:
        parsed['start_year'] = None
    
    parsed_projects.append(parsed)

# Create DataFrame
projects_df = pd.DataFrame(parsed_projects)

# Filter for disaster projects starting in 2022
disaster_2022 = projects_df[(projects_df['type'] == 'disaster') & (projects_df['start_year'] == '2022')]

print(f"Found {len(disaster_2022)} disaster projects starting in 2022 from documents")
print(f"Sample: {disaster_2022.head()}")

# Match with funding data
projects_2022_with_funding = []
for _, doc_proj in disaster_2022.iterrows():
    doc_name = doc_proj['Project_Name']
    
    # Try exact match
    match = disaster_projects[disaster_projects['Project_Name'].str.lower() == doc_name.lower()]
    
    if match.empty:
        # Try partial match
        match = disaster_projects[disaster_projects['Project_Name'].str.lower().str.contains(doc_name.lower(), na=False)]
    
    if match.empty and '(' in doc_name:
        # Try without suffix
        base_name = doc_name.split('(')[0].strip()
        match = disaster_projects[disaster_projects['Project_Name'].str.lower().str.contains(base_name.lower(), na=False)]
    
    if not match.empty:
        projects_2022_with_funding.extend(match.to_dict('records'))

# Also look for projects that explicitly have 2022 in their names
explicit_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Combine results
if projects_2022_with_funding:
    projects_2022_df = pd.DataFrame(projects_2022_with_funding).drop_duplicates()
    all_2022 = pd.concat([projects_2022_df, explicit_2022]).drop_duplicates()
else:
    all_2022 = explicit_2022

# Calculate total funding
total_funding = all_2022['Amount'].sum()
num_projects = len(all_2022)

print(f"\nFinal result:")
print(f"Number of 2022 disaster projects: {num_projects}")
print(f"Total funding: ${total_funding:,}")

result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': all_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
