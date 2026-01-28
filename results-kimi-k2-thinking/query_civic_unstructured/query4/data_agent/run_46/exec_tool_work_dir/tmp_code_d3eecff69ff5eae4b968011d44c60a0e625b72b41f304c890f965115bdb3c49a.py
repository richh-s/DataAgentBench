code = """import json, re, os
civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding = json.load(f)

print('Documents loaded:', len(civic_docs))
print('Funding records:', len(funding))

spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for lines that contain both a project name pattern and Spring 2022 date
    # Project names typically start with uppercase and are on their own line
    lines = text.split('\n')
    
    # First pass: identify all lines that might be project names
    potential_projects = []
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty, bullet points, and metadata lines
        if (line and not line.startswith('cid:') and not line.startswith('To:') 
            and not line.startswith('Prepared') and not line.startswith('Agenda')
            and len(line) > 10 and len(line) < 150
            and not any(marker in line for marker in ['\u2022', '\u00e2', '\u20ac'])):
            
            # Check if next few lines contain Spring 2022 date
            next_block = '\n'.join(lines[i:i+5])
            if '2022' in next_block and ('Spring' in next_block or 'Mar' in next_block or 'Apr' in next_block or 'May' in next_block):
                # Clean and add
                clean_name = re.sub(r'^[\-\*]+\s*', '', line)
                clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
                clean_name = ' '.join(clean_name.split())
                if clean_name and 'Agenda' not in clean_name and 'Report' not in clean_name:
                    potential_projects.append(clean_name)
    
    # Second pass: look more specifically for date patterns that confirm Spring 2022
    for proj_name in potential_projects:
        if proj_name in text:
            # Find occurrences of this project near Spring 2022 dates
            proj_pattern = re.escape(proj_name[:50])  # Use first 50 chars for pattern
            date_patterns = [
                proj_pattern + r'.*?Complete Design:\s*([A-Za-z0-9\- ]+)',
                proj_pattern + r'.*?Begin Construction:\s*([A-Za-z0-9\- ]+)'
            ]
            
            for pattern in date_patterns:
                matches = re.findall(pattern, text, re.DOTALL)
                for date_str in matches:
                    if '2022' in date_str:
                        # Check if spring
                        date_upper = date_str.upper()
                        if ('SPRING' in date_upper or 'MARCH' in date_upper or 'APRIL' in date_upper or 'MAY' in date_upper or
                            'MAR' in date_upper or 'APR' in date_upper or 'MAY' in date_upper):
                            spring_projects.add(proj_name)

spring_project_list = list(spring_projects)
print(f'Found {len(spring_project_list)} unique Spring 2022 projects:')
for p in sorted(spring_project_list):
    print(f'  {p}')

# Build funding lookup
funding_map = {}
for f in funding:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Match projects with funding
matched = []
total = 0
for project in spring_project_list:
    # Exact match
    if project in funding_map:
        matched.append({'project': project, 'amount': funding_map[project]})
        total += funding_map[project]
    else:
        # Try case-insensitive and partial matching
        found = False
        project_clean = re.sub(r'[^A-Za-z0-9]', '', project).lower()
        for fund_name, amount in funding_map.items():
            fund_clean = re.sub(r'[^A-Za-z0-9]', '', fund_name).lower()
            if project_clean in fund_clean or fund_clean in project_clean:
                matched.append({'project': project, 'amount': amount, 'matched_with': fund_name})
                total += amount
                found = True
                break
        
        if not found:
            print(f'No funding match for: {project}')

print(f'\nMatched {len(matched)} projects with total funding: ${total:,}')

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
