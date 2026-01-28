code = """import json
import re

# Load funding data
with open('var_functions.query_db:26', 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Create a dictionary for funding lookup
funding_dict = {}
for fund in funding_records:
    name = fund.get('Project_Name', '')
    funding_dict[name] = {
        'amount': int(fund.get('Amount', 0)),
        'source': fund.get('Funding_Source', '')
    }

# Search for Spring 2022 projects in civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project names followed by Spring 2022 schedule
    # Pattern: Project Name then somewhere mentions Spring 2022 or 2022 with March/April/May
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip common headers
        if any(x in line.lower() for x in ['page', 'agenda item', 'public works commission', 'capital improvement projects']):
            continue
            
        # Look for lines that look like project names (Title Case or mixed case, not bullet points)
        if (not line.startswith(('(', '·', '-', '•')) and 
            not any(phrase in line.lower() for phrase in ['updates:', 'project schedule:', 'complete', 'advertise', 'begin construction', 'estimated schedule']) and
            (line.istitle() or (sum(1 for c in line if c.isupper()) > 3 and not line.isupper()))):
            
            # Check if this project has Spring 2022 mentioned in following lines
            has_spring_2022 = False
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line:
                    # Check if it's a Spring month or Spring reference
                    if any(month in next_line for month in ['March', 'April', 'May', '03', '04', '05']) or 'Spring' in next_line:
                        has_spring_2022 = True
                        break
            
            if has_spring_2022:
                project_name = line.strip()
                
                # Determine project type
                name_lower = project_name.lower()
                if 'fema' in name_lower or 'fire' in name_lower:
                    proj_type = 'disaster'
                else:
                    proj_type = 'capital'
                
                spring_2022_projects.append({
                    'name': project_name,
                    'type': proj_type
                })

# Remove duplicates and get funding
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj

# Match with funding
matched_projects = []
total_funding = 0

for name, proj in unique_projects.items():
    # Check for exact match or partial match
    matched = False
    for fund_name, fund_info in funding_dict.items():
        if fund_name == name or name in fund_name:
            matched_projects.append({
                'name': name,
                'type': proj['type'],
                'funding': fund_info['amount'],
                'source': fund_info['source']
            })
            total_funding += fund_info['amount']
            matched = True
            break
    
    if not matched:
        # Try matching first few words
        name_words = name.split()[:3]
        if len(name_words) >= 2:
            name_prefix = ' '.join(name_words)
            for fund_name, fund_info in funding_dict.items():
                if name_prefix in fund_name:
                    matched_projects.append({
                        'name': name,
                        'type': proj['type'],
                        'funding': fund_info['amount'],
                        'source': fund_info['source'],
                        'matched_fund': fund_name
                    })
                    total_funding += fund_info['amount']
                    break

print('Spring 2022 project count:', len(matched_projects))
print('Total funding:', total_funding)

for proj in matched_projects:
    print('-', proj['name'], ':', proj['funding'])

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
