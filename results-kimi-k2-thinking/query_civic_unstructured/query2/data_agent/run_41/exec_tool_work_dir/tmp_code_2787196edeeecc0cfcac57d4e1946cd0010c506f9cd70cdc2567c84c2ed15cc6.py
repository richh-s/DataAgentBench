code = """import json

# Load civic documents
civic_docs_path = var_functions.query_db:2
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

print('Number of documents: ' + str(len(civic_docs)))

# Process first document
text = civic_docs[0].get('text', '')
print('First 300 chars: ' + text[:300])

# Initialize results list
park_projects_2022 = []

# Look through all documents for park projects completed in 2022
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip headers
        if any(word in line for word in ['Public Works', 'Commission', 'Agenda', 'Page', 'Item']) or len(line) < 10:
            continue
            
        # Check if line contains project keywords
        line_lower = line.lower()
        if any(word in line_lower for word in ['project', 'improvements', 'repairs', 'replacement', 'structure', 'walkway', 'shade', 'park']):
            
            # Look ahead for completion in 2022
            found_2022_completion = False
            for j in range(i+1, min(i+12, len(lines))):
                next_line = lines[j].strip()
                next_line_lower = next_line.lower()
                
                if '2022' in next_line and 'complete' in next_line_lower:
                    found_2022_completion = True
                    break
                    
            if found_2022_completion:
                # Check context for park keywords
                context_start = max(0, i-5)
                context_end = min(len(lines), i+12)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                park_keywords = ['park', 'playground', 'shade structure', 'walkway', 'bluffs', 'legacy park', 'marie canyon', 'point dume']
                is_park = any(keyword in context for keyword in park_keywords)
                
                if is_park:
                    project_name = line
                    if project_name.startswith('(') and ')' in project_name:
                        project_name = project_name.split(')', 1)[1].strip()
                    
                    if not any(p['name'] == project_name for p in park_projects_2022):
                        park_projects_2022.append({
                            'name': project_name,
                            'year': 2022,
                            'completed': True
                        })

print('Found park projects: ' + str(len(park_projects_2022)))

# Get funding data
funding_path = var_functions.query_db:5
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

print('Funding records: ' + str(len(funding_data)))

# Match projects with funding
matched_projects = []
for park_proj in park_projects_2022:
    proj_name = park_proj['name']
    # Find matching funding records
    for fund in funding_data:
        if fund['Project_Name'] == proj_name or proj_name in fund['Project_Name'] or fund['Project_Name'] in proj_name:
            matched_projects.append({
                'project_name': proj_name,
                'funding_record': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            break

# Calculate total funding
total_funding = sum(p['amount'] for p in matched_projects)

result = json.dumps({
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'park_projects_found': len(park_projects_2022)
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
