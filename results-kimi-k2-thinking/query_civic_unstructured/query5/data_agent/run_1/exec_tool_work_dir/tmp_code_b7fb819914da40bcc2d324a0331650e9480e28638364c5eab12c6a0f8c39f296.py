code = """import json

# Read the civic documents data
civic_docs_var = locals()['var_functions.query_db:6']

# Handle file path or direct data
if isinstance(civic_docs_var, str) and civic_docs_var.endswith('.json'):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

# Read the funding data
funding_var = locals()['var_functions.query_db:7']

# Handle file path or direct data
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

# Build lookup for disaster-related funding
disaster_funding_lookup = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if any(keyword in proj_name for keyword in ['(FEMA', '(CalOES', '(CalJPIA']):
        clean_name = proj_name.strip()
        disaster_funding_lookup[clean_name] = {
            'amount': int(record.get('Amount', 0)),
            'funding_source': record.get('Funding_Source', '')
        }

# Extract disaster projects with 2022 start dates from civic documents
projects_with_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Look for disaster project names (containing FEMA, CalOES, or CalJPIA)
        if any(keyword in line for keyword in ['(FEMA', '(CalOES', '(CalJPIA']):
            project_name = line.strip()
            
            # Skip if too short or looks like a header
            if len(project_name) < 5:
                continue
            skip_headers = ['Capital Improvement Projects', 'Disaster Recovery Projects', 'PROJECTS', 'AGENDA', 'To:', 'From:', 'Subject:']
            if any(header in project_name for header in skip_headers):
                continue
                
            # Look for 2022 in surrounding context
            context_start = max(0, i-5)
            context_end = min(len(lines), i+6)
            has_2022 = False
            
            for j in range(context_start, context_end):
                ctx_line = lines[j]
                if '2022' in ctx_line:
                    indicators = ['Start', 'Schedule', 'Complete', 'Begin', 'Design', 'Construction', 'Advertise']
                    if any(indicator in ctx_line for indicator in indicators):
                        has_2022 = True
                        break
            
            if has_2022:
                projects_with_2022.append({
                    'project_name': project_name,
                    'filename': doc.get('filename')
                })

# Get unique project names
unique_projects = {}
for proj in projects_with_2022:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = []
    unique_projects[name].append(proj['filename'])

# Match projects with funding
matched_projects = []
total_funding = 0

for proj_name in unique_projects.keys():
    # Try exact match
    if proj_name in disaster_funding_lookup:
        funding_info = disaster_funding_lookup[proj_name]
        matched_projects.append({
            'project_name': proj_name,
            'amount': funding_info['amount']
        })
        total_funding += funding_info['amount']
    else:
        # Try partial matching
        for funding_name in disaster_funding_lookup.keys():
            if proj_name in funding_name or funding_name in proj_name:
                funding_info = disaster_funding_lookup[funding_name]
                matched_projects.append({
                    'project_name': funding_name,
                    'amount': funding_info['amount']
                })
                total_funding += funding_info['amount']
                break

# Also check for any disaster projects in funding with 2022 in name
additional_projects = []
for proj_name in disaster_funding_lookup.keys():
    if '2022' in proj_name:
        # Check if not already matched
        already_matched = any(m['project_name'] == proj_name for m in matched_projects)
        if not already_matched:
            funding_info = disaster_funding_lookup[proj_name]
            additional_projects.append({
                'project_name': proj_name,
                'amount': funding_info['amount']
            })
            total_funding += funding_info['amount']

# Prepare result
result_summary = {
    'matched_projects': matched_projects,
    'additional_projects': additional_projects,
    'total_funding': total_funding,
    'total_projects_count': len(matched_projects) + len(additional_projects)
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
