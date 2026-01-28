code = """import json

# Load civic documents from the stored file path
civic_docs_var = var_functions.query_db:60
civic_docs = json.load(open(civic_docs_var))

# Load funding data from the stored file path
funding_var = var_functions.query_db:48
funding = json.load(open(funding_var))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park-related project names
        if 'Park' in line and len(line) > 10:
            # Skip headers and metadata
            skip_words = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:']
            if any(word in line for word in skip_words):
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_section = ''
            for j in range(i, min(i+15, len(lines))):
                next_section = next_section + ' ' + lines[j]
            
            # Check if completed in 2022
            next_lower = next_section.lower()
            if 'completed' in next_lower and '2022' in next_section:
                park_projects.append(line)

# Remove duplicates
unique_projects = []
for proj in park_projects:
    if proj not in unique_projects:
        unique_projects.append(proj)

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Check if project name appears in funding project name
        if project_lower in fund_name.lower():
            total_funding = total_funding + fund_amount
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
