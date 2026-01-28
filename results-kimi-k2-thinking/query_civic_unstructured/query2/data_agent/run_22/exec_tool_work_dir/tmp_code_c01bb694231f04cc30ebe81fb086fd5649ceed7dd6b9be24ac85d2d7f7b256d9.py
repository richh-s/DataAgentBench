code = """import json, re

civic_path = 'var_functions.query_db_36'
funding_path = 'var_functions.query_db_8'

# Load data from stored file paths
civic_docs = json.load(open(civic_path))
funding_data = json.load(open(funding_path))

park_projects = []

# Find park projects completed in 2022
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for park project names
        if 'Park' in line and len(line) < 150:
            # Skip metadata lines
            skip_terms = ['updates', 'schedule', 'description', 'page', 'agenda', 'item']
            if not any(term in line.lower() for term in skip_terms):
                # Check if this project was completed in 2022
                # Look in surrounding text for completion and 2022
                context = ' '.join(lines[max(0,i-2):min(len(lines),i+5)])
                if 'completed' in context.lower() and '2022' in context:
                    if line not in park_projects:
                        park_projects.append(line)

# Match with funding records
total = 0
matched = 0

for project in park_projects:
    proj_lower = project.lower().strip()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Match project names
        if proj_lower == fund_name:
            total += int(fund['Amount'])
            matched += 1
        elif fund_name.startswith(proj_lower):
            total += int(fund['Amount'])
            matched += 1

result = {'total_funding': total, 'projects_matched': matched, 'park_projects': park_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
