code = """import json

# Load all civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Search for completed park projects in 2022
park_projects = []

for doc in documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for lines mentioning completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'construction was completed' in line.lower()):
            # Look backwards to find the project name (usually 2-5 lines above)
            project_name = None
            for j in range(max(0, i-10), i):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 5 and not any(x in prev_line.lower() for x in [
                    'capital improvement', 'disaster recovery', 'public works', 'commission meeting',
                    'agenda report', 'recommended action', 'subject:', 'page ', 'item ', 'council meeting'
                ]):
                    # Check if this line is a project name (usually doesn't contain common words)
                    if 'Updates:' not in prev_line and 'project schedule' not in prev_line.lower():
                        project_name = prev_line
                        break
            
            if project_name and 'park' in project_name.lower():
                park_projects.append({
                    'project_name': project_name,
                    'completion_note': line
                })

# Load funding data to match with projects
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Find funding for park projects completed in 2022
total_funding = 0
funded_projects = []

for project in park_projects:
    project_name = project['project_name']
    
    # Find matching funding records
    for fund in funding_records:
        if project_name.lower() in fund['Project_Name'].lower() or \
           fund['Project_Name'].lower() in project_name.lower():
            amount = int(fund['Amount'])
            total_funding += amount
            funded_projects.append({
                'project': project_name,
                'funding_record': fund['Project_Name'],
                'amount': amount,
                'source': fund['Funding_Source']
            })

result = {
    'total_funding': total_funding,
    'funded_projects': funded_projects,
    'park_projects_found': len(park_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
