code = """import json
import re

# Load data
docs = json.load(open(locals()['var_functions.query_db:8']))

park_projects_2022 = set()

for doc in docs:
    text = doc.get('text','')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Basic check for project name with park
        if 'park' in line.lower() and len(line) < 150:
            # Skip headers
            header_words = ['capital improvement','disaster recovery','status report','discussion','recommended action','projects','agenda']
            skip = False
            for hw in header_words:
                if hw in line.lower():
                    skip = True
                    break
            if skip or line.startswith('(') or line.startswith('cid:'):
                continue
                
            # Check next few lines for completion
            for j in range(i, min(len(lines), i+8)):
                context = lines[j]
                if 'completed' in context.lower() and '2022' in context:
                    park_projects_2022.add(line)
                    break

# Load funding data
funding = json.load(open(locals()['var_functions.query_db:6']))

# Find funding for these completed 2022 projects
total_funding = 0
matched_projects = []

for proj in list(park_projects_2022):
    for record in funding:
        if proj.lower() in record['Project_Name'].lower():
            total_funding += int(record['Amount'])
            matched_projects.append(record['Project_Name'])
            break

result = {
    'completed_2022_park_projects': list(park_projects_2022),
    'funding_total': total_funding,
    'funding_records_matched': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:26': {'potential_docs_with_2022_completion': 5, 'park_projects_in_funding': 20}}

exec(code, env_args)
