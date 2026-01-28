code = """import json, os, re, sys

# Get the data files
files = os.listdir('.')
funding_files = [f for f in files if 'query_db' in f and 'Project_Name' in str(f)]
civic_files = [f for f in files if 'query_db' in f and 'text' in str(f)]

print('Found {} funding files and {} civic files'.format(len(funding_files), len(civic_files)))

# Load funding data
if funding_files:
    with open(funding_files[0], 'r') as f:
        funding_data = json.load(f)
else:
    print('No funding file found')
    sys.exit()

# Load civic documents
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

# Search for Spring 2022 patterns
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022 March', '2022 April', '2022 May', 'Spring 2022', 'March 2022', 'April 2022', 'May 2022']
spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if document mentions Spring 2022
    has_spring = False
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            has_spring = True
            break
    
    if has_spring:
        # Look for project names in this document
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or len(line) < 10:
                continue
            if line.startswith('Page') or 'Agenda Item' in line:
                continue
            
            # Check if line looks like a project name (title case or proper case, reasonably long)
            is_project_name = False
            if line.istitle() and len(line.split()) >= 2:
                is_project_name = True
            elif line[0].isupper() and len(line.split()) >= 3 and len(line) > 15:
                # Additional check: not a regular sentence
                if not line.endswith('.') or len(line.split()) < 8:
                    is_project_name = True
            
            if is_project_name:
                # Look at surrounding context for Spring 2022 dates
                context_start = max(0, i-2)
                context_end = min(len(lines), i+6)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                for pattern in spring_patterns:
                    if pattern.lower() in context:
                        existing_names = [p['name'] for p in spring_projects]
                        if line not in existing_names:
                            spring_projects.append({'name': line})
                        break

print('Found {} potential Spring 2022 projects'.format(len(spring_projects)))

# Also find projects with 2022 in their name (indicating they started in 2022)
for project_name in funding_dict.keys():
    if '2022' in project_name and '2022 Annual' not in project_name:
        # This might be a 2022 project not found in civic docs
        existing_names = [p['name'] for p in spring_projects]
        if project_name not in existing_names:
            spring_projects.append({'name': project_name})

print('Total Spring 2022 projects after adding 2022-named projects: {}'.format(len(spring_projects)))

# Match projects with funding
def match_projects(projects, funding_dict):
    matched = []
    total = 0
    for proj in projects:
        project_name = proj['name']
        
        # Exact match
        if project_name in funding_dict:
            amount = funding_dict[project_name]
            matched.append({'project': project_name, 'funding': amount, 'match': 'exact'})
            total += amount
        else:
            # Partial/fuzzy match
            for funded_name, amount in funding_dict.items():
                proj_lower = project_name.lower()
                funded_lower = funded_name.lower()
                
                # Check if one is contained in the other (avoid very short matches)
                if (proj_lower in funded_lower or funded_lower in proj_lower) and len(proj_lower) > 10 and len(funded_lower) > 10:
                    matched.append({'project': project_name, 'funding': amount, 'match': 'partial', 'matched_with': funded_name})
                    total += amount
                    break
    
    return matched, total

matched_projects, total_funding = match_projects(spring_projects, funding_dict)

print('Matched {} projects with funding data'.format(len(matched_projects)))

# Create final result
project_count = len(matched_projects)
funding_formatted = '{:,}'.format(total_funding)

result = 'Projects started in Spring 2022: ' + str(project_count) + '. Total funding: $' + funding_formatted

print('\n__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.list_db:89': ['civic_docs'], 'var_functions.list_db:90': ['Funding'], 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:93': 'file_storage/functions.query_db:93.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:105': 'file_storage/functions.query_db:105.json'}

exec(code, env_args)
