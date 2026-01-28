code = """import json
import re

# Load civic documents data
civic_docs_var = locals()['var_functions.query_db:24']
if isinstance(civic_docs_var, str) and civic_docs_var.endswith('.json'):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_var) if civic_docs_var else []

# Load funding data
funding_var = locals()['var_functions.query_db:25']
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = list(funding_var) if funding_var else []

# Build funding lookup - clean project names for better matching
funding_lookup = {}
disaster_funding_names = set()

for record in funding_data:
    proj_name = record.get('Project_Name', '').strip()
    amount = int(record.get('Amount', 0))
    funding_lookup[proj_name] = amount
    
    # Track which funding records are disaster-related
    if any(marker in proj_name for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
        disaster_funding_names.add(proj_name)

print(f"Total funding records: {len(funding_lookup)}")
print(f"Disaster-related funding records: {len(disaster_funding_names)}")

# Extract projects from civic documents
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project sections - typically project names are on their own line
    # followed by updates and schedules
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines, bullet points, and common headers
        if not line or line.startswith('\u2022') or line.startswith('(') or line.startswith('cid:'):
            continue
            
        skip_patterns = ['Capital Improvement', 'Disaster Recovery', 'PROJECTS', 
                        'AGENDA', 'To:', 'From:', 'Subject:', 'Prepared by:', 
                        'Approved by:', 'Date prepared:', 'Meeting date:',
                        'Public Works Commission', 'Item', 'Page ', 'Recommended Action']
        
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Check if this line looks like a project name (not too short, not all caps header)
        if len(line) > 10 and len(line) < 200 and not line.isupper():
            # Check context for 2022 schedule information
            context_start = max(0, i-8)
            context_end = min(len(lines), i+10)
            
            context_text = ' '.join(lines[context_start:context_end])
            
            # Check if this project has 2022 in its schedule/context
            if '2022' in context_text:
                # Check if it's disaster-related (has FEMA/CalOES/CalJPIA markers)
                is_disaster = any(marker in line for marker in ['(FEMA', '(CalOES', '(CalJPIA'])
                
                # Also check if it matches a disaster funding record (even if not explicitly marked in text)
                if not is_disaster:
                    for disaster_funding in disaster_funding_names:
                        # Check for name match in either direction
                        if line in disaster_funding or disaster_funding in line:
                            is_disaster = True
                            # Use the funding name for consistency
                            line = disaster_funding
                            break
                
                if is_disaster:
                    projects_2022.append({
                        'project_name': line,
                        'source_file': doc.get('filename', ''),
                        'is_disaster': True
                    })

# Remove duplicates and match with funding
unique_projects = {}
for proj in projects_2022:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = {
            'amount': 0,
            'matched': False
        }

# Match projects with funding amounts
for proj_name in unique_projects.keys():
    # Direct match
    if proj_name in funding_lookup:
        unique_projects[proj_name]['amount'] = funding_lookup[proj_name]
        unique_projects[proj_name]['matched'] = True
    else:
        # Try partial matching for similar names
        for funding_name in funding_lookup.keys():
            # Check if project names are very similar
            if (proj_name in funding_name or funding_name in proj_name) and len(proj_name) > 15:
                unique_projects[proj_name]['amount'] = funding_lookup[funding_name]
                unique_projects[proj_name]['matched'] = True
                unique_projects[proj_name]['funding_name_used'] = funding_name
                break

# Also include direct disaster funding records that have 2022 in the name
for funding_name in disaster_funding_names:
    if '2022' in funding_name and funding_name not in unique_projects:
        unique_projects[funding_name] = {
            'amount': funding_lookup[funding_name],
            'matched': True
        }

# Calculate totals
total_funding = sum(info['amount'] for info in unique_projects.values() if info['matched'])
matched_count = sum(1 for info in unique_projects.values() if info['matched'])

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': matched_count,
    'projects': [
        {
            'name': name,
            'amount': info['amount']
        }
        for name, info in unique_projects.items() 
        if info['matched']
    ]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json'}

exec(code, env_args)
