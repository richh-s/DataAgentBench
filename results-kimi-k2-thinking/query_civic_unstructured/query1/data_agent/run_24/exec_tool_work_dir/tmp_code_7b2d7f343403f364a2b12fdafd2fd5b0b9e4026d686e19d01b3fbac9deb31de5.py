code = """import json
import re

# Read funding data from file path
funding_file_path = var_functions.query_db:6
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Filter funding data for Amount > 50000
funding_over_50k = [record for record in funding_data if int(record['Amount']) > 50000]

# Read civic documents from file path
civic_file_path = var_functions.query_db:5
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    sections = re.split(r'\n(?=Capital Improvement Projects)', text)
    
    for section in sections:
        if 'Capital Improvement Projects' in section:
            if '(Design)' in section:
                status = 'design'
            elif '(Construction)' in section:
                status = 'construction'
            elif '(Not Started)' in section:
                status = 'not started'
            else:
                continue
                
            lines = section.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if not line or line.startswith('Capital Improvement Projects'):
                    continue
                if i + 1 < len(lines):
                    next_line = lines[i+1].strip()
                    if next_line.startswith('(cid:') or 'Updates:' in next_line or 'Project Schedule:' in next_line:
                        project_name = line
                        projects.append({
                            'Project_Name': project_name,
                            'type': 'capital',
                            'status': status
                        })

# Count design status projects
design_projects = [p for p in projects if p['status'] == 'design']

# Match design capital projects with funding > 50k
matched_projects = []
for project in design_projects:
    for funding_record in funding_over_50k:
        funding_name = funding_record['Project_Name']
        if project['Project_Name'] == funding_name or funding_name.startswith(project['Project_Name'] + ' '):
            matched_projects.append(project['Project_Name'])

result = len(matched_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
