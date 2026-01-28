code = """import json
import re

# Load the data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[project_name] = amount

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for completion indicators
    if 'completed' in lower_text and '2022' in lower_text and 'park' in lower_text:
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            # Look for park project names
            if 'park' in lower_line and len(line) > 10:
                # Skip metadata lines
                if any(skip in lower_line for skip in ['status:', 'updates:', 'schedule:', 'project description:', 'page']):
                    continue
                if line.startswith('(') or line.startswith('•'):
                    continue
                
                # Check context for completion in 2022
                context_lines = lines[max(0, i-2):min(len(lines), i+5)]
                context = ' '.join(context_lines).lower()
                
                if 'completed' in context and '2022' in context:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(park_projects_2022))

print('__RESULT__:')
print(json.dumps({'projects': unique_projects, 'count': len(unique_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
