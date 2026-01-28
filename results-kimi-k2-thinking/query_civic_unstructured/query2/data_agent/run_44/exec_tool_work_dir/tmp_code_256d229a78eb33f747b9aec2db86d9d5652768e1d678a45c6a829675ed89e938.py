code = """import json

# Load the data files
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert amounts to integers
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Simple approach: look for specific patterns in the text
    if 'park' in text.lower():
        # Check for 2022 completion
        if 'completed' in text.lower() and '2022' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Check if this is likely a project name
                if len(line) > 10 and len(line) < 150 and line[0].isupper():
                    if 'park' in line.lower() and line not in park_projects_2022:
                        park_projects_2022.append(line)

# Get funding for these projects
total_funding = 0
funded_projects = []

for project_name in park_projects_2022:
    proj_lower = project_name.lower()
    
    # Find matching funding records
    for fund in funding_data:
        fund_name_lower = fund['Project_Name'].lower()
        
        # Direct match or close match
        if proj_lower == fund_name_lower or fund_name_lower in proj_lower or proj_lower in fund_name_lower:
            total_funding += fund['Amount']
            funded_projects.append({
                'project': project_name,
                'funding_record': fund['Project_Name'],
                'amount': fund['Amount']
            })

result = {
    'park_projects_2022': park_projects_2022,
    'project_count': len(park_projects_2022),
    'total_funding': total_funding,
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
