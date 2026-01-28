code = """import json
import re

# Load data from storage
civic_docs = locals()['var_functions.query_db:32']
funding_records = locals()['var_functions.query_db:2']

# Find disaster-related projects mentioning 2022
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        # Look for FEMA/CalOES/CalJPIA projects
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 5:
                # Check for disaster indicators in the line
                if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                    # Clean project name
                    clean_name = re.sub(r'\s*\([A-Z/]*\s*Project\)', '', line)
                    if clean_name not in disaster_projects:
                        disaster_projects.append(clean_name)

# Find matching funding records
matched_funding = {}
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if this matches any disaster project
    for disaster_proj in disaster_projects:
        if disaster_proj.lower() in proj_name.lower() or proj_name.lower().replace(' (fema project)', '') in disaster_proj.lower():
            if proj_name not in matched_funding:
                matched_funding[proj_name] = 0
            matched_funding[proj_name] += amount

# Calculate total
total_funding = sum(matched_funding.values())

print('__RESULT__:')
print(json.dumps({
    "total_funding": total_funding,
    "disaster_projects_found": len(disaster_projects),
    "projects_with_funding": len(matched_funding),
    "funding_breakdown": matched_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
