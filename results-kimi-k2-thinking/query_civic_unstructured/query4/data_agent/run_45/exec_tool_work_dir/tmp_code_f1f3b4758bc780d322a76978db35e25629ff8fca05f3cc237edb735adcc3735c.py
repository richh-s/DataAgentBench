code = """import json, re
# Get file paths
civic_file = globals()['var_functions.query_db:60']
funding_file = globals()['var_functions.query_db:48']
print('Loading files:', civic_file, funding_file)

# Load data
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Data loaded - docs:', len(civic_docs), 'funding records:', len(funding_data))

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this line or nearby lines mention Spring 2022
        context_start = max(0, i-8)
        context_end = min(len(lines), i+9)
        context = ' '.join([l.strip() for l in lines[context_start:context_end]])
        
        has_spring = any(pattern in context for pattern in spring_patterns)
        
        # Look for project names (typically uppercase, contain keywords)
        project_keywords = ['PROJECT', 'IMPROVEMENTS', 'REPAIRS', 'REPAIR', 'IMPROVEMENT']
        if has_spring and any(kw in line.upper() for kw in project_keywords):
            # Check if line is mostly uppercase (project name)
            upper_count = sum(1 for c in line if c.isupper())
            total_alpha = len([c for c in line if c.isalpha()])
            
            if total_alpha > 0 and upper_count / total_alpha > 0.3 and len(line) > 10:
                spring_2022_projects.add(line.strip())

print('Spring 2022 projects found:', len(spring_2022_projects))

# Create funding lookup map
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name and amount > 0:
        # Also add variations without suffixes for matching
        base_name = proj_name.split('(')[0].strip()
        funding_map[proj_name] = amount
        if base_name != proj_name:
            funding_map[base_name] = amount

# Match projects with funding
matched = []
total_funding = 0

for project in spring_2022_projects:
    # Try exact match first
    if project in funding_map:
        amount = funding_map[project]
        matched.append({'project': project, 'amount': amount})
        total_funding += amount
    else:
        # Try base name without suffixes
        base_name = project.split('(')[0].strip()
        if base_name in funding_map:
            amount = funding_map[base_name]
            matched.append({'project': project, 'matched_as': base_name, 'amount': amount})
            total_funding += amount

# Also check for projects that might have "Advertise: Spring 2023" etc in their context
# Re-examining for projects with actual start times
confirmed_spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns that indicate actual project starts
    if '2022-Spring' in text or '2022-03' in text or '2022-04' in text or '2022-05' in text:
        # Extract project names that appear in sections mentioning Spring 2022
        for line in text.split('\n'):
            line = line.strip()
            if line and 'PROJECT' in line.upper():
                upper_count = sum(1 for c in line if c.isupper())
                if upper_count > len(line) * 0.3 and len(line) > 15:
                    confirmed_spring_projects.append(line)

confirmed_unique = set(confirmed_spring_projects)
print('Confirmed Spring 2022 projects:', len(confirmed_unique))

# Re-match with funding for confirmed projects
confirmed_matched = []
confirmed_total = 0
for project in confirmed_unique:
    if project in funding_map:
        amount = funding_map[project]
        confirmed_matched.append({'project': project, 'amount': amount})
        confirmed_total += amount
    else:
        base_name = project.split('(')[0].strip()
        if base_name in funding_map:
            amount = funding_map[base_name]
            confirmed_matched.append({'project': project, 'matched_as': base_name, 'amount': amount})
            confirmed_total += amount

print('Final matched projects:', len(confirmed_matched))
print('Total funding:', confirmed_total)

# Output result
result = {
    'project_count': len(confirmed_matched),
    'total_funding': confirmed_total,
    'projects': confirmed_matched[:30]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
