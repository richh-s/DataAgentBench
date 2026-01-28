code = """import json
import re

# Load civic documents from file
civic_docs = json.load(open('/tmp/tmp5.json'))

# Load funding data from file
funding_data = json.load(open('/tmp/tmp6.json'))

# Build funding lookup: project name -> total amount
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amt = int(str(record['Amount']).strip())
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amt

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))
print('Unique funded projects:', len(funding_lookup))

# Extract projects with 2022 dates
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project name followed by schedule info
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if this line looks like a project name
        # (not too short, not all caps, doesn't start with special chars)
        if len(line) > 15 and not line.isupper() and not line.startswith('(') and 'cid:' not in line:
            next_line = lines[i+1].strip()
            # Check if next line indicates project info
            if any(marker in next_line for marker in ['Updates:', 'Project Schedule:', 'Project Description:']):
                # Look for 2022 Spring in following lines (up to 5 lines ahead)
                for j in range(i, min(i+6, len(lines))):
                    future_line = lines[j]
                    if '2022' in future_line and 'Spring' in future_line:
                        projects_2022.append(line)
                        break

# Also check for 2022 in project names themselves
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if '2022' in line and len(line) > 10:
            # Skip if it's a schedule instruction line
            if not any(word in line for word in ['Complete:', 'Begin:', 'Advertise:', 'Construction', 'Design:']):
                projects_2022.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(projects_2022))
print('Found projects:', len(unique_projects))

# Match with funding
total_funding = 0
project_count = 0
matched_names = []

for proj in unique_projects:
    if proj in funding_lookup:
        total_funding += funding_lookup[proj]
        project_count += 1
        matched_names.append(proj)
    else:
        # Try partial match (first 20 chars)
        proj_start = proj[:20].lower()
        for funded_name in funding_lookup:
            if funded_name.lower().startswith(proj_start):
                total_funding += funding_lookup[funded_name]
                project_count += 1
                matched_names.append(funded_name)
                break

# Also include funding records with both 2022 and key project identifiers
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        if 'Morning View' in funded_name or 'Annual' in funded_name:
            if funded_name not in matched_names:
                total_funding += amount
                project_count += 1

result = {
    'count': project_count,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)
