code = """import json

# Load data from files
mongo_file = str(globals()['var_functions.query_db:5'])
funding_file = str(globals()['var_functions.query_db:20'])

with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Search for Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this is a project header (usually not indented, doesn't start with special chars)
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('▪') and 
            not line.startswith('•') and
            not line.lower().startswith('project ') and
            '2022' not in line and  # Skip lines with dates
            ':' not in line):  # Skip lines with colons
            current_project = line
        
        # Check for Spring 2022 schedule
        if current_project and ('Spring 2022' in line or 'spring 2022' in line):
            spring_2022_projects.append(current_project)
            break

# Match with funding
matched = []
total_funding = 0

for project in spring_2022_projects:
    if project in funding_map:
        matched.append({'name': project, 'funding': funding_map[project]})
        total_funding += funding_map[project]

result = {'count': len(matched), 'funding': total_funding, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}, 'var_functions.query_db:36': [{'count': '500', 'total_funding': '28094000'}]}

exec(code, env_args)
