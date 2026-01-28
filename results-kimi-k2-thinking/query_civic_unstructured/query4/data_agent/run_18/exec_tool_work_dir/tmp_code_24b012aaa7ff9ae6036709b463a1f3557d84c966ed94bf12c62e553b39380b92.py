code = """import json

# Load the data files
civic_docs_file = locals()['var_functions.query_db:11']
funding_file = locals()['var_functions.query_db:12']

civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    project_name = record.get('Project_Name', '').strip()
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

# Look for projects that started in Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Look for explicit mentions of Spring 2022
        if '2022' in line and 'Spring' in line:
            # Extract potential project name (clean up the line)
            if len(line) > 10 and not line.startswith('('):
                spring_2022_projects.append(line)

# Also look for projects that have 2022 in their name (like "2022 Morning View...")
projects_with_2022_in_name = []
for name in funding_map.keys():
    if '2022' in name:
        projects_with_2022_in_name.append(name)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_mentions': len(spring_2022_projects),
    'projects_with_2022_in_name': projects_with_2022_in_name,
    'funding_for_2022_projects': sum(funding_map.get(name, 0) for name in projects_with_2022_in_name)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
