code = """import json

# Load civic documents
civic_docs_path = var_functions.query_db:2
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

print(f'Number of documents: {len(civic_docs)}')

# Initialize results
park_projects_2022 = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if 'Public Works' in line or 'Commission' in line or 'Agenda' in line or 'Page' in line or 'Item' in line:
            continue
        
        # Check for project keywords
        line_lower = line.lower()
        has_project_keywords = any(word in line_lower for word in ['project', 'improvements', 'repairs', 'replacement', 'structure', 'walkway', 'shade', 'park'])
        
        if has_project_keywords:
            # Look for completion in 2022
            for j in range(i+1, min(i+12, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and 'complete' in next_line.lower():
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
                            park_projects_2022.append({'name': project_name})
                        break

print(f'Park projects found: {len(park_projects_2022)}')

# Load funding data
funding_path = var_functions.query_db:5
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

# Match projects with funding
total_funding = 0
matched_projects = []

for park_proj in park_projects_2022:
    proj_name = park_proj['name']
    for fund in funding_data:
        fund_name = fund['Project_Name']
        # Check for exact match or partial match
        if proj_name == fund_name or proj_name in fund_name or fund_name in proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': proj_name,
                'funding_record': fund_name,
                'amount': amount
            })
            break

result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'park_projects_count': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
