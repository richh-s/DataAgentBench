code = """import json

# Read the full civic_docs result
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Search text for completed park projects in 2022
completed_park_projects = []

for doc in documents:
    text = doc.get('text', '').lower()
    
    # Look for patterns indicating park projects completed in 2022
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Pattern 1: Explicit "completed yyyy" with park nearby
        if 'completed' in line_lower and '2022' in line:
            # Look backward and forward for park project name
            nearby_text = '\n'.join(lines[max(0,i-5):min(len(lines),i+5)])
            if 'park' in nearby_text.lower():
                completed_park_projects.append({
                    'context': nearby_text,
                    'completed_line': line.strip()
                })

# Also check funding records for 2022/park-related projects
park_funding_total = 0
park_projects_names = []

for record in funding_records:
    project_name = record['Project_Name']
    if 'park' in project_name.lower():
        park_projects_names.append(project_name)
        park_funding_total += int(record['Amount'])

result = {
    'completed_count': len(completed_park_projects),
    'park_funding_total_all': park_funding_total,
    'park_projects_found': len(park_projects_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
