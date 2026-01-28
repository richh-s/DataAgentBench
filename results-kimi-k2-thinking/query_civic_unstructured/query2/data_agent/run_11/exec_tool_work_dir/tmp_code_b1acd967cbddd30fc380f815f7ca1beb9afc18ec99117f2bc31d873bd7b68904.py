code = """import json

# Load civic documents data from the stored path
civic_docs_path = var_functions.query_db:60
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Load funding data from the stored path
funding_path = var_functions.query_db:48
with open(funding_path) as f:
    funding = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if line contains Park and looks like a project name
        if 'Park' in line and len(line) > 10:
            # Skip header lines
            header_terms = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:']
            if any(term in line for term in header_terms):
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for 2022 completion
            next_lines = '\n'.join(lines[i:i+15])
            lower_next = next_lines.lower()
            if 'completed' in lower_next and '2022' in next_lines:
                park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Find funding matches
total_funding = 0
funding_matches = []

for project in unique_projects:
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Match if project name is in funding project name
        if project.lower() in fund_name.lower():
            total_funding += fund_amount
            funding_matches.append([project, fund_name, fund_amount])

# Output final result
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'matches': funding_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
