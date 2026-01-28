code = """import json
import re

# Load civic documents from the stored path
civic_docs_path = var_functions.query_db:126
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names containing Park
        if 'Park' in line and len(line) > 5:
            # Skip headers/metadata
            skip_patterns = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']
            is_header = any(pattern in line for pattern in skip_patterns)
            
            if not is_header and not line.startswith('(') and not line.startswith('cid'):
                # Look ahead for status and dates
                next_context = '\n'.join(lines[i:i+15])
                lower_context = next_context.lower()
                
                # Check if completed in 2022
                if ('completed' in lower_context or 'completion' in lower_context) and '2022' in next_context:
                    # Make sure it's not scheduled for future
                    if 'will be completed' not in lower_context and 'to be completed' not in lower_context:
                        park_projects_2022.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))

print('Found park projects completed in 2022:', unique_park_projects)
print('Count:', len(unique_park_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:126': 'file_storage/functions.query_db:126.json'}

exec(code, env_args)
