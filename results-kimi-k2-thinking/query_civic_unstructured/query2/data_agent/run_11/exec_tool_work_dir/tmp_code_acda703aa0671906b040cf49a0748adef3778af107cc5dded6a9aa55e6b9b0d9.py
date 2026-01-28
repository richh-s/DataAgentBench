code = """import json, re

# Load the data from the stored file paths
civic_docs_file = var_functions.query_db:60
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = var_functions.query_db:48
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park-related project names
        if 'Park' in line and len(line) > 5:
            # Skip header lines
            header_keywords = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']
            is_header = any(keyword in line for keyword in header_keywords)
            if is_header or line.startswith('('):
                continue
            
            # Check if completed in 2022 by looking at following lines
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            # Check for completion indicators and 2022
            if ('completed' in next_text.lower() or 'completion' in next_text.lower()) and '2022' in next_text:
                park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding for these projects
total_funding = 0
matches = []

for project in unique_projects:
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Match if project name is contained in funding name
        if project.lower() in fund_name.lower():
            total_funding += fund_amount
            matches.append([project, fund_name, fund_amount])

# Output result
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
