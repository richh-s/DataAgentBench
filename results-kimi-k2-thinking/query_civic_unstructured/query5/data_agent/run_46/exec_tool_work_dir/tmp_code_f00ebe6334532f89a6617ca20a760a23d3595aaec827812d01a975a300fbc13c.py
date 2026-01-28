code = """import json
import re

# Access data from storage
funding_records = locals()['var_functions.query_db:2']
civic_docs = locals()['var_functions.query_db:32']

# Find all disaster projects from funding data (FEMA/CalOES/CalJPIA)
disaster_project_names = []
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    if '(FEMA' in proj_name or '(CalOES' in proj_name or '(CalJPIA' in proj_name:
        clean_name = proj_name.split(' (')[0]  # Remove suffix
        disaster_project_names.append(clean_name)

# Look for these projects starting in 2022 in civic documents
projects_starting_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Check each disaster project
    for disaster_proj in disaster_project_names:
        if disaster_proj in text and '2022' in text:
            # Verify it's actually starting in 2022 (check context)
            pos = text.find(disaster_proj)
            if pos != -1:
                # Look at surrounding text for date references
                snippet = text[max(0, pos-200):pos+200]
                if '2022' in snippet:
                    projects_starting_2022.append(disaster_proj)

# Remove duplicates
projects_starting_2022 = list(set(projects_starting_2022))

# Get funding for these projects
funding_totals = {}
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    base_name = proj_name.split(' (')[0]
    if base_name in projects_starting_2022:
        if base_name not in funding_totals:
            funding_totals[base_name] = 0
        funding_totals[base_name] += amount

# Calculate total funding
total_funding = sum(funding_totals.values())

result = {
    'total_funding': total_funding,
    'project_count': len(projects_starting_2022),
    'funded_project_count': len(funding_totals),
    'projects': projects_starting_2022,
    'funding_breakdown': funding_totals
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
