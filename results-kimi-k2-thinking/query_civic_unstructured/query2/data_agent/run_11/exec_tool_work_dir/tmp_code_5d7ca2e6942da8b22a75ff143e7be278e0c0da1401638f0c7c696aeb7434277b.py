code = """import json, re

# Load data from the stored file paths
civic_docs = json.load(open('/tmp/tmpu9m4oj6r.json'))
funding = json.load(open('/tmp/tmpg3x0v1j7.json'))

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding), 'funding records')

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        cleaned_line = lines[i].strip()
        
        # Look for project names containing Park
        if 'Park' in cleaned_line and len(cleaned_line) > 5:
            # Skip headers and metadata
            skip_terms = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']
            is_header = any(term in cleaned_line for term in skip_terms)
            
            if not is_header and not cleaned_line.startswith('(') and not cleaned_line.startswith('cid'):
                # Look ahead for completion status and date
                next_text = ''
                for j in range(i, min(i+15, len(lines))):
                    next_text = next_text + ' ' + lines[j]
                
                next_text_lower = next_text.lower()
                # Check if completed in 2022
                if ('completed' in next_text_lower or 'completion' in next_text_lower) and '2022' in next_text:
                    park_projects_2022.append(cleaned_line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

print('Found', len(unique_projects), 'park projects completed in 2022')
print('Projects:', unique_projects)

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Check if project matches funding record
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append({'project': project, 'funding_name': fund_name, 'amount': fund_amount})

print('Total funding found:', total_funding)
print('Matches:', len(matches))

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json'}

exec(code, env_args)
