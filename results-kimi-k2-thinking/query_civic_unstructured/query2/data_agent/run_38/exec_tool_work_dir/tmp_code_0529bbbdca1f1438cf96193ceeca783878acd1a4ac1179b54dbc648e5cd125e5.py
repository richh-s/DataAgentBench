code = """import json

# Load documents
civic_docs_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create simple dictionaries
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name'].lower()
    funding_lookup[project_name] = int(record['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    lines = doc.get('text', '').split('\n')
    
    # Look for projects that mention park, completed, and 2022 together
    if 'park' in text and 'completed' in text and '2022' in text:
        for line in lines:
            line_lower = line.lower()
            if ('park' in line_lower and 
                ('project' in line_lower or 'construction' in line_lower or 
                 'improvements' in line_lower or 'repairs' in line_lower)):
                park_projects.append(line.strip())

# Remove duplicates
unique_projects = list(set(park_projects))

# Match with funding - simple exact match approach
total_funding = 0
matched_names = []

for project in unique_projects:
    project_key = project.lower()
    if project_key in funding_lookup:
        total_funding += funding_lookup[project_key]
        matched_names.append(project)

# Output results
print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'projects_matched': matched_names,
    'candidates_found': unique_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
