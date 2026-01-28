code = """import json
import os

# Load funding data from the file path variable
with open(var_functions.query_db:2, 'r') as f:
    funding_data = json.load(f)

print('Total funding records:', len(funding_data))

# Load civic documents from the file path variable
with open(var_functions.query_db:4, 'r') as f:
    civic_docs = json.load(f)

print('Total civic documents:', len(civic_docs))

# Function to extract project information from document text
def extract_projects_from_text(text, doc_date=None):
    import re
    projects = []
    
    # Look for project patterns - project names are typically uppercase or title case
    # Common project patterns in the text
    project_markers = [
        r'^[A-Z][A-Z\s&\-]+(?:Project|Improvements|Repairs|Replacement|Construction)\b',
        r'^[A-Z][A-Z\s]+(?:Drainage|Road|Park|Center|Water|Treatment)\b.*$',
    ]
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Check if this line looks like a project name
        is_project_name = False
        if line.isupper() and len(line) < 150:
            # Skip common headers
            if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF', 'MALIBU']):
                continue
            is_project_name = True
        elif re.match(r'^[A-Z].*(?:Project|Improvements|Repairs)$', line):
            is_project_name = True
            
        if is_project_name:
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
    
    # Parse details from project text
    for proj in projects:
        text = proj['text'].lower()
        # Determine topic
        if any(kw in text for kw in ['park', 'playground', 'bluffs', 'landon center', 'arbors', 'benches']):
            proj['topic'] = 'park'
        elif any(kw in text for kw in ['road', 'street', 'bridge', 'highway', 'walkway', 'turn lane', 'drive']):
            proj['topic'] = 'road'
        elif any(kw in text for kw in ['drain', 'storm', 'water', 'sewer', 'flood']):
            proj['topic'] = 'drainage'
        elif any(kw in text for kw in ['fire', 'fema', 'warning', 'siren', 'emergency']):
            proj['topic'] = 'fire'
        
        # Determine status and completion year
        if 'completed' in text or 'construction was completed' in text or 'notice of completion' in text:
            if '2022' in proj['text']:
                proj['status'] = 'completed'
                proj['et'] = '2022'
            elif '2023' in proj['text']:
                proj['status'] = 'completed'
                proj['et'] = '2023'
        
        if 'complete design:' in text:
            if '2022' in proj['text']:
                proj['status'] = 'design'
                proj['st'] = '2022'
        
        # Determine type
        if any(kw in text for kw in ['fema', 'disaster', 'recovery', 'fire', 'emergency']):
            proj['type'] = 'disaster'
        elif any(kw in text for kw in ['capital', 'infrastructure', 'improvement', 'maintenance']):
            proj['type'] = 'capital'
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print(f'\nTotal projects extracted: {len(all_projects)}')

# Find park projects completed in 2022
park_projects_2022 = []
for proj in all_projects:
    if proj['topic'] == 'park' and proj['status'] == 'completed' and proj.get('et') == '2022':
        park_projects_2022.append(proj)

print(f'Park projects completed in 2022: {len(park_projects_2022)}')
for p in park_projects_2022[:5]:  # Show first 5
    print(f"- {p['project_name']}")

# Match with funding data
total_funding = 0
matched_funding = []

# Create a dictionary for easier lookup by project name
funding_by_project = {}
for fund in funding_data:
    name = fund['Project_Name'].lower()
    funding_by_project[name] = fund

# Try to match park projects with funding
for proj in park_projects_2022:
    proj_name = proj['project_name'].lower()
    
    # Direct match
    if proj_name in funding_by_project:
        fund = funding_by_project[proj_name]
        amount = int(fund['Amount'])
        total_funding += amount
        matched_funding.append({
            'project': proj['project_name'],
            'funding_project': fund['Project_Name'],
            'amount': amount,
            'source': fund['Funding_Source']
        })
        continue
    
    # Fuzzy match - check if any funded project name contains this project name
    for fund_name, fund in funding_by_project.items():
        if proj_name in fund_name or fund_name in proj_name:
            amount = int(fund['Amount'])
      total_funding += amount
            matched_funding.append({
      'project': proj['project_name'],
                'funding_project': fund['Project_Name'],
         'amount': amount,
                'source': fund['Funding_Source']
            })
            break

print(f'\nMatched {len(matched_funding)} park projects completed in 2022')
print(f'Total funding: ${total_funding:,}')

for mf in matched_funding:
    print(f"- {mf['project']}: ${mf['amount']:,} ({mf['source']})")

# Also check for park-related projects in funding data that might be completed in 2022
park_keywords = ['park', 'bluffs', 'playground', 'landon', 'arbors', 'benches', 'walkway']
additional_park_funding = []

for fund in funding_data:
    proj_name = fund['Project_Name'].lower()
    if any(kw in proj_name for kw in park_keywords):
        amount = int(fund['Amount'])
   additional_park_funding.append({
       'project': fund['Project_Name'],
  'amount': amount,
        'source': fund['Funding_Source']
    })

print(f'\nAll park-related funding records: {len(additional_park_funding)}')
additional_total = sum(pf['amount'] for pf in additional_park_funding)
print(f'Total of all park funding: ${additional_total:,}')

__RESULT__:
json.dumps({
    'direct_matches': matched_funding,
    'total_direct_funding': total_funding,
    'all_park_funding_count': len(additional_park_funding),
    'total_all_park_funding': additional_total
})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
