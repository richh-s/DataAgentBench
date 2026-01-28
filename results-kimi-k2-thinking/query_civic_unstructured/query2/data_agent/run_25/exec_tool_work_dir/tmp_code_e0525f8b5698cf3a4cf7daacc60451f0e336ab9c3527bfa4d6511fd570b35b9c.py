code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    doc_text = doc.get('text', '')
    lines = doc_text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        line_lower = line.lower()
        # Look for park in the line
        if 'park' in line_lower:
            # Check if line seems like a project name (not too short, not a header)
            if len(line.strip()) > 10 and 'capital improvement' not in line_lower and 'status report' not in line_lower:
                # Check subsequent lines for completion in 2022
                for j in range(i, min(i+15, len(lines))):
                    next_line = lines[j].lower()
                    if 'completed' in next_line and '2022' in next_line:
                        project_name = lines[i].strip()
                        if project_name not in park_projects:
                            park_projects.append(project_name)
                        break

# Find funding
funding_matches = []
total_funding = 0

for project in park_projects:
    # Direct match
    if project in funding_dict:
        funding_matches.append({'project': project, 'amount': funding_dict[project]})
        total_funding += funding_dict[project]
    else:
        # Check for partial matches
        for funding_project, amount in funding_dict.items():
            if project.lower() in funding_project.lower() or funding_project.lower() in project.lower():
                if any(park_word in funding_project.lower() for park_word in ['bluffs park', 'trancas canyon park', 'malibu park', 'legacy park']):
                    funding_matches.append({'project': funding_project, 'amount': amount})
                    total_funding += amount
                    break

result = {'park_projects': park_projects, 'funding_matches': funding_matches, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
