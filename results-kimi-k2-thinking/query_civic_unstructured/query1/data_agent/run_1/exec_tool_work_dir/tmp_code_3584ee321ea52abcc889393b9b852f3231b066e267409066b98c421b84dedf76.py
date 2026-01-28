code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[record['Project_Name']] = amount

# Look for capital projects with design status
found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        if in_design_section and 'Capital Improvement Projects' in line and 'Design' not in line:
            break
            
        if in_design_section and len(line) > 5 and line[0].isupper():
            # Check for project keywords
            has_keyword = False
            keywords = ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park', 'Drainage', 'Bridge']
            for kw in keywords:
                if kw in line:
                    has_keyword = True
                    break
            
            if has_keyword and line in funding_map:
                found_projects.append(line)

# Remove duplicates
unique_projects = list(set(found_projects))

print('__RESULT__:')
print(json.dumps({'count': len(unique_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
