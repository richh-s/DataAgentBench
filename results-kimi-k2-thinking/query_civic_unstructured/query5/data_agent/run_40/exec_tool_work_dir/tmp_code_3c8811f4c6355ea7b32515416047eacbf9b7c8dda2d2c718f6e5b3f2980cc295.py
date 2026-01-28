code = """import json

# Load the data
civic_docs_path = var_functions.query_db_58
funding_path = var_functions.query_db_59

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup by project name
funding_lookup = {}
for rec in funding_records:
    project_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_lookup[project_name] = amount

# Find disaster projects that started in 2022
total_funding = 0
projects_found = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this is a disaster project
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
            # Look for 2022 start date in nearby lines
            found_2022 = False
            start_line = max(0, i-2)
            end_line = min(len(lines), i+6)
            for j in range(start_line, end_line):
                context_line = lines[j]
                if '2022' in context_line and ('st:' in context_line.lower() or 'start:' in context_line.lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    projects_found.append({'name': project_name, 'funding': amount})

# Return result
result = {'total_funding': total_funding, 'project_count': len(projects_found)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json'}

exec(code, env_args)
