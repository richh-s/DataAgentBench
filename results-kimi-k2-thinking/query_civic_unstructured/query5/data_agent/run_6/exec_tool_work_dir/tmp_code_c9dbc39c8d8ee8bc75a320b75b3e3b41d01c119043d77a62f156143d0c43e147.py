code = """import json
import pandas as pd
import re

# Load funding data from the stored result
funding_result = var_functions.query_db_36
funding_df = pd.DataFrame(funding_result)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"Loaded {len(funding_df)} funding records")

# Load civic documents from the stored result
civic_result = var_functions.query_db_48
print(f"Loaded {len(civic_result)} civic documents")

# First, identify disaster projects from funding data
# Disaster projects have FEMA, CalOES, or CalJPIA in their names
disaster_pattern = r'\(FEMA|\(CalOES|\(CalJPIA|FEMA\b|CalOES\b|CalJPIA\b'
is_disaster = funding_df['Project_Name'].str.contains(disaster_pattern, case=False, na=False)
disaster_funding = funding_df[is_disaster].copy()

print(f"Found {len(disaster_funding)} disaster-related funding records")

# Extract project information from civic documents
projects_2022_disaster = []

for doc in civic_result:
    text = doc['text']
    
    # Look for disaster projects that mention 2022
    if '2022' in text and any(indicator in text.lower() for indicator in ['fema', 'caloes', 'caljpia']):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project names (typically title case, not uppercase, and reasonable length)
            if (len(line) > 10 and 
                line == line.title() and 
                not line.isupper() and 
                not line.startswith('(') and
                len(line.split()) >= 2):
                
                # Check if this project line contains 2022 or is near 2022/disaster mentions
                project_text = line + '\n' + '\n'.join(lines[lines.index(line):lines.index(line)+10])
                
                if '2022' in project_text and any(indicator in project_text.lower() for indicator in ['fema', 'caloes', 'caljpia']):
                    projects_2022_disaster.append(line)

# Remove duplicates
projects_2022_disaster = list(set(projects_2022_disaster))

print(f"Found {len(projects_2022_disaster)} disaster projects mentioned in 2022 civic documents")
for proj in projects_2022_disaster:
    print(f"  - {proj}")

# First approach: Find projects with 2022 explicitly in their name in funding data
explicit_2022 = disaster_funding[disaster_funding['Project_Name'].str.contains('2022', case=False, na=False)]

print(f"\nFound {len(explicit_2022)} disaster projects with '2022' in their funding record name")

# Second approach: Match document projects with funding data
matched_projects = []
for doc_proj in projects_2022_disaster:
    # Try exact match first
    matches = disaster_funding[disaster_funding['Project_Name'].str.lower() == doc_proj.lower()]
    
    if matches.empty:
        # Try partial match - look for projects containing key words from the doc project
        key_words = doc_proj.split()
        if len(key_words) >= 2:
            # Try with first few significant words
            search_terms = [word for word in key_words if len(word) > 3][:3]
            if search_terms:
                pattern = '|'.join(search_terms)
                matches = disaster_funding[disaster_funding['Project_Name'].str.lower().str.contains(pattern, case=False, na=False)]
    
    if not matches.empty:
        matched_projects.extend(matches.to_dict('records'))

# Create DataFrames
explicit_df = explicit_2022[['Project_Name', 'Amount']]
if matched_projects:
    matched_df = pd.DataFrame(matched_projects)[['Project_Name', 'Amount']].drop_duplicates()
    # Combine results
    all_2022_projects = pd.concat([explicit_df, matched_df]).drop_duplicates()
else:
    all_2022_projects = explicit_df

# Calculate total funding
total_funding = all_2022_projects['Amount'].sum()
num_projects = len(all_2022_projects)

print(f"\nFinal result:")
print(f"Total 2022 disaster projects: {num_projects}")
print(f"Total funding: ${total_funding:,}")
print("\nProject breakdown:")
for _, proj in all_2022_projects.iterrows():
    print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")

# If no explicit 2022 projects found, check all disaster projects
if total_funding == 0:
    print("\nNo 2022-specific disaster projects found. Here are ALL disaster projects:")
    total_all_disaster = disaster_funding['Amount'].sum()
    print(f"Total ALL disaster funding: ${total_all_disaster:,}")
    result = {
        'total_funding': int(total_all_disaster),
        'num_projects': len(disaster_funding),
        'note': 'No 2022-specific projects identified - showing all disaster projects',
        'projects': disaster_funding[['Project_Name', 'Amount']].head(10).to_dict('records')
    }
else:
    result = {
        'total_funding': int(total_funding),
        'num_projects': int(num_projects),
        'projects': all_2022_projects.to_dict('records')
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
