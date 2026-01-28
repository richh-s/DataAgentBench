code = """import json, re

# Load data from file paths stored in the variables
civic_docs_path = var_functions.query_db:60
funding_path = var_functions.query_db:48

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park project names
        if 'Park' in line and len(line) > 5:
            # Skip headers
            if any(skip in line for skip in ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:']):
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            if 'completed' in next_text.lower() and '2022' in next_text:
                park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding matches
total = 0
matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get('Project_Name', '')
        if proj.lower() in name.lower():
            amt = int(rec.get('Amount', 0))
            total += amt
            matches.append([proj, name, amt])

result = {'project_count': len(unique_projects), 'total_funding': total, 'projects': unique_projects, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
