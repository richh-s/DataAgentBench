code = """import json

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Find completed park projects from 2022
completed_projects = []

for doc in documents:
    text = doc.get('text', '')
    
    # Look for patterns
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        # Extract lines with park projects
        lines = text.split('\n')
        for line_num in range(len(lines)):
            line = lines[line_num].strip()
            
            # Look for park project names (reasonable length, not headers)
            if 'park' in line.lower() and len(line) < 150:
                skip = False
                skip_terms = ['capital improvement', 'disaster recovery', 'status report', 'discussion:', 'recommended action:', 'projects', 'agenda'] 
                for term in skip_terms:
                    if term in line.lower():
                        skip = True

                if line.startswith('(') or line.startswith('cid:'):
                    skip = True
                
                if not skip:
                    # Check if completed in 2022
                    for look_line in lines[line_num:line_num+10]:
                        look_line_lower = look_line.lower()
                        if 'completed' in look_line_lower and '2022' in look_line:
                            completed_projects.append(line)
                            break

# Get funding for all park projects
total_funding = 0
for record in funding_records:
    if 'park' in record['Project_Name'].lower():
        total_funding += int(record['Amount'])

result = {
    'completed_park_projects_2022': len(completed_projects),
    'total_park_funding_all': total_funding,
    'completed_projects': completed_projects[:5]  # First 5
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
