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
    lines = doc_text.split(chr(10))
    
    for i in range(len(lines)):
        line = lines[i]
        line_lower = line.lower()
        if 'park' in line_lower:
            if len(line.strip()) > 10 and 'capital improvement' not in line_lower and 'status report' not in line_lower:
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
    if project in funding_dict:
        funding_matches.append({'project': project, 'amount': funding_dict[project]})
        total_funding += funding_dict[project]

# Also check all completed 2022 projects
all_completed_2022 = []
for doc in civic_docs:
    doc_text = doc.get('text', '')
    lines = doc_text.split(chr(10))
    for line in lines:
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line_lower and 'park' in line_lower:
            all_completed_2022.append(line.strip())

result = {
    'park_projects': park_projects,
    'all_completed_2022': all_completed_2022,
    'funding_matches': funding_matches,
    'total_funding': total_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
