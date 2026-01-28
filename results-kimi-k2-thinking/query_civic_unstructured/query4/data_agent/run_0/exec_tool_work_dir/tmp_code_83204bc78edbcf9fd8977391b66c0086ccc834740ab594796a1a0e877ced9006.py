code = """import json
import re

# Read civic documents
civic_file = locals()['var_functions.query_db:22']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_file = locals()['var_functions.query_db:24']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Civic documents:', len(civic_docs))
print('Funding records:', len(funding_data))

# Create a mapping of project names to funding amounts
funding_map = {item['Project_Name'].lower().strip(): int(item['Amount']) for item in funding_data}

# Extract projects with Spring 2022 start dates from civic documents
spring_2022_projects = []
spring_patterns = [
    r'(?i)Begin[^:]*:\s*Spring\s+2022',
    r'(?i)Begin[^:]*:\s*Spring/Summer\s+2022',
    r'(?i)Begin[^:]*:\s*March\s+2022',
    r'(?i)Begin[^:]*:\s*April\s+2022',
    r'(?i)Begin[^:]*:\s*May\s+2022'
]

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project sections
    projects = re.split(r'\n\n[A-Z][^\n]*\n', text)
    
    for proj_text in projects:
        if len(proj_text.strip()) < 50:  # Skip too short sections
            continue
            
        # Check if this project has a Spring 2022 start date
        has_spring_date = any(re.search(pattern, proj_text) for pattern in spring_patterns)
        
        if has_spring_date:
            # Extract project name (first line or section header)
            lines = proj_text.strip().split('\n')
            project_name = 'Unknown'
            for line in lines[:5]:  # Look in first few lines
                if line.strip() and not line.strip().startswith('(') and not line.strip().startswith('cid:'):
                    project_name = line.strip()
                    break
            
            if project_name != 'Unknown' and len(project_name) < 100:
                spring_2022_projects.append({
                    'project_name': project_name,
                    'project_name_lower': project_name.lower(),
                    'source': doc.get('filename', '')
                })

print('Found Spring 2022 projects:', len(spring_2022_projects))
for proj in spring_2022_projects[:10]:
    print(' -', proj['project_name'])

# Match with funding and calculate totals
matched_projects = []
total_funding = 0

for proj in spring_2022_projects:
    # Direct match
    if proj['project_name_lower'] in funding_map:
        amount = funding_map[proj['project_name_lower']]
        matched_projects.append({
            'project_name': proj['project_name'],
            'funding': amount,
            'source': proj['source']
        })
        total_funding += amount
    else:
        # Try substring matching
        for fund_name, amount in funding_map.items():
            if (proj['project_name_lower'] in fund_name or 
                fund_name in proj['project_name_lower'] or
                proj['project_name_lower'].replace(' ', '') in fund_name.replace(' ', '') or
                fund_name.replace(' ', '') in proj['project_name_lower'].replace(' ', '')):
                matched_projects.append({
                    'project_name': proj['project_name'],
                    'funding': amount,
                    'source': proj['source']
                })
                total_funding += amount
                break

print('\nMatched projects:', len(matched_projects))
print('Total funding:', total_funding)

# Show detailed matches
for proj in matched_projects:
    print(f"- {proj['project_name']}: ${proj['funding']:,}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
