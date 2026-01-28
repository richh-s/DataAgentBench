code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Create funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[record['Project_Name']] = amount

# Look for capital projects with design status
count = 0
seen_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        if in_design_section:
            # Check if we've moved to the next section
            if 'Capital Improvement Projects' in line and 'Design' not in line:
                break
                
            # Look for project names (title case, contains keywords)
            if len(line) > 10 and line[0].isupper():
                has_project_keyword = False
                for keyword in ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park', 'Drainage', 'Bridge']:
                    if keyword in line:
                        has_project_keyword = True
                        break
                        
                if has_project_keyword:
                    # Check if this project has funding > 50k
                    if line in funding_map and line not in seen_projects:
                        count += 1
                        seen_projects.add(line)
                    else:
                        # Check for partial matches
                        for funded_name in funding_map:
                            if funded_name not in seen_projects:
                                if line.startswith(funded_name) or funded_name.startswith(line.split('(')[0].strip()):
                                    count += 1
                                    seen_projects.add(funded_name)
                                    break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
