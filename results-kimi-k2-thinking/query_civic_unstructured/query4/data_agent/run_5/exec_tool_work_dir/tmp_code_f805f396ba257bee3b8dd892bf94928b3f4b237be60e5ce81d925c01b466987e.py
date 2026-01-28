code = """import json
import re

# Load the data from temporary files
civic_docs = json.load(open('/tmp/tmp5.json'))
funding_data = json.load(open('/tmp/tmp6.json'))

# Build funding lookup dictionary
funding_lookup = {}
for rec in funding_data:
    proj_name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amount

# Find projects with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    current_project = None
    for i, line in enumerate(lines):
        # Check if this line might be a project name
        if len(line) > 15 and not line.isupper() and not line.startswith('('):
            # Look ahead to see if this is followed by project info
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if 'Updates:' in next_line or 'Schedule:' in next_line:
                    current_project = line
        
        # Check for Spring 2022 dates
        if '2022' in line and 'Spring' in line and current_project:
            spring_2022_projects.append(current_project)
            current_project = None
        
        # Also capture project names containing 2022
        if '2022' in line and len(line) > 10:
            # Skip schedule lines
            skip_words = ['Complete:', 'Begin:', 'Advertise:', 'Construction:']
            if not any(w in line for w in skip_words):
                spring_2022_projects.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))

# Match with funding and calculate totals
total_count = 0
total_funding = 0
matched = []

for project in unique_projects:
    # Exact match
    if project in funding_lookup:
        total_count += 1
        total_funding += funding_lookup[project]
        matched.append({'name': project, 'funding': funding_lookup[project], 'type': 'exact'})
    else:
        # Try partial matching (first word match)
        proj_words = project.split()
        if proj_words:
            first_word = proj_words[0]
            for funded_name in funding_lookup:
                if funded_name.startswith(first_word) and len(first_word) > 5:
                    total_count += 1
                    total_funding += funding_lookup[funded_name]
                    matched.append({'name': project, 'funding': funding_lookup[funded_name], 'type': 'partial', 'matched': funded_name})
                    break

result = {'count': total_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
