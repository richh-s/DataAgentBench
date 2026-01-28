code = """import json

# Load data from file paths
civic_path = var_functions.query_db:2
funding_path = var_functions.query_db:4

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Build funding lookup
funding = {}
for rec in funding_recs:
    name = rec.get('Project_Name', '')
    if name:
        funding[name] = int(rec.get('Amount', 0))

# Find all projects mentioned with Spring 2022
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Search for project names that might be in funding table
        for fund_name in funding:
            if fund_name in text:
                # Basic proximity check - is Spring 2022 near the project name?
                proj_idx = text.find(fund_name)
                spring_idx = text.find('Spring 2022')
                if spring_idx == -1:
                    spring_idx = text.find('2022-Spring')
                
                if proj_idx > 0 and spring_idx > 0 and abs(proj_idx - spring_idx) < 1000:
                    if fund_name not in [p['name'] for p in found_projects]:
                        found_projects.append({'name': fund_name, 'funding': funding[fund_name]})

# Also try to extract project names from the text itself
project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation']
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 15 < len(line) < 150 and any(k in line for k in project_keywords):
                if not line.startswith('(') and not line.startswith('To:') and not line.startswith('From:'):
                    # Check if this matches any funded project
                    for fund_name in funding:
                        if line.lower() in fund_name.lower() or fund_name.lower() in line.lower():
                            if fund_name not in [p['name'] for p in found_projects]:
                                found_projects.append({'name': fund_name, 'funding': funding[fund_name]})

# Remove duplicates and count
project_count = len(found_projects)
total_funding = sum(p['funding'] for p in found_projects)

result = json.dumps({'project_count': project_count, 'total_funding': total_funding})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
