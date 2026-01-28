code = """import json, re

# Get the file paths from the variables
civic_file = var_functions.query_db:60
funding_file = var_functions.query_db:48

# Load the data
with open(civic_file) as f:
    civic_docs = json.load(f)
with open(funding_file) as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check for park projects completed in 2022
    if 'Park' in text and '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) > 10:
                # Skip headers
                if 'Subject' in line or 'Page' in line or 'Item' in line or line.startswith('('):
                    continue
                # Look for nearby completion status
                line_index = lines.index(line)
                context = '\n'.join(lines[max(0, line_index-2):line_index+10])
                if 'completed' in context.lower() and '2022' in context:
                    park_projects_2022.append(line)

unique_projects = list(set(park_projects_2022))

# Find funding matches
total_funding = 0
matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get('Project_Name', '')
        if proj.lower() in name.lower():
            amount = int(rec.get('Amount', 0))
            total_funding += amount
            matches.append([proj, name, amount])

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'matches': matches
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
