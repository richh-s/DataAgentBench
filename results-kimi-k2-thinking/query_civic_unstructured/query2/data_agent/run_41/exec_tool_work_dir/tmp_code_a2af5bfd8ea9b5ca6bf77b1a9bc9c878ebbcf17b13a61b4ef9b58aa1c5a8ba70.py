code = """import json

# Load civic documents data
civic_docs_path = var_functions.query_db:2
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

print(f'Number of documents: {len(civic_docs)}')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        skip_terms = ['Public Works', 'Commission', 'Agenda', 'Page', 'Item']
        if any(term in line for term in skip_terms):
            continue
        
        # Check for project keywords
        line_lower = line.lower()
        project_terms = ['project', 'improvements', 'repairs', 'replacement', 'structure', 'walkway', 'shade', 'park']
        if any(term in line_lower for term in project_terms):
            
            # Look ahead for completion in 2022
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and 'complete' in next_line.lower():
                    
                    # Check if park-related
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+10)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    
                    park_keywords = ['park', 'playground', 'shade structure', 'walkway', 'bluffs park', 'legacy park', 'marie canyon', 'point dume']
                    if any(keyword in context for keyword in park_keywords):
                        
                        project_name = line
                        if project_name.startswith('(') and ')' in project_name:
                            parts = project_name.split(')', 1)
                            if len(parts) > 1:
                                project_name = parts[1].strip()
                        
                        if not any(p['name'] == project_name for p in park_projects):
                            park_projects.append({'name': project_name, 'status': 'completed', 'year': 2022})
                        break

print(f'Found {len(park_projects)} park projects completed in 2022')

# Load funding data and calculate total
funding_path = var_functions.query_db:5
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

total_funding = 0
project_matches = []

for park_project in park_projects:
    proj_name = park_project['name']
    for fund in funding_data:
        fund_name = fund['Project_Name']
        # Check for match
        if proj_name == fund_name or proj_name in fund_name or fund_name in proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            project_matches.append({
                'project': proj_name,
                'funding_record': fund_name,
                'amount': amount
            })
            print(f'Matched: {proj_name} -> {fund_name}: ${amount}')
            break

result = json.dumps({
    'total_funding': total_funding,
    'matched_projects': project_matches,
    'park_projects_identified': len(park_projects)
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
