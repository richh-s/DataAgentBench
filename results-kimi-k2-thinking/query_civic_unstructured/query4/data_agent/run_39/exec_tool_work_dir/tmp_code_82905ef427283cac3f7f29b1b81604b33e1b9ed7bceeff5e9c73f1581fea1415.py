code = """import json
import re

civic_docs = locals().get('var_functions.query_db:5', [])
funding_data = locals().get('var_functions.query_db:8', [])

# Handle file paths
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Extract project names with Spring 2022 start dates
projects_2022_spring = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and non-project lines
        skip_patterns = ['Page', 'Agenda Item', 'RECOMMENDED', 'To:', 'From:', 
                        'Subject:', 'Public Works', 'Commission Meeting', 'Item ']
        if any(p in line for p in skip_patterns):
            continue
        
        # Check following lines for Spring 2022 dates
        next_text = ' '.join(lines[i+1:min(i+15, len(lines))])
        
        # Look for Spring 2022 indicators
        spring_patterns = ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May',
                          'March 2022', 'April 2022', 'May 2022']
        
        has_spring_2022 = any(pattern in next_text for pattern in spring_patterns)
        
        if has_spring_2022:
            projects_2022_spring.append(line)

# Remove duplicates
unique_projects = list(set(projects_2022_spring))

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Match projects with funding
matched = []
total_funding = 0

for proj_name in unique_projects:
    # Direct match first
    if proj_name in funding_lookup:
        matched.append({'Project_Name': proj_name, 'Amount': funding_lookup[proj_name]})
        total_funding += funding_lookup[proj_name]
        continue
    
    # Check for partial matches with variations
    best_match = None
    best_amount = 0
    
    for fund_name, amount in funding_lookup.items():
        # Simple similarity check
        if (proj_name.lower() in fund_name.lower() or 
            fund_name.lower() in proj_name.lower() or
            abs(len(proj_name) - len(fund_name)) < 10 and 
            any(word in fund_name.lower() for word in proj_name.lower().split()[:3])):
            best_match = fund_name
            best_amount = amount
            break
    
    if best_match:
        matched.append({'Project_Name': proj_name + ' (matched: ' + best_match + ')', 'Amount': best_amount})
        total_funding += best_amount

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched[:15]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}}

exec(code, env_args)
