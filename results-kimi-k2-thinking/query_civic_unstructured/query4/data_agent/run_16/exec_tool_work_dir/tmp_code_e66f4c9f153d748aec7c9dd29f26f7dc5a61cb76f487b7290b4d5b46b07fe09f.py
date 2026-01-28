code = """import json

# Load civic documents from the file
civic_docs = json.load(open('/tmp/tmp7q6r1zwh.json', 'r'))

# Load funding data from the file  
funding_data = json.load(open('/tmp/tmptf8vwxq6.json', 'r'))

print('Data loaded successfully')
print(f'Civic documents: {len(civic_docs)}')
print(f'Funding records: {len(funding_data)}')

# Look for projects starting in Spring 2022
spring_2022_project_names = set()
spring_indicators = ['2022-Spring', '2022-spring', '2022-March', '2022-April', '2022-May', '2022-MAR', '2022-APR', '2022-MAY']

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Method 1: Look for Spring 2022 date patterns in the text
    for indicator in spring_indicators:
        if indicator in text:
            # Extract nearby project names - look for lines containing both the date and a project name
            lines = text.split('\n')
            for line in lines:
                if indicator in line:
                    # Look for project names in this line or nearby lines
                    if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'drainage', 'resurfacing']):
                        # Clean up the line to extract project name
                        project_line = line.strip()
                        if len(project_line) > 10 and not project_line.startswith('('):
                            spring_2022_project_names.add(project_line)
    
    # Method 2: Look for projects that have 2022 in their name format  
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        # Look for lines that start with '2022' and look like project names
        if line.startswith('2022') and ('Project' in line or 'Improvements' in line or 'Repairs' in line):
            # Clean up - remove bullet points etc
            clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
            spring_2022_project_names.add(clean_name)

print(f'\nFound {len(spring_2022_project_names)} potential Spring 2022 projects:')
for name in sorted(spring_2022_project_names):
    print(f'  - {name}')

# Match with funding data
funding_lookup = {f['Project_Name']: int(f['Amount']) for f in funding_data}
matched_projects = []
total_funding = 0

for project_name in spring_2022_project_names:
    # Direct match
    if project_name in funding_lookup:
        matched_projects.append({
            'name': project_name,
            'funding': funding_lookup[project_name]
        })
        total_funding += funding_lookup[project_name]
    else:
        # Try to find partial matches
        for funding_name, amount in funding_lookup.items():
            if (project_name in funding_name or funding_name in project_name):
                # Verify it's a real match, not too generic
                if len(project_name) > 15:
                    matched_projects.append({
                        'name': funding_name,
                        'funding': amount
                    })
                    total_funding += amount
                    break

print(f'\nMatched {len(matched_projects)} projects with funding data:')
for p in matched_projects:
    print(f'  - {p["name"]}: ${p["funding"]}')

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
