code = """import json
file_path = file_path_5  # This is the file path from file_path_5
with open(file_path, 'r') as f:
    civic_docs = json.load(f)
print('Number of documents:', len(civic_docs))
print('\nSample document structure:')
print(json.dumps(civic_docs[0].keys(), indent=2))

print('\nSample document content:')
print(json.dumps(civic_docs[0], indent=2)[:2000])

# Let's process to extract project information
def extract_projects_from_text(text):
    # Simple pattern matching to extract project blocks
    import re
    projects = []
    
    # Common patterns for project names
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        # Check for project names (typically capitalized/uppercase lines)
        if len(line) > 10 and line.isupper() and not line.startswith('(') and 'PAGE' not in line:
            if current_project:
                projects.append(current_project)
            current_project = {
                'project_name': line,
                'topic': '',
                'status': '',
                'type': '',
                'st': '',
                'et': '',
                'text': ''
            }
        elif current_project:
            current_project['text'] += line + '\n'
    
    if current_project:
        projects.append(current_project)
    
    # Now parse each project text for details
    for proj in projects:
        text = proj['text']
       # Extract topic based on keywords
        if any(kw in text.lower() for kw in ['park', 'bluffs', 'playground', 'landon center']):
            proj['topic'] = 'park'
        elif any(kw in text.lower() for kw in ['road', 'street', 'bridge', 'highway', 'walkway', 'turn lane']):
            proj['topic'] = 'road'
        elif any(kw in text.lower() for kw in ['drain', 'storm', 'water', 'sewer']):
            proj['topic'] = 'drainage'
        elif any(kw in text.lower() for kw in ['fire', 'fema', 'warning', 'siren']):
           proj['topic'] = 'fire'
        
        # Extract status
        if 'completed' in text.lower() or 'completion' in text.lower():
            # Check if completion was in 2022
            if '2022' in text:
                proj['status'] = 'completed'
                proj['et'] = '2022'
            elif '2023' in text:
                proj['status'] = 'completed' 
                proj['et'] = '2023'
        elif 'design' in text.lower() and 'complete design:' in text.lower():
            proj['status'] = 'design'
        elif 'not started' in text.lower():
            proj['status'] = 'not started'
            
        # Extract type based on keywords
        if 'disaster' in text.lower() or 'fema' in text.lower() or 'recovery' in text.lower() or 'fire' in text.lower():
            proj['type'] = 'disaster'
        elif 'capital' in text.lower() or 'infrastructure' in text.lower() or 'improvement' in text.lower():
           proj['type'] = 'capital'
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print(f'\nTotal projects extracted: {len(all_projects)}')

# Filter park-related projects completed in 2022
park_projects_2022 = []
for proj in all_projects:
    if proj['topic'] == 'park' and proj['status'] == 'completed' and proj.get('et') == '2022':
        park_projects_2022.append(proj)

print(f'\nPark-related projects completed in 2022: {len(park_projects_2022)}')
for p in park_projects_2022:
    print(f"- {p['project_name']}")

# Now load funding data
with open(file_path_funding, 'r') as f:
    funding_data = json.load(f)

print(f'\nTotal funding records: {len(funding_data)}')

# Find funding for park projects completed in 2022
total_funding = 0
funded_projects = []
for proj in park_projects_2022:
    proj_name = proj['project_name']
  # Look for matching funding records
    for fund in funding_data:
        if proj_name in fund['Project_Name'] or fund['Project_Name'] in proj_name:
            total_funding += int(fund['Amount'])
            funded_projects.append({
        'project': proj_name,
                'funding_record': fund['Project_Name'],
                'amount': int(fund['Amount']),
       'funding_source': fund['Funding_Source']
            })

print(f'\nMatching funding records found: {len(funded_projects)}')
print(f'Total funding: ${total_funding:,}')
for fp in funded_projects:
    print(f"- {fp['project']}: ${fp['amount']:,} ({fp['funding_source']})")

# Try to find more park projects by looking at project names
park_keywords = ['park', 'bluffs', 'playground', 'landon center', 'arbors', 'benches', 'walkway']
park_funded_projects = []
for fund in funding_data:
   proj_name = fund['Project_Name'].lower()
    if any(kw in proj_name for kw in park_keywords):
        park_funded_projects.append(fund)

print(f'\nAll park-related funding records: {len(park_funded_projects)}')
for pf in park_funded_projects:
    print(f"- {pf['Project_Name']}: ${int(pf['Amount']):,}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
