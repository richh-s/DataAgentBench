code = """import json
import re

# Load data
civic_file = open('/tmp/tmp1.json', 'r')
funding_file = open('/tmp/tmp2.json', 'r')

civic_docs = json.load(civic_file)
funding_data = json.load(funding_file)

civic_file.close()
funding_file.close()

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

# Find projects with Spring 2022 dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for project names (lines that look like titles)
        # Usually capitalized, not all uppercase, and followed by schedule info
        if len(line) > 15 and not line.isupper() and not any(marker in line for marker in ['(', 'cid:']):
            # Check if next lines contain schedule info
            if i + 1 < len(lines) and ('Schedule:' in lines[i+1] or any(x in lines[i+1] for x in ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Complete Construction:'])):
                current_project = line
        
        # Check for Spring 2022 in schedule lines
        if 'Spring 2022' in line:
            if current_project:
                spring_2022_projects.append(current_project)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))

print('Found', len(unique_projects), 'unique Spring 2022 projects')

# Match with funding
total = 0
matched = []

for project in unique_projects:
    if project in funding_lookup:
        amount = funding_lookup[project]
        total += amount
        matched.append({'project': project, 'funding': amount, 'match': 'exact'})
    else:
        # Try partial matching for projects with different naming conventions
        for funded_name, amount in funding_lookup.items():
            # Simple similarity check
            proj_words = set(project.lower().split())
            funded_words = set(funded_name.lower().split())
            
            # Check if share significant words
            common = proj_words.intersection(funded_words)
            if len(common) >= 2 or (len(common) == 1 and len(list(common)[0]) > 8):
                total += amount
                matched.append({'project': project, 'funding': amount, 'match': 'partial', 'matched_to': funded_name})
                break

result = {
    'count': len(matched),
    'total_funding': total,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
