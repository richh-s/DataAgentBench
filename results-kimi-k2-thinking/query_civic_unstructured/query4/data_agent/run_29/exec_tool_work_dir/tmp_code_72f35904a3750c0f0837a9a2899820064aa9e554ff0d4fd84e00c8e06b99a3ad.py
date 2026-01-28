code = """import json, os, re, sys

# List files to find our data
files = os.listdir('.')
print('Files in directory:', files[:10])

# Find the data files
funding_file = None
civic_file = None

for f in files:
    if 'query_db' in f:
        if any(num in f for num in ['14', '28', '44', '46']):
            funding_file = f
        else:
            civic_file = f

print('Funding file:', funding_file)
print('Civic file:', civic_file)

# Load the data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records count:', len(funding_data))
print('Civic documents count:', len(civic_data))

# Create funding lookup dictionary by project name
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name'].strip()
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

print('Funding dictionary entries:', len(funding_dict))
print('Sample project names:', list(funding_dict.keys())[:5])

# Define Spring 2022 date patterns to search for
spring_patterns = [
    '2022-Spring', '2022 March', '2022 April', '2022 May',
    'Spring 2022', 'March 2022', 'April 2022', 'May 2022',
    '2022-March', '2022-April', '2022-May'
]

# Search for Spring 2022 projects
spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    # Check if text contains any Spring 2022 indicators
    text_lower = text.lower()
    
    has_spring_2022 = False
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            has_spring_2022 = True
            break
    
    if has_spring_2022:
        # Parse line by line to find project names
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Skip empty lines and common headers/footers
            if not line or len(line) < 10:
                continue
            if line.startswith('Page') or line.startswith('---'):
                continue
            if 'Agenda Item' in line or 'Public Works Commission' in line:
                continue
                
            # Check if line looks like a project name (title case or long proper case)
            is_project_like = False
            if line.istitle() and len(line.split()) >= 3:
                is_project_like = True
            elif line[0].isupper() and len(line.split()) >= 4 and not line.isupper():
                # Check it doesn't look like a regular sentence
                if not line.endswith('.') or len(line.split()) < 8:
                    is_project_like = True
            
            if is_project_like:
                # Look ahead for Spring 2022 date patterns
                context = ' '.join(lines[i:i+10])
                context_lower = context.lower()
                
                for pattern in spring_patterns:
                    if pattern.lower() in context_lower:
                        # Found a project likely starting in Spring 2022
                        project_name = line
                        if project_name not in [p['name'] for p in spring_projects]:
                            spring_projects.append({
                                'name': project_name,
                                'context_preview': context[:150] + '...'
                            })
                        break

print('Spring 2022 projects found:', len(spring_projects))
for i, proj in enumerate(spring_projects[:10], 1):
    print(f'{i}. {proj["name"][:60]}')
    
# Match with funding data
matched_projects = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    
    # Direct exact match
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched_projects.append({
            'project_name': project_name,
            'funding_amount': amount,
            'match_type': 'exact'
        })
        total_funding += amount
        print(f'Direct match: {project_name} -> ${amount}')
    else:
        # Try partial matching - check if project name is contained in funded name or vice versa
        best_match = None
        best_amount = 0
        
        for funded_name, amount in funding_dict.items():
            proj_lower = project_name.lower()
            funded_lower = funded_name.lower()
            
            # Check for containment
            if proj_lower in funded_lower or funded_lower in proj_lower:
                # Ensure it's not too generic
                if len(proj_lower) > 10 and len(funded_lower) > 10:
                    best_match = funded_name
                    best_amount = amount
                    break
        
        if best_match:
            matched_projects.append({
                'project_name': project_name,
                'funding_amount': best_amount,
                'match_type': 'partial',
                'matched_with': best_match
            })
            total_funding += best_amount
            print(f'Partial match: {project_name} -> {best_match} = ${best_amount}')

# Prepare results
result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:20]  # Limit to avoid too much output
}

print('\\n=== FINAL RESULT ===')
print('Projects in Spring 2022 with funding:', len(matched_projects))
print('Total funding:', total_funding)

print('\\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
