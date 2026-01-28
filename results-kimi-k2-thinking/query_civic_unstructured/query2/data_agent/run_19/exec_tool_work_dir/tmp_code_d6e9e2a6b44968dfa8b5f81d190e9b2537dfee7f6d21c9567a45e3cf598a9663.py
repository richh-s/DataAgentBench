code = """import json
import re

# Load full datasets
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:14']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract projects completed in 2022 from civic documents
completed_2022_projects = []

for doc in civic_docs:
    if isinstance(doc, dict):
        text = doc.get('text', '')
        lines = text.split('\n')
        
        current_project = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines and bullets
            if not line or line.startswith('(cid:') or line.startswith('—'):
                continue
                
            # Look for project-like names (typically title case, not bullet points)
            if (len(line) > 10 and 
                not line.startswith('•') and 
                not line.startswith('(') and
                (line.istitle() or (line[0].isupper() and any(keyword in line.lower() for keyword in ['project', 'repair', 'improvement', 'structure'])))):
                current_project = line
                
            # Look for completion in 2022
            if current_project and '2022' in line:
                lower_line = line.lower()
                if 'completed' in lower_line or 'completion' in lower_line:
                    # Add to completed projects
                    completed_2022_projects.append({
                        'name': current_project,
                        'status_line': line
                    })

# Filter for park-related projects
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation', 'trancas canyon', 'legacy park']
park_projects_completed_2022 = []

for project in completed_2022_projects:
    name_lower = project['name'].lower()
    if any(keyword in name_lower for keyword in park_keywords):
        park_projects_completed_2022.append(project['name'])

# Match with funding data and calculate total funding
total_funding = 0
funded_park_projects = []

for funding in funding_records:
    if isinstance(funding, dict):
        project_name = funding.get('Project_Name', '')
        amount = int(funding.get('Amount', 0))
        
        # Check if this is a park project completed in 2022
        for completed_project in park_projects_completed_2022:
            # Match project names (partial match is OK)
            proj_lower = project_name.lower()
            completed_lower = completed_project.lower()
            
            # Check for name overlap
            if (project_name in completed_project or 
                completed_project in project_name or
                any(name_part in completed_lower for name_part in proj_lower.split()) and 
                any(name_part in proj_lower for name_part in completed_lower.split())):
                
                # Verify it's a park project
                if any(keyword in proj_lower for keyword in park_keywords):
                    total_funding += amount
                    funded_park_projects.append({
                        'project': project_name,
                        'matched_with': completed_project,
                        'amount': amount
                    })
                    break

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022_park_projects': total_funding,
    'project_count': len(funded_park_projects),
    'projects': funded_park_projects[:10]  # Sample
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
