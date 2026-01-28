code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding map for quick lookup
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[project_name] = amount

# Extract projects from civic documents
found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we're entering the design section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        # Check if we're leaving the design section
        if in_design_section and 'Capital Improvement Projects' in line and '(Design)' not in line:
            break
            
        # If we're in the design section, look for project names
        if in_design_section and line:
            # Project names typically start with capital letters and contain certain keywords
            keywords = ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park', 'Drainage', 'Bridge', 'Culvert', 'Wall', 'Signs', 'Study']
            
            if line[0].isupper() and any(kw in line for kw in keywords):
                # Check if this project is in our funding map
                if line in funding_map:
                    found_projects.append({
                        'name': line,
                        'funding': funding_map[line]
                    })
                else:
                    # Check for partial matches (project name might be a substring)
                    for funded_name in funding_map:
                        if line in funded_name or funded_name.startswith(line.split(' (')[0]):
                            found_projects.append({
                                'name': funded_name,
                                'funding': funding_map[funded_name]
                            })
                            break

# Remove duplicates
unique_projects = []
seen_names = set()
for p in found_projects:
    if p['name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['name'])

result = len(unique_projects)
print('__RESULT__:')
print(json.dumps({'count': result}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
