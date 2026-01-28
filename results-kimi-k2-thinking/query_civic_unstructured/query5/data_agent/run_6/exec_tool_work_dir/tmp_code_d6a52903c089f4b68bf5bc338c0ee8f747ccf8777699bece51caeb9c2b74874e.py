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

print(f"Loaded {len(funding_df)} funding records")
print(f"Loaded {len(civic_docs)} civic documents")

# Find disaster-related funding directly from funding data
# Disaster projects often have suffixes like (FEMA Project), (CalJPIA Project), (CalOES Project)
is_disaster = funding_df['Project_Name'].str.contains(r'(FEMA|CalOES|CalJPIA)', case=False, na=False)

disaster_funding_df = funding_df[is_disaster].copy()
disaster_funding_df['Amount'] = disaster_funding_df['Amount'].astype(int)

print(f"Found {len(disaster_funding_df)} disaster-related funding records")
print("Sample disaster projects:")
print(disaster_funding_df[['Project_Name', 'Amount']].head(10).to_string())

# Look for projects with 2022 in their name (explicit 2022 projects)
explicit_2022 = disaster_funding_df[disaster_funding_df['Project_Name'].str.contains('2022', case=False, na=False)]

print(f"\nFound {len(explicit_2022)} explicit 2022 disaster projects")
if len(explicit_2022) > 0:
    total_funding = explicit_2022['Amount'].sum()
    print(f"Total funding for explicit 2022 projects: ${total_funding:,}")
    print("\nExplicit 2022 Disaster Projects:")
    for _, proj in explicit_2022.iterrows():
        print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")
else:
    # If no explicit 2022 projects found, analyze documents for 2022 disaster projects
    projects_2022_from_docs = []
    
    for doc in civic_docs:
        text = doc['text']
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines mentioning 2022 and disaster indicators
            if '2022' in line:
                # Check surrounding context for disaster indicators
                context = ' '.join(lines[max(0, i-5):min(len(lines), i+5)])
                if any(indicator in context.lower() for indicator in ['fema', 'caloes', 'disaster', 'fire recovery']):
                    # Look for matching projects in funding data
                    for proj_name in disaster_funding_df['Project_Name']:
                        if any(part.lower() in context.lower() for part in proj_name.split() if len(part) > 4):
                            projects_2022_from_docs.append(proj_name)
    
    # Find unique projects
    unique_2022_projects = list(set(projects_2022_from_docs))
    print(f"\nFound {len(unique_2022_projects)} potential 2022 disaster projects from document analysis")
    
    # Filter funding data for these projects
    if unique_2022_projects:
        projects_2022_df = disaster_funding_df[disaster_funding_df['Project_Name'].isin(unique_2022_projects)]
        total_funding = projects_2022_df['Amount'].sum()
        print(f"Total funding for document-identified 2022 projects: ${total_funding:,}")
    else:
        total_funding = 0
        projects_2022_df = pd.DataFrame()

# Prepare result
if 'total_funding' in locals() and total_funding > 0:
    result = {
        'total_funding': int(total_funding),
        'num_projects': len(explicit_2022) if len(explicit_2022) > 0 else len(projects_2022_df),
        'projects': explicit_2022[['Project_Name', 'Amount']].to_dict('records') if len(explicit_2022) > 0 else projects_2022_df[['Project_Name', 'Amount']].to_dict('records')
    }
else:
    # Fallback - show overall disaster funding
    result = {
        'total_funding': int(disaster_funding_df['Amount'].sum()),
        'num_projects': len(disaster_funding_df),
        'note': 'Could not specifically identify 2022 start dates. Showing all disaster projects.',
        'projects': disaster_funding_df[['Project_Name', 'Amount']].head(10).to_dict('records')
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
