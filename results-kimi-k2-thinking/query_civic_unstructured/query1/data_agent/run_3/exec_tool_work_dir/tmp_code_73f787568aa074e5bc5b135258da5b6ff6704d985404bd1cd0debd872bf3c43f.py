code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find capital design projects
capital_design = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if 'Capital Improvement Projects (Design)' in line:
            # Look at next 50 lines for project names
            for j in range(i+2, min(i+50, len(lines))):
                proj_line = lines[j].strip()
                if 'Capital Improvement' in proj_line or 'Disaster Recovery' in proj_line:
                    break
                if proj_line and len(proj_line) > 8 and 'Project' in proj_line:
                    if 'fema' not in proj_line.lower():
                        capital_design.add(proj_line)

# Get count of capital design projects
count_design = len(capital_design)

# Match with funding > 50000
matches = []

for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        proj_name = funding['Project_Name']
        base_name = re.sub(r'\s*\([^)]*\)$', '', proj_name)
        
        if base_name in capital_design:
            matches.append(base_name)

final_count = len(set(matches))

result = {'count': final_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
