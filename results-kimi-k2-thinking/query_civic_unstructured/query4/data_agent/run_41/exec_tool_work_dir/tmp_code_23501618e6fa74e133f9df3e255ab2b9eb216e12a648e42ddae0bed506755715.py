code = """import json
import re

## Load funding data
funding_file = open('/tmp/tmp_3z7x6gk.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

## Load Spring 2022 documents
spring_file = open('/tmp/tmp_2z4l8jq.json', 'r')
spring_docs = json.load(spring_file)
spring_file.close()

print('Funding records: %d' % len(funding_data))
print('Spring 2022 documents: %d' % len(spring_docs))

## Find Spring 2022 projects
found_projects = []

for doc in spring_docs:
    text_lines = doc['text'].split('\n')
    for i in range(len(text_lines)):
        line = text_lines[i].strip()
        if 'Spring' in line and '2022' in line:
            if 'construction' in line.lower() or 'advertise' in line.lower() or 'begin' in line.lower():
                # Look for project name in previous lines
                project_line = None
                for j in range(i-1, max(i-15, -1), -1):
                    prev = text_lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•'):
                        bad_words = ['update', 'schedule', 'status', 'description', 'begin construction', 'advertise', 'complete design']
                        has_bad_word = any(word in prev.lower() for word in bad_words)
                        if not has_bad_word and len(prev) < 200:
                            project_line = prev
                            break
                
                if project_line and project_line not in found_projects:
                    found_projects.append(project_line)

print('Found %d unique Spring 2022 projects' % len(found_projects))

## Match with funding data
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

total_funding = 0
matched = 0

for proj in found_projects:
    if proj in funding_dict:
        total_funding += funding_dict[proj]
        matched += 1
    else:
        # Try partial matching
        for funded_name in funding_dict:
            if proj in funded_name or funded_name in proj:
                total_funding += funding_dict[funded_name]
                matched += 1
                break

print('Matched %d projects with funding' % matched)
print('Total funding amount: $%d' % total_funding)

result = {'spring_2022_project_count': len(found_projects), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
