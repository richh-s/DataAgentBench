code = """import json, re

funding_file = open('/tmp/tmp_3z7x6gk.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

spring_file = open('/tmp/tmp_2z4l8jq.json', 'r')
spring_docs = json.load(spring_file)
spring_file.close()

print('Funding:', len(funding_data))
print('Spring docs:', len(spring_docs))

projects = []
for doc in spring_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line:
            keyword_found = any(k in line.lower() for k in ['begin construction', 'construction', 'advertise', 'start'])
            if keyword_found:
                name = None
                for j in range(i-1, max(-1, i-15), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•'):
                        if len(prev) < 200:
                            bad = ['update', 'schedule', 'status', 'description', 'project']
                            if not any(word in prev.lower() for word in bad):
                                name = prev
                                break
                if name:
                    projects.append(name)

unique_projects = list(set(projects))
print('Spring 2022 projects:', len(unique_projects))
for p in sorted(unique_projects):
    print('- ' + p)

funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

matched_count = 0
total_funding = 0
for proj in unique_projects:
    if proj in funding_lookup:
        matched_count += 1
        total_funding += funding_lookup[proj]
    else:
        for funded_name in funding_lookup:
            if proj in funded_name or funded_name in proj:
                matched_count += 1
                total_funding += funding_lookup[funded_name]
                break

print('Matched count:', matched_count)
print('Total funding:', total_funding)

result = {'spring_2022_project_count': len(unique_projects), 'matched_projects': matched_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
