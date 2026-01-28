code = """import json
import re

civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_lookup[project_name] = amount

# Initialize results
total_funding = 0
found_projects = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Iterate through lines to find disaster projects
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for disaster project indicators in project names
        is_disaster = False
        if '(FEMA Project)' in line:
            is_disaster = True
        elif '(CalJPIA Project)' in line:
            is_disaster = True
        elif '(CalOES Project)' in line:
            is_disaster = True
        elif 'FEMA/CalOES Project' in line:
            is_disaster = True
        
        if is_disaster:
            project_name = line
            
            # Look for start date in next few lines
            project_start = ''
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if 'st:' in next_line.lower() or 'start:' in next_line.lower():
                    project_start = next_line
                    break
            
            # Check if project started in 2022
            if '2022' in project_start:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    found_projects.append({
                        'name': project_name,
                        'amount': amount,
                        'start': project_start
                    })

print('Found', len(found_projects), 'disaster projects that started in 2022')
print('Total funding:', total_funding)

# Print found projects
for p in found_projects:
    print(p['name'], ':', p['amount'])

# Return result
result = {
    'total_funding': total_funding,
    'project_count': len(found_projects),
    'projects': found_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
