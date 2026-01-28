code = """import json
import re

# Load the civic documents data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Convert funding records to a dictionary for easier lookup by project name
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[project_name] = amount

# Find park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Look for completion indicators with 2022
    if 'completed' in text and '2022' in text and 'park' in text:
        # Extract project names - look for lines before updates/schedule
        lines = doc.get('text', '').split('\n')
        current_project = None
        
        for line in lines:
            orig_line = line.strip()
            lower_line = orig_line.lower()
            
            # Skip empty lines and known section headers
            if not orig_line or any(skip in lower_line for skip in ['updates:', 'schedule:', 'project description:', 'status:']):
                continue
                
            # Check if this is a project name (not too short, starts with capital or has specific keywords)
            if ('park' in lower_line and 
                len(orig_line) > 10 and 
                not orig_line.startswith('(') and
                not orig_line.startswith('•') and
                not lower_line.startswith('page')):
                current_project = orig_line
                
                # Check if this specific project was completed in 2022
                project_index = doc.get('text', '').find(orig_line)
                if project_index != -1:
                    # Look for completion text after the project name
                    text_after = doc.get('text', '')[project_index:project_index+500].lower()
                    if 'completed' in text_after and '2022' in text_after:
                        park_projects_2022.append(current_project)

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for proj in park_projects_2022:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print('__RESULT__:')
print(json.dumps({
    'projects': unique_projects,
    'count': len(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
