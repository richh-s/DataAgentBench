code = """import json
import re

# Read civic documents
civic_file = locals()['var_functions.query_db:26']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_file = locals()['var_functions.query_db:24']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Civic documents count:', len(civic_docs))
print('Funding records count:', len(funding_data))

# Create funding map by project name (lowercase for matching)
funding_map = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower().strip()
    amount = int(item['Amount'])
    funding_map[proj_name] = amount

# Extract projects with Spring 2022 start dates
spring_projects = []
spring_patterns = [
    r'(?i)begin[^\n]*spring[^\n]*2022',
    r'(?i)begin[^\n]*spring/summer[^\n]*2022',
    r'(?i)begin[^\n]*march[^\n]*2022',
    r'(?i)begin[^\n]*april[^\n]*2022',
    r'(?i)begin[^\n]*may[^\n]*2022'
]

for doc in civic_docs:
    text = doc.get('text', '')
    # Split by project sections (look for capitalized headers)
    sections = re.split(r'\n\n[A-Z][A-Za-z\s&/-]{5,}\n', text)
    
    for section in sections:
        if len(section.strip()) < 50:
            continue
            
        # Check for Spring 2022 start date
        found_spring = any(re.search(pattern, section) for pattern in spring_patterns)
        
        if found_spring:
            # Extract project name (first line)
            lines = section.strip().split('\n')
            proj_name = 'Unknown'
            for line in lines[:3]:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith('(') and not 'cid:' in clean_line:
                    proj_name = clean_line
                    break
            
            if proj_name != 'Unknown' and len(proj_name) < 100:
                spring_projects.append({
                    'name': proj_name,
                    'name_lower': proj_name.lower()
                })

print('Spring 2022 projects found:', len(spring_projects))

# Match with funding data
matched = []
total_funding = 0

for proj in spring_projects:
    # Direct match
    if proj['name_lower'] in funding_map:
        amount = funding_map[proj['name_lower']]
        matched.append({
            'name': proj['name'],
            'funding': amount
        })
        total_funding += amount
    else:
        # Fuzzy/substring matching
        for fund_name, amount in funding_map.items():
            if (proj['name_lower'] in fund_name or 
                fund_name in proj['name_lower'] or
                proj['name_lower'].replace(' ', '') == fund_name.replace(' ', '')):
                matched.append({
                    'name': proj['name'],
                    'funding': amount
                })
                total_funding += amount
                break

print('Matched with funding:', len(matched))
print('Total funding amount:', total_funding)

# Show matches
if matched:
    print('\nProjects and funding:')
    for item in matched:
        print(f"- {item['name']}: ${item['funding']:,}")

print('\n__RESULT__:')
print(json.dumps({
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
