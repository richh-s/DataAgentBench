code = """import json
import re

# Load data from files
civic_docs_file = open('/tmp/tmp1.json', 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open('/tmp/tmp2.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = amount

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        # Look for Spring 2022 references
        if 'Spring 2022' in line or 'spring 2022' in line:
            # Find project name (usually 1-3 lines before)
            for j in range(i-1, max(-1, i-4), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 10:
                    # Skip section headers and markers
                    if not any(marker in prev_line for marker in ['(', 'cid:', 'Updates:', 'Schedule:', 'Design:', 'Construction:']):
                        spring_2022_projects.append(prev_line)
                        break

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))
print('Spring 2022 projects found:', len(unique_projects))

# Match with funding
total_funding = 0
matched_projects = []

for project in unique_projects:
    # Exact match
    if project in funding_lookup:
        amount = funding_lookup[project]
        total_funding += amount
        matched_projects.append({'name': project, 'funding': amount, 'match': 'exact'})
    else:
        # Partial match
        for funded_name in funding_lookup:
            if project.lower() in funded_name.lower() or funded_name.lower() in project.lower():
                amount = funding_lookup[funded_name]
                total_funding += amount
                matched_projects.append({'name': project, 'funding': amount, 'match': 'partial', 'matched_to': funded_name})
                break

result = {'count': len(matched_projects), 'total_funding': total_funding, 'projects': matched_projects}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
