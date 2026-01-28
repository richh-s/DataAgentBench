code = """import json, os, re, sys

# Get data files from storage
files = os.listdir('.')
funding_files = [f for f in files if 'query_db' in f and any(str(n) in f for n in [14, 28, 44, 46])]
civic_files = [f for f in files if 'query_db' in f and f not in funding_files]

if funding_files:
    with open(funding_files[0], 'r') as f:
        funding_data = json.load(f)
else:
    print('No funding file found')
    sys.exit()

if civic_files:
    with open(civic_files[0], 'r') as f:
        civic_data = json.load(f)
else:
    print('No civic file found')
    sys.exit()

print('Loaded {} funding records and {} civic documents'.format(len(funding_data), len(civic_data)))

# Build funding lookup dictionary
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

print('Funding dictionary contains {} projects'.format(len(funding_dict)))

# Search for Spring 2022 projects
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022 March', '2022 April', '2022 May', 'Spring 2022', 'March 2022', 'April 2022', 'May 2022']
spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if doc mentions Spring 2022
    has_spring = False
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            has_spring = True
            break
    
    if has_spring:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            if line.startswith('Page') or 'Agenda Item' in line:
                continue
                
            # Check if line looks like a project name
            if line.istitle() or (line[0].isupper() and len(line.split()) >= 3):
                # Look for spring date in surrounding context
                context_start = max(0, i-2)
                context_end = min(len(lines), i+5)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                for pattern in spring_patterns:
                    if pattern.lower() in context:
                        existing = [p['name'] for p in spring_projects]
                        if line not in existing:
                            spring_projects.append({'name': line})
                        break

print('Found {} potential Spring 2022 projects'.format(len(spring_projects)))

# Match with funding
matched = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    
    # Exact match
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched.append([project_name, amount, 'exact'])
        total_funding += amount
    else:
        # Partial match
        for funded_name, amount in funding_dict.items():
            proj_lower = project_name.lower()
            funded_lower = funded_name.lower()
            
            if proj_lower in funded_lower or funded_lower in proj_lower:
                if len(proj_lower) > 10 and len(funded_lower) > 10:
                    matched.append([project_name, amount, 'partial', funded_name])
                    total_funding += amount
                    break

print('Matched {} projects with funding data'.format(len(matched)))

# Format result
project_count = len(matched)
funding_formatted = '{:,}'.format(total_funding)

print('\n__RESULT__:')
print('Projects started in Spring 2022: ' + str(project_count) + '. Total funding: $' + funding_formatted)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.list_db:89': ['civic_docs'], 'var_functions.list_db:90': ['Funding'], 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:93': 'file_storage/functions.query_db:93.json'}

exec(code, env_args)
