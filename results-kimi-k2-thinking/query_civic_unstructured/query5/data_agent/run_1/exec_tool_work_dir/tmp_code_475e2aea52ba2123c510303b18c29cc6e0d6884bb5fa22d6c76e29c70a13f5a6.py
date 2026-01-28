code = """import json

# Load civic documents
civic_docs_variable = locals()['var_functions.query_db:24']
civic_docs = []
if isinstance(civic_docs_variable, str) and civic_docs_variable.endswith('.json'):
    with open(civic_docs_variable, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_variable) if civic_docs_variable else []

# Load funding data
funding_variable = locals()['var_functions.query_db:25']
funding_data = []
if isinstance(funding_variable, str) and funding_variable.endswith('.json'):
    with open(funding_variable, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = list(funding_variable) if funding_variable else []

# Build funding lookup by project name
funding_by_name = {}
disaster_related = set()
for record in funding_data:
    name = record.get('Project_Name', '').strip()
    amount = int(record.get('Amount', 0))
    funding_by_name[name] = amount
    if '(FEMA' in name or '(CalOES' in name or '(CalJPIA' in name:
        disaster_related.add(name)

# Extract disaster projects with 2022 start dates from civic documents
eligible_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Iterate through each line to find projects
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty lines and obvious non-project lines
        if not line:
            continue
        
        # Skip common headers and metadata
        skip_terms = ['Capital Improvement', 'Disaster Recovery', 'PROJECTS', 'AGENDA', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Public Works Commission', 'Item', 'Page ', 'Recommended Action', 'Updates:', 'Project Schedule:']
        should_skip = any(term in line for term in skip_terms)
        if should_skip:
            continue
        
        # Check if line might be a project name (reasonable length, not a bullet point)
        if len(line) > 10 and len(line) < 200:
            # Look for 2022 in context window
            context_start = max(0, i-8)
            context_end = min(len(lines), i+10)
            full_context = ' '.join(lines[context_start:context_end])
            
            if '2022' in full_context:
                # Check if disaster-related
                is_disaster = False
                
                # Explicit disaster markers in the line
                if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
                    is_disaster = True
                
                # Or matches a known disaster funding project
                if not is_disaster:
                    for disaster_name in disaster_related:
                        if line in disaster_name or disaster_name in line:
                            is_disaster = True
                            line = disaster_name
                            break
                
                if is_disaster:
                    eligible_projects.append({'name': line, 'matched': False, 'amount': 0})

# Remove duplicates and match with funding
unique_project_map = {}
for proj in eligible_projects:
    name = proj['name']
    if name not in unique_project_map:
        unique_project_map[name] = {'amount': 0, 'matched': False}

# Match projects with funding amounts
for proj_name in unique_project_map.keys():
    if proj_name in funding_by_name:
        unique_project_map[proj_name]['amount'] = funding_by_name[proj_name]
        unique_project_map[proj_name]['matched'] = True
    else:
        # Try fuzzy matching for similar project names
        for funding_name in funding_by_name.keys():
            if proj_name in funding_name or funding_name in proj_name:
                if len(proj_name) > 15:
                    unique_project_map[proj_name]['amount'] = funding_by_name[funding_name]
                    unique_project_map[proj_name]['matched'] = True
                    unique_project_map[proj_name]['funding_name_used'] = funding_name
                    break

# Also include disaster funding records that explicitly have 2022 in the name
for disaster_name in disaster_related:
    if '2022' in disaster_name and disaster_name not in unique_project_map:
        unique_project_map[disaster_name] = {'amount': funding_by_name[disaster_name], 'matched': True}

# Calculate final totals
total_funding_amount = 0
matched_project_list = []

for name, info in unique_project_map.items():
    if info['matched'] and info['amount'] > 0:
        total_funding_amount += info['amount']
        matched_project_list.append({'project_name': name, 'amount': info['amount']})

result = {
    'total_funding': total_funding_amount,
    'project_count': len(matched_project_list),
    'projects': matched_project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json'}

exec(code, env_args)
