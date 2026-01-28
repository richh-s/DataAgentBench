code = """import json
import re
import os

# Load data from files
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract projects with start dates from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections
    # Capital Improvement Projects
    capital_sections = re.split(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', text)
    
    # Disaster Recovery Projects
    disaster_match = re.search(r'Disaster Recovery Projects(.*)', text, re.DOTALL)
    
    # Process each section to find projects
    lines = text.split('\n')
    current_section = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'capital_design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'capital_construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'capital_not_started'
        elif 'Disaster Recovery Projects' in line:
            current_section = 'disaster'
        elif line and not line.startswith('cid:') and not line.startswith('â€¢') and not line.startswith('\u2022'):
            # This might be a project name
            if (current_section and 
                len(line) > 10 and 
                not line.endswith(':') and
                not line.startswith('Project') and
                not line.startswith('To:') and
                not line.startswith('Prepared') and
                not line.startswith('Approved') and
                not line.startswith('Date') and
                not line.startswith('Meeting') and
                not line.startswith('Subject') and
                not line.startswith('RECOMMENDED') and
                not line.startswith('DISCUSSION')):
                
                # Check if next lines contain schedule info
                project_block = '\n'.join(lines[i:i+10])
                
                # Extract dates
                start_date = None
                
                # Look for schedule patterns
                schedule_patterns = [
                    r'Complete Design:\s*([^\n]+)',
                    r'Advertise:\s*([^\n]+)',
                    r'Begin Construction:\s*([^\n]+)',
                    r'Complete Construction:\s*([^\n]+)',
                    r'Estimated Schedule:\s*\n\s*Complete Design:\s*([^\n]+)',
                ]
                
                for pattern in schedule_patterns:
                    match = re.search(pattern, project_block, re.IGNORECASE)
                    if match:
                        date_str = match.group(1).strip()
                        if date_str and '202' in date_str:
                            start_date = date_str
                            break
                
                # Determine status and type
                if current_section == 'capital_design':
                    status = 'design'
                    project_type = 'capital'
                elif current_section == 'capital_construction':
                    status = 'construction'
                    project_type = 'capital'
                elif current_section == 'capital_not_started':
                    status = 'not started'
                    project_type = 'capital'
                elif current_section == 'disaster':
                    status = 'design'  # default for disaster projects
                    project_type = 'disaster'
                else:
                    status = None
                    project_type = None
                
                # Clean project name
                project_name = re.sub(r'^(cid:\d+|[\u2022â€¢\-\*]+\s*)', '', line).strip()
                project_name = re.sub(r'\s+', ' ', project_name)
                
                if project_name and len(project_name) > 5 and start_date:
                    projects.append({
                        'Project_Name': project_name,
                        'start_date': start_date,
                        'status': status,
                        'type': project_type,
                        'source': filename
                    })

# Filter for Spring 2022 projects
spring_2022_projects = []

for project in projects:
    start_date = project['start_date']
    
    # Check for Spring 2022 patterns
    if '2022-Spring' in start_date:
        spring_2022_projects.append(project)
    elif '2022' in start_date:
        # Check for month names (March, April, May)
        if any(month in start_date for month in ['March', 'April', 'May', 'Mar', 'Apr', 'May']):
            spring_2022_projects.append(project)
        # Check for numeric months (03, 04, 05)
        elif any(f'-{m:02d}' in start_date or f'/{m:02d}' in start_date for m in [3, 4, 5]):
            spring_2022_projects.append(project)

print(f"Found {len(spring_2022_projects)} projects with Spring 2022 start dates")

# Show the projects found
for p in spring_2022_projects:
    print(f"  {p['Project_Name']}: {p['start_date']}")

# Match with funding data
# Create a mapping of project names to funding amounts
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    amount = int(f['Amount'])
    if name in funding_map:
        funding_map[name] += amount
    else:
        funding_map[name] = amount

# Find matching projects and calculate total funding
total_funding = 0
matched_projects = []

for project in spring_2022_projects:
    proj_name = project['Project_Name']
    
    # Direct match
    if proj_name in funding_map:
        total_funding += funding_map[proj_name]
        matched_projects.append({
            'name': proj_name,
            'funding': funding_map[proj_name],
            'date': project['start_date']
        })
    else:
        # Try fuzzy matching - check if any funding project name contains this name
        for fund_name, amount in funding_map.items():
            if proj_name in fund_name or fund_name in proj_name:
                total_funding += amount
                matched_projects.append({
                    'name': proj_name,
                    'funding': amount,
                    'matched_with': fund_name,
                    'date': project['start_date']
                })
                break

print(f"\nMatched {len(matched_projects)} projects with funding")
print(f"Total funding: ${total_funding:,}")

# Prepare final result
result = {
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects_with_funding': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
