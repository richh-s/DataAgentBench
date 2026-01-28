code = """import json

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:0'], 'r'))
funding_data = json.load(open(locals()['var_functions.query_db:1'], 'r'))

# Convert amounts
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Identify park projects completed in 2022
park_projects_2022 = []

# Based on document analysis, explicitly check for these projects:
target_projects = [
    'Bluffs Park Shade Structure',
    'Point Dume Walkway Repairs',
    'Marie Canyon Green Streets'  # This appears to be completed based on the preview
]

# Check each document for these projects
for doc in civic_docs:
    text = doc.get('text', '')
    
    for project in target_projects:
        if project in text:
            # Check if completed in 2022
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if project in line:
                    # Look ahead for completion status
                    for j in range(i, min(i+15, len(lines))):
                        if ('completed' in lines[j].lower() and '2022' in lines[j]) or \
                           ('Construction was completed' in lines[j] and 'November 2022' in lines[j]):
                            if project not in park_projects_2022:
                                park_projects_2022.append(project)

# Also scan for any other park projects
for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    for line in lines:
        line_stripped = line.strip()
        if 'Park' in line_stripped and len(line_stripped) > 10 and 'completed' in doc.get('text', '').lower() and '2022' in doc.get('text', ''):
            if line_stripped not in park_projects_2022 and line_stripped[0].isupper():
                park_projects_2022.append(line_stripped)

# Match park projects with funding
total_funding = 0
funding_matches = []

for project in park_projects_2022:
    proj_key = project.lower().strip()
    
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower().strip()
        
        # Check for match
        if proj_key == fund_key or fund_key in proj_key or proj_key in fund_key:
            total_funding += fund['Amount']
            funding_matches.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': fund['Amount'],
                'source': fund['Funding_Source']
            })

result = {
    'total_funding': total_funding,
    'project_count': len(park_projects_2022),
    'projects': park_projects_2022,
    'funding_matches': funding_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:24': {'civic_docs': 5, 'funding': 500}, 'var_functions.execute_python:26': {'specific_park_projects': ['Bluffs Park Shade Structure', 'Point Dume Walkway Repairs'], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'funding_record': 'Bluffs Park Shade Structure', 'amount': 21000, 'source': 'Government Grant'}, {'project': 'Point Dume Walkway Repairs', 'funding_record': 'Point Dume Walkway Repairs', 'amount': 59000, 'source': 'International Aid'}], 'total_funding': 80000, 'record_count': 2}}

exec(code, env_args)
