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
keywords = ['begin construction', 'construction', 'advertise', 'start']

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        spring_found = 'Spring' in line and '2022' in line
        keyword_found = any(k in line.lower() for k in keywords)
        
        if spring_found and keyword_found:
            project_name = None
            for j in range(i-1, max(-1, i-15), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    if len(prev_line) < 200:
                        bad_words = ['update', 'schedule', 'status', 'description', 'project', 'begin construction', 'advertise', 'complete design']
                        good_line = True
                        for word in bad_words:
                            if word in prev_line.lower():
                                good_line = False
                                break
                        if good_line:
                            project_name = prev_line
                            break
            
            if project_name:
                spring_2022_projects.append(project_name)

unique_projects = list(set(spring_2022_projects))

print('Unique Spring 2022 projects:', len(unique_projects))

# Display them
for proj in sorted(unique_projects):
    print('- ' + proj)

# Match with funding
project_funding = {}
for item in funding_data:
    project_funding[item['Project_Name']] = int(item['Amount'])

matched = []
total = 0

for proj in unique_projects:
    if proj in project_funding:
        amount = project_funding[proj]
        matched.append({'project': proj, 'funding': amount})
        total += amount
        print('Matched: ' + proj + ' = $' + str(amount))
    else:
        # Try partial match
        for funded_name, amount in project_funding.items():
            if proj in funded_name or funded_name in proj:
                matched.append({'project': proj, 'funding': amount, 'matched_to': funded_name})
                total += amount
                print('Partial: ' + proj + ' -> ' + funded_name + ' = $' + str(amount))
                break

print('Total matched:', len(matched))
print('Total funding:', total)

result = {'count': len(unique_projects), 'matched': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
