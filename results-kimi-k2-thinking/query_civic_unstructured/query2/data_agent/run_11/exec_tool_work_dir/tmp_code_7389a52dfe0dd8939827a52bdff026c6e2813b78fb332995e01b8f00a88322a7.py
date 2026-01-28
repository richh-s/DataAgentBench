code = """import json

# Load civic documents from stored path
civic_docs = json.load(open('/tmp/tmph_70y1n9.json'))

# Look for park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for park project names
        if 'Park' in line and len(line) > 10:
            # Skip headers
            if 'Subject' in line or 'Page' in line or 'Item' in line:
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_section = '\n'.join(lines[i:i+15])
            if 'completed' in next_section.lower() and '2022' in next_section:
                park_projects.append(line)

# Remove duplicates
unique_parks = list(set(park_projects))

print('Found park projects completed in 2022:', unique_parks)
print('Count:', len(unique_parks))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
