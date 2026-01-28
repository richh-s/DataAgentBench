code = """import json, re, os

# Load the filtered Spring 2022 documents
civic_docs_file = var_functions_query_db_36
if isinstance(civic_docs_file, str) and os.path.exists(civic_docs_file):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

# Load all funding data
funding_file = var_functions_query_db_34
if isinstance(funding_file, str) and os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

print('Spring 2022 documents:', len(civic_docs))
print('Total funding records:', len(funding_data))

# Manually extract Spring 2022 projects from the text
projects_found = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for patterns like "Begin Construction: Spring 2022" and extract project name from context
    spring_patterns = [
        (r'([^\n]{30,}?)\s*\n[^\n]{0,200}Begin[^\n]{0,50}Spring[^\n]{0,50}2022', 'construction'),
        (r'([^\n]{30,}?)\s*\n[^\n]{0,200}Begin[^\n]{0,50}(?:March|April|May)[^\n]{0,50}2022', 'construction'),
        (r'([^\n]{30,}?)\s*Project Schedule:[^\n]{0,300}Begin[^\n]{0,50}Spring[^\n]{0,50}2022', 'construction')
    ]
    
    for pattern, ptype in spring_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            project_name = match.group(1).strip()
            # Clean up the project name
            project_name = re.sub(r'^(cid:\d+\s*)+', '', project_name)
            project_name = re.sub(r'^[\-\*\•\d\.\s]+', '', project_name)
            project_name = project_name.replace('\n', ' ').strip()
            
            if project_name and len(project_name) > 15 and len(project_name) < 200:
                # Filter out obvious non-project lines
                if not any(skip in project_name.lower() for skip in ['page ', 'agenda item', 'subject:', 'discussion:']):
                    projects_found.append({
                        'name': project_name,
                        'filename': filename
                    })

# Remove duplicates by keeping the shortest version of similar names
unique_projects = {}
for proj in projects_found:
    name = proj['name']
    # Normalize the name for comparison
    key = name.lower().replace('project', '').replace('improvements', '').replace('repairs', '').strip()
    if key not in unique_projects or len(name) < len(unique_projects[key]['name']):
        unique_projects[key] = proj

final_projects = list(unique_projects.values())
print('Final unique Spring 2022 start projects:', len(final_projects))

for i, proj in enumerate(final_projects[:10], 1):
    print(f"{i}. {proj['name']}")

# Match with funding data
total_funding = 0
successful_matches = []

for project in final_projects:
    proj_name = project['name']
    proj_lower = proj_name.lower()
    
    # Try to find matching funding records
    best_matches = []
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        fund_amount = int(fund['Amount'])
        
        # Direct substring match
        if proj_lower in fund_name or fund_name in proj_lower:
            best_matches.append((fund, 1.0))
        else:
            # Word overlap score
            proj_words = set(w for w in proj_lower.split() if len(w) > 4)
            fund_words = set(w for w in fund_name.split() if len(w) > 4)
            
            if proj_words and fund_words:
                overlap = len(proj_words.intersection(fund_words))
                if overlap >= 2:  # At least 2 matching words
                    best_matches.append((fund, overlap / len(proj_words)))
    
    # Take the best match if any
    if best_matches:
        best_matches.sort(key=lambda x: x[1], reverse=True)
        best_fund = best_matches[0][0]
        total_funding += int(best_fund['Amount'])
        successful_matches.append({
            'project': proj_name,
            'funding': best_fund['Project_Name'],
            'amount': int(best_fund['Amount'])
        })

print(f'\nTotal funding for Spring 2022 projects: ${total_funding:,}')
print(f'Matched {len(successful_matches)} projects with funding')

print('__RESULT__:')
print(json.dumps({
    'number_of_projects': len(final_projects),
    'total_funding_dollars': total_funding,
    'matched_projects': len(successful_matches),
    'sample_projects': [p['name'] for p in final_projects[:5]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
