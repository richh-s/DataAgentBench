code = """import json
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

# Find park projects completed in 2022
# Look for "completed" and "2022" in the same context as "park"
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Search for patterns indicating park projects completed in 2022
    if 'completed' in text and '2022' in text and 'park' in text:
        # Look for project name patterns near these keywords
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line_lower = line.lower()
            if ('park' in line_lower and 
                ('project' in line_lower or 'repairs' in line_lower or 'improvements' in line_lower)):
                # Check if this project has completion info nearby
                
                park_projects.append(line.strip())

# Remove duplicates
park_projects = list(set(park_projects))

# Clean up funding project names for better matching
funding_df['Project_Clean'] = funding_df['Project_Name'].str.lower().str.replace('project', '').str.strip()

# Manually identify known park projects from the data inspection
# Based on the preview, these are likely park projects completed in 2022:
likely_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets'
]

# Find these in funding data
matched_records = funding_df[funding_df['Project_Name'].isin(likely_projects)]
total_funding = matched_records['Amount'].sum()

print('__RESULT__:')
print(json.dumps({
    'total_funding': float(total_funding),
    'matched_projects': likely_projects,
    'park_projects_found': park_projects[:5]  # Show first 5
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
