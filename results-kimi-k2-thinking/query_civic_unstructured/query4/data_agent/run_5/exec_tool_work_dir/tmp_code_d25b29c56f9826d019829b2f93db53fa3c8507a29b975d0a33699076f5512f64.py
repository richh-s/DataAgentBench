code = """import json
import re

# Get the stored data directly from local variables
civic_docs = locals()['var_functions.query_db:44']
funding_data = locals()['var_functions.query_db:31']

# Check if they're file paths (strings) or already loaded data
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Build funding lookup map
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amount

# Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for Spring 2022 date references
        if '2022' in line and 'Spring' in line:
            # Look backward for project name (up to 5 lines)
            project_name = None
            for j in range(i-1, max(-1, i-6), -1):
                candidate = lines[j].strip()
                # Filter out markers and short lines
                if len(candidate) > 10 and not candidate.startswith('(') and 'cid:' not in candidate:
                    # Skip lines that look like section headers
                    if not any(marker in candidate for marker in ['Updates:', 'Schedule:', 'Project Description:', 'Complete Design:']):
                        project_name = candidate
                        break
            
            if project_name:
                spring_2022_projects.append(project_name)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))
print('Found', len(unique_projects), 'potential Spring 2022 projects')

# Match projects with funding data
total_funding = 0
matched_projects = []
unmatched_projects = []

for project in unique_projects:
    # Direct exact match
    if project in funding_lookup:
        amount = funding_lookup[project]
        total_funding += amount
        matched_projects.append({
            'project_name': project,
            'funding_amount': amount,
            'match_type': 'exact'
        })
    else:
        # Try partial matching
        matched = False
        for funded_name in funding_lookup:
            # Check if project name appears in funded name or funded name appears in project
            if (project.lower() in funded_name.lower() or 
                funded_name.lower().startswith(project.split()[0].lower()) and len(project.split()[0]) > 5):
                amount = funding_lookup[funded_name]
                total_funding += amount
                matched_projects.append({
                    'project_name': project,
                    'funding_amount': amount,
                    'match_type': 'partial',
                    'matched_to': funded_name
                })
                matched = True
                break
        
        if not matched:
            unmatched_projects.append(project)

# Also check for projects with "2022" in their name that aren't already matched
for funded_name in funding_lookup:
    if '2022' in funded_name:
        # Check if not already matched
        already_matched = any(p['project_name'] == funded_name for p in matched_projects)
        if not already_matched:
            amount = funding_lookup[funded_name]
            total_funding += amount
            matched_projects.append({
                'project_name': funded_name,
                'funding_amount': amount,
                'match_type': 'funding_record'
            })

# Final result
result = {
    'total_projects': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:20]  # Limit output
}

print('FINAL RESULT:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
