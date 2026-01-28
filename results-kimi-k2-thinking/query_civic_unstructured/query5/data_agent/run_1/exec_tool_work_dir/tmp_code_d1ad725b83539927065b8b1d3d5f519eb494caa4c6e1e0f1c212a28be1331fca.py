code = """import json
import re

# Load data from storage
x1 = locals()['var_functions.query_db:32']
x2 = locals()['var_functions.query_db:33']

# Parse civic documents
if isinstance(x1, str) and x1.endswith('.json'):
    with open(x1, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(x1) if x1 else []

# Parse funding data
if isinstance(x2, str) and x2.endswith('.json'):
    with open(x2, 'r') as f:
        funding = json.load(f)
else:
    funding = list(x2) if x2 else []

# Build funding lookup by project name
funding_lookup = {}
for record in funding:
    name = record.get('Project_Name', '').strip()
    amount = int(record.get('Amount', '0'))
    funding_lookup[name] = amount

# Find disaster projects with 2022 start dates
found_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10 or len(line) > 300:
            continue
            
        # Skip headers and metadata
        skip_terms = ['Capital Improvement Projects', 'Disaster Recovery Projects', 'AGENDA', 'Item', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Page ', 'RECOMMENDED ACTION']
        if any(term in line for term in skip_terms):
            continue
        
        # Check context for 2022 dates
        context_start = max(0, i-6)
        context_end = min(len(lines), i+8)
        context = '\n'.join(lines[context_start:context_end])
        
        if '2022' in context:
            # Check if disaster-related
            is_disaster = False
            
            # Explicit markers
            if any(marker in line for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
                is_disaster = True
            
            # Or contains disaster keywords
            if not is_disaster and any(keyword in line.lower() for keyword in ['fema', 'disaster', 'fire', 'emergency']):
                is_disaster = True
            
            # Or matches known disaster funding records
            if not is_disaster:
                for disaster_proj in funding_lookup.keys():
                    if any(marker in disaster_proj for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
                        if line in disaster_proj or disaster_proj in line:
                            is_disaster = True
                            line = disaster_proj
                            break
            
            if is_disaster:
                found_project_names.add(line)

# Match found projects with funding and calculate total
total_funding = 0
matched_projects = []

for proj_name in found_project_names:
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        total_funding += amount
        matched_projects.append({'name': proj_name, 'amount': amount})
    else:
        # Try partial match
        for funding_name in funding_lookup.keys():
            if proj_name in funding_name or funding_name in proj_name:
                amount = funding_lookup[funding_name]
                total_funding += amount
                matched_projects.append({'name': funding_name, 'amount': amount})
                break

# Also include explicit 2022 disaster funding records
for funding_name in funding_lookup.keys():
    if '2022' in funding_name:
        # Check if disaster-related
        if any(marker in funding_name for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
            # Check if not already included
            already_included = any(p['name'] == funding_name for p in matched_projects)
            if not already_included:
                amount = funding_lookup[funding_name]
                total_funding += amount
                matched_projects.append({'name': funding_name, 'amount': amount})

# Prepare final result
result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
