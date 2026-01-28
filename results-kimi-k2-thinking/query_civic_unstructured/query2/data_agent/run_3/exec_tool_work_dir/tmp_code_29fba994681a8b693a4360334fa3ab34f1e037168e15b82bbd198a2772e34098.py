code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:3']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for record in funding_records:
    proj_name = record['Project_Name'].upper().strip()
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

print('Funding records loaded:', len(funding_records))
print('Civic documents loaded:', len(civic_docs))

# Extract projects from civic documents
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('Page') or line.startswith('---'):
            continue
        
        # Look for project completion patterns
        completion_patterns = [
            'completed', 'completion', 'completed,', 'completed.',
            'Notice of completion', 'construction was completed'
        ]
        
        for pattern in completion_patterns:
            if pattern.lower() in line.lower():
                # Look for year 2022 in this line or nearby
                if '2022' in line:
                    # Look back to find project name (usually same line or previous 1-2 lines)
                    for j in range(max(0, i-2), i+1):
                        project_line = lines[j].strip()
                        # Skip if it's the completion line itself
                        if any(pattern.lower() in project_line.lower() for pattern in completion_patterns):
                            continue
                        if project_line and len(project_line) > 8 and not project_line.startswith('('):
                            # Check if park-related
                            if 'park' in project_line.lower() or 'Park' in project_line:
                                all_projects.append({
                                    'name': project_line,
                                    'status': 'completed',
                                    'year': '2022',
                                    'topic': 'park'
                                })
                                break

# Remove duplicates by name
unique_projects = {}
for proj in all_projects:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj

park_completed_2022 = list(unique_projects.values())

print('\nPark projects completed in 2022 found:', len(park_completed_2022))
for proj in park_completed_2022[:5]:
    print('-', proj['name'])

# Match with funding data
total_funding = 0
matched_projects = []

for proj in park_completed_2022:
    proj_name_upper = proj['name'].upper()
    
    # Direct match
    if proj_name_upper in funding_lookup:
        amount = funding_lookup[proj_name_upper]
        total_funding += amount
        matched_projects.append({
            'project_name': proj['name'],
            'amount': amount
        })
    else:
        # Try partial matching (first 80 characters of project name)
        proj_short = proj_name_upper[:80]
        for funded_name, amount in funding_lookup.items():
            if proj_short in funded_name or funded_name in proj_name_upper:
                total_funding += amount
                matched_projects.append({
                    'project_name': proj['name'],
                    'matched_as': funded_name,
                    'amount': amount
                })
                break

print('\nMatched with funding:', len(matched_projects))
print('Total funding:', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'funding_details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
