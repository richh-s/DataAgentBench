code = """import json
import re
import pandas as pd

# Get the stored results
civic_docs_result = locals()['var_functions.query_db:2']
funding_result = locals()['var_functions.query_db:5']

# Read the civic documents
with open(civic_docs_result, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Parse civic documents to extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project blocks - pattern: project name followed by updates
    # Common pattern is project name on its own line, then indented updates with • or parentheses
    lines = text.split('\n')
    
    current_project = None
    project_text = ""
    
    for line in lines:
        line = line.strip()
        
        # Check if this is a project name (starts with capital letters, not a bullet point)
        if (line and 
            not line.startswith('\u2022') and 
            not line.startswith('(') and 
            not line.startswith('-') and
            not line.startswith('cid:') and
            len(line) < 150 and  # Reasonable length for project name
            any(keyword in line.lower() for keyword in ['project', 'repairs', 'improvements', 'construction', 'renovation'])):
            
            # Process previous project if exists
            if current_project:
                # Check if it's park-related and completed in 2022
                is_park = 'park' in project_text.lower() or 'park' in current_project.lower()
                is_completed = 'completed' in project_text.lower()
                completed_in_2022 = '2022' in project_text
                
                if is_park and is_completed and completed_in_2022:
                    park_projects_2022.append(current_project)
            
            # Start new project
            current_project = line
            project_text = line + "\n"
        elif current_project:
            project_text += line + "\n"
    
    # Don't forget the last project
    if current_project:
        is_park = 'park' in project_text.lower() or 'park' in current_project.lower()
        is_completed = 'completed' in project_text.lower()
        completed_in_2022 = '2022' in project_text
        
        if is_park and is_completed and completed_in_2022:
            park_projects_2022.append(current_project)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

print(f"Found {len(park_projects_2022)} park projects completed in 2022")
print("Projects:", park_projects_2022)

# Match with funding data
# Create a mapping of project names to cleaned names for matching
funding_projects = funding_df['Project_Name'].tolist()
matched_projects = []

for park_project in park_projects_2022:
    # Find matching funding records
    for funding_project in funding_projects:
        # Normalize names for comparison
        park_norm = park_project.lower().replace('project', '').strip()
        funding_norm = funding_project.lower().replace('project', '').strip()
        
        # Check for partial matches
        if (park_norm in funding_norm or funding_norm in park_norm or
            any(word in funding_norm.split() for word in park_norm.split() if len(word) > 3)):
            matched_projects.append(funding_project)

# Remove duplicates
matched_projects = list(set(matched_projects))

print(f"Matched with {len(matched_projects)} funding records")
print("Matched projects:", matched_projects[:10])  # Show first 10

# Get funding amounts
matched_funding = funding_df[funding_df['Project_Name'].isin(matched_projects)]
total_funding = matched_funding['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "park_projects_count": len(park_projects_2022),
    "matched_funding_count": len(matched_funding),
    "total_funding": int(total_funding),
    "park_projects": park_projects_2022,
    "matched_projects": matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
