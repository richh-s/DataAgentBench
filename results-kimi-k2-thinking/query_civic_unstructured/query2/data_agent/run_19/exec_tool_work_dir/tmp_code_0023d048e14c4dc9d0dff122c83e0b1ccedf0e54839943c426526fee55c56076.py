code = """import json
import re

funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:14']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation']
completed_2022_park_projects = []

for doc in civic_docs:
    if isinstance(doc, dict):
        text = doc.get('text', '').lower()
        
        # Check if it mentions completion in 2022
        if '2022' in text and ('completed' in text or 'construction was completed' in text):
            lines = doc.get('text', '').split('\n')
            current_project = None
            
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                
                # Look for project name
                if len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
                    # Likely a project name
                    current_project = line
                
                # Check if this line mentions completion in 2022
                if '2022' in line and 'completed' in line.lower():
                    # If current project is park-related, add it
                    if current_project and any(kw in current_project.lower() for kw in park_keywords):
                        completed_2022_park_projects.append(current_project)

# Now match with funding data
total_funding = 0
matched_projects = []

for funding in funding_records:
    if isinstance(funding, dict):
        project_name = funding.get('Project_Name', '')
        amount = int(funding.get('Amount', 0))
        
        # Check if park project
        proj_lower = project_name.lower()
        if not any(kw in proj_lower for kw in park_keywords):
            continue
        
        # Check if completed in 2022
        for completed_project in completed_2022_park_projects:
            # Simple name matching
            comp_lower = completed_project.lower()
            
            # Check for overlap
            name_match = False
            if project_name in completed_project or completed_project in project_name:
                name_match = True
            else:
                # Check if key words match
                proj_words = proj_lower.split()
                comp_words = comp_lower.split()
                if len(proj_words) > 1 and len(comp_words) > 1:
                    # Check if at least 2 words match
                    matching_words = sum(1 for w in proj_words if w in comp_words and len(w) > 3)
                    if matching_words >= 2:
                        name_match = True
            
            if name_match:
                total_funding += amount
                matched_projects.append({
                    'funding_name': project_name,
                    'doc_name': completed_project,
                    'amount': amount
                })
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
