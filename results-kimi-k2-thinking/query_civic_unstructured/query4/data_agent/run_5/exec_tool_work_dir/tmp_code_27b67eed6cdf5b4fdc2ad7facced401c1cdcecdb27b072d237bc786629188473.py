code = """import json
import re

# Open and read the data files
civic_docs_file = open('/tmp/tmp1.json', 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open('/tmp/tmp2.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

print('Loaded', len(civic_docs), 'documents and', len(funding_data), 'funding records')

# Build funding map
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

print('Funding map has', len(funding_map), 'projects')

# Find Spring 2022 projects in civic docs
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for lines mentioning Spring 2022
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Spring 2022' in line or 'spring 2022' in line:
            # Look backward for project name
            project_name = None
            for j in range(i-1, max(0, i-4), -1):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    if not any(x in prev.lower() for x in ['updates', 'schedule', 'complete', 'begin', 'advertise']):
                        project_name = prev
                        break
            if project_name:
                spring_2022_projects.append(project_name)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))
print('Found Spring 2022 projects:', len(unique_projects))

# Match with funding
total_funding = 0
matched = []

for proj in unique_projects:
    if proj in funding_map:
        amount = funding_map[proj]
        total_funding += amount
        matched.append({'name': proj, 'amount': amount})
    else:
        # Try partial match
        for funded_proj in funding_map:
            if proj.lower() in funded_proj.lower() or funded_proj.lower() in proj.lower():
                amount = funding_map[funded_proj]
                total_funding += amount
                matched.append({'name': proj, 'amount': amount, 'matched_to': funded_proj})
                break

result = {
    'count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
