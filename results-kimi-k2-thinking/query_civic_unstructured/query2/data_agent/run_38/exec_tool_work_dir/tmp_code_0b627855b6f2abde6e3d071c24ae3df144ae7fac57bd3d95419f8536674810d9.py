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

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for completed projects with 2022 dates
    # Pattern: project name line followed by updates mentioning completion and 2022
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for completion mentions with 2022
        if 'completed' in line.lower() and '2022' in line:
            # Look back to find the project name (could be 1-3 lines back)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if (prev_line and 
                    not prev_line.startswith('\u2022') and 
                    not prev_line.startswith('(') and 
                    len(prev_line) < 100 and
                    ('project' in prev_line.lower() or 'repairs' in prev_line.lower() or 
                     'improvements' in prev_line.lower() or 'construction' in prev_line.lower())):
                    
                    # Check if it's park-related
                    if 'park' in prev_line.lower():
                        park_projects_2022.add(prev_line)
                    # Also check the text around it
                    context = ' '.join(lines[max(0, i-3):i+3]).lower()
                    if 'park' in context:
                        park_projects_2022.add(prev_line)

# Convert to list
park_projects_2022 = list(park_projects_2022)

# Manual inspection of some key project names for matching
print(f"Found {len(park_projects_2022)} park projects completed in 2022")

# Create a dictionary of normalized project names for matching
funding_projects = funding_df['Project_Name'].tolist()
project_lookup = {}

for funding_project in funding_projects:
    # Create variations for matching
    key = funding_project.lower().replace('project', '').replace('  ', ' ').strip()
    project_lookup[key] = funding_project

# Match the park projects with funding records
matched_funding_records = []

for park_project in park_projects_2022:
    park_key = park_project.lower().replace('project', '').replace('  ', ' ').strip()
    
    # Find matches
    for lookup_key, original_name in project_lookup.items():
        if (park_key in lookup_key or lookup_key in park_key):
            matched_funding_records.append(original_name)
        # Also check word overlap
        elif len(set(park_key.split()) & set(lookup_key.split())) >= 2:
            matched_funding_records.append(original_name)

# Remove duplicates
matched_funding_records = list(set(matched_funding_records))

# Get funding amounts
matched_funding_df = funding_df[funding_df['Project_Name'].isin(matched_funding_records)]
total_funding = matched_funding_df['Amount'].sum()

# Also manually check for some obvious matches
print("Sample matched projects:", matched_funding_records[:5])
print("Total funding matched:", total_funding)

print("__RESULT__:")
print(json.dumps({
    "park_projects_2022": park_projects_2022,
    "matched_funding_count": len(matched_funding_records),
    "total_funding": float(total_funding),
    "sample_matched_projects": matched_funding_records[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
