code = """import json
import re

civic_docs_result = locals().get('var_functions.query_db:6')

# Load civic documents data
if isinstance(civic_docs_result, str) and '.json' in civic_docs_result:
    import os
    if os.path.exists(civic_docs_result):
        with open(civic_docs_result, 'r') as f:
            civic_docs = json.load(f)
    else:
        civic_docs = []
else:
    civic_docs = civic_docs_result if isinstance(civic_docs_result, list) else []

# Parse projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    section_type = ''
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect section type
        if line.startswith('Capital Improvement Projects'):
            if 'Design' in line:
                section_type = 'design'
            elif 'Construction' in line:
                section_type = 'construction'
            elif 'Not Started' in line:
                section_type = 'not started'
            continue
        
        # Look for project name (uppercase, not starting with parenthesis)
        if line.isupper() and len(line) > 10 and not line.startswith('('):
            project = {
                'Project_Name': line,
                'topic': '',
                'type': 'capital',
                'status': section_type,
                'st': '',
                'et': ''
            }
            projects.append(project)
            continue
        
        # Look for schedule information
        if projects and ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                field = parts[0].strip().lower()
                value = parts[1].strip()
                
                # Check for spring 2022 start
                if '2022' in value and 'spring' in value.lower():
                    if not projects[-1]['st']:
                        projects[-1]['st'] = value
                
                # Extract topics
                topics = []
                v_lower = value.lower()
                if 'drain' in v_lower or 'storm' in v_lower:
                    topics.append('drainage')
                if 'fema' in v_lower:
                    topics.append('FEMA')
                if 'road' in v_lower:
                    topics.append('road')
                if 'park' in v_lower:
                    topics.append('park')
                if 'bridge' in v_lower:
                    topics.append('bridge')
                
                if topics:
                    if projects[-1]['topic']:
                        projects[-1]['topic'] += ', ' + ', '.join(topics)
                    else:
                        projects[-1]['topic'] = ', '.join(topics)
        
        # Check for disaster project indicators
        if projects and ('fema' in line.lower() or 'caloes' in line.lower()):
            projects[-1]['type'] = 'disaster'

# Filter projects that started in Spring 2022
spring_2022_projects = []
for proj in projects:
    st = proj.get('st', '')
    if st and '2022' in st and 'spring' in st.lower():
        spring_2022_projects.append(proj)

# Get funding data
funding_result = locals().get('var_functions.query_db:12')
if isinstance(funding_result, str) and '.json' in funding_result:
    import os
    if os.path.exists(funding_result):
        with open(funding_result, 'r') as f:
            funding_data = json.load(f)
    else:
        funding_data = []
else:
    funding_data = funding_result if isinstance(funding_result, list) else []

# Convert funding amounts to integers
for fund in funding_data:
    try:
        fund['Amount'] = int(str(fund.get('Amount', '0')))
    except:
        fund['Amount'] = 0

# Build a mapping of project names to funding amounts
funding_map = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = fund.get('Amount', 0)
    if name:
        funding_map[name] = funding_map.get(name, 0) + amount

# Calculate total funding for Spring 2022 projects
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_map:
        funding = funding_map[proj_name]
        total_funding += funding
        matched_projects.append({
            'name': proj_name,
            'funding': funding
        })
        continue
    
    # Fuzzy match - check partial names
    for fund_name, amount in funding_map.items():
        # Check if one name contains the other
        if (proj_name.lower() in fund_name.lower() or 
            fund_name.lower() in proj_name.lower() or
            (len(proj_name) > 15 and any(word in fund_name.lower() for word in proj_name.lower().split()))):
            total_funding += amount
            matched_projects.append({
                'name': proj_name,
                'funding': amount,
                'matched_to': fund_name
            })
            break

result = {
    'spring_2022_project_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'sample_projects': matched_projects[:5] if matched_projects else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records'}

exec(code, env_args)
