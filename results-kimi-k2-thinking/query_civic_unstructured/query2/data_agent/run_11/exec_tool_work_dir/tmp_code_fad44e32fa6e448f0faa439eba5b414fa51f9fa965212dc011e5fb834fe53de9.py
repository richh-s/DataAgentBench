code = """import json
import re

# Access the stored data from previous query results
civic_docs_var = var_functions.query_db:60
funding_var = var_functions.query_db:48

# Load civic documents data
if isinstance(civic_docs_var, str):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

# Load funding data  
if isinstance(funding_var, str):
    with open(funding_var, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_var

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park-related project names
        if 'Park' in line and len(line) > 5:
            # Skip header metadata
            header_words = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission']
            if any(word in line for word in header_words) or line.startswith('('):
                continue
            
            # Look ahead for completion status and 2022 date
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            # Check if completed in 2022
            if ('completed' in next_text.lower() or 'completion' in next_text.lower()) and '2022' in next_text:
                # Avoid future scheduled completions
                if 'to be completed' not in next_text.lower():
                    park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Match if project name appears in funding record name
        if project.lower() in fund_name.lower():
            total_funding += fund_amount
            matches.append([project, fund_name, fund_amount])

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
