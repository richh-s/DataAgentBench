code = """import json
import pandas as pd

# Get stored results
civic_docs_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Identify park projects completed in 2022 from civic docs
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Look for park-related projects with completion in 2022
        if ('park' in line_lower and 
            ('completion' in line_lower or 'completed' in line_lower) and
            '2022' in text):
            park_projects_2022.append(line.strip())

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))

# From inspection of the preview, extract specific completed park projects
likely_matches = []

for project in funding_df['Project_Name']:
    p_lower = project.lower()
    # Match projects that are park-related and likely completed in 2022
    if ('park' in p_lower or 'green streets' in p_lower):
        likely_matches.append(project)

# Get funding for these projects
matched_df = funding_df[funding_df['Project_Name'].isin(likely_matches)]
total_amount = matched_df['Amount'].sum()

result = {
    'total_funding_2022': float(total_amount),
    'num_projects': len(likely_matches),
    'projects': likely_matches[:10]  # First 10
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
