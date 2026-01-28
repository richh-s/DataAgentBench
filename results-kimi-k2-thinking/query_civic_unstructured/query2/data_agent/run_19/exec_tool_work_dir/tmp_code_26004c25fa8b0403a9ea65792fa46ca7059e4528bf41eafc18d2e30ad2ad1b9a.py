code = """import json
import re

# Access the stored results
funding_data = locals()['var_functions.query_db:0']
civic_docs = locals()['var_functions.query_db:4']

# Since these might be file paths if too large, check and load
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Parse civic docs to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split by project sections (this is a simplified approach)
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        # Look for project name patterns
        if re.match(r'^[A-Z].+Project$', line.strip()) or 
           re.match(r'^[A-Z].+Improvements$', line.strip()) or
           re.match(r'^[A-Z].+Repair$', line.strip()):
            # Found a potential project name
            current_project = line.strip()
            
        # Look for status information
        if current_project and 'Updates:' in line:
            # Check next few lines for actual status
            continue
            
        # Look for completed status
        if current_project and 'Complete' in line and '2022' in line:
            status = 'completed'
            if 'Construction' in line or 'construction' in line:
                # Extract project info
                projects.append({
                    'project_name': current_project,
                    'status': status,
                    'completion_year': '2022'
                })
        elif current_project and 'completed' in line and '2022' in line:
            status = 'completed'
            projects.append({
                'project_name': current_project,
                'status': status,
                'completion_year': '2022'
            })

print(f"__RESULT__:")
print(json.dumps({
    'funding_count': len(funding_data),
    'civic_docs_count': len(civic_docs),
    'extracted_projects': len(projects),
    'sample_projects': projects[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
