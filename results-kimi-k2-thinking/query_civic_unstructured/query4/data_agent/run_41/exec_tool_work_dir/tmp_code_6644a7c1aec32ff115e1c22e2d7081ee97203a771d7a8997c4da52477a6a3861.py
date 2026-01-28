code = """import json, re

funding_file = open('/tmp/tmp_3z7x6gk.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

spring_file = open('/tmp/tmp_2z4l8jq.json', 'r')
spring_docs = json.load(spring_file)
spring_file.close()

print('Funding records:', len(funding_data))
print('Spring 2022 documents:', len(spring_docs))

spring_2022_projects = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if 'Spring' in line and '2022' in line and any(k in line.lower() for k in ['begin construction', 'construction', 'advertise', 'start']):
            project_name = None
            for j in range(i-1, max(-1, i-15), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    if len(prev_line) < 200:
                        stop_words = ['update', 'schedule', 'status', 'description', 'project', 'begin construction', 'advertise', 'complete design']
                        if not any(word in prev_line.lower() for word in stop_words):
                            project_name = prev_line
                            break
            
            if project_name:
                spring_2022_projects.append(project_name)

unique_spring_projects = list(set(spring_2022_projects))

print('Unique Spring 2022 projects:', len(unique_spring_projects))
print('\nSpring 2022 projects:')
for proj in sorted(unique_spring_projects):
    print('- ' + proj)

funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding_data}

matched_projects = []
total_funding = 0

for proj_name in unique_spring_projects:
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        matched_projects.append({'project': proj_name, 'funding': amount})
        total_funding += amount
        print('Exact match: ' + proj_name + ' - $' + str(amount))
    else:
        for funded_proj, amount in funding_lookup.items():
            if proj_name in funded_proj or funded_proj in proj_name:
                matched_projects.append({'project': proj_name, 'funding': amount, 'matched_to': funded_proj})
                total_funding += amount
                print('Partial match: ' + proj_name + ' -> ' + funded_proj + ' - $' + str(amount))
                break

print('\nMatched projects: ' + str(len(matched_projects)))
print('Total funding: $' + str(total_funding))

result = {
    'spring_2022_project_count': len(unique_spring_projects),
    'matched_projects': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
